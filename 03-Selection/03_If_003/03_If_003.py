# --------------------------------------------------
# File Name : 03_If_003.py
# Problem   : Flowchart 01
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

a, b, c, d = [int(e) for e in input().split()]

if a > b:
    a, b = b, a

    if not d >= a:
        c = c + a
    else:
        if c > d:
            c = c - a

    b = a + c + d
else:
    if c > a >= b:
        d = d + a

    if d > c:
        b = b + 2
    else:
        b = 2 * b

print(a, b, c, d)
