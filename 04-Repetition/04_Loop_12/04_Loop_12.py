# --------------------------------------------------
# File Name : 04_Loop_12.py
# Problem   : Zig Zag 1
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input number of rows
n = int(input())

# Initialize lists
a = []
b = []

# Loop to read input values
for i in range(n):
    x, y = [int(e) for e in input().split()]
    if i % 2 == 0:
        a += [x]
        b += [y]
    else:
        a += [y]
        b += [x]

# Output the results
cmd = input().strip()
if cmd == "Zig-Zag":
    print(min(a), max(b))
elif cmd == "Zag-Zig":
    print(min(b), max(a))
