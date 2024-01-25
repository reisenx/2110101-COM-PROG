# Input a float
a = float(input())

# Create an interval [L,U]
# U is how many times to floor division the number until it reaches 0
# Example: number = 120
# 120//10 = 12 --> 12//10 = 1 --> 1//10 = 0 so U = 3
L = 0
U = 0
temp = a
while(temp != 0):
    temp = temp//10
    U = U+1
x = (L+U)/2

# Using bisection algorithm until |a-10^x| <= 10^(-10) * max(a,10^x)
# Math Function
# x = log10(a) --> 10^x = a
# Algorithm
# - If 10^x > a then change U = x --> interval [L,x]
# - If 10^x < a then change L = x --> interval [x,U]
while(abs(a-(10**x)) > (10**(-10)) * max(a,10**x)):
    if(10**x > a):
        U = x
    elif(10**x < a):
        L = x
    x = (L+U)/2

# Output the value
print(round(x,6))