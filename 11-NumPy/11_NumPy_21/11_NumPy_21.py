# --------------------------------------------------
# File Name : 11_Numpy_21.py
# Problem   : Slicing and Element-wise Operation
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

import numpy as np


# Sum every two rows of a 2D array
def sum_2_rows(M: np.ndarray) -> np.ndarray:
    return M[::2] + M[1::2]


# Split a 2D array into left and right halves, and sum the elements in each half
def sum_left_right(M: np.ndarray) -> np.ndarray:
    mid = M.shape[1] // 2
    return M[:, :mid] + M[:, mid:]


# Split a 2D array into upper and lower halves, and sum the elements in each half
def sum_upper_lower(M: np.ndarray) -> np.ndarray:
    mid = M.shape[0] // 2
    return M[:mid] + M[mid:]


# Split a 2D array into four quadrants and sum the elements in each quadrant
def sum_4_quadrants(M: np.ndarray) -> np.ndarray:
    mid_row = M.shape[0] // 2
    mid_col = M.shape[1] // 2
    q1 = M[:mid_row, :mid_col]
    q2 = M[:mid_row, mid_col:]
    q3 = M[mid_row:, :mid_col]
    q4 = M[mid_row:, mid_col:]
    return q1 + q2 + q3 + q4


# Sum every four cells in a 2D array by grouping them into 2x2 blocks
def sum_4_cells(M: np.ndarray) -> np.ndarray:
    return M[::2, ::2] + M[::2, 1::2] + M[1::2, ::2] + M[1::2, 1::2]


# Count the number of leap years in a given array of years
def count_leap_years(years: np.ndarray) -> int:
    y = years - 543
    return np.sum((y % 400 == 0) | ((y % 100 != 0) & (y % 4 == 0)))


# Execute an input string as code
exec(input().strip())
