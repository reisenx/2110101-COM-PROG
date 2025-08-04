# --------------------------------------------------
# File Name : 04_Loop_11.py
# Problem   : RLE
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input text
text = input().strip()

# Construct RLE string
rle = ""

# Initialize counter
char = text[0]
count = 1

# Iterate through the text
for i in range(1, len(text)):
    if text[i] == char:
        count += 1
    else:
        rle += char + " " + str(count) + " "
        char = text[i]
        count = 1

# Append the last character and its count
rle += char + " " + str(count)

# Output the RLE string
print(rle)
