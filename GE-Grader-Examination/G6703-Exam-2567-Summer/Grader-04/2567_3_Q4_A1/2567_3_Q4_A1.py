# --------------------------------------------------
# File Name : 2567_3_Q4_A1.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

a, b, c, d = [int(num) for num in input().split()]

if a <= b:
    if b <= c:
        if c <= d:
            print((b + c) / 2)
        else:
            if d <= b:
                if d <= a:
                    print(d, a, b, c)
                else:
                    print(a, d, b, c)
            else:
                print(a, b, d, c)
    else:
        print((a + c + d) / 3)

else:
    x, y = 0, a
    m = (x + y) / 2

    while abs((m**2) - a) > 10 ** (-b):
        if (m**2) < a:
            x = m
        else:
            y = m
        m = (x + y) / 2

    print(m)
