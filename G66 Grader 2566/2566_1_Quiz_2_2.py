# Not guarantee 100/100 points on this code
# Example testcase filename: 2110100.txt

# Input filename
filename = input().strip()

# Open a file
file = open(filename, "r")

# Read student details in a file
# Each line in the file will be in this format
# [ID],[Gender],[Faculty code],[Section],[Professor]
# We will read and collect the data in the dictionary in this format
# professor = {Professor:[[List of sections], Female, Male]}
professor = {}
for line in file:
    ID,gender,faculty,sec,prof = line.strip().split(',')
    sec = int(sec)
    # Add a new data, if that professor data is not exists yet
    if(prof not in professor):
        if(gender == 'F'):
            professor[prof] = [[sec],1,0]
        elif(gender == 'M'):
            professor[prof] = [[sec],0,1]
    # Edit data, if that professor data is already exists
    else:
        # Check gender
        if(gender == 'F'):
            professor[prof][1] += 1
        elif(gender == 'M'):
            professor[prof][2] += 1
        # Check section
        if(sec not in professor[prof][0]):
            professor[prof][0].append(sec)

# Sort the section list
for prof in professor:
    professor[prof][0].sort()

# Close the file
file.close()

# Input name of the professor
output_prof = input().strip()

# Output
if(output_prof not in professor):
    print("Not found")
else:
    text = ""
    sec_list,M,F = professor[output_prof]
    for i in range(len(sec_list)):
        sec_list[i] = str(sec_list[i])
    # Put 's' after 'Section' when that professor teach more than 1 section
    if(len(sec_list) == 1):
        text += "Section: "
    elif(len(sec_list) > 1):
        text += "Sections: "
    text += ",".join(sec_list) + " --> " + "F = " + str(F) + ", M = " + str(M)
    print(text)