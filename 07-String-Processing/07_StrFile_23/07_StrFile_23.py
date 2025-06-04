# Input a namefile and year
# Slice 2 last digits from "year" string 
name,year = input().split()
year = year[-2:]

# Read a file
file = open(name, "r")

# Read data from a file and put the data in a list 'students'
# students = [[ID01, Score01], [ID02, Score02], ...]
students = []
for line in file:
    ID,score = line.strip().split()
    students.append([ID, float(score)])

# Close a file
file.close()

# Find score of all students in specified year
score_in_year = []
for ID,score in students:
    if(ID[0:2] == year):
        score_in_year.append(score)

# In case of there are no student in that year
if(score_in_year == []):
    print("No data")
else:
    # Calculate minimum, maximum and average score
    max = max(score_in_year)
    min = min(score_in_year)
    average = sum(score_in_year) / len(score_in_year)
    # Output
    print(min,max,average)