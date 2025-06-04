a,b,c = [int(e) for e in input().split()]
if(a < b):
    d = c
    x = 'B'
    if(c == 0):
        x = str(c) + x
    else:
        while(c > 0):
            r = c % 2
            x = str(r) + x
            c = c // 2
    print(d, x)
else:
    if(a > b):
        d = int(input())
        if(a > c):
            a,b = b,a
            a,c = c,a
            a = a + 1
            b = b * 2
        else:
            pass
        
        if(b > d):
            b,d = d,b
            a = a + 2
            b = b * 3
        else:
            pass
        
        c = a + (2 * b)
        d = c - (3 * a)
        print(a,b,c,d)
    else:
        e = float(input())
        f = float(input())
        out = e*(1 + (f / (100 * a)))**(a * c)
        print(round(out, 2))