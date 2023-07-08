#!/usr/bin/python3
""" Lockboxes Challenge """


def canUnlockAll(boxes):
    """
     A function that determines if all the boxes(lists) can be opened.
    """
    keys = set()
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            if boxes[i][j] != i:
                keys.add(boxes[i][j])

    if (len(keys) >= len(boxes) - 1):
        return True
    return False
