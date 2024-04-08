number = [int(e) for e in input().split()]
number.sort()

unique_num = [number[0]]
for i in range(1,len(number)):
    if(number[i] != number[i-1]):
        unique_num.append(number[i])

print(len(unique_num))
print(unique_num[:10])