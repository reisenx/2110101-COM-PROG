# --------------------------------------------------
# File Name : 09_Nested_34.py
# Problem   : Fill in Numbers
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# ---------- Patterns 01 ----------
# rows is the number of rows
# cols is the number of columns
# [[ 1,  2,  3,  4,  5,  6,  7],
#  [ 8,  9, 10, 11, 12, 13, 14],
#  [15, 16, 17, 18, 19, 20, 21]]
def pattern1(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Calculate the number based on row and column indices
            num = (i * cols) + j + 1
            row.append(num)
        # Add each row to a matrix
        matrix.append(row)
    return matrix


# ---------- Patterns 02 ----------
# rows is the number of rows
# cols is the number of columns
# [[1, 4, 7, 10, 13, 16, 19],
#  [2, 5, 8, 11, 14, 17, 20],
#  [3, 6, 9, 12, 15, 18, 21]]
def pattern2(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Calculate the number based on row and column indices
            num = (j * rows) + i + 1
            row.append(num)
        # Add each row to a matrix
        matrix.append(row)
    return matrix


# ---------- Patterns 03 ----------
# N is the number of rows and columns
# [[1, 2,  3,  4,  5],
#  [0, 6,  7,  8,  9],
#  [0, 0, 10, 11, 12],
#  [0, 0,  0, 13, 14],
#  [0, 0,  0,  0, 15]]
def pattern3(rows):
    num = 0
    matrix = []
    for i in range(rows):
        # Create a row with zeros at the beginning
        row = [0] * i
        for _ in range(i, rows):
            # Append the current number to the row
            num += 1
            row.append(num)
        # Add each row to a matrix
        matrix.append(row)
    return matrix


# ---------- Patterns 04 ----------
# N is the number of rows and columns
# [[1, 3, 6, 10, 15],
#  [0, 2, 5,  9, 14],
#  [0, 0, 4,  8, 13],
#  [0, 0, 0,  7, 12],
#  [0, 0, 0,  0, 11]]
def pattern4(rows):
    matrix = []
    for i in range(rows):
        # Create a row with zeros at the beginning
        row = [0] * i
        # Calculate the first number in the row
        num = (i * (i + 1)) // 2 + 1
        for j in range(i, rows):
            # Append the current number to the row
            row.append(num)
            # Get the next number by adding (j + 2)
            num += j + 2
        # Add each row to a matrix
        matrix.append(row)
    return matrix


# ---------- Patterns 05 ----------
# N is the number of rows and columns
# [[1, 6, 10, 13, 15],
#  [0, 2,  7, 11, 14],
#  [0, 0,  3,  8, 12],
#  [0, 0,  0,  4,  9],
#  [0, 0,  0,  0,  5]]
def pattern5(rows):
    matrix = []
    for i in range(rows):
        # Create a row with zeros at the beginning
        row = [0] * i
        # Calculate the first number in the row
        num = i + 1
        for j in range(rows - i):
            # Append the current number to the row
            row.append(num)
            # Get the next number by adding (N - i - j)
            num += rows - j
        # Add each row to a matrix
        matrix.append(row)
    return matrix


# ---------- Patterns 06 ----------
# N is the number of rows and columns
# [[1, 9, 10, 14, 15],
#  [0, 2,  8, 11, 13],
#  [0, 0,  3,  7, 12],
#  [0, 0,  0,  4,  6],
#  [0, 0,  0,  0,  5]]
def pattern6(rows):
    # Initialize the matrix with zeros
    matrix = []
    for i in range(rows):
        matrix.append([0] * i)

    # Fill the matrix with numbers
    num = 1
    for j in range(rows):
        for i in range(rows - j):
            if j % 2 == 0:
                matrix[i].append(num)
            else:
                matrix[rows - j - (i + 1)].append(num)
            num += 1
    return matrix


# Execute an input string
exec(input().strip())
