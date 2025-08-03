# --------------------------------------------------
# File Name : 2567_3_Q4_A0.py
# Problem   : Average Grade
# Author    : Worralop Srichainont
# Date      : 2025-07-26
# --------------------------------------------------

# --------------------------------------------------
# THIS IS A GRADER PROBLEM, NOT A SOLUTION.
# length_limit: 300
# nonIO_step_limit: 4
# --------------------------------------------------

G = input().split()

c = 0
for g in G:
    if g == "A+":
        c += 4.0
    elif g == "A":
        c += 3.75
    elif g == "B+":
        c += 3.5
    elif g == "B":
        c += 3.0
    elif g == "C+":
        c += 2.75
    elif g == "C":
        c += 2.5
    elif g == "D+":
        c += 1.5
    elif g == "D":
        c += 1.0
    elif g == "F":
        c += 0.0

gx = round(c / len(G), 2)
print(gx)
