# Input 2 filenames
name1,name2 = input().split()
# Create an empty list for contain unique faculty code and student year
# Example: 66322002[21]
unique_faculty = []

# Read the first file
file1 = open(name1, "r")

# Import data from the first file and put them in a list
# Example: [["6232222228", "3.54"], ["6632200221", "4.00"]]
i = 0
student_data = []
for line in file1:
    student_data.append(line.split())
    # Check unique faculty (Example: 66322002[21])
    if(student_data[i][0][-2:] not in unique_faculty):
        unique_faculty.append(student_data[i][0][-2:])
    i += 1
# Close the first file
file1.close()

# Read the second file
file2 = open(name2, "r")

# Import data from the second file and put them in a list
i = 0
for line in file2:
    student_data.append(line.split())
    # Check unique faculty (Example: 66322002[21])
    if(student_data[i][0][-2:] not in unique_faculty):
        unique_faculty.append(student_data[i][0][-2:])
    i += 1

# Close the second file
file2.close()
# Sorting code in unique_faculty
unique_faculty.sort()

# Sorting and Output the data
# Loop output using unique faculty
for code in unique_faculty:
    student_data_in_year = []
    # Find a student in each faculty code
    for sublist in student_data:
        if(sublist[0][-2:] == code):
            student_data_in_year.append(sublist)
    # Sorting student ID in each faculty
    student_data_in_year.sort()
    # Output student data in each faculty
    for id,GPA in student_data_in_year:
        print(id, GPA)