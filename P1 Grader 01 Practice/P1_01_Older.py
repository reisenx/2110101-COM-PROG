# Input a string
person01 = input().strip()
person02 = input().strip()

# Delete symbol "," from the string
person01 = person01.replace(",", " ")
person02 = person02.replace(",", " ")

# Split a string to get data
# Don't forget to convert day and year to integers
name01, month01, day01, year01 = person01.split()
name02, month02, day02, year02 = person02.split()
day01, year01, day02, year02 = int(day01), int(year01), int(day02), int(year02)

# Convert month name to month number
month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month01 = month_list.index(month01) + 1
month02 = month_list.index(month02) + 1

# Put day, month, year and name in a list and sort. This makes it a lot easier
# Sorting order: year --> month --> day
birthday = [[year01, month01, day01, name01], [year02, month02, day02, name02]]
birthday.sort()

# Output
# Case 1: Both have the same birthday
if(birthday[0][0:3] == birthday[1][0:3]):
    print(name01,name02)
# Case 2: Both have different birthday
# A person appears in the first sublist is older
else:
    print(birthday[0][3])