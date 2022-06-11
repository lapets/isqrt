from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="isqrt",
    version="0.12.0",
    packages=["isqrt",],
    install_requires=[],
    license="MIT",
    url="https://github.com/lapets/isqrt",
    author="Andrei Lapets",
    author_email="a@lapets.io",
    description="Efficient native Python implementation of the "+\
                "integer square root function.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
)
