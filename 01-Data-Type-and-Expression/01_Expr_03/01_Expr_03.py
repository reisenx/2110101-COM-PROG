# --------------------------------------------------
# File Name : 01_Expr_03.py
# Problem   : An Expression
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math

# Calculate numerator and denominator of a fraction
numerator = (
    math.pi
    - (math.factorial(10) / (8**8))
    + (math.log(9.7)) ** ((7 / math.sqrt(71)) - math.sin(math.radians(40)))
)
denominator = 1.2 ** (2.3 ** (1 / 3))

# Output
# Round the result to 6 decimal places
print(round(numerator / denominator, 6))
