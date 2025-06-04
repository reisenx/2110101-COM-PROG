# Not guarantee 100/100 points on this code

# Input a number from a keyboard and split as a list
number = [int(e) for e in input().split()]

# Sort a list in ascending order
number.sort()

# Split into 2 list with the same length
# Case 1: length of the list is even number
# Example: [1,3,5,5,5,5,5,6,6,6,6,7,18,20] --> [1,3,5,5,5,5,5] and [6,6,6,6,7,18,20]
# Case 2: length of the list is odd number --> Ignore the center number in the list
# Example: [1,3,4,5,5,5,(5),6,6,6,7,18,20] --> [1,3,4,5,5,5] and [6,6,6,7,18,20]
if(len(number)%2 == 0):
    list01 = number[:len(number)//2]
    list02 = number[len(number)//2:]
else:
    list01 = number[:len(number)//2]
    list02 = number[len(number)//2 + 1:]

# Find Q1 which is median of the first list
# Case 1: length of the list is even number
# Example: [1,3,(4,5),5,5] --> Median = (4+5)/2 = 4.5
# Case 2: length of the list is odd number
# Example: [6,6,6,(6),7,18,20] --> Median = 6
if(len(list01)%2 == 0):
    Q1 = (list01[len(list01)//2 - 1] + list01[len(list01)//2]) / 2
else:
    Q1 = list01[len(list01)//2]

# Find Q3 which is median of the second list
if(len(list02)%2 == 0):
    Q3 = (list02[len(list02)//2 - 1] + list02[len(list02)//2]) / 2
else:
    Q3 = list02[len(list02)//2]

# Find IQR
IQR = Q3 - Q1

# Find L and U
L = Q1 - (1.5*IQR)
U = Q3 + (1.5*IQR)

# Outlier of the data is data that less than L or more than U
outlier = []
for num in number:
    if(num < L or num > U):
        outlier.append(num)

# Output L,U and outlier
for i in range(len(outlier)):
    outlier[i] = str(outlier[i])
print("L =", L, "U =", U)
if(outlier == []):
    print("Not found")
else:
    print(" ".join(outlier))