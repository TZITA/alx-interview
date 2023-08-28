#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Returns perimeter of the island grid"""

    sides_2 = 0
    sides_3 = 0

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            sides = 0
            if grid[i][j] == 1:
                # check the surrounding
                if grid[i + 1][j] == 0:
                    sides += 1
                if grid[i - 1][j] == 0:
                    sides += 1
                if grid[i][j + 1] == 0:
                    sides += 1
                if grid[i][j - 1] == 0:
                    sides += 1

                # one square in contact with only one square
                # contributes 3 units in the perimeter
                if sides == 3:
                    sides_3 += 1
                # one square in contact with two squares
                # contributes 2 units in the perimeter
                if sides == 2:
                    sides_2 += 1

    return ((sides_3 * 3) + (sides_2 * 2))
