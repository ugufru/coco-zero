#!/usr/bin/env python3
"""Build spec/coco-zero-spec.pdf, the whole standard on one page.

It opens with the conformance line, and carries the version number from
docs/versioning.md.

The spec/*.md pages stay the source of truth. This only ever reads them.

    python3 tools/spec_pdf.py [out.pdf]

Only the requirements go in: Status lines and the form factor's Source section
are left out. The page uses the PDF standard Helvetica fonts, so the script
needs nothing beyond Python. It stops with an error rather than spill onto a
second page.
"""

import datetime
import re
import subprocess
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ["form-factor.md", "machines.md", "zero-os.md", "features.md"]
OUT = ROOT / "spec" / "coco-zero-spec.pdf"

W, H = 612, 792  # US Letter, in points
LEFT, RIGHT, TOP, BOTTOM = 60, 552, 732, 74

# Advance widths per 1000 units, from the Adobe Helvetica AFMs, for ASCII 32-126.
_REG = [278, 278, 355, 556, 556, 889, 667, 191, 333, 333, 389, 584, 278, 333, 278, 278,
        556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 278, 278, 584, 584, 584, 556,
        1015, 667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778,
        667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 278, 278, 278, 469, 556,
        333, 556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556, 556,
        556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500, 334, 260, 334, 584]
_BOLD = [278, 333, 474, 556, 556, 889, 722, 238, 333, 333, 389, 584, 278, 333, 278, 278,
         556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 333, 333, 584, 584, 584, 611,
         975, 722, 722, 722, 722, 667, 611, 778, 722, 278, 556, 722, 611, 833, 722, 778,
         667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 333, 278, 333, 584, 556,
         333, 556, 611, 556, 611, 556, 333, 611, 611, 278, 278, 556, 278, 889, 611, 611,
         611, 611, 389, 556, 333, 611, 556, 778, 556, 556, 500, 389, 280, 389, 584]


def width(text, size, bold=False):
    table = _BOLD if bold else _REG
    return sum(table[ord(c) - 32] if 32 <= ord(c) <= 126 else 556 for c in text) * size / 1000


def wrap(text, size, room, bold=False):
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}" if line else word
        if line and width(trial, size, bold) > room:
            lines.append(line)
            line = word
        else:
            line = trial
    return lines + ([line] if line else [])


def inline(text):
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<(https?://[^>]+)>", r"\1", text)
    return text.replace("**", "").replace("`", "").replace("*", "")


def parse(path):
    """One spec page as (kind, payload) blocks."""
    blocks, para, table, skip = [], [], [], False

    def flush():
        if para:
            blocks.append(("para", " ".join(para)))
            para.clear()
        if table:
            blocks.append(("table", list(table)))
            table.clear()

    for raw in path.read_text().splitlines():
        line = raw.rstrip()
        if line.startswith("# "):
            title = line[2:].replace("CoCo Zero ", "")
            blocks.append(("section", title[0].upper() + title[1:]))
        elif line.startswith("Status:"):
            continue
        elif line.startswith("## "):
            flush()
            name = line[3:].strip()
            skip = name == "Source"
            if not skip and name != "Requirements":
                blocks.append(("subhead", name))
        elif skip:
            continue
        elif line.startswith("|"):
            if para:
                flush()
            cells = [inline(c.strip()) for c in line.strip("|").split("|")]
            if not all(set(c) <= set("-: ") for c in cells):
                table.append(cells)
        elif line.lstrip().startswith("- "):
            flush()
            level = (len(line) - len(line.lstrip())) // 2
            blocks.append(("bullet", (level, inline(line.lstrip()[2:]))))
        elif not line.strip():
            flush()
        elif line.startswith(" ") and not para and blocks and blocks[-1][0] == "bullet":
            level, text = blocks[-1][1]  # a bullet's wrapped continuation line
            blocks[-1] = ("bullet", (level, f"{text} {inline(line.strip())}"))
        else:
            para.append(inline(line.strip()))
    flush()
    return blocks


class Page:
    def __init__(self):
        self.ops = []
        self.y = TOP

    def text(self, x, y, s, size, bold=False, grey=0):
        s = s.encode("cp1252").replace(b"\\", b"\\\\").replace(b"(", b"\\(").replace(b")", b"\\)")
        self.ops.append(b"BT %.3f g /%s %.1f Tf %.2f %.2f Td (%s) Tj ET"
                        % (grey, b"F2" if bold else b"F1", size, x, y, s))

    def rule(self, x1, x2, y, weight=0.5, grey=0):
        self.ops.append(b"%.3f G %.2f w %.2f %.2f m %.2f %.2f l S" % (grey, weight, x1, y, x2, y))

    def down(self, dy):
        self.y -= dy
        if self.y < BOTTOM:
            sys.exit("spec_pdf: the spec no longer fits on one page")


SIZE, LEAD = 10, 12.5


GUTTER = 24


def height(blocks, left, right):
    scratch = Page()
    scratch.y = 10000
    render(scratch, blocks, left, right)
    return 10000 - scratch.y


def render_page(page, blocks):
    """A spec page with subheadings goes in two columns, split at the subheading
    that makes them most even, so the short Features lists do not run down the page."""
    heads = [i for i, (kind, _) in enumerate(blocks) if kind == "subhead"]
    if len(heads) < 2:
        render(page, blocks)
        return
    mid = (LEFT + RIGHT + GUTTER) / 2
    split = min(heads[1:], key=lambda i: max(height(blocks[heads[0]:i], LEFT, mid - GUTTER),
                                             height(blocks[i:], mid, RIGHT)))
    render(page, blocks[:heads[0]])
    page.down(-(LEAD + 4) + 14)  # the first subheading sits just under the rule
    top = page.y
    render(page, blocks[heads[0]:split], LEFT, mid - GUTTER)
    low = page.y
    page.y = top
    render(page, blocks[split:], mid, RIGHT)
    page.y = min(low, page.y)


def render(page, blocks, left=LEFT, right=RIGHT):
    for kind, payload in blocks:
        if kind == "section":
            page.down(22)
            page.text(left, page.y, payload, 13, bold=True)
            page.rule(left, right, page.y - 5, 0.4, 0.6)
            page.down(6)
        elif kind == "subhead":
            page.down(LEAD + 4)
            page.text(left, page.y, payload, SIZE, bold=True)
        elif kind == "para":
            for line in wrap(payload, SIZE, right - left):
                page.down(LEAD)
                page.text(left, page.y, line, SIZE)
            page.down(4)
        elif kind == "bullet":
            level, text = payload
            indent = left + 4 + level * 16
            for i, line in enumerate(wrap(text, SIZE, right - indent - 12)):
                page.down(LEAD)
                if i == 0:
                    page.text(indent, page.y, "•" if level == 0 else "–", SIZE)
                page.text(indent + 12, page.y, line, SIZE)
        elif kind == "table":
            first = max(width(r[0], SIZE, i == 0) for i, r in enumerate(payload)) + 18
            page.down(6)
            page.rule(left, right, page.y)
            for i, row in enumerate(payload):
                page.down(LEAD + 1)
                for col, cell in enumerate(row[:2]):
                    page.text(left + (first if col else 0), page.y, cell, SIZE, bold=i == 0)
                if i == 0:
                    page.rule(left, right, page.y - 5, 0.4)
            page.rule(left, right, page.y - 5)
            page.down(4)


def spec_date():
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", "spec/*.md"], cwd=ROOT,
                             capture_output=True, text=True, check=True).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain", "--", "spec/*.md"], cwd=ROOT,
                               capture_output=True, text=True, check=True).stdout.strip()
        if out and not dirty:
            return out
    except (OSError, subprocess.CalledProcessError):
        pass
    return datetime.date.today().isoformat()


def spec_version():
    m = re.search(r"Current version: \*\*([0-9.]+)\*\*", (ROOT / "docs" / "versioning.md").read_text())
    if not m:
        sys.exit("spec_pdf: no 'Current version' line in docs/versioning.md")
    return m.group(1)


def pdf(content):
    stream = zlib.compress(content)
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 %d %d] "
        b"/Resources << /Font << /F1 4 0 R /F2 5 0 R >> >> /Contents 6 0 R >>" % (W, H),
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>",
        b"<< /Length %d /Filter /FlateDecode >>\nstream\n%s\nendstream" % (len(stream), stream),
        b"<< /Title (CoCo Zero standard) /Author (CoCo Zero) >>",
    ]
    out, offsets = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"), []
    for n, body in enumerate(objects, 1):
        offsets.append(len(out))
        out += b"%d 0 obj\n%s\nendobj\n" % (n, body)
    xref = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objects) + 1)
    out += b"".join(b"%010d 00000 n \n" % o for o in offsets)
    out += b"trailer\n<< /Size %d /Root 1 0 R /Info 7 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (
        len(objects) + 1, xref)
    return bytes(out)


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else OUT
    page = Page()
    page.text(LEFT, page.y, "CoCo Zero", 22, bold=True)
    label = f"The standard, version {spec_version()}"
    page.text(RIGHT - width(label, 11), page.y, label, 11, grey=0.4)
    page.down(8)
    render(page, [("para", "A CoCo Zero is anything that meets every requirement on this page.")])
    for name in PAGES:
        render_page(page, parse(ROOT / "spec" / name))

    grey = 0.4
    page.rule(LEFT, RIGHT, 62, 0.4, 0.6)
    page.text(LEFT, 50, f"github.com/ugufru/coco-zero  ·  spec as of {spec_date()}  ·  CC BY 4.0", 8, grey=grey)
    page.text(LEFT, 39, "“Raspberry Pi” is a trademark of Raspberry Pi Ltd. Tandy and Color Computer "
              "belong to their owners.", 8, grey=grey)

    out.write_bytes(pdf(b"\n".join(page.ops)))
    print(f"built {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")


if __name__ == "__main__":
    main()
