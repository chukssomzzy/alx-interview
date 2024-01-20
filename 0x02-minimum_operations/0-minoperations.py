#!/usr/bin/env python3
"""Find minimum operation"""
import math


def minOperations(n: int) -> int:
    """GET THE MINIMUM OPERATIONS"""
    if n == 1 or n == 0:
        return 0
    if not n % 2:
        ops = minOperations(math.floor(n / 2)) + 2
    elif math.floor(math.sqrt(n)) ** 2 == n:
        ops = minOperations(math.floor(math.sqrt(n))) \
            + math.floor(math.sqrt(n))
    else:
        ops = n
    return ops
