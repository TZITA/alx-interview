#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed
    to meet a given amount total.
    """
    if total == 0:
        return 0

    sorted_coins = sorted(coins)
    coins = len(sorted_coins)
    num_coins = 0

    for i in range(1, coins):
        num_each_coin = int(total / sorted_coins[coins - i])
        num_coins += num_each_coin
        total -= (num_each_coin * sorted_coins[coins - i])

    if total == 0:
        return num_coins
    return -1
