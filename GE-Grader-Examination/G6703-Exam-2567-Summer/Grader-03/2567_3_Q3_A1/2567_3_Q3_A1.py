# --------------------------------------------------
# File Name : 2567_3_Q3_A1.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------

a, b, c, d, e = [int(num) for num in input().split()]

if a > 0:
    if a % 2 == 0:
        if b < c:
            b *= e
        else:
            if b < d:
                b //= e
            b -= e
    else:
        if b > c:
            b, c = c, b

        if b > d:
            b, d = d, b
        else:
            b += e

else:
    while a <= d:
        a += 1
        if a > b:
            break
        b -= 1

print(a, b, c, d, e)
