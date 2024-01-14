#Input score string then split the string to get the score
txt = str(input())
score = txt.split()
a,b,c,d = float(score[0]), float(score[1]), float(score[2]), float(score[3])

#Find maximum score then find minimum score then reset them both to 0
#Case 1: if a is a maximum score
if(a>=b and a>=c and a>=d):
    #Case 1.1 if b is a minimum score
    if(b<=a and b<=c and b<=d):
        a=0
        b=0
    #Case 1.2 if c is a minimum score
    elif(c<=a and c<=b and c<=d):
        a=0
        c=0
    #Case 1.3 if d is a minimum score
    elif(d<=a and d<=b and d<=c):
        a=0
        d=0

#Case 2: if b is a maximum score
elif(b>=a and b>=c and b>=d):
    #Case 2.1 if a is a minimum score
    if(a<=b and a<=c and a<=d):
        b=0
        a=0
    #Case 2.2 if c is a minimum score
    elif(c<=a and c<=b and c<=d):
        b=0
        c=0
    #Case 2.3 if d is a minimum score
    elif(d<=a and d<=b and d<=c):
        b=0
        d=0

#Case 3: if c is a maximum score
elif(c>=a and c>=b and c>=d):
    #Case 3.1 if a is a minimum score
    if(a<=b and a<=c and a<=d):
        c=0
        a=0
    #Case 3.2 if b is a minimum score
    elif(b<=a and b<=c and b<=d):
        c=0
        b=0
    #Case 3.3 if d is a minimum score
    elif(d<=a and d<=b and d<=c):
        c=0
        d=0

#Case 4: if d is a maximum score
elif(d>=a and d>=b and d>=c):
    #Case 4.1 if a is a minimum score
    if(a<=b and a<=c and a<=d):
        d=0
        a=0
    #Case 4.1 if b is a minimum score
    elif(b<=a and b<=c and b<=d):
        d=0
        b=0
    #Case 4.1 if c is a minimum score
    elif(c<=a and c<=b and c<=d):
        d=0
        c=0

#Calculuate and output the average score of 2 referees 
print(round((a+b+c+d)/2,2))