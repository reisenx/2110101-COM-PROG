# --------------------------------------------------
# File Name : 01_Expr_02.py
# Problem   : Quadratic Root
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math

# Input a, b and c as float
a = float(input())
b = float(input())
c = float(input())

# Calculate roots of the equation ax^2 + bx + c
x1 = (-1 * b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
x2 = (-1 * b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)

# Output
# Round the result to 3 decimal places
print(round(x1, 3), round(x2, 3))
