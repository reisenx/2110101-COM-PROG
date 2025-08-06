# --------------------------------------------------
# File Name : 2565_1_Q3_03.py
# Problem   : APEC Headache
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

# Initialize dictionaries to store allies and enemies of countries
allies = {}
enemies = {}


# Initialize the allies and enemies dictionaries for each country
def init_countries(countries):
    for country in countries:
        if country not in allies:
            allies[country] = set()
        if country not in enemies:
            enemies[country] = set()


# Add allies of each country based on the list of countries
def add_allies(countries):
    for country in countries:
        allies[country] |= set(countries) - {country}


# Add enemies of each country based on the list of countries
def add_enemies(countries):
    for country in countries:
        enemies[country] |= set(countries) - {country}


# Add more enemies based on the allies and enemies relationships
def add_more_enemies():
    # Add allies of enemies to the enemies of each country
    for country, enemy_countries in enemies.items():
        # Collect all allies of enemies
        allies_of_enemies = set()
        for enemy in enemy_countries:
            allies_of_enemies |= allies[enemy]
        # Add these allies to the enemies of the country
        enemies[country] |= allies_of_enemies

    # Add enemies of allies to the enemies of each country
    for country, ally_countries in allies.items():
        # Collect all enemies of allies
        enemies_of_allies = set()
        for ally in ally_countries:
            enemies_of_allies |= enemies[ally]
        # Add these enemies to the enemies of the country
        enemies[country] |= enemies_of_allies


# Check if two countries are enemies
def is_enemy_pair(country01, country02):
    return country02 in enemies[country01] or country01 in enemies[country02]


# Check if the circular table of countries can be a valid arrangement
def is_table_valid(countries):
    # Ensure the list is circular by appending the first country to the end
    circular_countries = countries + [countries[0]]
    # Check each pair of adjacent countries if they are enemies
    for i in range(len(circular_countries) - 1):
        # If any adjacent pair is an enemy pair, return False
        if is_enemy_pair(circular_countries[i], circular_countries[i + 1]):
            return False
    # If no adjacent pairs are enemies, return True
    return True


# Main function
def main():
    while True:
        # Read input data
        data = input().strip().split()
        # If the input is "End", break the loop
        if data == ["End"]:
            break

        # Extract the command and the list of countries
        cmd = data[0]
        countries = data[1:]

        # Initialize the allies and enemies dictionary for the given countries
        init_countries(countries)
        # Add allies for each country in the list
        if cmd == "Ally":
            add_allies(countries)
        # Add enemies for each country in the list
        elif cmd == "Enemy":
            add_enemies(countries)
        # Check if the arrangement of countries can be a valid table arrangement
        elif cmd == "Table":
            # Add more enemies based on the current allies and enemies relationships
            add_more_enemies()
            # Check if the arrangement of countries is valid
            if is_table_valid(countries):
                print("Okay")
            else:
                print("No")


# Run the main function to start the program
main()
