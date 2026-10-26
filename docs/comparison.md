# CoCo 2, CoCo 3, CoCo Zero

**The same Color BASIC you remember. Everything around it, fixed.**
Tandy fixed some of it in 1986. The rest took forty years.

| | Tandy CoCo 2 (1983) | Tandy CoCo 3 (1986) | CoCo Zero (2026) |
|---|---|---|---|
| **Picture** | ✕ RF out to channel 3 or 4: fuzz, shimmer and a fight with the TV's tuner. | ✓ Composite and RGB outputs, sharp on Tandy's CM-8 monitor if you bought one. | ✓ A sharp digital picture at 60 frames a second on an ordinary TV, with the NTSC artifact colours recreated. |
| **Sound** | ✕ A 6-bit DAC squeezed through the same RF signal, so the picture's buzz comes along for free. | ✕ The same 6-bit DAC, and still no sound chip. | ✓ Clean digital sound over the same one cable, plus the Games Master Cartridge's three-voice sound chip built in. |
| **Speed** | ✕ `POKE 65497,0` doubles the speed and scrambles the screen. | ✓ 1.79 MHz with `POKE 65497,0`, and the picture holds. | ✓ Both high-speed POKEs work on the CoCo 2, up to twice as fast with a clean screen, and the CoCo 3 runs at 1.79 MHz. |
| **Storage** | ✕ Cassette tapes at 1,500 baud. Floppy drives cost extra, and so did the controller. | ✕ The same cassettes, or the same floppy drive and controller, bought separately. | ✓ A microSD card full of disks, programs and cartridges. Disks are writable, and NitrOS-9 boots. |
| **Loading a game** | ✕ Type `CLOADM`, press PLAY, wait, and hope the volume knob was right. | ✕ Still typed: `LOADM` or `RUN`, then wait for the drive. | ✓ Pick it from an on-screen list, or have it start by itself at power-on. |
| **Text** | ✕ 32 columns, and lower case shows as inverse capitals on most models. | ✓ True lower case, and 40 or 80 columns. | ✓ 32, 40 or 80 columns, and a choice of fonts on the CoCo 2 with true lower case by default. |
| **Keyboard** | ✕ No Ctrl, no Alt, no function keys, and no auto-repeat. | ✓ Adds Ctrl, Alt, F1 and F2. | ✓ A USB keyboard. Each key types what is printed on it, with auto-repeat. |
| **Joysticks** | ✕ Analog sticks that drift, on cables that tangle. | ✕ The same analog sticks, drifting the same way. | ✓ A USB gamepad works as both joysticks, and it can pick and start games too. |
| **Screenshots** | ✕ Point a camera at the TV and try not to catch the scan lines. | ✕ Point a camera at the monitor instead. | ✓ Print Screen saves a picture straight to the card. |
| **Settings** | ✕ None to speak of. What it does at power-on is fixed in ROM. | ✕ Still fixed in ROM. | ✓ A text file on the card, for every game or just one, editable on screen. |
| **Between you and the machine** | ✓ Nothing: switch on and BASIC is there. | ✓ Nothing: switch on and BASIC is there. | ✓ Still nothing. No operating system, only a small menu for disks and settings. Switch on and BASIC is there. |
| **Size and power** | ✕ A keyboard-sized case with a mains cord, and 40-year-old capacitors inside. | ✕ The same: a keyboard-sized case, a mains cord, and capacitors nearly as old. | ✓ A 65 x 30 mm board, the size of a Raspberry Pi Zero, powered by a phone charger. A printable case, styled after the CoCo 2's ventilated top, is optional. |
| **What came next** | ✕ Want a CoCo 3? Buy a CoCo 3. | ✕ Nothing. Tandy never made a CoCo 4. | ✓ One board that emulates a CoCo 2 or a 128 KB CoCo 3, and switches by itself for a game that needs the CoCo 3. The CoCo 2 can have the CoCo 3's palette and timer too. |

Bring your own ROMs, from hardware you own.

## About this page

The CoCo Zero column describes the reference implementation: XRoar running
on a Waveshare RP2350-PiZero,
[xroar-waveshare-rp2350-pizero](https://github.com/ugufru/xroar-waveshare-rp2350-pizero).
Every claim in it ships in that firmware. Another CoCo Zero may do more or
less of it. What every CoCo Zero must do is set out in [`spec/`](../spec/).

This page is adapted from the reference project's `docs/coco-comparison.html`
and `docs/coco2-vs-coco-zero.html`. Changes from those pages:
- "What came next" now describes one firmware that is both machines, rather
  than a separate experimental CoCo 3 build.
- The CoCo Zero's speed and text rows now include the CoCo 3.
- The "Between you and the machine" row is new.
