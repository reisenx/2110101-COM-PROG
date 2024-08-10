# Not guarantee 100/100 points on this code

# Input N M K value
N,M,K = [int(e) for e in input().strip().split()]

# Input data which contains
# [Name] [Faculty]
# Put the data in 'students' dictionary in the format
# students = {Name:Faculty}
# Example: students = {'Luffy':'faculty_a', 'Nami':'faculty_a'}
students = {}
for i in range(N):
    name, faculty = input().strip().split()
    students[name] = faculty

# Input data which contains
# [Guest] [Name01] [Name02] [Name03] ...
# Put the data in 'guests' dictionary in the format
# 'guests' = {Guest:{Set of Faculty}}

# Set of Faculty is set of Name01, Name02, Name03, ... faculty
# Example: "Eren Nami Chopper Brook"
# > Nami and Chopper are in 'faculty_a' and Brook are in 'faculty_c'
# > We will get 'guests' = {Eren:{faculty_a, faculty_c}}
guests = {}
for i in range(M):
    faculty = set()
    data = input().strip().split()
    for name in data[1:]:
        faculty.add(students[name])
    guests[data[0]] = faculty

# Convert the value in 'students' from string to a set.
# This will make the next step easier
# Example: students = {'Luffy':'faculty_a'} --> {'Luffy':{faculty_a}}
for name, faculty in students.items():
    students[name] = {faculty}

# Input data which contains
# [Name01] [Name02] [Name03] ...
# Check if what faculty that all person in the same line must go

# == Algorithm ==
# 1.) Create a set to contains faculty that all person need to go
# 2.) Manage data in the set
#   2.1) Setup initial value of set as the set of Name01
#   2.2) Intersect the set with the set of Name02, Name03 and so on
# 3.) Output
#   3.1) if len(set) == 0, output "None"
#   3.2) if len(set) > 0, output the faculty in alphabetical order
for i in range(K):
    names = input().strip().split()
    for index in range(len(names)):
        name = names[index]
        # Setup initial value of set as the set of Name01
        if(index == 0):
            if(name in students):
                matching = students[name]
            elif(name in guests):
                matching = guests[name]
        # Intersect the set with the set of Name02, Name03 and so on
        else:
            if(name in students):
                matching = matching & students[name]
            elif(name in guests):
                matching = matching & guests[name]
    # Sort the faculty in alphabetical order
    matching = sorted(matching)
    
    # Output
    if(len(matching) == 0):
        print("None")
    else:
        print(" ".join(matching))