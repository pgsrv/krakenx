from setuptools import setup

setup(
    name='krakenx',
    version='0.0.2',
    packages=['krakenx'],
    scripts=['bin/colctl', 'bin/colctl.py'],
    install_requires=['pyusb'],
)
