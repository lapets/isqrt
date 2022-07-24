=====
isqrt
=====

Efficient pure-Python implementation of the integer square root function.

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
Given an arbitrarily large non-negative integer ``n``, the `integer square root <https://en.wikipedia.org/wiki/Integer_square_root>`__ function finds the largest integer ``r`` such that ``r**2 <= n`` and ``(r + 1)**2 > n``.

.. |math_isqrt| replace:: ``math.isqrt``
.. _math_isqrt: https://docs.python.org/3/library/math.html#math.isqrt

.. |math_sqrt| replace:: ``math.sqrt``
.. _math_sqrt: https://docs.python.org/3/library/math.html#math.sqrt

**The built-in** |math_isqrt|_ **function was introduced in Python 3.8 and should normally be used instead of the function defined in this library.** To provide the best performance possible while retaining backwards-compatible behavior for this library, the implementation in this library invokes |math_isqrt|_ when it is available. If |math_isqrt|_ is not available, this library attempts to use |math_sqrt|_ and then (if |math_sqrt|_ does not produce the correct result or the input is outside the range supported by |math_sqrt|_) defaults to a pure Python implementation in which the number of executed Python arithmetic operations is linear in the bit length of the input integer.

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/isqrt>`__::

    python -m pip install isqrt

The library can be imported in the usual way::

    from isqrt import isqrt

Examples
^^^^^^^^
The exported function ``isqrt`` provides a pure-Python implementation of the `integer square root <https://en.wikipedia.org/wiki/Integer_square_root>`__ algorithm::

    >>> isqrt(4)
    2
    >>> isqrt(16)
    4
    >>> list(map(isqrt, range(16, 26)))
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 5]
    >>> isqrt(2**30000) == 2**15000
    True

Development
-----------
All installation and development dependencies are fully specified in ``pyproject.toml``. The ``project.optional-dependencies`` object is used to `specify optional requirements <https://peps.python.org/pep-0621>`__ for various development tasks. This makes it possible to specify additional options (such as ``test``, ``lint``, and so on) when performing installation using `pip <https://pypi.org/project/pip>`__::

    python -m pip install .[test,lint]

Testing and Conventions
^^^^^^^^^^^^^^^^^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see the ``pyproject.toml`` file for configuration details)::

    python -m pip install .[test]
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__::

    python src/isqrt/isqrt.py -v

Style conventions are enforced using `Pylint <https://pylint.pycqa.org>`__::

    python -m pip install .[lint]
    python -m pylint src/isqrt

Acknowledgments
^^^^^^^^^^^^^^^
The initial version of this function was `posted <http://stackoverflow.com/a/23279113/2738025>`__ on Stack Overflow. A `more efficient version <https://gist.github.com/castle-bravo/e841684d6bad8e0598e31862a7afcfc7>`__ was implemented by Alexander Gosselin. The implementation in this package is adapted directly from these previous implementations.

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/isqrt>`__ for this library.

Versioning
^^^^^^^^^^
Beginning with version 0.10.0, the version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/isqrt>`__ by a package maintainer. First, install the dependencies required for packaging and publishing::

    python -m pip install .[publish]

Ensure that the correct version number appears in the ``pyproject.toml`` file. Create and push a tag for this version (replacing ``?.?.?`` with the version number)::

    git tag ?.?.?
    git push origin ?.?.?

Remove any old build/distribution files. Then, package the source into a distribution archive::

    rm -rf build dist src/*.egg-info
    python -m build --sdist --wheel .

Finally, upload the package distribution archive to `PyPI <https://pypi.org>`__::

    python -m twine upload dist/*
