from setuptools import find_packages, setup

from BeamEnergy.version import __version__, licence
from BeamEnergy import __doc__, __author__, __author_email__

setup(
    name="beam_energy",
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    license=licence,
    description="A simple facade device for calculating beam's energy",
    long_description=__doc__,
    url="https://github.com/synchrotron-solaris/dev-solaris-beamenergy.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["setuptools", "facadedevice", "pytango"],
    entry_points={
        "console_scripts": ["BeamEnergy = "
                            "BeamEnergy.BeamEnergy:run"]}
)
