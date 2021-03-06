=====
isqrt
=====

Efficient Python implementation of the integer square root function.

|pypi| |travis| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/isqrt.svg
   :target: https://badge.fury.io/py/isqrt
   :alt: PyPI version and link.

.. |travis| image:: https://travis-ci.com/lapets/isqrt.svg?branch=master
    :target: https://travis-ci.com/lapets/isqrt

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/isqrt/badge.svg?branch=master
   :target: https://coveralls.io/github/lapets/isqrt?branch=master

Purpose
-------
Given an arbitrarily large non-negative integer :code:`n`, finds the largest integer :code:`r` such that :code:`r**2 <= n` and :code:`(r+1)**2 > n`. The running time is linear in the bit length of the integer.

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install isqrt

The library can be imported in the usual way::

    from isqrt import isqrt

Testing and Conventions
-----------------------
All unit tests are executed and their coverage is measured when using `nose <https://nose.readthedocs.io/>`_ (see ``setup.cfg`` for configution details)::

    nosetests

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`_::

    python isqrt/isqrt.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    pylint isqrt

Acknowledgments
---------------
The initial version of this function was `posted <http://stackoverflow.com/a/23279113/2738025>`_ on Stack Overflow. A more efficient version was implemented by Alexander Gosselin `here <https://gist.github.com/castle-bravo/e841684d6bad8e0598e31862a7afcfc7>`_. The implementation in this package is adapted almost directly from these previous implementations.

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the GitHub page for this library.

Versioning
----------
Beginning with version 0.10.0, the version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.
