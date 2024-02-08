# Input a string, convert them into a list then sort them
number = [int(e) for e in input().split()]
number.sort()

# Create a list that contains unique numbers
unique_list = [number[0]]
for i in range(1,len(number)):
    if(number[i] != number[i-1]):
        unique_list.append(number[i])

# Output number of unique number and the first 10 unique numbers
print(len(unique_list))
print(unique_list[:10])