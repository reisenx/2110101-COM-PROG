# Input id and a grade
id = []
grade = []
while(True):
    data = input()
    if(data != "q"):
        data = data.split()
        id.append(data[0])
        grade.append(data[1])
    else:
        break

# Input id that need to upgrade
upgrade_id = input().split()

# Upgrade B+ to A, B to B+, C+ to B and so on
old_grade = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
new_grade = ["A", "A", "B+", "B", "C+", "C", "D+", "D"]
for item in upgrade_id:
    grade[id.index(item)] = new_grade[old_grade.index(grade[id.index(item)])]

for i in range(0,len(id)):
    print(id[i], grade[i])