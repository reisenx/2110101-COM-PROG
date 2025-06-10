# --------------------------------------------------
# File Name : 01_Expr_06.py
# Problem   : Duration
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input the initial time in the format h1 : m1 : s1
h1 = int(input())
m1 = int(input())
s1 = int(input())

# Input the final time in the format h2 : m2 : s2
h2 = int(input())
m2 = int(input())
s2 = int(input())

# Convert the initial time and final time into seconds
t1 = (h1 * 3600) + (m1 * 60) + s1
t2 = (h2 * 3600) + (m2 * 60) + s2

# Calculate the duration in seconds
# Ensure that the duration is always positive by using modulo operation
dt = ((24 * 3600) + t2 - t1) % (24 * 3600)

# Convert the duration in seconds to hours, minutes, and seconds
dh = dt // 3600
dt = dt - (dh * 3600)
dm = dt // 60
dt = dt - (dm * 60)
ds = dt

# Output
print(str(dh) + ":" + str(dm) + ":" + str(ds))
