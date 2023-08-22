#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed
    to meet a given amount total.
    """
    num_coins = 0

    if total <= 0:
        return 0

    try:
        sorted_coins = sorted(coins)
        coins = len(sorted_coins)
    except Exception:
        return -1

    for i in range(1, coins):
        num_each_coin = int(total / sorted_coins[coins - i])
        num_coins += num_each_coin
        total -= (num_each_coin * sorted_coins[coins - i])

    if total == 0:
        return num_coins
    return -1
