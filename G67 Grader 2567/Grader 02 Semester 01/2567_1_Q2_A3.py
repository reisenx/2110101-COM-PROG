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

# Input command
command = input()
# Create newImg as an empty list to contains flipped image
newImg = []

# Horizontal flip
# Original Image        | Rotated Image
# [00][01][02]...[0c]   | [0c]...[02][01][00]
# [10][11][12]...[1c]   | [1c]...[12][11][10]
# [20][21][22]...[2c]   | [2c]...[22][21][20]
# ... ... ...    ...    | ...    ... ... ...
# [r0][r1][r2]...[rc]   | [rc]...[r2][r1][r0]
if(command == "hflip"):
    # Reversed each line in img
    for line in img:
        newImg.append(line[::-1])

# Vertical flip
# Original Image        | Rotated Image
# [00][01][02]...[0c]   | [r0][r1][r2]...[rc]
# [10][11][12]...[1c]   | ...    ... ... ...
# [20][21][22]...[2c]   | [20][21][22]...[2c]
# ... ... ...    ...    | [10][11][12]...[1c]
# [r0][r1][r2]...[rc]   | [00][01][02]...[0c]
if(command == "vflip"):
    # Start at the last line, and stop at the first line
    for r in range(row-1, -1, -1):
        newImg.append(img[r])

# Output
for line in newImg:
    print(line)