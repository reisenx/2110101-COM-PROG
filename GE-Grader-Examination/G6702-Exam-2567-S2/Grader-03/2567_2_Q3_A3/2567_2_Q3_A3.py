# --------------------------------------------------
# File Name : 2567_2_Q3_A3.py
# Problem   : Red Ball
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------

# Input initial balls order
balls = input().strip().split(",")

# Swap balls operations
n = int(input())
for _ in range(n):
    # Input start and end indices for the swap operation in 1-based indexing
    start_idx, end_idx = [int(idx) for idx in input().split()]

    # Convert to 0-based indexing
    # NOTE: No need to decrement end_idx because the operation includes the end index
    start_idx -= 1

    # Swap the balls in range to the end of the list
    balls = balls[:start_idx] + balls[end_idx:] + balls[start_idx:end_idx]

# Output the final order of balls
print(",".join(balls))
