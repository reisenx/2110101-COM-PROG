# --------------------------------------------------
# File Name : 2567_1_Q3_C2-sol1.py
# Problem   : The Python
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Initialize sets to store all employees and their bosses
all_employees = set()
boss_of = {}

# Initialize a dictionary to store sales values for each employee
sales = {}

# Input the subordinate and their boss along with the sales value
n = int(input())
for _ in range(n):
    # Extract subordinate, boss, and sales value from input
    sub, boss, sale = input().strip().split(",")

    # Add the subordinate and boss to the set of all employees
    all_employees.add(sub)
    all_employees.add(boss)

    # Add the boss to subordinate's boss mapping
    boss_of[sub] = boss
    # Add the sales value for the subordinate
    sales[sub] = int(sale)

    # Initialize the sales value for the boss if not already present
    if boss not in sales:
        sales[boss] = 0

# Add subordinates sales to their big boss
for sub, boss in boss_of.items():
    # Get the sales value of the subordinate
    sale = sales[sub]

    # Traverse up the hierarchy to find the big boss of the subordinate
    current_boss = boss
    while current_boss in boss_of:
        current_boss = boss_of[current_boss]

    # Add the subordinate's sales to the big boss's sales
    sales[current_boss] += sale

# Initialize a list to store the big boss and their total sales
result = []

# Find all big bosses (those who are not subordinates of anyone)
big_bosses = all_employees - set(boss_of.keys())

# Store the total sales for each big boss
for boss in big_bosses:
    result.append((-sales[boss], boss))
result.sort()

# Output the total sales for each big boss sorted by sales value in descending order
for sale, boss in result:
    print(f"Boss {boss} {-sale}")
