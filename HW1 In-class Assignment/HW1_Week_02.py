# Input string
txt = str(input())

# Split txt with ',' and get surname from index 0
# Ex. "Gibb,Robin:22/December/1949" --> ["Gibb", "Robin:22/December/1949"]
data1 = txt.split(",")
surname = data1[0]

# Split data1[1] with ':' and get name from index 0
# Ex. data1[1] = "Robin:22/December/1949"
#     "Robin:22/December/1949" --> ["Robin", "22/December/1949"]
data2 = data1[1].split(":")
name = data2[0]

# Split data2[1] with "/" and get day, month and year
# Ex. data2[1] = 22/December/1949
#     "22/December/1949" --> ["22","December","1949"]
data3 = data2[1].split("/")
day,month,year = data3[0], data3[1], data3[2]

# Output in the specific format
print(name, surname + ":", month, day + ",", year)