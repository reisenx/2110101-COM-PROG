# Input image as a list of string
# Example: img = ["@@@@@.", "@@@@@.", "@@@@@.", "@.....", "@....."] can be represented as
# @@@@@.
# @...@.
# @@@@@.
# @.....
# @.....
row = int(input())
img = []
for i in range(row):
    data = input().strip()
    img.append(data)

# Find column of the picture
col = len(img[0])

# Input command
command = input()
# Create newImg as an empty list to contains rotated image
newImg = []

# Rotate 90 degree clockwise
# Original Image        | Rotated Image
# [00][01][02]...[0c]   | [r0]...[20][10][00]
# [10][11][12]...[1c]   | [r1]...[21][11][01]
# [20][21][22]...[2c]   | [r2]...[22][12][02]
# ... ... ...    ...    | ...    ... ... ...
# [r0][r1][r2]...[rc]   | [rc]...[2c][1c][0c]
if(command == "rot90"):
    for c in range(col):
        data = ""
        for r in range(row-1, -1, -1):
            data += img[r][c]
        newImg.append(data)

# Rotate 180 degree
# Original Image        | Rotated Image
# [00][01][02]...[0c]   | [rc]...[r2][r1][r0]
# [10][11][12]...[1c]   | ...    ... ... ...
# [20][21][22]...[2c]   | [2c]...[22][21][20]
# ... ... ...    ...    | [1c]...[12][11][10]
# [r0][r1][r2]...[rc]   | [0c]...[02][01][00]
elif(command == "rot180"):
    for r in range(row-1, -1, -1):
        data = img[r][::-1]
        newImg.append(data)

# Output
for txt in newImg:
    print(txt)