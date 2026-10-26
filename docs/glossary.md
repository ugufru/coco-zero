# Glossary

## Background

Tandy sold the TRS-80 Color Computer through Radio Shack from 1980. Owners
called it the CoCo. Three models followed: the CoCo 1, the smaller CoCo 2 in
1983, and the CoCo 3 in 1986, with more memory, more colors and 80-column
text. All three run Microsoft's Color BASIC on a Motorola 6809, and they were
sold until 1991. A CoCo Zero emulates them.

For more, [CoCopedia](https://www.cocopedia.com/) is the Color Computer wiki,
and the [Color Computer Archive](https://colorcomputerarchive.com/) keeps the
software, manuals and magazines.

## Terms

**6809.** The Motorola 8-bit processor in every CoCo. It runs at 0.89 MHz, or
1.79 MHz at double speed.

**Artifact colors.** Colors an NTSC TV shows when it is fed fine black and
white patterns. Many CoCo games draw in them on purpose.

**AY-3-8910.** A three-voice sound chip from General Instrument, used in the
CoCo PSG and Symphony-12 sound cartridges.

**Bare metal.** Software that runs straight on the hardware, with no operating
system underneath. See [Zero operating system](../spec/zero-os.md).

**Class-compliant USB audio.** A USB sound device that follows the USB Audio
Class standard, so it works without a driver of its own.

**Color BASIC, Extended, Disk and Super Extended Color BASIC.** The CoCo's
BASIC in its four ROMs. Color BASIC is the base; Extended adds graphics and
sound commands; Disk adds the disk commands, from the disk controller
cartridge; Super Extended is the CoCo 3's, for its new screen modes. A CoCo
Zero needs these ROMs, dumped from hardware you own.

**Configuration screen.** The one screen a CoCo Zero shows besides the CoCo
itself, for emulator options, disk images, system information and loading
programs and cartridges.

**DSK.** The usual file format for a CoCo floppy disk image.

**DVI.** The digital video signal a CoCo Zero sends, with its sound embedded.
It travels over a mini HDMI cable.

**Games Master Cartridge (GMC).** A modern CoCo cartridge with an SN76489
sound chip, for games written for it.

**GIME.** The CoCo 3's custom graphics and memory chip, which took over from
the SAM and VDG.

**High-speed POKE.** `POKE 65495,0` and `POKE 65497,0` speed up the 6809. On a
real CoCo 2 the second one scrambles the screen; the CoCo 3 was built for it.

**Mini HDMI.** The small video connector on a Raspberry Pi Zero, and the cable
that fits it. In this standard the name means only the connector and cable.

**NitrOS-9.** A community-developed version of the OS-9 operating system for
the CoCo. It runs on the emulated CoCo, not under it.

**Orchestra-90CC.** Tandy's stereo music cartridge, with two 8-bit DACs.

**PIA.** The MC6821 Peripheral Interface Adapter. The CoCo has two, for the
keyboard, joysticks, cassette and sound.

**Pi HAT.** An add-on board that plugs onto a Raspberry Pi's 40-pin header. A
CoCo Zero sets no height limit, so builders are free to try them.

**Pi Zero size.** The 65 x 30 mm board outline and four mounting holes of the
Raspberry Pi Zero. See [Form factor](../spec/form-factor.md).

**ROM.** The chips that hold the CoCo's BASIC. No CoCo Zero ships with them.

**RP2350.** The Raspberry Pi microcontroller on the reference CoCo Zero's
board.

**SAM.** The MC6883 Synchronous Address Multiplexer, which handles memory and
timing in the CoCo 1 and 2.

**SN76489.** A three-voice sound chip from Texas Instruments, used in the
Games Master Cartridge.

**VDG.** The MC6847 Video Display Generator, the CoCo 1 and 2's video chip,
with its 32 by 16 green text screen.

**XRoar.** Ciaran Anscomb's emulator of the Dragon and Tandy CoCo computers.
The reference CoCo Zero is built on it.
