# --------------------------------------------------
# File Name : 2567_3_Q2_A1.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------

a, b, c, d = [int(num) for num in input().split()]

if a > b:
    if b < 0:
        c, d = d, c
    else:
        if b > 5:
            c -= d

        if b < 3:
            if b > 2:
                c //= d
            else:
                c *= d
        else:
            c += d
            c *= d

else:
    while a > d:
        b += 1
        a -= 1
        d += c

print(a, b, c, d)
