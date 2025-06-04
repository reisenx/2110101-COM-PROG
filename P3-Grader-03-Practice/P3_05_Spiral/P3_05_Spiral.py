# This function returns a list with number in spiral pattern
# n is an positive odd number
# Example: spiral_square(3)
# [[5,4,3]
#  [6,1,2]
#  [7,8,9]]
# Example: spiral_square(5)
# [[17,16,15,14,13]
#  [18, 5, 4, 3,12]
#  [19, 6, 1, 2,11]
#  [20, 7, 8, 9,10]
#  [21,22,23,24,25]]

# == Operaion ==
# 1.) Right Operation (R)
# > This operation move from index [i][j] to index [i][j+1]
# > Example: R2 means move from index [i][j] to [i][j+1] to [i][j+2]
# 2.) Up Operation (U)
# > This operation move from index [i][j] to index [i-1][j]
# > Example: U2 means move from index [i][j] to [i-1][j] tp [i-2][j]
# 3.) Left Operation (L)
# > This operation move from index [i][j] to index [i][j-1]
# > Example: L2 means move from index [i][j] to [i][j-1] to [i][j-2]
# 2.) Down Operation (D)
# > This operation move from index [i][j] to index [i+1][j]
# > Example: D2 means move from index [i][j] to [i+1][j] tp [i+2][j]

# == Algorithm ==
# 1.) Create a nxn matrix list that contains all 0
# 2.) Start at the center point which at the index [(n-1)//2][(n-1)//2]
# 3.) Do operation in the pattern below and change the value of each index
# > spiral_square(3) do [R1 U1] [L2 D2] [R2]
# > spiral_square(5) do [R1 U1] [L2 D2] [R3 U3] [L4 D4] [R4]
# > spiral_square(7) do [R1 U1] [L2 D2] [R3 U3] [L4 D4] [R5 U5] [L6 D6] [R6]
def spiral_square(n):
    # Create a nxn matrix list that contains all 0
    matrix = []
    for i in range(n):
        matrix.append([0]*n)
    # Start at center point
    num = 1
    row = (n-1)//2
    col = (n-1)//2
    matrix[row][col] = num
    
    # Do the operation in pattern until 'move' is equal to 'n'
    move = 1
    while(move < n):
        # If 'move' is an odd number do R and U operation
        if(move%2 == 1):
            # R operation
            for i in range(move):
                col += 1
                num += 1
                matrix[row][col] = num
            # U operation
            for i in range(move):
                row -= 1
                num += 1
                matrix[row][col] = num
            move += 1
        
        # If 'move' is an even number do L and D operation
        elif(move%2 == 0):
            # L operation
            for i in range(move):
                col -= 1
                num += 1
                matrix[row][col] = num
            # D operation
            for i in range(move):
                row += 1
                num += 1
                matrix[row][col] = num
            move += 1
        
    # If move is equal to n end the process with R(n-1) operation
    if(move == n):
        # R operation
        for i in range(move-1):
                col += 1
                num += 1
                matrix[row][col] = num
    # Returns a matrix
    return matrix

# Print a number in a list in the specified format
def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

# Execute an input string
exec(input().strip())