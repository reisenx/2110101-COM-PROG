# --------------------------------------------------
# File Name : 2566_3_Q1_01.py
# Problem   : Longest Repeated Characters
# Author    : Worralop Srichainont
# Date      : 2025-07-15
# --------------------------------------------------

# Input text
text = input().strip()

# Initialize counter
max_char = text[0]
char = text[0]

max_count = 1
count = 1

# Iterate through the text
for i in range(1, len(text)):
    if text[i] == char:
        count += 1
    else:
        if count > max_count:
            max_count = count
            max_char = char
        char = text[i]
        count = 1

# Check the last character count
if count > max_count:
    max_count = count
    max_char = char

# Output the maximum character repeated and its count
print(max_char, max_count)
