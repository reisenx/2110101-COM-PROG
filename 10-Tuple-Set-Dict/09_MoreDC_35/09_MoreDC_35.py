# Input student data
# Example: [['Krit','A','97','CP'], ['Oat','A','98','CE'], ['Pim','C','99','CP'], ...]
n = int(input())
students = []
for i in range(n):
    data = input().strip().split()
    students.append(data)

# Input search data as a set
# Example: {'A','CP'}
search = input().strip().split()
search = set(search)

# ---------- Search student ----------
# 1.) Convert student to a set (Ex. ['Krit','A','97','CP'] --> {'Krit','A','97','CP'})
# 2.) Check if the student has all attributes by using .issubset()
#     {'A','CP'} is subset of {'Krit','A','97','CP'} --> Add to found
#     {'A','CP'} is not subset of {'Oat','A','98','CE'} --> Skip
# NOTE: There's a case like "Dog N 110 PE" or "ENV S 105 ME"
found = []
groups = ('A','B','C','Dog','E','F','G','H','J','K','L','M','N','P','Q','R','S','T')
departments = ('CE','EE','ME','AE','IE','CHE','PE','GE','ENV','SV','MT','CP','NT','CEDT','ICE','NANO','ADME','CHPE','AI','AERO','SEMI')

for student in students:
    name, group, generation, department = student
    if(search.issubset(set(student)) and (name not in groups) and (name not in departments)):
        found.append(student)

# Output
if(len(found) == 0):
    print("Not Found")
else:
    # Don't forget to sort students by name
    found.sort()
    for name, group, generation, department in found:
        print(name, group, generation, department)