# Example testcase filename 1: courses.txt
# Example testcase filename 2: teachers.txt
# Example testcase filename 3: database.txt
# Example testcase filename 4: database2.txt

# Input filenames
filename01 = input().strip()
filename02 = input().strip()
filename03 = input().strip()

# Open files
file01 = open(filename01, "r")
file02 = open(filename02, "r")
file03 = open(filename03, "r")

# Create a 'courses' dictionary from data in 'file01'
# file01 is a courses file and each line will be in the format
# [Course Number],[Course Code]
# Example: "1,2110101"
courses = {}
for line in file01:
    c_num, c_code = line.strip().split(',')
    courses[c_num] = c_code

# Create a 'professors' dictionary from data in 'file02'
# file02 is a professor file and each line will be in the format
# [Professor Number],[Professor Name]
# Example: 9,Somchai
professors = {}
for line in file02:
    p_num, p_name = line.strip().split(',')
    professors[p_num] = p_name

# Output by using data 'file03'
# file03 is a database file and each line will be in the format
# [Course Number],[Professor Number]
# If the number isn't exist, output "record error"
for line in file03:
    c_num, p_num = line.strip().split(',')
    if((c_num not in courses) or (p_num not in professors)):
        print("record error")
    else:
        print(courses[c_num] + "," + professors[p_num])

# Close the file
file01.close()
file02.close()
file03.close()