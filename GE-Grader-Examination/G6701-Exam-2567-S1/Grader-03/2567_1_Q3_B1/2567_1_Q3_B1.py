# Create generation dictionary
# Key:   Generation acronym
# Value: list of [year, month, day, name]
generation = {'S':[], 'B':[], 'X':[], 'Y':[], 'Z':[], 'A':[]}

# Input names and their birthday
while(True):
    data = input().strip()
    # If the input is "-1", stop the process
    if(data == "-1"):
        break
    
    # Get name and their birthday information
    name, date = data.split()
    day, month, year = [int(item) for item in date.split('/')]
    
    # Input the information into the dictionary
    if(2468 <= year <= 2488):
        generation['S'].append([year, month, day, name])
    if(2489 <= year <= 2507):
        generation['B'].append([year, month, day, name])
    if(2508 <= year <= 2523):
        generation['X'].append([year, month, day, name])
    if(2524 <= year <= 2539):
        generation['Y'].append([year, month, day, name])
    if(2540 <= year <= 2555):
        generation['Z'].append([year, month, day, name])
    if(year >= 2556):
        generation['A'].append([year, month, day, name])

# Sort the name by their age in ascending order
# To do that, we need to sort their birthday in descending order
# For example, People who born at 25/3/2559 are younger than people who born at 17/1/2524
# But [2559,3,25] is greater than [17,1,2524]
generation['S'].sort(reverse = True)
generation['B'].sort(reverse = True)
generation['X'].sort(reverse = True)
generation['Y'].sort(reverse = True)
generation['Z'].sort(reverse = True)
generation['A'].sort(reverse = True)

# Output
n = int(input())
for i in range(n):
    letter = input().strip()
    output = letter + " : "
    # There is no people in that generation
    if(len(generation[letter]) == 0):
        output += "Not found"
    # There are people in that generation
    else:
        for [year, month, day, name] in generation[letter]:
            output += name + " "
    print(output)