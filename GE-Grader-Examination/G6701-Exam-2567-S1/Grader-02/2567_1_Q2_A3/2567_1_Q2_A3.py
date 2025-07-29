# --------------------------------------------------
# File Name : 2567_1_Q2_A3.py
# Problem   : Horizontal & Vertical Flip
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
if cmd == "hflip":
    for row in img:
        modified_img.append(row[::-1])

# Rotate the image by 180 degrees
elif cmd == "vflip":
    modified_img = img[::-1]

# Output the modified image
for line in modified_img:
    print(line)
