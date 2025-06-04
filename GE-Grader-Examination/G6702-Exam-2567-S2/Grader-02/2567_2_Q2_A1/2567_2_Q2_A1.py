a,b,c,d,e = [int(e) for e in input().split()]
if(e == 1):
    if(a < b):
        a,b = b,a
    if(c < d):
        c,d = d,c
    if(a >= c):
        if(b >= c):
            print(b)
        else:
            print(c)
    else:
        if(a >= b):
            print(a)
        else:
            print(d)
else:
    while(e < 3):
        if(a >= b):
            a,b = b,a
        if(b >= c):
            b,c = c,b
        if(c >= d):
            c,d = d,c
        e += 1
    print(b)