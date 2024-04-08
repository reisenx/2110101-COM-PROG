# Flowchart
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if(a > b):
    a,b = b,a
else:
    pass
if(c > d):
    c,d = d,c
else:
    pass
if(a > c):
    b,d = d,b
    c = a
else:
    pass
a = e
if(a > b):
    a,b = b,a
else:
    pass
if(c > a):
    b,d = d,b
    a = c
else:
    pass
if(a > d):
    print(d)
else:
    print(a)
