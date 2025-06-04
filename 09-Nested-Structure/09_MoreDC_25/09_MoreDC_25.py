# Convert tiles of number into a list (Replace a blank spot to '0')
#  1 |  7 |  2 |  3
#  6 |    |  8 |  4
#  5 |  9 | 10 | 11
# 13 | 14 | 15 | 12
# We will get a list [[1,7,2,3], [6,0,8,4], [5,9,10,11], [13,14,15,12]]

# This fuction returns row number of list 't' that contains 'num' (Top row is index 0) 
def row_number(t, num):
    row_index = 0
    for row in t:
        if(num in row):
            return row_index
        else:
            row_index += 1

# Flatten: convert a list with sublist to a list (Remove 0)
# Example: [[1,2,0],[3,5,6],[4,7,8]] = [1,2,3,5,6,4,7,8]
def flatten(t):
    new = []
    for row in t:
        for num in row:
            if(num != 0):
                new.append(num)
    return new

# Inversion: compare all (num1,num2) possible and count (num1,num2) that num1 > num2
# Example: [1,2,3,5,6,4,7,8]
# > Compare (1,2),(1,3),...,(1,7),(1,8),(2,3),(2,5),...,(5,4),...,(6,4),...,(4,7),(4,8),(7,8)
# > In this case the function returns 2 
def inversions(x):
    count = 0
    for i in range(0, len(x)-1):
        for j in range(i+1, len(x)):
            if(x[i] > x[j]):
                count += 1
    return count

# Solvable: returns True if it meet the citeria below, else returns False
# rows = len(t)
# inversion = inversions(flatten(t))
# number of row that contains '0' = row_number(t,0)
# 1.) rows = odd  | inversion = even | number of row that contains '0' = any
# 2.) rows = even | inversion = odd  | number of row that contains '0' = even
# 3.) rows = even | inversion = even | number of row that contains '0' = odd
def solvable(t):
    rows = len(t)
    inv = inversions(flatten(t))
    row_0 = row_number(t,0)
    if(rows%2 == 1 and inv%2 == 0):
        return True
    elif(rows%2 == 0 and inv%2 == 1 and row_0%2 == 0):
        return True
    elif(rows%2 == 0 and inv%2 == 0 and row_0%2 == 1):
        return True
    else:
        return False

# Execute an input string
exec(input().strip())