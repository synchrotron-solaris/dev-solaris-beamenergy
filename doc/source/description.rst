Description
======================

A facade device for calculating beam's energy at the end of the linac.

- MagnetPS - A proper Tango name of a power supply which energy is used in
    calculations, with name of the attribute of the PS that the energy will be
    calculated from. For example: some/device/somewhere/attribute
- A - The square factor in the energy calculation.
- B - The linear factor in the energy calculation.
- C - The absolute factor in the energy calculation.
- Energy - Energy of the beam

Energy is calculated according to:

Energy = MagnetPS^2 * A + MagnetPS * B + C