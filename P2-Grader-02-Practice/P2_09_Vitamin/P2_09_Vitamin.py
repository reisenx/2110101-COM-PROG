# Input put number of friuts
n = int(input())

# Input vitamin details of input fruits and put them in the dictionary
# data[0] is fruit name, and the rest are vitamin details
# Exmaple: "apricots 0.2 0.06 0.05 0.05" --> {'apricots':[0.2, 0.06, 0.05, 0.05]}
fruits = {}
for i in range(n):
    data = input().split()
    # Convert vitamin amount from string to float
    for j in range(1,len(data)):
        data[j] = float(data[j])
    fruits[data[0]] = data[1:]

# Input command
command = input().strip().split()
# 'show' command is to show all input data
if(command[0] == 'show'):
    for item in fruits:
        # Create an empty string
        text = ""
        # Add the name of the fruit
        text += item + " "
        # Add amount of vitamins of that fruit
        for amount in fruits[item]:
            text += str(amount) + " "
        # Output
        print(text.strip())

# 'get' command is to show the input friut data
# command[1] is the fruit name
# Considered that uppercase and lowercase are not the same
# If there're no matching name, output as "not found"
# Example: get banana
elif(command[0] == 'get'):
    if(command[1] in fruits):
        # Create an empty string
        text = ""
        # Add the name of the fruit
        text += command[1] + " "
        # Add amount of vitamins of that fruit
        for amount in fruits[command[1]]:
            text += str(amount) + " "
        # Output
        print(text.strip())
    else:
        print(command[1], "not found")

# 'avg' command is to find the average amount of that vitamin type
# round a average number to 4 decimal places
# Example: {'apricots':[0.2, 0.06, 0.05, 0.05]} means
# - Apricots has vitamin 1 = 0.2
# - Apricots has vitamin 2 = 0.06
# - Apricots has vitamin 3 = 0.05
# - Apricots has vitamin 4 = 0.05
elif(command[0] == 'avg'):
    index = int(command[1])-1
    vitamin_list = []
    for item in fruits:
        vitamin_list.append(fruits[item][index])
    average = round(sum(vitamin_list) / len(vitamin_list), 4)
    print(average)

# 'max' command is to find maximum amount of that vitamin type
# If there are mone than 1 friut that have maximum vitamin, output the first name that appear in dictionary
elif(command[0] == 'max'):
    # Create and find a list contains amount of vitamin of each fruit
    index = int(command[1])-1
    vitamin_list = []
    for item in fruits:
        vitamin_list.append(fruits[item][index])
    # Find maximum amount of vitamin
    maximum = max(vitamin_list)
    # Find a list of fruit names that have maximum amout of vitamin
    max_fruit = []
    for item in fruits:
        if(fruits[item][index] == maximum):
            max_fruit.append(item)
    # Sort a name in alphabetical order
    max_fruit.sort()
    # Output the first name in 'max_fruit' and 'maximum' value
    print(max_fruit[0], maximum)

# 'sort' command is to sort a fruit bu its vitamin in ascending order
# If there are mone than 1 friut that have maximum vitamin, output the first name that appear in dictionary
elif(command[0] == 'sort'):
    # Create and find a list contains amount of vitamin of each fruit
    index = int(command[1])-1
    vitamin_list = []
    for item in fruits:
        if(fruits[item][index] not in vitamin_list):
            vitamin_list.append(fruits[item][index])
    # Sort the vitamin in ascending order
    vitamin_list.sort()
    # Output the name using the value in 'vitamin_list'
    name_sort = ""
    for amount in vitamin_list:
        # Reset the temp_name list
        temp_name = []
        # Find a list of fruit names that have the same amout of vitamin
        for item in fruits:
            if(fruits[item][index] == amount):
                temp_name.append(item)
        # Sort the name that have the same amount of vitamin
        temp_name.sort()
        # Put them all to a string
        for name in temp_name:
            name_sort += name + " "
    # Output the string
    name_sort = name_sort.strip()
    print(name_sort)
