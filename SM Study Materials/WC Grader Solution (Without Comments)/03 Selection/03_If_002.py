# Flowchart
d,m,y = [int(e) for e in input().split()]
m30list = [4,6,9,11]
y = y-543
n = 31

if(m in m30list):
    n = 30
else:
    if(m == 2):
        n = 28
        if(y%400 == 0):
            n = 29
        if(y%4 == 0 and y%100 != 0):
            n = 29
d += 15

if(d > n):
    d = d-n
    m += 1
if(m > 12):
    m -= 12
    y += 1

y += 543
print(str(d) + "/" + str(m) + "/" + str(y))