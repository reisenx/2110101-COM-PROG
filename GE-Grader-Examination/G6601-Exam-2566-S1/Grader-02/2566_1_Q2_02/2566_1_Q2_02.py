# --------------------------------------------------
# File Name : 2566_1_Q2_02.py
# Problem   : Registration
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------

# Input course database filename and query professor name
filename = input().strip()
search_professor = input().strip()

# Initialize lists to store information of query professor
sections = []
males = []
females = []

# Read the file and get information of the query professor
with open(filename) as file:
    for line in file:
        # Extract data from each line
        sid, sex, faculty, section, professor = line.strip().split(",")
        # If the professor matches the search query, store the information
        if professor == search_professor:
            # Store section number of the query professor
            if int(section) not in sections:
                sections.append(int(section))
            # Store male student IDs of the query professor
            if sex == "M" and sid not in males:
                males.append(sid)
            # Store female student IDs of the query professor
            elif sex == "F" and sid not in females:
                females.append(sid)
# Sort the sections in ascending order
sections.sort()

# Determine the output based on the number of sections found
result = ""
if len(sections) == 0:
    result = "Not found"
elif len(sections) == 1:
    result = f"Section: {sections[0]}"
elif len(sections) > 1:
    result = f"Sections: {','.join([str(section) for section in sections])}"

# Add the student count to the result if there are sections found
if len(sections) > 0:
    result += f" --> F = {len(females)}, M = {len(males)}"
# Output
print(result)
