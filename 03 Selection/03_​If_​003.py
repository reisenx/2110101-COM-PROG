# Flowchart

# Input a,b,c,d value
a,b,c,d = [int(e) for e in input().split()]

# Condition: a>b
# If true, swap a,b value then check the following condition
# If false, check the following condition
if(a > b):
    a,b = b,a
    # Condition: d>=a
    # If true, check the following condition
    # If false, change the value of c to c+a
    if(d >= a):
        # Condition: c>d
        # If true, change the value of c to c-a
        # If false, do nothing
        if(c > d):
            c = c-a
        else:
            pass
    else:
        c = c+a
    # Change the value b to a+c+d
    b = a+c+d
else:
    # Condition: c>a>=b
    # If true, change the value of d to d+a
    # If false, do nothing
    if(c > a and a >= b):
        d = d+a
    else:
        pass
    # Condition: d>c
    # If true, change the value of b to b+2
    # If false, change the value of b to 2*b
    if(d > c):
        b = b+2
    else:
        b = 2*b

# Output the value of a,b,c and d
print(a,b,c,d)