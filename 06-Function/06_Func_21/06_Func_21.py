# --------------------------------------------------
# File Name : 06_Func_21.py
# Problem   : Function Call
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Constants for grading criteria
# - A: 80 and above
# - B: 70 to 79
# - C: 60 to 69
# - D: 50 to 59
# - F: below 50
GRADING_CRITERIA = [[80, "A"], [70, "B"], [60, "C"], [50, "D"]]


# This function reads answers from input
# It returns a list in the format [[sid1, ans1], [sid2, ans2], ...]
def read_answers():
    n = int(input())
    answers = []
    for _ in range(n):
        student_id, ans = input().split()
        answers.append([student_id, ans])
    return answers


# This function can mark a single answer against a its solution
def marking(answer, solution):
    score = 0
    for i in range(len(answer)):
        if answer[i] == solution[i]:
            score += 1
    return score


# This function grades a score based on the grading criteria
def grading(score):
    for required_score, letter in GRADING_CRITERIA:
        if score >= required_score:
            return letter
    return "F"


# This function scores a list of answers against a solution
# "answers" is [[student_id1, ans1], [student_id2, ans2], ...]
# "solution" is a string representing the correct answer
# It returns a [[student_id1, score1, grade1], [student_id2, score2, grade2], ...]
def scoring(answers, solution):
    scores = []
    for student_id, ans in answers:
        score = marking(ans, solution) / len(solution) * 100
        grade = grading(score)
        scores.append([student_id, score, grade])
    return scores


# This function prints the scores in the specified format
def report(scores):
    for student_id, score, grade in scores:
        print(student_id, score, grade)


# This function sorts the scores in ascending order based on score
def sort(scores):
    sorted_scores = []
    for student_id, score, grade in scores:
        sorted_scores.append([score, student_id, grade])
    sorted_scores.sort()

    for i in range(len(scores)):
        score, student_id, grade = sorted_scores[i]
        scores[i] = [student_id, score, grade]


# Input the solution
solution = input().strip()

# Read the answers from input
answers = read_answers()

# Score the answers against the solution
scores = scoring(answers, solution)

# Sort the scores in ascending order
sort(scores)

# Print the report of scores in descending order
report(scores[::-1])
