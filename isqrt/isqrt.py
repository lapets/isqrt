"""
Efficient native Python implementation of the integer square root function.
"""
from __future__ import annotations
import doctest
from math import sqrt

def isqrt(n: int) -> int:
    """
    Returns the largest root such that ``root**2 <= n (root + 1)**2 > n``.

    This implementation is adapted from the sources below:
    * https://gist.github.com/castle-bravo/e841684d6bad8e0598e31862a7afcfc7
    * http://stackoverflow.com/a/23279113/2738025

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
    >>> isqrt('abc')
    Traceback (most recent call last):
      ...
    TypeError: input must be an integer
    >>> isqrt(-2)
    Traceback (most recent call last):
      ...
    ValueError: input must be a non-negative integer
    """
    if n is None or (not isinstance(n, int)):
        raise TypeError("input must be an integer")

    if n < 0:
        raise ValueError("input must be a non-negative integer")

    try: # Attempt to use the native math library's sqrt function.
        root = int(sqrt(n))
        if pow(root, 2) == n: # No error from floating point conversion.
            return root
    except OverflowError: # Use the integer-only bit-wise algorithm.
        pass

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
