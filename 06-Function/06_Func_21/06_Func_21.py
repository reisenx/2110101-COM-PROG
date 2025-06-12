# --------------------------------------------------
# File Name : 06_Func_21.py
# Problem   : Function Call
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# This function reads answers from input
# It returns a list in the format [[sid1, ans1], [sid2, ans2], ...]
def read_answers() -> list:
    N = int(input())
    answers = []
    for _ in range(N):
        sid, ans = input().split()
        answers.append([sid, ans])
    return answers


# This function can mark a single answer against a its solution
def marking(answer: str, solution: str) -> int:
    score = 0
    for i in range(len(answer)):
        if answer[i] == solution[i]:
            score += 1
    return score


# This function grades a score based on the following criteria:
# - A: 80 and above
# - B: 70 to 79
# - C: 60 to 69
# - D: 50 to 59
# - F: below 50
def grading(score: float) -> str:
    CRITERIA = [[80, "A"], [70, "B"], [60, "C"], [50, "D"]]
    for required_score, letter in CRITERIA:
        if score >= required_score:
            return letter
    return "F"


# This function scores a list of answers against a solution
# "answers" is a list in the format [[sid1, ans1], [sid2, ans2], ...]
# "solution" is a string representing the correct answer
# It returns a list in the format [[sid1, score1, grade1], [sid2, score2, grade2], ...]
def scoring(answers: list, solution: str) -> list:
    scores = []
    for sid, ans in answers:
        score = marking(ans, solution) / len(solution) * 100
        grade = grading(score)
        scores.append([sid, score, grade])
    return scores


# This function prints the scores in the specified format
def report(scores: list) -> None:
    for sid, score, grade in scores:
        print(sid, score, grade)


# This function sorts the scores in ascending order based on score
def sort(scores: list) -> None:
    sorted_scores = []
    for sid, score, grade in scores:
        sorted_scores.append([score, sid, grade])
    sorted_scores.sort()

    for i in range(len(scores)):
        score, sid, grade = sorted_scores[i]
        scores[i] = [sid, score, grade]


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
