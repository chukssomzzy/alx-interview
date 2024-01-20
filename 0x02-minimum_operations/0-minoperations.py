#!/usr/bin/python3
"""Find minimum operation"""
import math
from typing import Tuple, Union


def minOperations(n: int) -> int:
    """GET THE MINIMUM OPERATIONS"""
    fac: Union[Tuple[int, int], None]
    if n == 1 or n == 0 or n < 0:
        return 0

    if not n % 2:
        ops = minOperations(math.floor(n / 2)) + 2
    elif fac := factor(n):
        ops = minOperations(fac[1]) + fac[0]
    elif math.floor(math.sqrt(n)) ** 2 == n:
        ops = minOperations(math.floor(math.sqrt(n))) \
            + math.floor(math.sqrt(n))
    else:
        ops = n
    return ops


def factor(n: int) -> Union[Tuple[int, int], None]:
    """Get all factors of a number"""

    for i in range(2, math.floor(math.sqrt(n))):
        for j in range(2, math.floor(n / 2)):
            if i * j == n:
                return (i, j)
    return None
