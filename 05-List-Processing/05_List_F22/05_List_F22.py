# This function can find index of ID in grades list
# grades is a list [[id1, grade1], [id2, grade2], ...]
def index_of(grades, ID):
    # Find an index of ID in grades
    IsValid = False
    index = 0
    for sid,grade in grades:
        if(sid == ID):
            IsValid = True
            break
        else:
            index += 1
    
    # Retuns a value
    if(IsValid):
        return index
    else:
        return -1

# This function can upgrade a students who are in IDs list
# grades is a list [[id1, grade1], [id2, grade2], ...]
# IDs is list [id1, id2, id3]
def upgrade(grades, IDs):
    # Create list using for upgrade
    old_grades = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
    new_grades = ["A", "A", "B+", "B", "C+", "C", "D+", "D"]
    
    # Upgrade each student in IDs
    for sid in IDs:
        # Find index of each ID in grades
        std_index = index_of(grades, sid)
        # Upgrade each students
        if(std_index != -1):
            old = grades[std_index][1]
            index = old_grades.index(old)
            grades[std_index][1] = new_grades[index]
    
    # Sorting a data
    grades.sort()

# Execute a 3 input strings
exec(input())
exec(input())
exec(input())