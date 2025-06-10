# --------------------------------------------------
# File Name : 01_Expr_01.py
# Problem   : Stirling Factorial
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math

# Input n
n = int(input())

# Calculate the lower bound of n!
lower = (
    math.sqrt(2 * math.pi) * n ** (n + (1 / 2)) * math.e ** (-n + (1 / (12 * n + 1)))
)
print(lower)

# Calculate the upper bound of n!
upper = math.sqrt(2 * math.pi) * n ** (n + (1 / 2)) * math.e ** (-n + (1 / (12 * n)))
print(upper)
