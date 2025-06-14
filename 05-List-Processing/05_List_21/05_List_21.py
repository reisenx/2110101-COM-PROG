# --------------------------------------------------
# File Name : 05_List_21.py
# Problem   : Upgrade
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# List of letter grades
GRADES = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]

# Input student information
students = []
while True:
    student = input().strip()
    # Stop if input is 'q'
    if student == "q":
        break
    # Add student information to the list
    # Convert grade to index
    sid, grade = student.split()
    students.append([sid, GRADES.index(grade)])

# Upgrade student grades
upgrade_ids = input().split()
for student in students:
    sid, grade = student
    if sid in upgrade_ids:
        # Upgrade the grade of that student
        student[1] = max(grade - 1, 0)

# Output the upgraded grades
for sid, grade in students:
    print(sid, GRADES[grade])
