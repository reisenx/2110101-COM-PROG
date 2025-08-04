# --------------------------------------------------
# File Name : 09_Nested_22.py
# Problem   : Matrix
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Return a matrix of n rows as a list of lists.
def read_matrix():
    # Read the number of rows from input
    n = int(input())
    # Read matrix rows from input
    matrix = []
    for _ in range(n):
        row = [float(num) for num in input().split()]
        matrix.append(row)
    return matrix


# Multiply each element of the matrix by a constant c.
def mult_c(const, matrix):
    result = matrix[:]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] *= const
    return result


def mult(a, b):
    # Get the number of rows and columns for A and B
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    # Matrix multiplication
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            num = 0
            for k in range(cols_a):
                num += a[i][k] * b[k][j]
            row.append(num)
        result.append(row)
    return result


# Execute the input string as code
exec(input().strip())
