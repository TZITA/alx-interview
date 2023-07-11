#!/usr/bin/python3


def minOperations(n: int) -> int:
    if n < 6 or n % 2 != 0:
        return n
