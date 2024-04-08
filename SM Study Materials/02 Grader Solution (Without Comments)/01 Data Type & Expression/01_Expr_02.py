import math
a = float(input())
b = float(input())
c = float(input())

x1 = (-1*b - math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-1*b + math.sqrt(b**2 - 4*a*c))/(2*a)
print(round(x1,3),round(x2,3))