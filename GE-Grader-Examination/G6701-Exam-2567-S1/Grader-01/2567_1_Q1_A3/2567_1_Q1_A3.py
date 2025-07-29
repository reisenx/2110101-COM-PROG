# --------------------------------------------------
# File Name : 2567_1_Q1_A3.py
# Problem   : rot90 & rot180
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input number of rows and the image
rows = int(input())
img = [input().strip() for _ in range(rows)]

# Find the number of columns
cols = len(img[0])

# Initialize the modified image
modified_img = []

# Input command to modify the image
cmd = input().strip()

# Rotate the image by 90 degrees clockwise
if cmd == "rot90":
    for c in range(cols):
        line = ""
        for r in range(rows - 1, -1, -1):
            line += img[r][c]
        modified_img.append(line)

# Rotate the image by 180 degrees
elif cmd == "rot180":
    for r in range(rows - 1, -1, -1):
        modified_img.append(img[r][::-1])

# Output the modified image
for line in modified_img:
    print(line)
