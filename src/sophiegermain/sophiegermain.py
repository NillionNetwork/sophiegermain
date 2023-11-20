"""
Pure-Python library that provides a selection of Sophie Germain primes.
"""
from __future__ import annotations
import doctest

_DATA = [
    2,
    5,
    11,
    23,
    41,
    83,
    131,
    281,
    593,
    1031,
    2063,
    4211,
    8243,
    16421,
    32771,
    65633,
    131321,
    262193,
    524351,
    1048583,
    2097169,
    4194319,
    8388617,
    16777259,
    33554467,
    67108879,
    134217757,
    268435459,
    536870923,
    1073741827,
    2147483659
]

def sophiegermain(bit_length: int) -> int:
    """
    Return the smallest Sophie Germain prime that can be represented using
    the specified number of bits.
    
    >>> sophiegermain(2)
    2
    >>> sophiegermain(8)
    131

    The result returned by :obj:`sophiegermain` can always be represented
    using the specified number of bits.
    
    >>> all([sophiegermain(k).bit_length() == k for k in range(2, 33)])
    True

    If a bit length outside the supported range is supplied, an
    exception is raised.

    >>> sophiegermain(-1)
    Traceback (most recent call last):
      ...
    ValueError: all Sophie Germain primes have bit lengths of at least 2
    >>> sophiegermain(1)
    Traceback (most recent call last):
      ...
    ValueError: all Sophie Germain primes have bit lengths of at least 2
    >>> sophiegermain(33)
    Traceback (most recent call last):
      ...
    ValueError: bit lengths greater than 32 are not supported

    The supplied bit length must be an integer.
    
    >>> sophiegermain('abc')
    Traceback (most recent call last):
      ...
    TypeError: bit length must be an integer
    """
    if not isinstance(bit_length, int):
        raise TypeError('bit length must be an integer')

    if bit_length < 2:
        raise ValueError(
            'all Sophie Germain primes have bit lengths of at least 2'
        )

    if bit_length > len(_DATA) + 1:
        raise ValueError(
            'bit lengths greater than ' + str(len(_DATA) + 1) + ' are not supported'
        )

    return _DATA[bit_length - 2]

if __name__ == '__main__':
    doctest.testmod()
