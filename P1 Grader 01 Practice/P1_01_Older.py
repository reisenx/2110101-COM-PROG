# Input a string
person1 = str(input())
person2 = str(input())

# Delete symbol "," from the string
for i in range(0,len(person1)):
    if(person1[i]==","):
        person1 = person1[:i] + " " + person1[i+1:]
for i in range(0,len(person2)):
    if(person2[i]==","):
        person2 = person2[:i] + " " + person2[i+1:]

# Split a string to get data
data1 = person1.split()
data2 = person2.split()
name1, month1, day1, year1 = data1[0], data1[1], int(data1[2]), int(data1[3])
name2, month2, day2, year2 = data2[0], data2[1], int(data2[2]), int(data2[3])

# Convert month name to month number
list_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for item in list_month:
    if(month1 == item):
        month1 = list_month.index(item) + 1
    if(month2 == item):
        month2 = list_month.index(item) + 1

# Compare and Output who is older
# Check the year of brithday
if(year1 == year2):
    # If in the same year, check the month of birthday
    if(month1 == month2):
        # If in the same month, check the day of birthday
        # If both birthday is the same, print both
        if(day1 == day2):
            print(name1,name2)
        elif(day1 < day2):
            print(name1)
        elif(day2 < day1):
            print(name2)
    elif(month1 < month2):
        print(name1)
    elif(month2 < month1):
        print(name2)
elif(year1 < year2):
    print(name1)
elif(year2 < year1):
    print(name2)