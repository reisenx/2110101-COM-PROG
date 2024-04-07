# Input score and convert to float
a,b,c,d = [float(e) for e in input().split()]

# Find sum of all score
sum = a + b + c + d

# Find minimum score
minimum = a
if(b < minimum):
    minimum = b
if(c < minimum):
    minimum = c
if(d < minimum):
    minimum = d

# Find maximum score
maximum = a
if(b > maximum):
    maximum = b
if(c > maximum):
    maximum = c
if(d > maximum):
    maximum = d

# Subtract minimum score and maximum score from 'sum'
sum -= minimum + maximum

# Find average score
average = round(sum/2, 2)
print(average)