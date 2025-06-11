# --------------------------------------------------
# File Name : 04_Loop_20.py
# Problem   : Zig Zag 2
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Initialize variables
line = 0
min_A, max_A = 0, 0
min_B, max_B = 0, 0

# Loop to read input values
while True:
    # Read input data
    data = input().strip().split()

    # Output the result
    if len(data) == 1:
        cmd = data[0]
        if cmd == "Zig-Zag":
            print(min_A, max_B)
        elif cmd == "Zag-Zig":
            print(min_B, max_A)
        break

    # Get the numbers
    X, Y = int(data[0]), int(data[1])

    # Update min and max values based on the line number
    if line == 0:
        min_A, max_A = X, X
        min_B, max_B = Y, Y
    else:
        if line % 2 == 0:
            min_A, max_A = min(min_A, X), max(max_A, X)
            min_B, max_B = min(min_B, Y), max(max_B, Y)
        else:
            min_A, max_A = min(min_A, Y), max(max_A, Y)
            min_B, max_B = min(min_B, X), max(max_B, X)

    # Increment the line number
    line += 1
