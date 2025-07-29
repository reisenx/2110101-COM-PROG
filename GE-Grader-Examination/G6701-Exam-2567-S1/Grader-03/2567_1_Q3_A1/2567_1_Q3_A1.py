# --------------------------------------------------
# File Name : 2567_1_Q3_A1.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

a, b, c, d = [int(e) for e in input().split()]
if a > 1:
    while b < d:
        b = b + 1
        if b > c:
            c = c + 3
        else:
            break
else:
    a = b + c + d
    if b > 7:
        if b > 9:
            c = (2 * d) + 2
            if b > 12:
                c = 4 * d
            if b > 15:
                d = c - a
            else:
                d = c + (2 * a)
            print(c, d)
        else:
            c = 3 * d
    else:
        if b > 5:
            b = c + d
        else:
            if b > 2:
                b = 2 * c
            else:
                b = c - d
        print(a, b)
print(a, b, c, d)
