# Input number of students
n = int(input())

# Input data of each student details which contains
# [Name] [Group] [Generation] [Department]
# We will indicate a student with a number and put students details in a dictionary
# Example: students = {1:['Krit','A','97','CP'], 2:['Oat','A','98','CE']}
# Example: num2name = {1:'Krit', 2:'Oat'}
# Example: name2num = {'Krit':1, 'Oat',2}
students = {}
num2name = {}
name2num = {}
for i in range(1, n+1):
    data = input().strip().split()
    students[i] = data
    num2name[i] = data[0]
    name2num[data[0]] = i

# Input searching data
# Example: "CP 97" --> ['CP','97']
search = input().strip().split()

# There might be a case that the student name is the name of a group or department
# So we need to create a tuple of these name
# Example: "Dog N 110 PE" might have a little bit of problem
groups = ('A','B','C','Dog','E','F','G','H','J','K','L','M','N','P','Q','R','S','T')
departments = ('CE','EE','ME','AE','IE','CHE','PE','GE','ENV','SV','MT','CP','NT','CEDT')

# Seaching Process
# 1.) Search each object in 'search' list in 'students' dictionary value
# 2.) If found, put the student number (dictionary key) to a set 'temp'
# 3.) If i = 0, setup matching = temp as initial value
# 4.) If i > 0, matching is an intersection between matching and temp 
for i in range(len(search)):
    # Serching
    temp = set()
    for num, data in students.items():
        # Searching name
        if(search[i] == data[0] and search[i] not in groups and search[i] not in departments):
            temp.add(num)
        # Serching group
        if(search[i] == data[1] and search[i] in groups):
            temp.add(num)
        # Searching generation
        if(search[i] == data[2]):
            temp.add(num)
        # Seaching department
        if(search[i] == data[3] and search[i] in departments):
            temp.add(num)
    # Put data in 'matching'
    if(i == 0):
        matching = temp
    else:
        matching = matching & temp

# Convert 'matching' to a list
matching = list(matching)
# Convert all numbers in 'matching' to name, put them in 'matching_name' and sort them in alphabetical order
matching_name = []
for num in matching:
    matching_name.append(num2name[num])
matching_name.sort()
matching = []
# Convert all name in 'matching_name' to numbers and put them in 'matching' again
for name in matching_name:
    matching.append(name2num[name])

# Output
if(len(matching) == 0):
    print("Not Found")
else:
    for num in matching:
        print(" ".join(students[num]))