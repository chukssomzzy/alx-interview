#!/usr/bin/python3
"""
Solves N queens problem
"""


from typing import List


def create_board(N: int) -> List[List[int]]:
    """Create N*N board
    Args:
        N: represent the row and column of board
    Returns:
        board of N*N size
    """
    return [[0 for _ in range(N)] for _ in range(N)]


def print_board(board: List[List[int]], N: int) -> None:
    """Prints a board
    Args:
        board (list of list): list representation of a board
        N (int): size of board
    Returns:
        None
    """
    for row in board:
        print(" ".join(map(str, row)))
    print()


def is_safe(board: List[List[int]], row: int, col: int, N: int) -> bool:
    """Check if the position a queen is to be inserted is not under attack
    Args:
        board (list of list): A representation of a board
        row (int): rank position of a queen
        col (int): files position of a queen
    Returns:
        bool
    """

    for i in range(row - 1, -1, -1):
        if board[i][col]:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j]:
            return False
    return True


def solve_board(board: List[List[int]], row: int, N: int) -> bool:
    """Find all possible position N queens can be put in a
    N*N square without attacking each other
    Args:
        board: representation of a board in memory
        row: current row to position queen in
        N: size of board
    Returns:
        board
    SideEffect:
        print board
    """
    if row >= N:
        return True
    for i in range(N):
        if is_safe(board, row, i, N):
            board[row][i] = 1
            if not solve_board(board, row + 1, N):
                board[row][i] = 0
            else:
                print_board(board, N)
                continue

    return False


def main():
    """Control flow of execution of program"""
    import sys
    N = 0
    try:
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            exit(1)
        elif int(sys.argv[1]) < 4:
            print("N must be at least 4")
            exit(1)
    except (ValueError):
        print("N must be a number")
        exit(1)

    N = int(sys.argv[1])
    board = create_board(N)
    solve_board(board, 0, N)


if __name__ == "__main__":
    main()
