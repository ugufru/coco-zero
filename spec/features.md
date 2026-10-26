# CoCo Zero features

Status: **accepted** (CZ-16, CZ-21, CZ-4, CZ-29)

## Connectors

- Two USB-C ports:
  - one for power and programming;
  - one a USB host for peripherals.
- Video output is a mini HDMI connector.
- Storage is a microSD card slot.

## USB devices

- A standard USB-C keyboard works when plugged into the host port.
- A USB joystick or gamepad works as the CoCo's joysticks.
- A keyboard and a joystick work together through a simple USB hub (one with
  a single hub chip).
- A class-compliant USB audio device can play the sound in place of the video
  cable.

## Video and sound

- 640 x 480 at 60 Hz, as a DVI signal.
- Sound is embedded in the DVI signal.

## Performance

- The emulated CoCo runs in real time at double speed (about 1.79 MHz).
- No dropped frames.
- No gaps in the sound.
- Power-on goes straight to the BASIC prompt.

## Cooling

- Passively cooled. No fan.

## Firmware

- The firmware is open source.
