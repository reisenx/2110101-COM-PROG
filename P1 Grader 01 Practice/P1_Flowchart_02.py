# Flowchart
n,k = [int(e) for e in input().split()]

if(n%2!=0):
    sum_a,sum_b,sum_c,m = 0,0,0,0
    while(m < k):
        a,b,c = [int(e) for e in input().split()]
        if(a==b):
            if(a==b and b==c):
                if(a+b > k):
                    sum_a = sum_a + 1
                    sum_b = sum_b + 2
                    sum_c = sum_c - 3
                else:
                    sum_a = sum_a - 3
                    sum_b = sum_b - 2
                    sum_c = sum_c + 1
            else:
                sum_a = sum_a + 2
                sum_b =sum_b - 3
        else:
            pass
        m = m+1
    print(sum_a,sum_b,sum_c)
else:
    s,t = [int(e) for e in input().split()]
    x=s
    y=t
    if(s>t):
        x = s-t
    else:
        if(s<t):
            y = 2*(t-s)
    if(x+y>k):
        x,y = y,x
        x = y+(s**2)
        print(x,y)