#!/usr/bin/python3
"""N non-attacking queens in NxN chess board"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

# if N is < 4, impossible to have non-attacking positions of the queens
if N < 4:
    print("N must be at least 4")
    exit(1)

else:
    print(sys.argv[1])
