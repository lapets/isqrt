=====
isqrt
=====

Efficient Python implementation of the integer square root function.

|pypi|

.. |pypi| image:: https://badge.fury.io/py/isqrt.svg
   :target: https://badge.fury.io/py/isqrt
   :alt: PyPI version and link.

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
All unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`_::

    python isqrt/isqrt.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    pylint isqrt

Acknowledgments
---------------
The initial version of this function was `posted <http://stackoverflow.com/a/23279113/2738025>`_ on Stack Overflow. A more efficient version was implemented by Alexander Gosselin `here <https://gist.github.com/castle-bravo/e841684d6bad8e0598e31862a7afcfc7>`_. The implementation in this package is adapted almost directly from these previous implementations.
