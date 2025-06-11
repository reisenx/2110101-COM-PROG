# --------------------------------------------------
# File Name : 04_Loop_12.py
# Problem   : Zig Zag 1
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input number of rows
n = int(input())

# Initialize lists
A = []
B = []

# Loop to read input values
for i in range(n):
    X, Y = [int(e) for e in input().split()]
    if i % 2 == 0:
        A += [X]
        B += [Y]
    else:
        A += [Y]
        B += [X]

# Output the results
cmd = input().strip()
if cmd == "Zig-Zag":
    print(min(A), max(B))
elif cmd == "Zag-Zig":
    print(min(B), max(A))
