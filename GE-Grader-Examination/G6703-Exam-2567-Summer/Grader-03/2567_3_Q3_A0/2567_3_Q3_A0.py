# --------------------------------------------------
# File Name : 2567_3_Q3_A0.py
# Problem   : Total Card Value
# Author    : Worralop Srichainont
# Date      : 2025-07-26
# --------------------------------------------------

# --------------------------------------------------
# THIS IS A GRADER PROBLEM, NOT A SOLUTION.
# length_limit: 300
# nonIO_step_limit: 4
# --------------------------------------------------

C = input().split()
total = 0
for c in C:
    if c == '2':
        p = 2
    elif c == '3':
        p = 3
    elif c == '4':
        p = 4
    elif c == '5':
        p = 5
    elif c == '6':
        p = 6
    elif c == '7':
        p = 7
    elif c == '8':
        p = 8
    elif c == '9':
        p = 9
    elif c in 'JQK':
        p = 10
    elif c == 'A':
        p = 1
    total += p
print(total)
