# --------------------------------------------------
# File Name : 09_Nested_11.py
# Problem   : Dedent
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input python code as a string
n = int(input())
code = []
for _ in range(n):
    code.append(input().strip())

# Output the dedented code
for line in code:
    # Count amount of leading dot
    leading_dots = 0
    for char in line:
        if char == ".":
            leading_dots += 1
        else:
            break
    # Remove half of leading dots
    dedented_line = line[leading_dots // 2 :]
    # Print the dedented line
    print(dedented_line)
