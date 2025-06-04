# Create a function to find median
# Step 1: Sort the list in ascending order
# > Example: sublist = [2,3,6,1,4] --> [1,2,3,4,6]
# Step 2 : Find median of a list
# > sublist = [1,2,3,4,6] --> median is sublist[2]
# > sublist = [1,2,3,6]   --> median is (sublist[1] + sublist[2])/2
# NOTE: 5//2 and 4//2 is 2
def median(sublist):
    sublist.sort()
    N = len(sublist)
    if(N % 2 == 1):
        pos = N//2
        return float(sublist[pos])
    else:
        pos = N//2
        return (sublist[pos-1] + sublist[pos])/2

# Input length of sublist
K = int(input())
# Convert Input to list of sublist with length K
# Example: input is ['1','3','2','4','5','5','2','1','6','7','3','4'] and K = 5
# > data = [[1,3,2,4,5], [5,2,1,6,7], [3,4]]
data = []
sublist = []
for item in input().split():
    # Append input into a list until len(sublist) == K
    sublist.append(int(item))
    # Append sublist into a data and reset sublist to an empty list
    if(len(sublist) == K):
        data.append(sublist)
        sublist = []
# Don't forget to append the last list
if(len(sublist) > 0):
    data.append(sublist)

# Find medians of K
# Example: data = [[1,3,2,4,5], [5,2,1,6,7], [3,4]]
# > medians = [3.0, 5.0, 3.5]
medians = []
for sublist in data:
    medians.append(median(sublist))
# Find median of medians of K
print(median(medians))