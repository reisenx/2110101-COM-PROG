#Input a,b,c,d and e as integers
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

#Condition: a>b 
#if yes, swap a,b value
#if no, do nothing
if(a>b):
    a,b = b,a
else:
    pass

#Condition: c>d 
#if yes, swap c,d value
#if no, do nothing
if(c>d):
    c,d = d,c
else:
    pass

#Condition: c>d 
#if yes, swap b,d value and change c value
#if no, do nothing
if(a>c):
    b,d = d,b
    c = a
else:
    pass

#change a value
a = e

#Condition: a>b 
#if yes, swap a,b value
#if no, do nothing
if(a>b):
    a,b = b,a
else:
    pass

#Condition: c>a 
#if yes, swap b,d value and change value of a to c
#if no, do nothing
if(c>a):
    b,d=d,b
    a=c
else:
    pass

#Condition: a>d
#if yes, Output d
#if no, Output a
if(a>d):
    print(d)
else:
    print(a)
