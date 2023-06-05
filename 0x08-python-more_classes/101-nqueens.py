#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys

def is_safe(board, row, col, N):
    # Check if the current position is safe for a queen

    # Check row on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens(N):
    # Create an empty chessboard
    board = [['.' for _ in range(N)] for _ in range(N)]

    # Recursive function to solve the N-queens problem
    def solve_util(board, col):
        if col >= N:
            # All queens have been placed, print the solution
            print_solution(board)
            return

        for row in range(N):
            if is_safe(board, row, col, N):
                # Place the queen and recursively solve the problem for
		# the next column
                board[row][col] = 'Q'
                solve_util(board, col + 1)
                # Backtrack and remove the queen to explore other possibilities
                board[row][col] = '.'

    def print_solution(board):
        # Print the current solution
        for row in board:
            print(' '.join(row))
        print()

    # Start solving the problem
    solve_util(board, 0)

# Main program
if __name__ == '__main__':
    # Check the number of arguments
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    # Get the value of N from command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    # Solve the N-queens problem
    solve_nqueens(N)
