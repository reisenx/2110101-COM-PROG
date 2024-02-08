# This function can find index of ID in grades list
# grades is a list [[id1, grade1], [id2, grade2], ...]
def index_of(grades, ID):
    IsValid = False
    index = 0
    for sublist in grades:
        if(sublist[0] == ID):
            IsValid = True
            break
        else:
            index += 1
    if(IsValid == True):
        return index
    else:
        return -1

# This function can upgrade a students who are in IDs list
# grades is a list [[id1, grade1], [id2, grade2], ...]
# IDs is list [id1, id2, id3]
def upgrade(grades, IDs):
    # Upgrade
    old_grade = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
    new_grade = ["A", "A", "B+", "B", "C+", "C", "D+", "D"]
    for sublist in grades:
        if(sublist[0] in IDs):
            index = grades.index(sublist)
            grades[index][1] = new_grade[old_grade.index(grades[index][1])]
    # Sorting a data
    grades.sort()

# Execute a 3 input strings
exec(input())
exec(input())
exec(input())