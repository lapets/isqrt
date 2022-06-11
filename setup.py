from setuptools import setup

with open('README.rst', 'r') as fh:
    long_description = fh.read()

name = 'isqrt'
version = '0.12.0'

setup(
    name=name,
    version=version,
    packages=[name,],
    install_requires=[],
    extras_require={
        'test': [
            'pytest~=7.0',
            'pytest-cov~=3.0'
        ],
        'lint': [
            'pylint~=2.14.0'
        ],
        'coveralls': [
            'coveralls~=3.3.1'
        ],
        'publish': [
            'setuptools~=62.0',
            'wheel~=0.37',
            'twine~=4.0'
        ]
    },
    license='MIT',
    url='https://github.com/lapets/isqrt',
    author='Andrei Lapets',
    author_email='a@lapets.io',
    description='Efficient pure Python implementation of the ' + \
                'integer square root function.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
)
