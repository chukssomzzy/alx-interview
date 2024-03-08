#!/usr/bin/python3


"""Find island perimeter"""


def island_perimeter(grid):
    """Find island perimeter
    Args:
        grid (list of list): grid representing a map of land (1) and water (0)
    Returns:
        int: Perimeter of the island
    """
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]  # Kee

    def dfs(i, j):

        """
        Depth-First Search to explore connected island cells
        """
        if (i < 0 or i >= rows or j < 0 or j >= cols or (grid[i][j] == 0
                                                         ) or visited[i][j]):
            return 0  # Reached water or visited cell, no perimeter adde
        visited[i][j] = True  # Mark cell as visited

        perimeter = 0  # Initialize perimeter for this island branch
        perimeter += 1 if i == 0 or grid[i - 1][j] == 0 else 0
        perimeter += 1 if i == rows - 1 or grid[i + 1][j] == 0 else 0
        perimeter += 1 if j == 0 or grid[i][j - 1] == 0 else 0
        perimeter += 1 if j == cols - 1 or grid[i][j + 1] == 0 else 0  #

        # Explore unvisited connected land cells recursively
        perimeter += dfs(i - 1, j)
        perimeter += dfs(i + 1, j)
        perimeter += dfs(i, j - 1)
        perimeter += dfs(i, j + 1)

        return perimeter

    # Find a starting land cell and perform DFS
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                return dfs(i, j)

    return 0
