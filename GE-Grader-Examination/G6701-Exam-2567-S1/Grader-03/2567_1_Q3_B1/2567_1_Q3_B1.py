# --------------------------------------------------
# File Name : 2567_1_Q3_B1.py
# Problem   : Generations
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Generations information about name, start year, and end year
GEN_INFO = (
    ("S", 2468, 2488),
    ("B", 2489, 2507),
    ("X", 2508, 2523),
    ("Y", 2524, 2539),
    ("Z", 2540, 2555),
    ("A", 2556, 9999),
)

# Dictionary to hold people by generation
GEN_PEOPLE = {"S": [], "B": [], "X": [], "Y": [], "Z": [], "A": []}

while True:
    # Input each line of data
    data = input().strip()
    # Stop, if the input is "-1"
    if data == "-1":
        break

    # Extract name, birth day, month, and year
    name, birth_date = data.split()
    birth_day, birth_month, birth_year = [int(num) for num in birth_date.split("/")]

    # Create a tuple with birth year, month, day, and name
    info = (birth_year, birth_month, birth_day, name)

    # Determine the generation based on the birth year and add to the corresponding list
    for gen_name, start_year, end_year in GEN_INFO:
        if start_year <= birth_year <= end_year:
            GEN_PEOPLE[gen_name].append(info)

# Sort each generation's people by age in ascending order
# which means sorting by birth date in descending order
for _, people in GEN_PEOPLE.items():
    people.sort(reverse=True)

# Input query of generation names
n = int(input())
query_gen = []
for _ in range(n):
    query_gen.append(input().strip())

# Iterate through each queried generation name
for gen_name in query_gen:
    # If the generation exists and has people
    if gen_name in GEN_PEOPLE and len(GEN_PEOPLE[gen_name]) > 0:
        # Get the names of people in that generation
        names = []
        for _, _, _, name in GEN_PEOPLE[gen_name]:
            names.append(name)
        # Output the generation name and names
        print(f"{gen_name}: {' '.join(names)}")

    # If the generation does not exist or has no people
    else:
        print(f"{gen_name}: Not found")
