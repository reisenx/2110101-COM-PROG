def index_of(grades, ID):
    IsValid = False
    index = 0
    for sid,grade in grades:
        if(sid == ID):
            IsValid = True
            break
        else:
            index += 1
    
    if(IsValid):
        return index
    else:
        return -1

def upgrade(grades, IDs):
    old_grades = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
    new_grades = ["A", "A", "B+", "B", "C+", "C", "D+", "D"]
    for sid in IDs:
        std_index = index_of(grades, sid)
        if(std_index != -1):
            old = grades[std_index][1]
            index = old_grades.index(old)
            grades[std_index][1] = new_grades[index]
    grades.sort()

exec(input())
exec(input())
exec(input())