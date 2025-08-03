# --------------------------------------------------
# File Name : 2567_3_Q5_B1.py
# Problem   : Least Common Animal
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Input animal amount and ranking display limit
animal_amount, ranking_display_limit = [int(num) for num in input().split()]

# Input animal name and its count, then store them in a dictionary based on count
animal_ranking = {}
for _ in range(animal_amount):
    # Extract animal name and count from input
    data = input().split()
    animal_name = data[0]
    animal_count = int(data[1])

    # Store the animal name in the dictionary based on its count
    if animal_count not in animal_ranking:
        animal_ranking[animal_count] = []
    animal_ranking[animal_count].append(animal_name)

# Output the animal names sorted by count and name in ascending order
for animal_count, animal_names in sorted(animal_ranking.items()):
    # Stop if the ranking display limit is reached
    if ranking_display_limit <= 0:
        break

    # Decrease the ranking display limit by the number of animal names on this count
    ranking_display_limit -= len(animal_names)

    # Sort animal names alphabetically and print them
    for animal_name in sorted(animal_names):
        print(animal_name, animal_count)
