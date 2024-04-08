number = input().split()
sum = int(number[0],2) + int(number[1],2)
sum = bin(sum)
print(sum[2:])