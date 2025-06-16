# --------------------------------------------------
# File Name : 10_TSD_37.py
# Problem   : Department Selection
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input departments and their seats
n = int(input())
department_seats = {}
for _ in range(n):
    department, seats = input().strip().split()
    department_seats[department] = int(seats)

# Input students score and their department rankings preference
n = int(input())
student_to_department = {}
student_ranking = []
student_preference = {}
department_ranking = {}
has_department = {}
for _ in range(n):
    # Input student ID, score, and department
    data = input().strip().split()
    student_id = data[0]
    score = float(data[1])
    preference = data[2:]

    # Update student information
    student_to_department[student_id] = ""
    has_department[student_id] = False
    student_preference[student_id] = preference
    student_ranking.append((score, student_id))

    # Update department rankings
    for department in preference:
        if department not in department_ranking:
            department_ranking[department] = []
        department_ranking[department].append((score, student_id))

# Sort students by score in descending order
student_ranking.sort(reverse=True)

# Sort the department rankings by score in descending order
for _, rankings in department_ranking.items():
    rankings.sort(reverse=True)

# Assign student to departments starting from the highest score
for _, student_id in student_ranking:
    for department in student_preference[student_id]:
        # Check if the department has available seats
        # and the student hasn't been assigned to any department yet
        if department_seats[department] > 0 and not has_department[student_id]:
            # Assign student to the department
            student_to_department[student_id] = department
            has_department[student_id] = True
            department_seats[department] -= 1
            break

# Output the results
for student_id, department in sorted(student_to_department.items()):
    print(f"{student_id} {department}")
