t = 0
s1 = 0
v1, v2 = 0,0
a1, a2, s2 = [float(e) for e in input().split()]

if(a2 >= a1):
    print("Not possible")
else:
    while(s2 > s1):
        t += 1
        
        s1 += v1 + 0.5 * a1
        s2 += v2 + 0.5 * a2
        
        v1 += a1
        v2 += a2
    print(t, round(s1, 2))