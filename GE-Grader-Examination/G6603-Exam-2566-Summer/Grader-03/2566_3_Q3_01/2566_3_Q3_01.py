# --------------------------------------------------
# File Name : 2566_3_Q3_01.py
# Problem   : Customized Grading
# Author    : Worralop Srichainont
# Date      : 2025-07-15
# --------------------------------------------------

# Input customized grading criteria.
grade_criteria = []
while True:
    # Read input until "Done" is entered.
    data = input().strip().split()
    if data == ["Done"]:
        break
    # Each line contains a grade and a score threshold.
    grade = data[0]
    score = float(data[1])
    grade_criteria.append([score, grade])
grade_criteria.sort(reverse=True)

# Input student scores and names
students_scores = []
n = int(input())
for _ in range(n):
    # Read each student's name and score.
    data = input().strip().split()
    name = data[0]
    score = float(data[1])
    # Store the score and name in a list.
    students_scores.append([int(score), name])

# Initialize a list to store students' grades.
students_grades = []
# Assign grades based on the criteria.
for score, name in students_scores:
    # Default grade is "F" if no criteria match.
    info = [0, "F", name]
    # Check each grading criteria to assign the appropriate grade.
    for criteria_score, criteria_letter in grade_criteria:
        if score >= criteria_score:
            # If the score meets a criteria, update the grade and break.
            info = [criteria_score, criteria_letter, name]
            break
    # Append the student's grade information to the list.
    students_grades.append(info)
# Sort students by grade and then by name.
students_grades.sort()

# Output students with their grades.
for _, grade, name in students_grades:
    print(name, grade)
