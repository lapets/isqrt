=====
isqrt
=====

Efficient Python implementation of the integer square root function.

|pypi| |actions| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/isqrt.svg
   :target: https://badge.fury.io/py/isqrt
   :alt: PyPI version and link.

.. |actions| image:: https://github.com/lapets/isqrt/workflows/lint-test-cover-docs/badge.svg
   :target: https://github.com/lapets/isqrt/actions/workflows/lint-test-cover-docs.yml
   :alt: GitHub Actions status.

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/isqrt/badge.svg?branch=master
   :target: https://coveralls.io/github/lapets/isqrt?branch=master
   :alt: Coveralls test coverage summary.

Purpose
-------
Given an arbitrarily large non-negative integer :code:`n`, the `integer square root <https://en.wikipedia.org/wiki/Integer_square_root>`_ function finds the largest integer :code:`r` such that :code:`r**2 <= n` and :code:`(r+1)**2 > n`. The running time is linear in the bit length of the input integer.

Package Installation and Usage
------------------------------
The package is available on `PyPI <https://pypi.org/project/isqrt/>`_::

    python -m pip install isqrt

The library can be imported in the usual way::

    from isqrt import isqrt

The function ``isqrt`` is an efficient implementation of the `integer square root <https://en.wikipedia.org/wiki/Integer_square_root>`_ algorithm::

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
All unit tests are executed and their coverage is measured when using `nose <https://nose.readthedocs.io/>`_ (see ``setup.cfg`` for configution details)::

    python -m pip install nose coverage
    nosetests --cover-erase

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`_::

    python isqrt/isqrt.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    python -m pip install pylint
    pylint isqrt

Acknowledgments
---------------
The initial version of this function was `posted <http://stackoverflow.com/a/23279113/2738025>`_ on Stack Overflow. A more efficient version was implemented by Alexander Gosselin `here <https://gist.github.com/castle-bravo/e841684d6bad8e0598e31862a7afcfc7>`_. The implementation in this package is adapted almost directly from these previous implementations.

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/isqrt>`_ for this library.

Versioning
----------
Beginning with version 0.10.0, the version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.
