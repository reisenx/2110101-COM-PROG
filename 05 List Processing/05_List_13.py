# Input a first set of data
n = int(input())
list_01 = []
for i in range(0,n):
    number = int(input())
    list_01.append(number)

# Input a second set of data
number = str(input())
if(number == ""):
    list_02 = []
else:
    list_02 = [int(e) for e in number.split()]

# Input a third set of data
list_03 = []
while(True):
    number = int(input())
    if(number == -1):
        break
    else:
        list_03.append(number)

# Merge all list into 1 list
merge_list = list_01 + list_02 + list_03

# Create a new list by 
# - Add a data at the back of a list 
# - Add a data at the front of a list
# - Do the previous 2 step reapeatly until all data are added
# Example: [1,2,3,4,5,6] --> [6,4,2,1,3,5]
backfront_list = []
for i in range(0,len(merge_list)):
    if(i%2 == 0):
        backfront_list.append(merge_list[i])
    else:
        backfront_list.insert(0,merge_list[i])

# Output a list
print(backfront_list)