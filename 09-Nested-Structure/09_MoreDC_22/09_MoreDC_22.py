# This function can input a matrix
def read_matrix():
    matrix = []
    nrows = int(input())
    for k in range(nrows):
        temp = input().split()
        row = []
        for num in temp:
            row.append(float(num))
        matrix.append(row)
    return matrix

# This function can multiply a matrix with c
def mult_c(c,matrix):
    new_matrix = []
    for row in matrix:
        temp_row = []
        for column in range(len(row)):
            temp_row.append(row[column] * c)
        new_matrix.append(temp_row)
    return new_matrix

# This function can multiply matrix A with matrix B
# Definition: Given matrix C = AB
# If A is n x m matrix and B is m x p matrix, then C is n x p matrix
# C[i][j] = (A[i][1]*B[1][j]) + (A[i][2]*B[2][j]) + ... + (A[i][n]*B[n][j])
# when i = 1,2,...,n and j = 1,2,...,p
def mult(A,B):
    # Create new matrix
    C = []
    # 'n' is row of matrix A
    n = len(A)
    # 'p' is column of matrix B
    p = len(B[0])
    # 'm' is column of matrix A or row of matrix B
    m = len(B)
    # Calculate matrix C = AB
    for i in range(n):
        # Calculate each row of the matrix C 
        row = []
        for j in range(p):
            # Calculate each member of the matrix 
            num = 0
            for k in range(m):
                num += A[i][k]*B[k][j]
            row.append(num)
        C.append(row)
    return C

# Execute an input string
exec(input().strip())