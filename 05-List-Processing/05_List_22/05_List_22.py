# --------------------------------------------------
# File Name : 05_List_22.py
# Problem   : Upgrade 2
# Author    : Worralop Srichainont
# Date      : 2025-06-12
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
    student_id, grade = student.split()
    students.append([student_id, GRADES.index(grade)])

# Upgrade student grades
upgrade_ids = input().split()
for i in range(len(students)):
    # Extract information from the list
    student_id, grade = students[i]

    # Check if the student ID is in the upgrade list
    if student_id in upgrade_ids:
        # Upgrade the grade of that student
        students[i][1] = max(grade - 1, 0)

# Sort students by id in ascending order
students.sort()

# Output the upgraded grades
for student_id, grade in students:
    print(student_id, GRADES[grade])
