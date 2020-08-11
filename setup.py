from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="isqrt",
    version="0.10.0",
    packages=["isqrt",],
    install_requires=[],
    license="MIT",
    maintainer="Andrei Lapets",
    maintainer_email="a@lapets.io",
    url="https://github.com/lapets/isqrt",
    description="Efficient native Python implementation of the "+\
                "integer square root function.",
    long_description=open("README.rst").read(),
    test_suite="nose.collector",
    tests_require=["nose"],
)
