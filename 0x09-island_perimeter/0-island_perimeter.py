#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Returns perimeter of the island grid"""

    sides_2 = 0
    sides_3 = 0
    sides_4 = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
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

                if sides == 4:
                    sides_4 += 1
                # one square in contact with only one square
                # contributes 3 units in the perimeter
                elif sides == 3:
                    sides_3 += 1
                # one square in contact with two squares
                # contributes 2 units in the perimeter
                elif sides == 2:
                    sides_2 += 1

    return ((sides_4 * 4) + (sides_3 * 3) + (sides_2 * 2))
