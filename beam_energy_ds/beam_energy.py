"""
This module contains device class BeamEnergy and run method for it.
- A: square factor of energy equation
- B: linear factor of energy equation
- C: absolute factor of energy equation
"""

# Imports
from tango import DevState, AttrWriteType, DispLevel
from facadedevice import Facade, proxy_attribute, logical_attribute, local_attribute


class BeamEnergy(Facade):
    """
    A facade device for calculating beam's energy, biased on magnet power 
    supply's current. In calculations has been used second order polynomial
    model:
    >>> energy = val ** 2 * a + val * b + c
    where:
    - a, b and c -square, linear and absolute factors of equation
    - val - value of magnet's current
    - energy - energy of the beam
    """

    # device initialization

    def safe_init_device(self):
        """
        This is a method to safely initialize the BeamEnergy device
        :return: does not return anything
        """
        super(BeamEnergy, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running.")

    # proxy attributes

    MagnetPS = proxy_attribute(
        dtype=str,
        access=AttrWriteType.READ_WRITE,
        property_name='MagnetPSAttribute',
        description="This is proper TANGO name of attribute (current), which "
                    "will be used in energy calculations. For example: "
                    "some/device/somewhere/attribute")

    # local attributes

    A = local_attribute(
        dtype=float,
        access=AttrWriteType.READ_WRITE,
        display_level=DispLevel.EXPERT,
        description="This is a square factor of energy calculation in second"
                    " order polynomial")

    B = local_attribute(
        dtype=float,
        access=AttrWriteType.READ_WRITE,
        display_level=DispLevel.EXPERT,
        description="This is a linear factor of energy calculation in second"
                    " order polynomial")

    C = local_attribute(
        dtype=float,
        access=AttrWriteType.READ_WRITE,
        display_level=DispLevel.EXPERT,
        description="This is an absolute factor of energy calculation in second"
                    " order polynomial")

    # logical attributes

    @logical_attribute(
        dtype=float,
        bind=['A', 'B', 'C', 'MagnetPS'],
        description="This is an attribute holding value of calculated beam's "
                    "energy. In calculation is used second order polynomial "
                    "model, specified in class' documentation")
    def Energy(self, a, b, c, val):
        return val ** 2 * a + val * b + c

# run server

run = BeamEnergy.run_server()

if __name__ == '__main__':
    run()
