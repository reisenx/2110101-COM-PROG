# Input number of path
n = int(input())

# Input data which contains [Island] [Next Island] [Days]
# Example: "WanoKuni Sphinx 6"
# Put a data into a 'next_island'
# next_island = {"WanoKuni" : ("Sphinx", 6), ...}
# NOTE: There's only 1 exit of each island only
#       Example: "WanoKuni" ---> "Sphinx" is correct but "Sphinx" ---> "WanoKuni" is wrong
next_island = {}
for i in range(n):
    island01, island02, days = input().strip().split()
    next_island[island01] = (island02, int(days))

# == Path ==
# 1.) Closed Path: It is the path that can go to the same island again
#     Example: ApplenineIsland ---> NewMarineford ---> PunkHazard ---> ApplenineIsland ---> ...
# 2.) Open Path: It is the path that can't go to the same island again
#     Example: Zou ---> WholecakeIsland ---> WanoKuni ---> Sphinx [END]

# == Algorithm ==
# 1.) Set initial 'current_island' as 'island01' and 'travel_islands' = ['island01']
# 2.) Travel to the next island and append data to 'travel_islands' and 'travel_days' 
#     then change the value in 'current_island'
# 3.) Loop until 'current_island' is equal to 'island02'
# 4.) The function returns a value
#     If found 'island02', returns sum(travel_days)
#     If not found, returns -1
def CheckPath(island01, island02):
    travel_days = []
    travel_islands = [island01]
    current_island = island01

    # Loop until 'current_island' is equal to 'island02'
    while(current_island != island02):
        # Get next island data
        if(current_island in next_island):
            island, days = next_island[current_island]
        # If current_island is not found, that means it is the end of an open path
        else:
            return -1
        
        # Check if we travel to the same island again, that means it is the end of a closed path
        if(island in travel_islands):
            return -1
        
        # Change the data to 'travel_days', 'travel_islands' and 'current_island'
        travel_days.append(days)
        travel_islands.append(island)
        current_island = island
    
    # If found 'island02', returns sum(travel_days)
    return sum(travel_days)

# Input number of cases
n = int(input())

# Input data that contains [Island01] [Island02]
# Example: "Wanokuni Zou"
# And check if there's a path from [Island01] to [Island02]
for i in range(n):
    island01, island02 = input().strip().split()
    days = CheckPath(island01,island02)
    if(days != -1):
        print(days)
    else:
        print("Route not found")