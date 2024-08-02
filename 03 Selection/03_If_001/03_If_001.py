# Flowchart

# Input a,b,c,d and e as integers
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

# Condition: a>b 
# If true, swap a,b value
# If false, do nothing
if(a>b):
    a,b = b,a
else:
    pass

#Condition: c>d 
# If true, swap c,d value
# If false, do nothing
if(c>d):
    c,d = d,c
else:
    pass

# Condition: c>d 
# If true, swap b,d value and change c value
# If false, do nothing
if(a>c):
    b,d = d,b
    c = a
else:
    pass

# Change 'a' value
a = e

# Condition: a>b 
# If true, swap a,b value
# If false, do nothing
if(a>b):
    a,b = b,a
else:
    pass

# Condition: c>a 
# If true, swap b,d value and change value of a to c
# If false, do nothing
if(c>a):
    b,d=d,b
    a=c
else:
    pass

# Condition: a>d
# If true, Output d
# If false, Output a
if(a>d):
    print(d)
else:
    print(a)
