# Input integer n
n = int(input())

# Collatz's Problem
# Collect n of each loop in a list
collatz_list = [n]
while(n != 1):
    if(n%2 == 0):
        n = n//2
        collatz_list.append(n)
    else:
        n = (3*n) + 1
        collatz_list.append(n)

# Make a string that show last 15 process of Collatz's Problem
length = len(collatz_list)
process = ""
# In case of length of the list is less than or equal to 15
if(length<=15):
    for i in range(0,length):
        if(i < length-1):
            process += str(collatz_list[i]) + "->"
        else:
            process += str(collatz_list[i])
# In case of length of the list is more than 15
else:
    for i in range(length-15,length):
        if(i < length-1):
            process += str(collatz_list[i]) + "->"
        else:
            process += str(collatz_list[i])

# Output
print(process)