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

# Horizontal flip
# Original Image        | Rotated Image
# [00][01][02]...[0c]   | [0c]...[02][01][00]
# [10][11][12]...[1c]   | [1c]...[12][11][10]
# [20][21][22]...[2c]   | [2c]...[22][21][20]
# ... ... ...    ...    | ...    ... ... ...
# [r0][r1][r2]...[rc]   | [rc]...[r2][r1][r0]
if(command == "hflip"):
    # Reversed each row in img, then output
    for row in img:
        print(row[::-1])

# Vertical flip
# Original Image        | Rotated Image
# [00][01][02]...[0c]   | [r0][r1][r2]...[rc]
# [10][11][12]...[1c]   | ...    ... ... ...
# [20][21][22]...[2c]   | [20][21][22]...[2c]
# ... ... ...    ...    | [10][11][12]...[1c]
# [r0][r1][r2]...[rc]   | [00][01][02]...[0c]
if(command == "vflip"):
    # Reverse all row in img list
    img[::-1]
    # Output
    for row in img:
        print(row)