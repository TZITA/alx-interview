#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Prime Game:
    Attributes:
        1. x: number of rounds
        2. nums: array of n
    Returns:
        1. Name of the player that won the most rounds OR
        2. None
    """
    winner = []
    for n in range(x):
        prime_factors = []
        for i in range(1, nums[n]+1):
            while i % 2 == 0:
                prime_factors.append(2)
                i /= 2

            for j in range(3, int(i ** 0.5) + 1, 2):
                while i % j == 0:
                    prime_factors.append(j)
                    i /= j

            if i > 2:
                prime_factors.append(i)

        if len(prime_factors) % 2 == 0:
            winner.append("Ben")
        else:
            winner.append("Maria")

    if winner.count("Ben") > winner.count("Maria"):
        return "Ben"
    elif winner.count("Ben") < winner.count("Maria"):
        return "Maria"
    else:
        return None
