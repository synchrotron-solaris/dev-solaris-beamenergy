""""
   A facade device for calculating beam's energy at the end of the linac.
   MagnetPS - A proper Tango name of a power supply which energy is used in
   calculations, with name of the attribute of the PS that the energy will be
   calculated from. For example: some/device/somewhere/attribute
   A - The square factor in the energy calculation.
   B - The linear factor in the energy calculation.
   C - The absolute factor in the energy calculation.
   Energy - Energy of the beam
"""

# Imports
from tango import DevState, AttrWriteType
from facadedevice import Facade, proxy_attribute, logical_attribute, local_attribute


class BeamEnergy(Facade):

    # device initialization

    def safe_init_device(self):
        super(BeamEnergy, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running.")

    # proxy attributes

    MagnetPS = proxy_attribute(
        dtype=str,
        access=AttrWriteType.READ_WRITE,
        property_name='MagnetPSAttribute')

    # local attributes

    A = local_attribute(
        dtype=float,
        access=AttrWriteType.READ_WRITE,
        property_name='SquareFactorAttribute')

    B = local_attribute(
        dtype=float,
        access=AttrWriteType.READ_WRITE,
        property_name='LinearFactorAttribute')

    C = local_attribute(
        dtype=float,
        access=AttrWriteType.READ_WRITE,
        property_name='AbsoluteFactorAttribute')

    # logical attributes

    @logical_attribute(
        dtype=float,
        bind=['A', 'B', 'C', 'MagnetPS'])
    def Energy(self, a, b, c, val):
        return val * val * a + val * b + c

# run server

run = BeamEnergy.run_server()

if __name__ == '__main__':
    run()
