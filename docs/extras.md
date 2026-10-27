# Beyond the CoCo

Things a CoCo Zero does that the original Color Computers never did. The list
will keep growing. This page requires nothing: what every CoCo Zero must do is
set out in [`spec/`](../spec/).

## On every CoCo Zero

These follow from the spec.

- **One cable to a TV.** Picture and sound together over a mini HDMI cable,
  640 x 480 at 60 Hz.
- **A USB keyboard.** A standard USB-C keyboard on the USB host port.
- **A USB joystick or gamepad** in place of the CoCo's analog joysticks.
- **A USB hub**, so the keyboard and joystick plug in together.
- **USB audio:** headphones or speakers on a class-compliant USB audio device,
  in place of the video cable's sound.
- **A microSD card** in place of tapes and floppy drives.
- **Assign disk images** from the microSD to drives using a configuration
  screen.
- **USB-C power**, from whatever you plug in.
- **The size of a Raspberry Pi Zero**, in place of a keyboard-sized case.

## In the reference CoCo Zero

The [reference firmware](https://github.com/ugufru/xroar-waveshare-rp2350-pizero)
also has these. Other CoCo Zeros may do more or less.

- **Programs and cartridges without typing**, loaded straight from the
  configuration screen.
- **Three machines in one firmware**, a CoCo 2, a CoCo 3 and the CoCo Zero (a
  CoCo 3 with extras), and a game can switch to the one it needs.
- **The CoCo 2's high-speed POKEs** run up to twice as fast with a clean screen.
- **True lower case** and a choice of fonts on the CoCo 2.
- **Sound cartridges built in:** the Games Master Cartridge's three-voice
  chip, the CoCo PSG and Symphony-12 chips, and the Orchestra-90CC's stereo
  DACs, all playing at once.
- **The CoCo 3's palette registers and timer** on the CoCo 2.
- **A keyboard that types what is printed on it**, with auto-repeat.
- **A gamepad that works as both joysticks**, and can also pick and start games.
- **Volume on the keyboard's volume keys** for USB audio.
- **Settings in text files**, for every game or just one.
- **Screenshots** to the card with Print Screen.
- **Autorun:** a game can start by itself at power-on.
- **NitrOS-9**, from a boot disk an included script builds.
- **A printable case** styled after the ventilated top of a CoCo 2.

For the same ground row by row against a CoCo 2 and a CoCo 3, see
[CoCo 2, CoCo 3, CoCo Zero](comparison.md).
