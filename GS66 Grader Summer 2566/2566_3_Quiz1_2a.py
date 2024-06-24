# Unofficial Solution

# Example
# d = ['01H10', '02H10', '01A10', '03H14', '04H12']
# result = ['Home', 26]
def f(d):
    # Convert 'd' into a 'process'
    # Example:
    # > d = ['01H10', '02H10', '01A10', '03H14', '04H12']
    # > process = [['H', 10], ['H', 10], ['A', 10], ['H', 14], ['H', 12]]
    process = []
    for player in d:
        team, time = player[2], int(player[3:])
        process.append([team, time])
    
    # Calculate football possesion time
    home,away = 0,0
    possession = []
    for i in range(len(process)):
        team, time = process[i]
        # Special Case 1
        # Example: [..., '01A10', '03H14', ...]
        if(team == 'H' and away > 0):
            possession.append([away, 'Away'])
            away = 0
            home += time
            
        # Special Case 2
        # Example: [..., '02H10', '01A10', ...]
        elif(team == 'A' and home > 0):
            possession.append([home, 'Home'])
            home = 0
            away += time
            
        # Normal Cases
        elif(team == 'H'):
            home += time
        elif(team == 'A'):
            away += time
    
    # Don't forget to append the last one
    if(process[-1][0] == 'H'):
        possession.append([home, 'Home'])
    elif(process[-1][0] == 'A'):
        possession.append([away, 'Away'])
    
    # Sort a value (Maximum time will be at the last one)
    # Example: [[10, 'Away'], [20, 'Home'], [26, 'Home']]
    possession.sort()

    # Return a value
    return possession[-1][::-1]

print(f(['01H10', '02H10', '01A10', '03H14', '04H12']))