#!/usr/bin/python3
"""
Provides various function and variables that are used to
manipulate different parts of the Python runtime environment
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at the given row and
    column on the board
    """
    for a in range(col):
        if board[col][a] == 1:
            return False

    for a, b in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[a][b] == 1:
            return False

    for a, b in zip(range(row, n), range(col, -1, -1)):
        if board[a][b] == 1:
            return False

    return True


def solve_nqueens(n):
    """Solve the N-Queens problem and print all possible solutions."""

    if not isinstance(n, int):
        raise ValueError("N must be a number")

    if n < 4:
        raise ValueError("N must be at least 4")

    board = [[0] * n for _ in range(n)]

    def print_solution(board):
        solution = []
        for a in range(n):
            for b in range(n):
                if board[a][b] == 1:
                    solution.append([a, b])
        return solution

    def backtrack(row):
        """Recursively backtrack to find all solutions."""

        if row == n:
            solution = print_solution(board)
            for row in solution:
                print(row)
            print()

        for col in range(n):
            if is_safe(board, row, col, n):

                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
