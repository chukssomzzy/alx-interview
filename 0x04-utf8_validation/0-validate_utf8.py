#!/usr/bin/python3
"""Validate utf8"""


from typing import List


def validUTF8(data: List[int]) -> bool:
    """Validate utf8"""
    b_seen = 0
    b_expec = 0
    b_len = 8
    for code_point in data:
        if code_point >= 256:
            return False
        b = f"{code_point:08b}"
        for i in range(b_len):
            current_b = int(b[i], base=2)
            next_b = 0
            if i < (b_len - 1):
                next_b = int(b[i + 1], base=2)
            if not i and not current_b and not b_expec:
                break
            elif not i and current_b and not next_b:
                b_seen += 1
                break
            elif b_expec < 4 and not b_seen and current_b and next_b:
                b_expec += 1
            elif b_expec < 4 and not b_seen and current_b and not next_b:
                break
            elif b_expec == 1 and current_b == 1:
                return False  # Reject overlong encoding
            else:
                return False
            if b_seen == b_expec:
                b_seen = 0
                b_expec = 0
                break
    if b_seen != b_expec:
        return False
    return True
