import numpy as np

# Returns sum of 2 row that close to each other
# Example:
# M = [[ 0  1  2  3] --> sum = [[ 0+4  1+5   2+6   3+7]
#      [ 4  5  6  7]            [8+12 9+13 10+14 11+15]]
#      [ 8  9 10 11]
#      [12 13 14 15]]
def sum_2_rows(M):
    odd_rows = M[0::2, :]
    even_rows = M[1::2, :]
    return odd_rows + even_rows

# Returns sum of first half and second half (left-right)
# Example:
# M = [[ 0  1  2  3  4  5] --> sum = [[  0+3   1+4   2+5]
#      [ 6  7  8  9 10 11]            [  6+9  7+10  8+11]
#      [12 13 14 15 16 17]            [12+15 13+16 14+17]
#      [18 19 20 21 22 23]]           [18+21 19+22 20+23]]
def sum_left_right(M):
    ncols = len(M[0])
    left_half = M[:, 0:ncols//2]
    right_half = M[:, ncols//2:]
    return left_half + right_half

# Returns sum of first half and second half (upper-lower)
# Example:
# M = [[ 0  1  2  3] --> sum = [[0+12 1+13  2+14  3+15]
#      [ 4  5  6  7]            [4+16 5+17  6+18  7+19]
#      [ 8  9 10 11]            [8+20 9+21 10+22 11+23]]
#      [12 13 14 15]
#      [16 17 18 19]
#      [20 21 22 23]]
def sum_upper_lower(M):
    nrows = len(M)
    upper_half = M[0:nrows//2]
    lower_half = M[nrows//2:]
    return upper_half + lower_half

# Returns sum of each element when divide to 4 quadrants
# Example:
# M = [[ 0  1  2  3] --> sum = [[0+2+8+10   1+3+9+11]
#      [ 4  5  6  7]            [4+6+12+14 5+7+13+15]]
#      [ 8  9 10 11]
#      [12 13 14 15]]
def sum_4_quadrants(M):
    nrows = len(M)
    ncols = len(M[0])
    Q1 = M[0:nrows//2, 0:ncols//2]
    Q2 = M[0:nrows//2, ncols//2:]
    Q3 = M[nrows//2:, 0:ncols//2]
    Q4 = M[nrows//2:, ncols//2:]
    return Q1 + Q2 + Q3 + Q4

# Returns sum of cell of 4 element
# Example:
# M = [[ 0  1  2  3  4  5] --> sum = [[    0+1+6+7     2+3+8+9   4+5+10+11]
#      [ 6  7  8  9 10 11]            [12+13+18+19 14+15+20+21 16+17+22+23]]
#      [12 13 14 15 16 17]
#      [18 19 20 21 22 23]]
def sum_4_cells(M):
    upper_left = M[0::2, 0::2]
    upper_right = M[0::2, 1::2]
    lower_left = M[1::2, 0::2]
    lower_right = M[1::2, 1::2]
    return upper_left + upper_right + lower_left + lower_right

# Returns how many years in 'years' array is leap year
# Example: years = [2543 2559 2560] --> [2000 2016 2017] --> [True True False] --> 2
# Make sure to use bitwise operation (AND is '&') (OR is '|')
def count_leap_years(years):
    years = years - 543
    leap_check = (years % 400 == 0) | ((years % 100 != 0) & (years % 4 == 0))
    count = np.sum(leap_check)
    return count

# Execute an input string
exec(input().strip())