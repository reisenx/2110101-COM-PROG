# --------------------------------------------------
# File Name : 04_Loop_03.py
# Problem   : MCQ
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input answer and solution
answer = input().strip()
solution = input().strip()

# Initialize score
score = 0

# Output the score
if len(answer) == len(solution):
    for i in range(len(answer)):
        if answer[i] == solution[i]:
            score += 1
    print(score)
else:
    print("Incomplete answer")
