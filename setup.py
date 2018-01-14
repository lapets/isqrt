from setuptools import setup

setup(
    name             = 'isqrt',
    version          = '0.9.2.0',
    packages         = ['isqrt',],
    install_requires = [],
    license          = 'MIT',
    maintainer       = 'Andrei Lapets',
    maintainer_email = 'a@lapets.io',
    url              = 'https://github.com/lapets/isqrt',
    description      = 'Efficient native Python implementation of the integer square root function.',
    long_description = open('README.rst').read(),
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
)
