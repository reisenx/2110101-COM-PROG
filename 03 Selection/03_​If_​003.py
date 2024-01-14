#Input string
txt=str(input())

#Split the string to gain a,b,c and d value
num = txt.split()
a,b,c,d = int(num[0]), int(num[1]), int(num[2]), int(num[3])

#Condition: a>b
#if yes, swap a,b value then check the following condition
#if no, check the following condition
if(a>b):
    a,b = b,a
    #Condition: d>=a
    #if yes, check the following condition
    #if no, change the value of c to c+a
    if(d>=a):
        #Condition: c>d
        #if yes, change the value of c to c-a
        #if no, do nothing
        if(c>d):
            c = c-a
        else:
            pass
    else:
        c = c+a
    #Change the value b to a+c+d
    b = a+c+d
else:
    #Condition: c>a>=b
    #if yes, change the value of d to d+a
    #if no, do nothing
    if(c>a and a>=b):
        d = d+a
    else:
        pass
    #Condition: d>c
    #if yes, change the value of b to b+2
    #if no, change the value of b to 2*b
    if(d>c):
        b = b+2
    else:
        b = 2*b

#Output the value of a,b,c and d
print(a,b,c,d)