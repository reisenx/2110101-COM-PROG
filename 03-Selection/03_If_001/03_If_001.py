# --------------------------------------------------
# File Name : 03_If_001.py
# Problem   : Median 5 (Flowchart)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a > b:
    a, b = b, a

if c > d:
    c, d = d, c

if a > c:
    b, d = d, b
    c = a

a = e

if a > b:
    a, b = b, a

if c > a:
    b, d = d, b
    a = c

if a > d:
    print(d)
else:
    print(a)
