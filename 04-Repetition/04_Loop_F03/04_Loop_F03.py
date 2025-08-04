# --------------------------------------------------
# File Name : 04_Loop_F03.py
# Problem   : MCQ (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------


# Create a function to grade multiple-choice questions (MCQ)
def grade_mcq(sol, ans):
    # Initialize score
    score = 0

    # Returns a score
    if len(ans) == len(sol):
        for i in range(len(ans)):
            if ans[i] == sol[i]:
                score += 1
        return score
    return -1


# Execute the input string as code
exec(input())
