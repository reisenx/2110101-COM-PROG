# Input integer n
n = int(input())

# Collatz's Problem
# Collect n of each loop in a list
collatz_num = [n]
while(n != 1):
    if(n%2 == 0):
        n = n//2
        collatz_num.append(n)
    else:
        n = (3*n) + 1
        collatz_num.append(n)

# Output the last 15 items in 'collatz_num'.
# Convert all item in a list to string and join each item with "-->" string
process = collatz_num[-15:]
for i in range(len(process)):
    process[i] = str(process[i])
print("->".join(process))