# --------------------------------------------------
# File Name : 10_TSD_14.py
# Problem   : Database
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input filenames
course_filename = input().strip()
professor_filename = input().strip()
database_filename = input().strip()

# Initialize dictionaries for courses and professors
courses = {}
professors = {}

# Read courses from the course file
with open(course_filename) as course_file:
    for line in course_file:
        course_num, course_code = line.strip().split(",")
        courses[course_num] = course_code

# Read professors from the professor file
with open(professor_filename) as professor_file:
    for line in professor_file:
        prof_num, prof_name = line.strip().split(",")
        professors[prof_num] = prof_name

# Read the database file and process each entry
with open(database_filename) as database_file:
    for line in database_file:
        course_num, prof_num = line.strip().split(",")
        if course_num in courses and prof_num in professors:
            course_code = courses[course_num]
            prof_name = professors[prof_num]
            print(f"{course_code},{prof_name}")
        else:
            print("record error")
