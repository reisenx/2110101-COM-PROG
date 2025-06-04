# Given A and B matrix have the same size
# Given that convolute of matrix A and B is the sum of all A[i][j]*B[i][j]
def convolute(A,B):
    # Find a number of matrix row and column
    nrows = len(A)
    ncols = len(A[0])
    # Calculate a convolute of matrix A and B
    sum = 0
    for i in range(nrows):
        for j in range(ncols):
            sum += A[i][j]*B[i][j]
    # Return a value
    return sum

# Execute an input string
exec(input().strip())