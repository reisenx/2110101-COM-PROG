# --------------------------------------------------
# File Name : 11_Numpy_11.py
# Problem   : Indexing and Slicing
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Import numpy library
import numpy as np


# Reverse column of 2D array (matrix)
def get_column_from_bottom_to_top(matrix, col):
    return matrix[::-1, col]


# Get odd rows of 2D array (matrix)
def get_odd_rows(matrix):
    return matrix[1::2]


# Get even rows of the last row of 2D array (matrix)
def get_even_column_last_row(matrix):
    return matrix[-1, ::2]


# Get the diagonal elements of a 2D array (matrix)
# From top-left to bottom-right
def get_diagonal1(matrix):
    idx = np.arange(matrix.shape[0])
    return matrix[idx, idx]


# Get the diagonal elements of a 2D array (matrix)
# From top-right to bottom-left
def get_diagonal2(matrix):
    row_idx = np.arange(matrix.shape[0])
    col_idx = np.arange(matrix.shape[1] - 1, -1, -1)
    return matrix[row_idx, col_idx]


# Execute an input string as code
exec(input().strip())
