#!/usr/bin/python3
"""
Solves N queens problem
"""


def create_board(N):
    """Create N*N board
    Args:
        N: represent the row and column of board
    Returns:
        board of N*N size
    """
    return [[0 for _ in range(N)] for _ in range(N)]


def print_board(board):
    """Prints a board
    Args:
        board (list of list): list representation of a board
        N (int): size of board
    Returns:
        None
    """
    printable_board = []
    for i, row in enumerate(board):
        printable_board.append(
            list([i, j] for j, val in enumerate(row) if val)[0])
    print(printable_board)


def is_safe(board, row, col, N):
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


def solve_board(board, row, N):
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
            if solve_board(board, row + 1, N):
                print_board(board)
            board[row][i] = 0
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
