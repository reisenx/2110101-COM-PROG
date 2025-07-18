# --------------------------------------------------
# File Name : P2_09_Vitamin.py
# Problem   : Part-II Vitamin
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# Initialize the fruit dictionary
FRUITS = {}

# Input fruit information
n = int(input())
for _ in range(n):
    data = input().strip().split()
    fruit = data[0]
    vitamins = [float(percent) for percent in data[1:]]
    FRUITS[fruit] = vitamins

# Input the command
cmd = input().strip().split()

# Command: show
# Output all fruits with their vitamin percentages in the order of input
if cmd[0] == "show":
    for fruit, vitamins in FRUITS.items():
        print(f"{fruit} {' '.join([str(percent) for percent in vitamins])}")

# Command: get
# Output the vitamin percentages of a specific fruit
elif cmd[0] == "get":
    fruit = cmd[1]
    # Check if the fruit exists in the dictionary
    if fruit in FRUITS:
        vitamins = FRUITS[fruit]
        print(f"{fruit} {' '.join([str(percent) for percent in vitamins])}")
    # If the fruit does not exist, output "not found"
    else:
        print(f"{fruit} not found")

# Command: avg
# Output the average percentage of a specific vitamin across all fruits
elif cmd[0] == "avg":
    idx = int(cmd[1]) - 1
    # Get all vitamin percentages for the specified index
    percentages = []
    for _, vitamins in FRUITS.items():
        percentages.append(vitamins[idx])
    # Calculate and print the average percentage
    print(round(sum(percentages) / len(percentages), 4))

# Command: max
# Output the fruit with the maximum percentage of a specific vitamin
elif cmd[0] == "max":
    idx = int(cmd[1]) - 1
    # Create a list of fruits with their vitamin percentages for sorting
    vitamin_ranks = []
    for fruit, vitamins in FRUITS.items():
        vitamin_ranks.append([-vitamins[idx], fruit])
    # Sort the list by vitamin percentage (descending) and fruit name (ascending)
    vitamin_ranks.sort()

    # Output the fruit with the maximum percentage
    max_fruit = vitamin_ranks[0][1]
    max_percentage = -vitamin_ranks[0][0]
    print(f"{max_fruit} {max_percentage}")

# Command: sort
# Output all fruits sorted by a specific vitamin percentage
elif cmd[0] == "sort":
    idx = int(cmd[1]) - 1
    # Create a list of fruits with their vitamin percentages for sorting
    vitamin_ranks = []
    for fruit, vitamins in FRUITS.items():
        vitamin_ranks.append([vitamins[idx], fruit])
    # Sort the list by vitamin percentage (ascending) and fruit name (ascending)
    vitamin_ranks.sort()

    # Output the sorted fruits
    result = []
    for _, fruit in vitamin_ranks:
        result.append(fruit)
    print(" ".join(result))
