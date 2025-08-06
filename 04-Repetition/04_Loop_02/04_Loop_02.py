# --------------------------------------------------
# File Name : 04_Loop_02.py
# Problem   : Bisection Log 10
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input a number
num = float(input())

# Initialize variables
lower = 0
upper = num
x = (lower + upper) / 2

# Bisection method
while abs(num - 10**x) > (10**-10) * max(num, 10**x):
    if 10**x > num:
        upper = x
    else:
        lower = x
    x = (lower + upper) / 2

# Output the result
print(round(x, 6))
