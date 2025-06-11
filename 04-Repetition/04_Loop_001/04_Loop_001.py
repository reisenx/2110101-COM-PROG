# --------------------------------------------------
# File Name : 04_Loop_001.py
# Problem   : Birthday Paradox (Flowchart)
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

p = float(input())

k = 1
t = 1

t = (t * (365 - k + 1)) / 365

while t > 1 - p:
    k += 1
    t = (t * (365 - k + 1)) / 365

print(k)
