=====
isqrt
=====

Efficient pure Python implementation of the integer square root function.

|pypi| |actions| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/isqrt.svg
   :target: https://badge.fury.io/py/isqrt
   :alt: PyPI version and link.

.. |actions| image:: https://github.com/lapets/isqrt/workflows/lint-test-cover/badge.svg
   :target: https://github.com/lapets/isqrt/actions/workflows/lint-test-cover.yml
   :alt: GitHub Actions status.

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/isqrt/badge.svg?branch=main
   :target: https://coveralls.io/github/lapets/isqrt?branch=main
   :alt: Coveralls test coverage summary.

Purpose
-------
Given an arbitrarily large non-negative integer :code:`n`, the `integer square root <https://en.wikipedia.org/wiki/Integer_square_root>`__ function finds the largest integer :code:`r` such that :code:`r**2 <= n` and :code:`(r + 1)**2 > n`. The number of Python arithmetic operations executed during an invocation of the function is linear in the bit length of the input integer.

.. |math_isqrt| replace:: ``math.isqrt``
.. _math_isqrt: https://docs.python.org/3/library/math.html#math.isqrt

The built-in |math_isqrt|_ function was introduced in Python 3.8 and should be used instead of the function defined in this package.

Package Installation and Usage
------------------------------
The package is available on `PyPI <https://pypi.org/project/isqrt>`__::

    python -m pip install isqrt

The library can be imported in the usual way::

    from isqrt import isqrt

The function ``isqrt`` is an efficient implementation of the `integer square root <https://en.wikipedia.org/wiki/Integer_square_root>`__ algorithm::

    >>> isqrt(4)
    2
    >>> isqrt(16)
    4
    >>> list(map(isqrt, range(16, 26)))
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 5]
    >>> isqrt(2**30000) == 2**15000
    True

Testing and Conventions
-----------------------
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see ``setup.cfg`` for configuration details)::

    python -m pip install pytest pytest-cov
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__::

    python isqrt/isqrt.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org>`__::

    python -m pip install pylint
    python -m pylint egcd

Acknowledgments
---------------
The initial version of this function was `posted <http://stackoverflow.com/a/23279113/2738025>`__ on Stack Overflow. A `more efficient version <https://gist.github.com/castle-bravo/e841684d6bad8e0598e31862a7afcfc7>`__ was implemented by Alexander Gosselin. The implementation in this package is adapted directly from these previous implementations.

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/isqrt>`__ for this library.

Versioning
----------
Beginning with version 0.10.0, the version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
----------
This library can be published as a `package on PyPI <https://pypi.org/project/isqrt>`__ by a package maintainer. Install the `wheel <https://pypi.org/project/wheel>`__ package, remove any old build/distribution files, and package the source into a distribution archive::

    python -m pip install wheel
    rm -rf dist *.egg-info
    python setup.py sdist bdist_wheel

Next, install the `twine <https://pypi.org/project/twine>`__ package and upload the package distribution archive to `PyPI <https://pypi.org>`__::

    python -m pip install twine
    python -m twine upload dist/*
