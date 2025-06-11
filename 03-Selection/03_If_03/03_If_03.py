# --------------------------------------------------
# File Name : 03_If_03.py
# Problem   : Gymnastic Score
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input the scores of 4 judges
score = input().strip().split()
score[0] = float(score[0])
score[1] = float(score[1])
score[2] = float(score[2])
score[3] = float(score[3])

# Find the maximum and minimum scores
max_score = score[0]
min_score = score[0]

if score[1] > max_score:
    max_score = score[1]
if score[1] < min_score:
    min_score = score[1]

if score[2] > max_score:
    max_score = score[2]
if score[2] < min_score:
    min_score = score[2]

if score[3] > max_score:
    max_score = score[3]
if score[3] < min_score:
    min_score = score[3]

# Calculate the average score
score_total = score[0] + score[1] + score[2] + score[3]
average_score = (score_total - max_score - min_score) / 2

# Output the average score
print(round(average_score, 2))
