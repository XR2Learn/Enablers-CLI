from setuptools import setup

requirements = ['click']

setup(
    name='xr2learn_enablers_cli',
    version='0.1.1',
    description='Command-Line Interface to access functionalities of Enablers 2-6.',
    author='UM-XR2Learn-Enablers',
    packages=['xr2learn_enablers_cli'],
    install_requires=requirements,
    zip_safe=False
)
