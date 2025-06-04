# Input number of students
n = int(input())

# Create register dictionary that contains
# register = {Subject:{Year:Amount, ...}, ...}
# NOTE: We can use dictionary inside a dictionary
register = {}
for i in range(n):
    # Get student information
    # - data[0] is student ID
    # - data[0][:2] is the first 2 digit of an ID (Ex. '6632200221' --> '66')
    # - data[1:] are subjects list
    data = input().strip().split()
    year = 2500 + int(data[0][:2])
    subjects = data[1:]
    
    # Put a student information into a dictionary
    for subject in subjects:
        # Create a subject in register dictionary
        if(subject not in register):
            register[subject] = {}
        # Create year in subject dictionary
        if(year not in register[subject]):
            register[subject][year] = 1
        else:
            register[subject][year] += 1

# Output
subjectOut = input().strip().split()
for subject in subjectOut:
    # Subject not found
    if(subject not in register):
        print(subject, "None")
    # Output subject information
    else:
        # Convert {2567:1, 2565:3} --> ["2565:3", "2567:1"]
        sortedInfo = []
        for year, amount in register[subject].items():
            sortedInfo.append(str(year) + ":" + str(amount))
        sortedInfo.sort()
        # Output
        print(subject, ", ".join(sortedInfo))