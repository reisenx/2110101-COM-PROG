# --------------------------------------------------
# File Name : 2566_2_Q1_02.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------

n, a, b = [int(e) for e in input().split()]

if a > b:
    d, e = -1, -1
    while n < a:
        c = int(input())
        if c > d:
            d, e = c, d
        elif c > e:
            e = c
        n = n + b
else:
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    if e < f:
        e, f = f, e
    if d < e:
        d, e = e, d
    if c < d:
        c, d = d, c
    if d > e:
        if d > f:
            pass
        else:
            d, f = f, d
    elif e > f:
        d, e = e, d
    else:
        d, f = f, d
print(d, e)
