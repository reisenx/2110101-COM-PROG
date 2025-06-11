# --------------------------------------------------
# File Name : 04_Loop_10.py
# Problem   : Bisection Log 10 [2]
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input a number
a = float(input())

# Initialize lower bound
L = 0

# Calculate upper bound
U = 0
temp = a
while temp > 0:
    temp //= 10
    U += 1

# Initialize x as the midpoint
x = (L + U) / 2

# Bisection method
while abs(a - 10**x) > (10**-10) * max(a, 10**x):
    if 10**x > a:
        U = x
    else:
        L = x
    x = (L + U) / 2

# Output the result
print(round(x, 6))
