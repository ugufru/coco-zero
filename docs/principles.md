# Design principles

The rules behind the standard's choices, so future decisions follow the same
grain. The first one governs the rest.

1. **Fix the outside, leave the inside.** Like a shipping container or an AA
   battery, the standard sets the size and how a CoCo Zero connects, and
   leaves everything else to the builder. A spec page carries requirements
   only, as few as will do. Builders can rely on third-party boards for the
   electronics.

2. **Zero operating system.** One layer of software between you and the
   machine. Switch it on and BASIC is there. Libraries are allowed, but each
   one is a layer of its own between the emulator and the hardware, so keep
   them as few and as thin as the emulator can manage with.

3. **Look forward.** A CoCo Zero uses what people already own: a TV, a phone
   charger, a USB keyboard, a microSD card. The extras are modern
   conveniences, not recreations of old peripherals.

4. **Open.** The standard is CC BY 4.0, and every CoCo Zero's firmware is open
   source.

5. **Bring your own ROMs.** No CoCo Zero ships with them. They come from
   hardware you own.

6. **For everyone.** Builders, developers, retro gamers, and anyone curious
   enough to spend $20. Nothing in the standard should price them out or
   shut them out.

7. **Room to play.** A CoCo Zero is a playground for developers. Its limits
   need not be practical, as long as they are within reach. The spec sets a
   floor, never a ceiling: a 2M CoCo 3, every sound cartridge built in at once,
   or a HAT nobody planned for are all welcome.

8. **Only what is true.** Every claim about a CoCo Zero describes something a
   real one does today. What is planned is called planned.
