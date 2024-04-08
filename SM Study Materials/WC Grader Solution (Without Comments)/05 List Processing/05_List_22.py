students = []
while(True):
    data = input().strip().split()
    if(data[0] != "q"):
        students.append(data)
    else:
        break

upgrade_ID = input().split()
old_grade = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
new_grade = ["A", "A", "B+", "B", "C+", "C", "D+", "D"]
for details in students:
    ID, grade = details[0], details[1]
    if(ID in upgrade_ID):
        index = old_grade.index(grade)
        details[1] = new_grade[index]
students.sort()

for ID, grade in students:
    print(ID,grade)