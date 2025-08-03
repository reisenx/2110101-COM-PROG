# --------------------------------------------------
# File Name : 2567_3_Q1_A0.py
# Problem   : Get Min-Max Out of 6
# Author    : Worralop Srichainont
# Date      : 2025-07-26
# --------------------------------------------------

# --------------------------------------------------
# THIS IS A GRADER PROBLEM, NOT A SOLUTION.
# length_limit: 300
# nonIO_step_limit: 4
# --------------------------------------------------

d1 = float(input())
d2 = float(input())
d3 = float(input())
d4 = float(input())
d5 = float(input())
d6 = float(input())

m1 = d1
m2 = d1

if d2 > m1:
    m1 = d2
if d3 > m1:
    m1 = d3
if d4 > m1:
    m1 = d4
if d5 > m1:
    m1 = d5
if d6 > m1:
    m1 = d6

if d2 < m2:
    m2 = d2
if d3 < m2:
    m2 = d3
if d4 < m2:
    m2 = d4
if d5 < m2:
    m2 = d5
if d6 < m2:
    m2 = d6

s = (d1 + d2 + d3 + d4 + d5 + d6) - m1 - m2
print(s)
