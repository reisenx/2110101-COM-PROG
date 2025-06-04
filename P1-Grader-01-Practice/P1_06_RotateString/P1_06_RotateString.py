# Input a operation and number of row
command = str(input().strip())
row = int(input().strip())

# Input a string, strip() it then put it in a list
# Example:
# "ABCD"
# "1234"
# "WXYZ"
# string = [['A','B','C','D'], ['1','2','3','4'], ['W','X','Y','Z']]
# string[0] = ['A','B','C','D']
# string[0][0] = 'A'
string = []
for i in range(row):
    line = list(input().strip())
    string.append(line)

# Check the length of the string
# If all line have the same length then SizeValid = True
# If there's a line that has a different length then SizeValid = False
SizeValid = True
column = len(string[0])
for line in string:
    if(len(line) != column):
        SizeValid = False
        break

# Invalid Size
if(not SizeValid):
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
elif(command == "90"):
    for j in range(column):
        line = ""
        for i in range(row-1, -1, -1):
            line += string[i][j]
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
elif(command == "180"):
    for i in range(row-1, -1, -1):
        line = ""
        for j in range(column-1, -1, -1):
            line += string[i][j]
        print(line)

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
elif(command == "flip"):
    for i in range(row):
        line = ""
        for j in range(column-1, -1, -1):
            line += string[i][j]
        print(line)