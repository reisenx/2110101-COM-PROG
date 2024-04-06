import numpy as np

# Returns an 2D array with nrows x ncols size
# Example: mult_table(12,5)
# [[ 1  2  3  4  5  6  7  8  9 10 11 12]
#  [ 2  4  6  8 10 12 14 16 18 20 22 24]
#  [ 3  6  9 12 15 18 21 24 27 30 33 36]
#  [ 4  8 12 16 20 24 28 32 36 40 44 48]
#  [ 5 10 15 20 25 30 35 40 45 50 55 60]]

# == Algorithm ==
# 1.) Create first matrix (Size: nrows x ncols) in the pattern
# > Example: [[1 2 3 4 5 ...]
#             [1 2 3 4 5 ...]
#             [1 2 3 4 5 ...]]
# 2.) Create second matrix (Size: nrows x ncols) in the pattern
# > Example: [[1 1 1 1 1 ...]
#             [2 2 2 2 2 ...]
#             [3 3 3 3 3 ...]]
# 3.) Multiply both matrix and we get the result
def mult_table(nrows, ncols):
    # Create first matrix
    list01 = []
    for i in range(nrows):
        list01.append(list(range(1,ncols+1)))
    matrix01 = np.array(list01)
    
    # Create second matrix
    list02 = []
    for i in range(nrows):
        list02.append([i+1]*ncols)
    matrix02 = np.array(list02)

    table = matrix01 * matrix02
    return table

# Execute an input string
exec(input().strip())