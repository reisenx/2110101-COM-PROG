# --------------------------------------------------
# File Name : 2567_3_Q5_A1.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

a, b, c, d = [int(num) for num in input().split()]

if a == 1:
    c, d = d, c

    if b == 1:
        c = c + d
    else:
        if b < 5:
            c = c - d
        else:
            if b <= 10:
                c = c / d

else:
    if a != 10:
        if b > 1:
            c = c + d

        if b > 2:
            c = c % d

        if b > 3:
            c = c + (c**d)
        else:
            c -= 1

    else:
        while a > d:
            a = a - b
            c += 1

print(a, b, c, d)
