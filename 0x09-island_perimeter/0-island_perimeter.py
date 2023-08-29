#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Returns perimeter of the island grid
    """
    perimeter = 0

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == 1:
                sides = 0
                # check the surrounding
                if grid[i + 1][j] == 0:
                    sides += 1
                if grid[i - 1][j] == 0:
                    sides += 1
                if grid[i][j + 1] == 0:
                    sides += 1
                if grid[i][j - 1] == 0:
                    sides += 1

                perimeter += sides

    return perimeter
