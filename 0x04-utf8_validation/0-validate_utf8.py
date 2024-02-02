#!/usr/bin/python3
"""Validate utf8"""


from typing import List


def validUTF8(data: List[int]) -> bool:
    """Validate utf8"""
    n_byte = 0

    for byte in data:
        if not n_byte:
            if byte >> 7 != 0:
                return False
            elif byte >> 5 == 0b110:
                n_byte = 1
            elif byte >> 4 == 0b1110:
                n_byte = 2
            elif byte >> 3 == 0b11110:
                n_byte = 3
            else:
                return False
        else:
            print(n_byte)
            if byte >> 6 == 0b10 and n_byte:
                n_byte -= 1
            else:
                return False
    return (n_byte == 0)
