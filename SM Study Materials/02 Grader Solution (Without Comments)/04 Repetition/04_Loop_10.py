a = float(input())
L = 0
U = 0
temp = a
while(temp != 0):
    temp = temp//10
    U += 1
x = (L+U)/2

while(abs(a-(10**x)) > (10**(-10)) * max(a,10**x)):
    if(10**x > a):
        U = x
    elif(10**x < a):
        L = x
    x = (L+U)/2

print(round(x,6))