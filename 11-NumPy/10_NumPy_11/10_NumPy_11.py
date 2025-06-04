# Import numpy library
import numpy as np

# Given that A is 2D array (matrix)
# Slice row in reverse order and fix column
# Example: A = [[1 2] [3 4]], column = 1
# Returns [3 4]
def get_column_from_bottom_to_top(A, column):
    return A[::-1, column]

# Given that A is 2D array (matrix)
# Slice only odd row
# Example: A = [[1 2] [3 4] [5 6] [7 8]]
# Returns [[3 4] [7 8]]
def get_odd_rows(A):
    return A[1::2, :]

# Given that A is 2D array (matrix)
# Fix row and slice only even column
# Example: A = [[1 2 3] [4 5 6]]
# Returns [4 6]
def get_even_column_last_row(A):
    return A[-1, ::2]

# Given that A is 2D array (square matrix)
# Get number from top-left corner down to bottom-right corner
# Example: A = [[1 2 3] [4 5 6] [7 8 9]]
# Returns [1 5 9]
def get_diagonal1(A):
    n = A.shape[0]
    return A[list(range(n)), list(range(n))]

# Given that A is 2D array (square matrix)
# Get number from top-right corner down to bottom-left corner
# Example: A = [[1 2 3] [4 5 6] [7 8 9]]
# Returns [3 5 7]
def get_diagonal2(A):
    n = A.shape[0]
    return A[list(range(n)), list(range(n-1, -1, -1))]

# Execute an input string
exec(input().strip())