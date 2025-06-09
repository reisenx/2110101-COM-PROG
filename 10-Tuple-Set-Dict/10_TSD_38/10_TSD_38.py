# Input a BTS stations in the format below
# [Staion 1-1] [Staion 1-2]     <-- Input 2 stations that distance = 1 station
# [Staion 2-1] [Staion 2-2]     <-- Input 2 stations that distance = 1 station
# [Staion 3-1] [Staion 3-2]     <-- Input 2 stations that distance = 1 station
# ...
# [Current Station]             <-- Input 1 station where the traveler is

# Put a data to 'Stations' which its item contains
# {Station name : {Set of stations that distance = 1 station}, ...}
# After get the final line of the input, manage the data and put in set 'Travel'
# Travel = {Set of station that distance = 0-2 station}

# == Stations Algorithm ==
# 1.) Split input into a list
# > Example: "Siam ChitLom" --> data = ["Siam", "ChitLom"]
# 2.) Put data[0] as a key and data[1] as a value (if data[0] key already exists, then just add data[1] to value)
# > Example: Stations = {"Siam":{"ChitLom"}}
# 3.) Put data[1] as a key and data[0] as a value (if data[1] key already exists, then just add data[0] to value)
# > Example: Stations = {"Siam":{"ChitLom"}, "ChitLom":{"Siam"}}

# == Travel Algorithm ==
# 1.) After get final line of input, Setup 'Travel' = value of 'Stations' with the input key
# > Example: Stations = {'Siam' : {'ChitLom', 'NationalStadium', 'PhayaThai'}}
# > If Current Station = "Siam", then 'Travel' = {'ChitLom', 'NationalStadium', 'PhayaThai'} data
# 2.) Union 'Travel' with 'Stations' value of all items in the set from step 1
# > Example: 'Travel' = {'ChitLom', 'NationalStadium', 'PhayaThai'}
# > Then union 'Travel' with Stations['ChitLom'], Stations['NationalStadium'] and Stations['PhayaThai']
Stations = {}
while(True):
    data = input().strip()
    # Input 2 stations that distance = 1 station
    if(len(data.split()) == 2):
        data = data.split()
        # Put data[0] as a key and data[1] as a value
        if(data[0] not in Stations):
            Stations[data[0]] = {data[1]}
        else:
            Stations[data[0]].add(data[1])
        # Put data[1] as a key and data[0] as a value
        if(data[1] not in Stations):
            Stations[data[1]] = {data[0]}
        else:
            Stations[data[1]].add(data[0])
    
    # Input Current Station
    else:
        # In case of Current Station doesn't exist in 'Stations' dictionary, just output Current Station
        if(data not in Stations):
            print(data)
            break
        else:
            # Find Travel set
            Travel = Stations[data]
            for item in Stations[data]:
                Travel = Travel.union(Stations[item])
            # Convert Travel from set to list and sort in alphabetical order
            Travel = sorted(Travel)
            # Output
            for item in Travel:
                print(item)
            break