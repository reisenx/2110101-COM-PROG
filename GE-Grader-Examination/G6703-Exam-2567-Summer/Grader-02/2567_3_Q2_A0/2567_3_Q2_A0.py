# --------------------------------------------------
# File Name : 2567_3_Q2_A0.py
# Problem   : Interest Rate
# Author    : Worralop Srichainont
# Date      : 2025-07-26
# --------------------------------------------------

# --------------------------------------------------
# THIS IS A GRADER PROBLEM, NOT A SOLUTION.
# length_limit: 300
# nonIO_step_limit: 4
# --------------------------------------------------

principal = float(input())
total = principal
for m in range(1, 11):
    if m in [1, 2, 3]:
        r = 1
    elif m == 4:
        r = 1
    elif m == 5 or m == 6:
        r = 2
    elif m == 7:
        r = 3
    elif m == 8:
        r = 4
    else:
        r = 7
    total *= (1 + r / 12 / 100)

total = round(total, 2)
print(total)
