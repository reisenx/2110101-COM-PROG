# Input a operation and number of row
func = str(input().strip())
row = int(input().strip())

# Input a string, strip() it then put it in a list
# Example:
# ABCD
# 1234
# WXYZ
# string = [['A','B','C','D'], ['1','2','3','4'], ['W','X','Y','Z']]
# string[0] = ['A','B','C','D']
# string[0][0] = 'A'
string = []
for i in range(0,row):
    txt = str(input())
    string.append(list(txt.strip()))

# Check the length of the string
# If all line have the same length then SizeValid = True
# If there's a line that has a different length then SizeValid = False
SizeValid = True
column = len(string[0])
for i in range(1,row):
    if(len(string[i]) != column):
        SizeValid = False
        break

# Invalid Size
if(SizeValid == False):
    print("Invalid size")

# Rotate 90 degrees clockwise
# Orginal String
# [11][12][13]...[1j]
# [21][22][23]...[2j]
# [31][32][33]...[3j]
# ... ... ...    ...
# [i1][i2][i3]...[ij]

# Modified string
# [i1]...[31][21][11]
# [i2]...[32][22][12]
# [i3]...[33][23][13]
# ...    ... ... ...
# [ij]...[3j][2j][1j]
elif(func == "90"):
    for j in range (0,column):
        line = ""
        i = row - 1
        while(i >= 0):
            line = line + string[i][j]
            i = i-1
        print(line)

# Rotate 180 degrees
# Orginal String
# [11][12][13]...[1j]
# [21][22][23]...[2j]
# [31][32][33]...[3j]
# ... ... ...    ...
# [i1][i2][i3]...[ij]

# Modified string
# [ij]...[i3][i2][i1]
# ...    ... ... ...
# [3j]...[33][32][31]
# [2j]...[23][22][21]
# [1j]...[13][12][11]
elif(func == "180"):
    i = row - 1
    while(i >= 0):
        line = ""
        j = column - 1
        while(j >= 0):
            line = line + string[i][j]
            j = j-1
        print(line)
        i = i-1

# Flip
# Orginal String
# [11][12][13]...[1j]
# [21][22][23]...[2j]
# [31][32][33]...[3j]
# ... ... ...    ...
# [i1][i2][i3]...[ij]

# Modified string
# [1j]...[13][12][11]
# [2j]...[23][22][21]
# [3j]...[33][32][31]
# ...    ... ... ...
# [ij]...[i3][i2][i1]
elif(func == "flip"):
    for i in range(0,row):
        line = ""
        j = column - 1
        while(j >= 0):
            line = line + string[i][j]
            j = j-1
        print(line)