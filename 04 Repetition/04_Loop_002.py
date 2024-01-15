#Input string then split them and collect in d list
d = [int(e) for e in input().split()]

#Set initial value
#p is the rightmost data in the list d
#n is the length of the list d
p = d[-1]
i = -1 ; j = 0
n = len(d)

#Loop if j < n-1
while(j < n-1):
    #Condition: d[j] <= p
    #if yes, add i by 1 then swap the value d[i] and d[j]
    #if no, do nothing
    if(d[j] <= p):
        i += 1
        d[i],d[j] = d[j],d[i]
    #Add j by 1
    j += 1

#Swap the value of d[i+1] and the rightmost data in list d
d[i+1],d[-1] = d[-1],d[i+1]

#Output
print(d)