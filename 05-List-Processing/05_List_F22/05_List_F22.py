# --------------------------------------------------
# File Name : 05_List_F22.py
# Problem   : Upgrade 2 (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# List of letter grades
GRADES = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]


# Find the index of a student ID in the grades list
def index_of(grades: list, ID: str) -> int:
    idx = 0
    for sid, _ in grades:
        if sid == ID:
            return idx
        idx += 1
    return -1


# Upgrade the grades of students based on their IDs
# After upgrading, sort students by ID in ascending order
def upgrade(grades: list, IDs: list) -> None:
    for ID in IDs:
        idx = index_of(grades, ID)
        old_grade = GRADES.index(grades[idx][1])

        if idx > -1 and old_grade > GRADES.index("A"):
            new_grade = GRADES[old_grade - 1]
            grades[idx][1] = new_grade
    grades.sort()


# Execute the input string as code
exec(input())
exec(input())
exec(input())
