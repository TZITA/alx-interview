#!/usr/bin/python3
""" Minimum Operations function """


def minOperations(n: int) -> int:
    """Calculates the minimum number of operations"""
    if n < 6 or n % 2 != 0:
        return n
