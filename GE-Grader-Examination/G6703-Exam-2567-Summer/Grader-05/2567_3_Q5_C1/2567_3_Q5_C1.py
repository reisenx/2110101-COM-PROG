# --------------------------------------------------
# File Name : 2567_3_Q5_C1.py
# Problem   : Student Registration
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Initialize dictionaries to store student IDs by year, faculty, and subject
students_in_year = {}
students_in_faculty = {}
students_in_subject = {}

# Input the filename and display type
data = input().strip().split()
filename = data[0].strip()
display_type = int(data[1])

# Read the file and store student IDs in the respective dictionaries
with open(filename) as file:
    # Read each line in the file
    for line in file:
        # Extract student ID, subject, year and faculty from the line
        student_id, subject = line.strip().split()
        year = student_id[:2]
        faculty = student_id[-2:]

        # Add student ID grouped on year to the dictionaries
        if year not in students_in_year:
            students_in_year[year] = []
        students_in_year[year].append(student_id)

        # Add student ID grouped on faculty to the dictionaries
        if faculty not in students_in_faculty:
            students_in_faculty[faculty] = []
        students_in_faculty[faculty].append(student_id)

        # Add student ID grouped on subject to the dictionaries
        if subject not in students_in_subject:
            students_in_subject[subject] = []
        students_in_subject[subject].append(student_id)

# Output the student IDs grouped by year in input order
if display_type == 1:
    for _, student_ids in students_in_year.items():
        print(" ".join(student_ids))

# Output the student IDs grouped by faculty in input order
elif display_type == 2:
    for _, student_ids in students_in_faculty.items():
        print(" ".join(student_ids))

# Output the student IDs grouped by subject in input order
elif display_type == 3:
    for _, student_ids in students_in_subject.items():
        print(" ".join(student_ids))
