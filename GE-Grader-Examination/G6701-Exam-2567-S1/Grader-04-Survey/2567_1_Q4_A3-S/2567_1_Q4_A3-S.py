# --------------------------------------------------
# File Name : 2567_1_Q4_A3-S.py
# Problem   : MCQ Checker
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Input solution answer of the exam
solution_answer = input().strip()

# Input score gained or deducted for correct and incorrect answers
correct_score, incorrect_score = [int(score) for score in input().split()]

# Input candidate's answer
candidate_answer = input().strip()

# Initialize counters
correct_count = 0
incorrect_count = 0
no_answer_count = 0

# Calculate scores based on answers
for i in range(len(solution_answer)):
    # Candidate answered correctly
    if solution_answer[i] == "X" or candidate_answer[i] == solution_answer[i]:
        correct_count += 1

    # Candidate answered incorrectly
    else:
        incorrect_count += 1

    # Candidate did not answer
    if candidate_answer[i] == "-":
        no_answer_count += 1

# Calculate total score
total_score = (correct_count * correct_score) + (incorrect_count * incorrect_score)
# Ensure score is not negative
total_score = max(0, total_score)

# Output the results
print(correct_count, incorrect_count, no_answer_count, total_score)
