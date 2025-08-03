# --------------------------------------------------
# File Name : 2567_3_Q5_A0.py
# Problem   : Move String Right hand
# Author    : Worralop Srichainont
# Date      : 2025-07-26
# --------------------------------------------------

# --------------------------------------------------
# THIS IS A GRADER PROBLEM, NOT A SOLUTION.
# length_limit: 300
# nonIO_step_limit: 2
# --------------------------------------------------

s = input()
n = int(input())

while n > 0:
    s = "." + s[:-1]
    n -= 1

print(s)
