# Imports
from tango import DevState, AttrWriteType, DevFailed
from facadedevice import Facade, proxy_attribute, logical_attribute


class BeamEnergy(Facade):
    """"BeamEnergy docstring"""

    # Device initialization

    def safe_init_device(self):
        super(BeamEnergy, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running.")

    # proxy attributes

    MagnetPSName = proxy_attribute(
        dtype=str,
        access=AttrWriteType.READ,
        property_name='MagnetPSNameAttribute')

    MagnetPSAttribute = proxy_attribute(
        dtype=str,
        access=AttrWriteType.READ,
        property_name='MagnetPSAttrAttribute')  # I'm not sure if property_name is correct

    A = proxy_attribute(
        dtype=float,
        access=AttrWriteType.READ,
        property_name='SquareFactorAttribute')

    B = proxy_attribute(
        dtype=float,
        access=AttrWriteType.READ_WRITE,
        property_name='LinearFactorAttribute')

    C = proxy_attribute(
        dtype=float,
        access=AttrWriteType.READ_WRITE,
        property_name='AbsoluteFactorAttribute')

    # logical attributes

    @logical_attribute(
        dtype=float,
        bind=['A', 'B', 'C', 'MagnetPSName', 'MagnetPSAttribute'])
    def Energy(self, a, b, c, name, attr):
        if name and attr:
            try:
                val = name.read_attribute(attr).value
                ret = val * val * a
                ret += val * b
                ret += c
                return ret
            except DevFailed, e:
                print 'ERROR in communication with', name
                print e
        else:
            return 0.0
        attr.set_value(self.attr_Energy_read)


if __name__ == '__main__':
    BeamEnergy.run_server()
