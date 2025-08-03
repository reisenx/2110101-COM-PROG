# --------------------------------------------------
# File Name : 2567_1_Q1_A1-W.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

a, b, c, d = [int(e) for e in input().split()]

if a == 1:
    a = b + c + d
    if b == 1:
        c += c + d
    else:
        if b == 2:
            c += c - d
        else:
            if b > 4:
                c += c * d
            if b > 5:
                c += c % d
            else:
                c += c // d
    print(c)
else:
    while b < c:
        b += 1
        if b > a:
            break

        c -= 1

        if a > d:
            break
        a += c

print(a, b, c, d)
