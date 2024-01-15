#Input p as a float
p = float(input())

#Setup the value of k and t
k = 1
t = 1
t = (t*(365-(k-1)))/365

#Loop the process until 1-t >= p
while(1-t < p):
    k = k+1
    t = (t*(365-(k-1)))/365

#Output the value of k if 1-t >=p (loop process done)
print(k)