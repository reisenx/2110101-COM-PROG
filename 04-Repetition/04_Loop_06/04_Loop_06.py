# --------------------------------------------------
# File Name : 04_Loop_06.py
# Problem   : Print Triangle
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input the height of the triangle
n = int(input())

# Construct the triangle
triangle = ""
for i in range(n - 1):
    # Add leading dots
    triangle += "." * (n - i - 1)
    # Add the first star
    triangle += "*"
    # Add dots between stars and the second star
    if i > 0:
        triangle += "." * ((2 * i) - 1)
        triangle += "*"
    # Add newline character
    triangle += "\n"
# Add base of the triangle
triangle += "*" * ((2 * n) - 1)

# Output the triangle
print(triangle)
