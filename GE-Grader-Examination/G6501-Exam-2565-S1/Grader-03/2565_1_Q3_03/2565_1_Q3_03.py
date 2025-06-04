# Create dictionary that contains set of allies and enemies of every input countries
allies = {}
enemies = {}

while(True):
    command = input().strip().split()
    
    # Command: End
    # Stop all process (break the loop)
    if(command[0] == "End"):
        break

    # Command: Ally
    # This command tell us that the following countries are allies
    # Example: "Ally America England France"
    # This tell us that America, England and France are allies

    # == Algorithm ==
    # 1.) command[1:] will be list of countries
    # > Example: command[1:] = ['America', 'England', 'France']
    # 2.) Reconstruct the list to find allies of each country and contains in 'temp' list
    # > Example: command[1] == 'America', command[2] == 'England', command[3] == 'France'
    # > Allies of 'America' are command[1:1] + command[2:] = ['England','France']
    # > Allies of 'England' are command[1:2] + command[3:] = ['America','France']
    # > Allies of 'France' are command[1:3] + command[4:] = ['America','England']
    # 3.) Contains the data in 'allies' dictionary (Convert the list of countries to a set)
    #   3.1.) If the country is not exist in 'allies' dictionary, just add it
    #   3.2.) If the country is already exist in 'allies' dictionary, union the set
    # > Example: allies = {'America':{'England','France'}, 'England':{'America','France'}, ...}
    if(command[0] == "Ally"):
        for i in range(1, len(command)):
            # Reconstruct the list to find allies of each country
            country = command[i]
            temp = command[1:i] + command[i+1:]
            # Contains the data in 'allies' dictionary
            temp = set(temp)
            if(country not in allies):
                allies[country] = temp
            else:
                allies[country] = allies[country] | temp
            # Ensure that every country are in 'enemies' dictionary
            if(country not in enemies):
                enemies[country] = set()
    
    # Command: Enemy
    # This command tell us that the following countries are enemies
    # Example: "Enemy China America"
    # This tell us that China and America are enemies

    # == Algorithm ==
    # 1.) command[1:] will be list of countries
    # > Example: command[1:] = ['China','America']
    # 2.) Reconstruct the list to find enemies of each country and contains in 'temp' list
    # > Example: command[1] == 'China', command[2] == 'America'
    # > Enemies of 'China' are command[1:1] + command[2:] = ['America']
    # > Enemies of 'America' are command[1:2] + command[3:] = ['China']
    # 3.) Contains the data in 'enemies' dictionary (Convert the list of countries to a set)
    #   3.1.) If the country is not exist in 'enemies' dictionary, just add it
    #   3.2.) If the country is already exist in 'enemies' dictionary, union the set
    # > Example: enemies = {'China':{'America'}, 'America':{'China'}, ...}
    if(command[0] == "Enemy"):
        for i in range(1, len(command)):
            # Reconstruct the list to find enemy of each country
            country = command[i]
            temp = command[1:i] + command[i+1:]
            # Contains the data in 'enemies' dictionary
            temp = set(temp)
            if(country not in enemies):
                enemies[country] = temp
            else:
                enemies[country] = enemies[country] | temp
            # Ensure that every country are in 'allies' dictionary
            if(country not in allies):
                allies[country] = set()
    
    # Update 'allies' and 'enemies' dictionary
    # - Allies of an enemy is always enemies
    for country in enemies:
        temp = set()
        for enemy in enemies[country]:
            temp = temp | allies[enemy]
        enemies[country] = enemies[country] | temp
    # - Enemies of ally is always enemies
    for country in allies:
        temp = set()
        for ally in allies[country]:
            temp = temp | enemies[ally]
        enemies[country] = enemies[country] | temp
    
    # Command: Table
    # This command can check if the there're no enemies that sit close to each other
    # The country may not exist in both 'allies' and 'enemies' dictionary
    # == Possible cases ==
    # Case 1: Only 1 country sitting
    # > This always 'Okay'
    # Case 2: Only 2 country sitting
    # > Just enemy status of both country
    # Case 3: More than 2 country sitting
    # > Check by using algorithm below
    # NOTE: The table is round table

    # == Algorithm ==
    # 0.) First of all, to make sure that every country exist in 'allies' and 'enemy' dictionary.
    #     Just add an empty set as a dictionary value to the country that not exist in the dictionary
    # 1.) Check cases above. If it is in case 3 do the following
    # 2.) Since it is round table, append command[1] and command[2] to the end of the table
    # > Example: ['America','England','Iceland'] --> ['America','England','Iceland','America','England']
    # 3.) Check if the left or the right of each country is the enemy (If enemy found, break the loop)
    # > Example: ['America','England','Iceland','America','England']
    # > Loop 1 ('England'): Check enemy status of 'America' and 'Iceland'
    # > Loop 2 ('Iceland'): Check enemy status of 'England' and 'America'
    # > Loop 3 ('America'): Check enemy status of 'Iceland' and 'England'
    if(command[0] == "Table"):
        
        print(allies)
        print(enemies)
        
        # Ensure that every country are in 'allies' and 'enemies' dictionary
        for country in command[1:]:
            if(country not in allies):
                allies[country] = set()
            if(country not in enemies):
                enemies[country] = set()
        
        # Case 1: Only 1 country sitting
        if(len(command) == 2):
            print("Okay")
        # Case 2: Only 2 country sitting
        elif(len(command) == 3):
            if(command[1] in enemies[command[2]] or command[2] in enemies[command[1]]):
                print("No")
            else:
                print("Okay")
        # Case 3: More than 2 country sitting
        elif(len(command) > 3):
            IsOkay = True
            command.append(command[1])
            command.append(command[2])
            for i in range(2, len(command)-1):
                if(command[i-1] in enemies[command[i]] or command[i+1] in enemies[command[i]]):
                    IsOkay = False
                    break
            if(IsOkay):
                print("Okay")
            else:
                print("No")