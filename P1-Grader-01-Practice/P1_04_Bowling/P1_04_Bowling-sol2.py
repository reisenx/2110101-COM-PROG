# --------------------------------------------------
# File Name : P1_04_Bowling-sol2.py
# Problem   : Part-I Bowling
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input bowling result and frame to display
result_str = input().strip()
display_frame = int(input())

# Convert the result string into a list of integers
result = []
for i in range(len(result_str)):
    if result_str[i] == "X":
        result.append(10)
    elif result_str[i] == "/":
        result.append(10 - int(result[i - 1]))
    else:
        result.append(int(result_str[i]))

# Initialize variables
frame_scores = []
idx = 0

# Calculate scores for each frame
for _ in range(10):
    # Initialize score for the current frame
    score = 0
    # Check for strike (X)
    if result[idx] == 10:
        score = sum(result[idx : idx + 3])
        idx += 1
    # Check for spare (/)
    elif sum(result[idx : idx + 2]) == 10:
        score = sum(result[idx : idx + 3])
        idx += 2
    # Normal case (two rolls)
    else:
        score = sum(result[idx : idx + 2])
        idx += 2
    frame_scores.append(score)

# Output
if 1 <= display_frame <= 10:
    print(frame_scores[display_frame - 1])
else:
    print(sum(frame_scores))
