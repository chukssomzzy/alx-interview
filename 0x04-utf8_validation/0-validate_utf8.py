#!/usr/bin/python3
"""Validate utf8"""


from typing import List


def validUTF8(data: List[int]) -> bool:
    """Validate utf8"""
    n_byte = 0
    c_ra_str = 128
    c_ra_end = 191
    max_byte = 247

    for byte in data:
        if byte > max_byte:
            return False
        if not n_byte:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110 and c_ra_str > byte < c_ra_end:
                n_byte += 1
            elif byte >> 4 == 0b1110 and c_ra_str > byte < c_ra_end:
                n_byte += 2
            elif byte >> 3 == 0b11110 and c_ra_str > byte < c_ra_end:
                n_byte += 3
            elif byte >> 2 == 0b111110 and c_ra_str > byte < c_ra_end:
                n_byte += 4
            else:
                return False
        else:
            print(n_byte)
            if byte >> 6 == 0b10 and n_byte:
                n_byte -= 1
            else:
                return False
    return True
