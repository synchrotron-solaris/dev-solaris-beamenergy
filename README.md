Beam Energy
========================
Tango device for calculating beam's power at the end of the linac.

What's inside
-------------
There are directories for source code, documentation and tests as well as
`LICENCE` and `MANIFEST.in` files as well as a setup script.
 
How to install
--------------

First, clone git repository:
```console
git clone https://github.com/synchrotron-solaris/dev-solaris-beamenergy.git
```
Then, enter the repository:
```console
cd dev-solaris-beamenergy
```
Now you can use:
```console
python setup.py install
```
or:
```console
pip install .
```

How to run
----------
After installation, there is only one script: `BeamEnergy`.

Requirements
------------

- `setuptools`
- `facadedevice` >= 1.0.1
- `pytango` >= 9.2.1

License
-------
This sample project is distributed under LGPLv3 (see `LICENSE` file).
