a,b,c,d = [float(e) for e in input().split()]
sum = a + b + c + d

minimum = a
if(b < minimum):
    minimum = b
if(c < minimum):
    minimum = c
if(d < minimum):
    minimum = d

maximum = a
if(b > maximum):
    maximum = b
if(c > maximum):
    maximum = c
if(d > maximum):
    maximum = d

sum -= minimum + maximum
average = round(sum/2, 2)
print(average)