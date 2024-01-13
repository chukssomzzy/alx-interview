#!/usr/bin/python3

""" LockBoxes """


from typing import List


def canUnlockAll(boxes: List[List]) -> bool:
    """Test if boxes can be unlocked"""
    keys_map = dict(enumerate(boxes))
    unlocked = 1
    for box in range(1, len(boxes)):
        for box_i, keys in keys_map.items():
            if box_i != box and box in keys:
                unlocked += 1
                break
    if (unlocked) == len(boxes):
        return True
    return False
