# Input ID and grade of each student
# Put the data in a 'students' list in the format
# [[ID01,grade01], [ID02,grade02], ...]
students = []
while(True):
    data = input().strip().split()
    if(data[0] != "q"):
        students.append(data)
    else:
        break

# Input ID that need to upgrade
upgrade_ID = input().split()

# Upgrade B+ to A, B to B+, C+ to B and so on
old_grade = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
new_grade = ["A", "A", "B+", "B", "C+", "C", "D+", "D"]
for details in students:
    ID, grade = details[0], details[1]
    if(ID in upgrade_ID):
        index = old_grade.index(grade)
        details[1] = new_grade[index]

# Output
for ID, grade in students:
    print(ID,grade)