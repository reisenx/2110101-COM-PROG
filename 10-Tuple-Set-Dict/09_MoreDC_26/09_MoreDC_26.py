# Input number of IDs
n = int(input())

# Input social network data.
# Each line contains [ID]: [City1], [City2], [City3], ...
# It is guarantee that each ID have at least 1 city
# Put data in a dictionary 'IDs'
# IDs = {ID:[City1, City2, City3, ...], ...}
IDs = {}
unique_IDs = []
for i in range(n):
    ID, cities = input().strip().split(": ")
    cities = cities.split(", ")
    IDs[ID] = cities
    unique_IDs.append(ID)

# Input KeyID
KeyID = input()

# Find ID that went to same city of KeyID
# Contains ID in a set to prevent duplication
samecity_ID = set()
for key_city in IDs[KeyID]:
    temp = set()
    for ID, cities in IDs.items():
        if((key_city in cities) and (ID != KeyID)):
            temp.add(ID)
    samecity_ID = samecity_ID.union(temp)

# Output 'samecity_ID' in input order
# If 'samecity_ID' is an empty set, then output "Not Found"
if(len(samecity_ID) == 0):
    print("Not Found")
else:
    for ID in unique_IDs:
        if(ID in samecity_ID):
            print(ID)