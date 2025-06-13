# --------------------------------------------------
# File Name : 09_Nested_22.py
# Problem   : Matrix
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Return a matrix of n rows as a list of lists.
def read_matrix() -> list:
    # Read the number of rows from input
    n = int(input())
    # Read matrix rows from input
    matrix = []
    for _ in range(n):
        row = [float(num) for num in input().split()]
        matrix.append(row)
    return matrix


# Multiply each element of the matrix by a constant c.
def mult_c(c: int, A: list) -> list:
    new_matrix = A[:]
    for i in range(len(A)):
        for j in range(len(A[i])):
            new_matrix[i][j] *= c
    return new_matrix


def mult(A: list, B: list) -> list:
    # Get the number of rows and columns for A and B
    n = len(A)
    m = len(A[0])
    p = len(B[0])

    # Matrix multiplication
    result = []
    for i in range(n):
        row = []
        for j in range(p):
            num = 0
            for k in range(m):
                num += A[i][k] * B[k][j]
            row.append(num)
        result.append(row)
    return result


# Execute the input string as code
exec(input().strip())
