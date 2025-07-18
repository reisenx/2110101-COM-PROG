# --------------------------------------------------
# File Name : 07_StrFile_33.py
# Problem   : File Merge
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input file names
filenames = input().strip().split()

# Initialize a list to store student data
students = []

# Read each file and append the data to the students list
for filename in filenames:
    with open(filename) as file:
        for line in file:
            sid, grade = line.split()
            faculty = sid[-2:]
            students.append([faculty, sid, grade])

# Sort the students list by faculty and then by student ID
students.sort()

# Output the sorted student data
for _, sid, grade in students:
    print(sid, grade)
