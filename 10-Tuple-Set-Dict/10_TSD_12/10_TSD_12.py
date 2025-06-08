# Input number of sets
n = int(input())

# Create union and intersect set as an empty set
# So it won't be error if n = 0
union = set()
intersect = set()

# Input sets
for i in range(n):
    # Input each line as a list first, then convert to a set
    data = [int(e) for e in input().split()]
    data = set(data)
    # In the first loop, setup initial sets as input in the first line
    if(i == 0):
        union = data
        intersect = data
    # Find union and intersect after the first loop
    else:
        union = union | data
        intersect = intersect & data

# Output the length of the union set and intersect set
print(len(union))
print(len(intersect))