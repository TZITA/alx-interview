#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Returns perimeter of the island grid
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                sides = 0
                # check the surrounding
                if i == 0:
                    sides += 1
                if j == 0:
                    sides += 1

                try:
                    if grid[i + 1][j] == 0:
                        sides += 1
                except IndexError:
                    sides += 1
                try:
                    if grid[i - 1][j] == 0:
                        sides += 1
                except IndexError:
                    sides += 1
                try:
                    if grid[i][j + 1] == 0:
                        sides += 1
                except IndexError:
                    sides += 1
                try:
                    if grid[i][j - 1] == 0:
                        sides += 1
                except IndexError:
                    sides += 1

                perimeter += sides

    return perimeter
