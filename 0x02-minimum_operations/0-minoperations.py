#!/usr/bin/python3
""" Minimum Operations function """


def minOperations(n: int) -> int:
    """Calculates the minimum number of operations"""
    if type(n) != int:
        return 0
    elif n < 6 or n % 2 != 0:
        return n
    else:
        if n % 4 != 0:
            return int(n / 2 + 2)
        return int(n / 4 + 4)
