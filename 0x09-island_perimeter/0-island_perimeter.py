#!/usr/bin/python3


"""Find island perimeter"""


def island_perimeter(grid):
    """Find island perimeter
    Args:
        grid (list of list): grid
    """
    island = 0
    for i in range(1, len(grid) - 1, 1):
        for j in range(1, len(grid[0]) - 1, 1):
            if grid[i][j] == 1:
                if island:
                    return 0
                island = find_island(grid, i, j)
    return (island + 1) * 2


def find_island(grid, i, j):
    """Find connected island"""
    if i == len(grid) - 1 or i == 0 or j == 0 or\
            j == len(grid[0]) - 1 or grid[i][j] == 2:
        return 0
    if not grid[i][j] or grid[i][j] == 2:
        return 0
    grid[i][j] = 2
    return (1 + find_island(grid, i - 1, j) + find_island(
        grid, i + 1, j) + find_island(grid, i, j + 1) + find_island(
            grid, i, j - 1))
