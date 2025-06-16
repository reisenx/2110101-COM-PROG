# --------------------------------------------------
# File Name : P1_05_Golf.py
# Problem   : Part-I Golf
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

import math

# Initialize variables
total_par = 0
total_stroke = 0
total_modified_stroke = 0

# Read score of each hole
for _ in range(9):
    par, stroke, select = [int(num) for num in input().split()]
    # Calculate total par stroke and modified stroke
    total_par += par
    total_stroke += stroke
    total_modified_stroke += select * min(stroke, par + 2)

# Calculate the score
handicap = math.floor(0.8 * (1.5 * total_modified_stroke - total_par))
total_score = total_stroke - handicap

# Output the result
print(total_stroke)
print(handicap)
print(total_score)
