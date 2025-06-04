# Not guarantee 100/100 points on this code

# Input number of teams
n = int(input())

# Input football team details which contains
# [Name] [Country]
# Put a data to a dictionary in format
# teams = {Name:Country}
teams = {}
for i in range(n):
    name, country = input().strip().split()
    teams[name] = country

# Input team group and check if the group is valid
# The team group is valid when it meets all citeria below
# 1.) All team must be in 'teams' dictionary
# 2.) All team in a group must come from different country
while(True):
    data = input().strip()
    IsValid = True
    country = []
    if(data == 'q'):
        break
    else:
        group = data.split()
        # Check if the group is valid or not
        for item in group:
            # Check if a team is not exist in a teams dictionary
            if(item not in teams):
                IsValid = False
                break
            # Check if there's the same country in the same group
            elif(teams[item] in country):
                IsValid = False
                break
            # Add country of each team to a list
            country.append(teams[item])
        
        # Output
        if(IsValid):
            print("OK")
        else:
            print("Not OK")
