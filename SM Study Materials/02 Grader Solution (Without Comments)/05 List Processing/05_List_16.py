n = int(input())

collatz_num = [n]
while(n != 1):
    if(n%2 == 0):
        n = n//2
        collatz_num.append(n)
    else:
        n = (3*n) + 1
        collatz_num.append(n)

process = collatz_num[-15:]
for i in range(len(process)):
    process[i] = str(process[i])
print("->".join(process))