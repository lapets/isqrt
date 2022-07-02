"""
Efficient pure-Python implementation of the integer square root function.
"""
from __future__ import annotations
import doctest
import math

def isqrt(n: int) -> int:
    # pylint: disable=R0912,C0301 # Accommodate long link URLs and branch count.
    """
    Returns the largest root such that ``root**2 <= n (root + 1)**2 > n``.
    When using Python 3.8 or later, this function acts as a wrapper for the
    built-in :obj:`math.isqrt` function.

    For all other supported versions of Python, this function reverts to a
    pure Python algorithm that is adapted from an
    `implementation by Alexander Gosselin <https://gist.github.com/castle-bravo/e841684d6bad8e0598e31862a7afcfc7>`__,
    which is based on a `Stack Overflow answer by Tobin Fricke <http://stackoverflow.com/a/23279113/2738025>`__.

    >>> isqrt(4)
    2
    >>> isqrt(16)
    4
    >>> list(map(isqrt, range(16, 26)))
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 5]
    >>> from random import randint
    >>> all([isqrt(r**2 + randint(0, r)) == r  for r in range(0, 1000)])
    True
    >>> r = randint(2**511, 2**512 - 1)
    >>> isqrt(r**2) == r
    True
    >>> isqrt(2**30000) == 2**15000
    True

    The type and sign of the input are checked.

    >>> isqrt(-2)
    Traceback (most recent call last):
      ...
    ValueError: input must be a non-negative integer
    >>> isqrt('abc')
    Traceback (most recent call last):
      ...
    TypeError: input must be an integer

    Test scenarios in which the :obj:`math.isqrt` function is not available.

    >>> if hasattr(math, 'isqrt'):
    ...     delattr(math, 'isqrt')
    >>> isqrt(16)
    4
    >>> isqrt(2**30000) == 2**15000
    True
    >>> isqrt(-2)
    Traceback (most recent call last):
      ...
    ValueError: input must be a non-negative integer
    >>> isqrt('abc')
    Traceback (most recent call last):
      ...
    TypeError: input must be an integer
    """
    # Try using built-in integer square root function (available in Python 3.8 or later).
    # To ensure this implementation is backwards-compatible with previous versions while
    # not introducing performance overheads for the most common case, only convert
    # exceptions if the initial call to the built-in function raises an exception.
    if hasattr(math, 'isqrt'):
        try:
            return math.isqrt(n)
        except ValueError as e:
            if str(e) == 'isqrt() argument must be nonnegative':
                raise ValueError('input must be a non-negative integer') from None
            # Continue to default implementation to ensure backwards-compatible behavior.
        except TypeError as e:
            if str(e).endswith('object cannot be interpreted as an integer'):
                raise TypeError('input must be an integer') from None
            # Continue to default implementation to ensure backwards-compatible behavior.
        except: # pylint: disable=W0702 # pragma: no cover
            pass # Continue to default implementation to ensure backwards-compatible behavior.

    try: # Attempt to use the :obj:`math.sqrt` function.
        root = int(math.sqrt(n))
        if root * root == n: # No error from floating point conversion.
            return root
    except ValueError as e:
        if str(e) == 'math domain error':
            raise ValueError('input must be a non-negative integer') from None
        # Continue to default implementation to ensure backwards-compatible behavior.
    except TypeError as e:
        if str(e).startswith('must be real number'):
            raise TypeError('input must be an integer') from None
        # Continue to default implementation to ensure backwards-compatible behavior.
    except OverflowError:
        pass # Use the integer-only bit-wise algorithm.

    if n is None or (not isinstance(n, int)):
        raise TypeError('input must be an integer') # pragma: no cover

    if n < 0:
        raise ValueError('input must be a non-negative integer') # pragma: no cover

    root = 0 # Running result.
    rmdr = 0 # Running remainder n - root**2.
    for s in reversed(range(0, n.bit_length(), 2)): # Shift n by s bits.
        bits = n >> s & 3 # The next two most significant bits of n.
        rmdr = rmdr << 2 | bits # Increase the remainder.
        cand = root << 2 | 1 # Shifted candidate root value to try.
        bit_next = int(rmdr >= cand) # The next bit in the remainder.
        root = root << 1 | bit_next # Add next bit to running result.
        rmdr -= cand * bit_next # Reduce the remainder if bit was added.
    return root

if __name__ == "__main__":
    doctest.testmod() # pragma: no cover
