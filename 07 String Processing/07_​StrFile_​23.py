# Input a namefile and year
# Slice 2 last digits from "year" string 
name,year = input().split()
year = year[-2:]

# Read a file
file = open(name, "r")

# Import data from a file
id_list = []
score_list = []
for line in file:
    id,score = line.split()
    id_list.append(id)
    score_list.append(float(score))

# Close a file
file.close()

# Calculate and output a minimum, maximum and average score of students in specified year
score_in_year_list = []
for i in range(len(id_list)):
    # Check ID if it is in the specified year and contain a score into a new list
    if(id_list[i][0:2] == year):
        score_in_year_list.append(score_list[i])
# In case of there are no student in that year
if(score_in_year_list == []):
    print("No data")
else:
    # Calculate a score
    max = max(score_in_year_list)
    min = min(score_in_year_list)
    average = sum(score_in_year_list) / len(score_in_year_list)
    # Output
    print("{:.1f} {:.1f} {:.1f}".format(min,max,average))