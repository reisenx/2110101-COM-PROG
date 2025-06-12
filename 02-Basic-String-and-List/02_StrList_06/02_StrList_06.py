# --------------------------------------------------
# File Name : 02_StrList_06.py
# Problem   : Add Vector
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input two vectors
u = input().strip()
v = input().strip()

# Remove parentheses and split into a list
u = u[1:-1].split(",")
v = v[1:-1].split(",")

# Convert string elements to floats
u[0], u[1], u[2] = float(u[0]), float(u[1]), float(u[2])
v[0], v[1], v[2] = float(v[0]), float(v[1]), float(v[2])

# Output the sum of the two vectors
total = [u[0] + v[0], u[1] + v[1], u[2] + v[2]]
print(f"{u} + {v} = {total}")
