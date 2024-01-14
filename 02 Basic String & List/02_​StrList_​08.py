#Import Math library
import math

#Import input decimal as a string
#The format of the input is A,B,C (Example 0,08,3)
#A is a integer part of the input
#B is a decimal part of the input
#C is a repeating decimal part of the input
#Example 0.022727272727... ---> 0,02,27
decimal = str(input())
A,B,C = decimal.split(",")

#How to convert a repeating decimal to a fraction
#Example: 10.23456456456... (A=10, B=23, C=456)
#Given X = 10.23456456456...
#(10^2)X = 1,023.456456456... (len(B)=2)
#(10^5)X = 1,023,456.456456456... (len(B)+len(C)=5)
#(10^5)X - (10^2)X = 1,023,456.456456456 - 1,023.456456456
# (10^5 - 10^2)X = 1,023,456 - 1,023
#X = (1,023,456 - 1,023)/(10^5 - 10^2)
numerator = int(A+B+C) - int(A+B)
denominator = 10**(len(B)+len(C)) - 10**len(B)

#Output the Simplified fraction
gcd = math.gcd(numerator,denominator)
print(numerator//gcd,"/",denominator//gcd)