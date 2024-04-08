import math

decimal = str(input())
A,B,C = decimal.split(",")

numerator = int(A+B+C) - int(A+B)
denominator = 10**(len(B)+len(C)) - 10**len(B)

gcd = math.gcd(numerator,denominator)
print(numerator//gcd,"/",denominator//gcd)