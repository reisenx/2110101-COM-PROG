# Pattern 1
# Example: pattern1(3,7)
# [[1, 2, 3, 4, 5, 6, 7],
#  [8, 9, 10,11,12,13,14],
#  [15,16,17,18,19,20,21]]
def pattern1 (nrows, ncols):
    # Set initial number as 1
    num = 1
    # Create nrows x ncols matrix
    matrix = []
    for i in range(nrows):
        row = []
        for j in range(ncols):
            row.append(num)
            num += 1
        # Add each row to a matrix
        matrix.append(row)
    return matrix

# Pattern 2
# Example: pattern2(3,7)
# [[1, 4, 7, 10, 13, 16, 19],   <-- start at 1 and increase by 3 (nrows = 3)
#  [2, 5, 8, 11, 14, 17, 20],   <-- start at 2 and increase by 3 (nrows = 3)
#  [3, 6, 9, 12, 15, 18, 21]]   <-- start at 3 and increase by 3 (nrows = 3)
def pattern2(nrows,ncols):
    # Create nrows x ncols matrix
    matrix = []
    for i in range(1, nrows+1):
        num = i
        row = []
        for j in range(ncols):
            row.append(num)
            num += nrows
        # Add each row to a matrix
        matrix.append(row)
    return matrix

# Pattern 3
# Example: pattern3(5)
# [[1, 2, 3,  4,  5],   <-- Has 0 '0' and 5-0 = 5 numbers
#  [0, 6, 7,  8,  9],   <-- Has 1 '0' and 5-1 = 4 numbers
#  [0, 0, 10, 11, 12],  <-- Has 2 '0' and 5-2 = 3 numbers
#  [0, 0, 0,  13, 14],  <-- Has 3 '0' and 5-3 = 2 numbers
#  [0, 0, 0,  0,  15]]  <-- Has 4 '0' and 5-4 = 1 number
def pattern3(N):
    # Set initial number as 1
    num = 1
    # Create N x N matrix
    matrix = []
    for i in range(N):
        # Add 0 before adding a number
        row = [0]*i
        # Add number after 0
        for j in range(i,N):
            row.append(num)
            num += 1
        # Add each row to a matrix
        matrix.append(row)
    return matrix

# Pattern 4
# Example: pattern4(5)
# [[1, 3, 6, 10, 15],   <-- Has 0 '0' and 5-0 = 5 numbers | start at 1       then +2 +3 +4 +5
#  [0, 2, 5, 9,  14],   <-- Has 1 '0' and 5-1 = 4 numbers | start at 2 (1+1) then +3 +4 +5
#  [0, 0, 4, 8,  13],   <-- Has 2 '0' and 5-2 = 3 numbers | start at 4 (2+2) then +4 +5
#  [0, 0, 0, 7,  12],   <-- Has 3 '0' and 5-3 = 2 numbers | start at 7 (4+3) then +5
#  [0, 0, 0, 0,  11]]   <-- Has 4 '0' and 5-4 = 1 number  | start at 11 (7+4)
def pattern4(N):
    # Set initial start number at row 1
    start = 1
    # Create N x N matrix
    matrix = []
    for i in range(N):
        # Add 0 before adding a number
        row = [0]*i
        # Setup a start number of each row
        start += i
        # Calculate numbers after 0
        num = start
        for j in range(i,N):
            row.append(num)
            num += j+2
        # Add each row to a matrix
        matrix.append(row)
    return matrix

# Pattern 5
# Example: pattern5(5)
# [[1, 6, 10, 13, 15],  <-- Has 0 '0' and 5-0 = 5 numbers | start at 1 then +5 +4 +3 +2
#  [0, 2, 7,  11, 14],  <-- Has 1 '0' and 5-1 = 4 numbers | start at 2 then +5 +4 +3
#  [0, 0, 3,  8,  12],  <-- Has 2 '0' and 5-2 = 3 numbers | start at 3 then +5 +4
#  [0, 0, 0,  4,  9],   <-- Has 3 '0' and 5-3 = 2 numbers | start at 4 then +5
#  [0, 0, 0,  0,  5]]   <-- Has 4 '0' and 5-4 = 1 number  | start at 5
def pattern5(N):
    # Create N x N matrix
    matrix = []
    for i in range(N):
        # Add 0 before adding a number
        row = [0]*i
        # Calculate numbers after 0
        num = i+1
        for j in range(N, i, -1):
            row.append(num)
            num += j
        # Add each row to a matrix
        matrix.append(row)
    return matrix

# Pattern 6
# Example: pattern6(5)
# [[1, 9, 10, 14, 15],  <-- Has 0 '0' and 5-0 = 5 numbers
#  [0, 2, 8,  11, 13],  <-- Has 1 '0' and 5-1 = 4 numbers
#  [0, 0, 3,  7,  12],  <-- Has 2 '0' and 5-2 = 3 numbers
#  [0, 0, 0,  4,  6],   <-- Has 3 '0' and 5-3 = 2 numbers
#  [0, 0, 0,  0,  5]]   <-- Has 4 '0' and 5-4 = 1 number

# Algorithm
# 1.) Create sublist index n with n '0'
# 2.) Append a number in sublist in these index sequence 
# {0,1,2,...,N-1} --> {N-2,...,2,1,0}  --> {0,1,2,...,N-3} --> ... --> {0,1,2} --> {1,0} --> {0}
def pattern6(N):
    # Set initial number = 1
    num = 1
    # Create N x N matrix
    matrix = []
    # Create sublist index n with n '0'
    for n in range(N):
        matrix.append([0]*n)
    # Append num in sublist in the sequence
    for n in range(N):
        # If n is an even number, the index sequence is forward (Example: {0,1,2,...,N-1})
        if(n % 2 == 0):
            for index in range(0, N-n, 1):
                matrix[index].append(num)
                num += 1
        # If n is an odd number, the index sequence is reverse (Example: {N-2,...,2,1,0})
        else:
            for index in range(N-n-1, -1, -1):
                matrix[index].append(num)
                num += 1
    return matrix

# Execute an input string
exec(input().strip())