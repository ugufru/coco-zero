# CoCo Zero

**A Tandy Color Computer on a board the size of a Raspberry Pi Zero.**

<p align="center">
  <img src="docs/images/in-use-angle.jpg" width="460"
       alt="The reference CoCo Zero in its printed case, shaped like a CoCo 2, with its mini HDMI cable and two USB-C cables plugged in and a microSD card in its slot">
</p>

This repository is the CoCo Zero standard. It describes what a CoCo Zero is
and what qualifies as one. It does not tell you how to build one.

## The vision

Every CoCo 2 was the same machine on the outside. Tandy built it in more than
one factory and more than one revision, including the boards made in Korea,
but the motherboard was always the same size and shape and fitted the same
case. The CoCo Zero carries that idea forward. There can be many CoCo Zeros,
from different builders on different boards, and they all fit the same case.

The **Zero** means two things.

**The board size.** Raspberry Pi set the Pi Zero size in 2015, and others
have followed it since, from Waveshare to Orange Pi. A CoCo Zero is built on
a board of that size: 65 x 30 mm, with the same four mounting holes.

**Zero operating system.** There is nothing between you and the machine but
one layer of software: the emulated CoCo, and a lightweight monitor and
configuration screen that runs nothing else. Switch it on and BASIC is there,
just as it was in 1983. The CoCo Zero gets as close to that as it can while
keeping the essence of what it means to operate a CoCo.

**A CoCo, and more.** A CoCo Zero is a CoCo 1, 2 or 3. The CoCo 3 has 128K,
and ideally 512K, 2M or more. A CoCo Zero also does things the original
machines never did: a sharp digital picture and clean sound on an ordinary
TV, a USB keyboard and gamepad, a microSD card in place of tapes and floppies.
That list will keep growing. See [CoCo 2, CoCo 3, CoCo Zero](docs/comparison.md)
for the comparison, row by row.

**A standard, not a blueprint.** Think of the rules for a kei car, or for a
US mailbox: they fix the general shape and leave the rest to the builder.
This standard is deliberately sparse. It leaves the most room for DIY
builders to adapt a CoCo Zero and make it their own, while letting them rely
on third-party manufacturers for the electronics, as with any computer case.

**Quiet.** Every CoCo Zero is passively cooled. No fan.

**Open.** In the tradition of [XRoar](https://www.6809.org.uk/xroar/), the
emulator it grew from, the reference firmware is completely open source.

## The standard

| Page | What it sets |
|---|---|
| [Form factor](spec/form-factor.md) | The Raspberry Pi Zero outline and mounting holes |
| [Features](spec/features.md) | Two USB-C ports (power and programming, and a USB host), mini HDMI, microSD; 640 x 480 at 60 Hz over HDMI with sound; real time at double speed with no dropped frames or sound gaps; passive cooling |

More is on the way: the machines and memory sizes, bare metal, and a
one-page definition. The work is tracked in [`issues.jsonl`](issues.jsonl)
and ranked in [`roadmap.jsonl`](roadmap.jsonl), and
[`issues.html`](issues.html) shows both (download the repository and open it
in a browser).

## The reference CoCo Zero

The first CoCo Zero is XRoar running on a
[Waveshare RP2350-PiZero](https://www.waveshare.com/rp2350-pizero.htm). It is a
CoCo 2 or a 128K CoCo 3 in one firmware, with a printable case shaped like a
CoCo 2.

<p align="center">
  <img src="docs/images/board-wired.jpg" width="380"
       alt="The bare Waveshare RP2350-PiZero board running, with USB-C power, a USB-C host cable, a mini HDMI adapter and a microSD card">
  <img src="docs/images/three-quarter-ports.jpg" width="380"
       alt="The printed case from the connector side: the mini HDMI port, two USB-C ports, and the microSD slot at the end">
</p>

Source, build instructions and the case:
[ugufru/xroar-waveshare-rp2350-pizero](https://github.com/ugufru/xroar-waveshare-rp2350-pizero)

The name began there, as a name for a CoCo on a Pi Zero size board. It became
the name for the idea once the same board ran a CoCo 3 too.

## ROMs

No CoCo Zero ships with ROMs. Color, Extended, Disk and Super Extended Color
BASIC are © Microsoft, Tandy and Microware and may not be redistributed. Use
dumps from hardware you own.

## Resources

- [XRoar](https://www.6809.org.uk/xroar/): the Dragon and CoCo emulator by
  Ciaran Anscomb, the heart of the reference firmware.
- [Reference firmware](https://github.com/ugufru/xroar-waveshare-rp2350-pizero):
  XRoar on the Waveshare RP2350-PiZero.
- [Waveshare RP2350-PiZero](https://www.waveshare.com/rp2350-pizero.htm) and its
  [wiki](https://www.waveshare.com/wiki/RP2350-PiZero): the reference board.
- Raspberry Pi mechanical drawings, the source of the form factor:
  [Pi Zero](https://datasheets.raspberrypi.com/rpizero/raspberry-pi-zero-mechanical-drawing.pdf)
  and [Pi Zero 2 W](https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-mechanical-drawing.pdf).
- [CoCopedia](https://www.cocopedia.com/): the Color Computer wiki.
- [Color Computer Archive](https://colorcomputerarchive.com/): software,
  manuals and magazines.

## Trademarks

Tandy and Color Computer belong to their owners. "Raspberry Pi" is a
trademark of Raspberry Pi Ltd. A CoCo Zero is not a Tandy or Raspberry Pi
product.
