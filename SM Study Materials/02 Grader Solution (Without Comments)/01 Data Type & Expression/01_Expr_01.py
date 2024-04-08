import math
n = int(input())

lower = math.sqrt(2*math.pi) * n**(n+(1/2)) * math.e**(-n+(1/(12*n + 1)))
print(lower)
upper = math.sqrt(2*math.pi) * n**(n+(1/2)) * math.e**(-n+(1/(12*n)))
print(upper)