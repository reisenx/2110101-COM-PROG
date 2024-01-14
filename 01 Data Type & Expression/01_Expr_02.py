#Import Math library
import math

#Find root of the equation ax^2 + bx + c
#input a,b and c as float variable
a=float(input())
b=float(input())
c=float(input())

#Calculate first root of equation ax^2 + bx + c and round into 3 decimal digits
x1 = (-1*b - math.sqrt(b**2 - 4*a*c))/(2*a)

#Calculate second root of equation ax^2 + bx + c and round into 3 decimal digits
x2 = (-1*b + math.sqrt(b**2 - 4*a*c))/(2*a)

#Output x1 and x2 in the same line
#Don't forget to round the answer into 3 digits decimal
print(round(x1,3),round(x2,3))