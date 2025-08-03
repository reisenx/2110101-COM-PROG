# --------------------------------------------------
# File Name : 2567_3_Q1_A1.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------

a, b, c, d, e = [int(num) for num in input().split()]

if a >= e:
    i = 0
    n = 4

    while i <= n:
        if a >= b:
            a, b = b, a

        if b >= c:
            b, c = c, b

        if c >= d:
            c, d = d, c

        if d >= e:
            d, e = e, d

        i += 1
    print(a, b, c, d, e)


else:
    if a == 1:
        if b >= c:
            b, c = c, b

        if c >= d:
            c, d = d, c

        if d >= e:
            d, e = e, d

        if b <= c:
            if b <= d:
                print((c + d) / 2)
            else:
                print((b + c) / 2)

        else:
            if c <= d:
                print((b + d) / 2)
            else:
                print((b + c) / 2)
    else:
        ans = (((b**2) + (c**2) + (d**2)) ** 0.5) / (a**2)
        print(round(ans, 2))
