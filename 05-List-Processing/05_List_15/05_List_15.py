# Input a string, convert them into a list then sort them
number = [int(e) for e in input().split()]
number.sort()

# Create a list that contains unique numbers
# == Algorithm ==
# 1.) Sort all number in a list in ascending order
# 2.) Loop each number in a list and check if that number in index i and i-1 are different
# > Example: 11,11,11,12,13,13,13,13,13
#   Loop i=1: [11,11],11,12,13,13,13,13,13    <-- unique_num = [11]
#   Loop i=2: 11,[11,11],12,13,13,13,13,13    <-- unique_num = [11]
#   Loop i=3: 11,11,[11,12],13,13,13,13,13    <-- unique_num = [11,12]
#   Loop i=4: 11,11,11,[12,13],13,13,13,13    <-- unique_num = [11,12,13]
#   Loop i=5: 11,11,11,12,[13,13],13,13,13    <-- unique_num = [11,12,13]
#   ...
unique_num = [number[0]]
for i in range(1,len(number)):
    if(number[i] != number[i-1]):
        unique_num.append(number[i])

# Output number of unique number and the first 10 unique numbers
print(len(unique_num))
print(unique_num[:10])