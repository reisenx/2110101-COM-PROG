# Import Math Library
import math

# Stirling's approximation of n!
# Input the value of n as integer variable
n = int(input())

# Calculate Lower bound of n!
lower = math.sqrt(2*math.pi) * n**(n+(1/2)) * math.e**(-n+(1/(12*n + 1)))
print(lower)

# Calculate Upper bound of n!
upper = math.sqrt(2*math.pi) * n**(n+(1/2)) * math.e**(-n+(1/(12*n)))
print(upper)