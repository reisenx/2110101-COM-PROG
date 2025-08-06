# --------------------------------------------------
# File Name : 02_StrList_06.py
# Problem   : Add Vector
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input two vectors, remove parentheses and split into a list
raw_u = input().strip("[] ").split(", ")
raw_v = input().strip("[] ").split(", ")

# Convert string elements to floats
u = [float(raw_u[0]), float(raw_u[1]), float(raw_u[2])]
v = [float(raw_v[0]), float(raw_v[1]), float(raw_v[2])]

# Output the sum of the two vectors
total = [u[0] + v[0], u[1] + v[1], u[2] + v[2]]
print(f"{u} + {v} = {total}")
