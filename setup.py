from setuptools import find_packages, setup

from beam_energy_ds.version import __version__, licence
from beam_energy_ds import __doc__, __author__, __author_email__

setup(
    name="tangods-beam_energy",
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    license=licence,
    description="A simple facade device for calculating beam's energy",
    long_description=__doc__,
    url="https://github.com/synchrotron-solaris/dev-solaris-beamenergy.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["setuptools"],
    entry_points={
        "console_scripts": ["BeamEnergy = "
                            "beam_energy_ds.beam_energy:run"]}
)
