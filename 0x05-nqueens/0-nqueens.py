#!/usr/bin/python3
"""N non-attacking queens in NxN chess board"""
import sys


def is_safe(board, row, col, N):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_n_queens(board, row, N, solutions):
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_n_queens(board, row + 1, N, solutions)


def n_queens(N):
    board = [-1] * N
    solutions = []
    solve_n_queens(board, 0, N, solutions)
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # if N is < 4, impossible to have non-attacking positions of the queens
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = n_queens(N)
    for solution in solutions:
        print(solution)
