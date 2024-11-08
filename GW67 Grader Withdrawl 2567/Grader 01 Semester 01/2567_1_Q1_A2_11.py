import math
# Input x and epsilon
x, epsilon = [float(e) for e in input().split()]

# Loop until |term| < epsilon
# term = (-1^n)(x^2n)/(2n!)
# cosine is sum of all n term
cosine = 0
n = 0
while(True):
    term = (((-1)**n) * (x**(2*n))) / math.factorial(2*n)
    if(abs(term) < epsilon):
        break
    cosine += term
    n += 1

# Output
print(round(cosine, 6))