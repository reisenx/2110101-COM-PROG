# --------------------------------------------------
# File Name : 05_List_12.py
# Problem   : Nicknames
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# List of real names and their corresponding nicknames
REAL_NAMES = [
    "Robert",
    "William",
    "James",
    "John",
    "Margaret",
    "Edward",
    "Sarah",
    "Andrew",
    "Anthony",
    "Deborah",
]
NICKNAMES = [
    "Dick",
    "Bill",
    "Jim",
    "Jack",
    "Peggy",
    "Ed",
    "Sally",
    "Andy",
    "Tony",
    "Debbie",
]

# Input amount of names
n = int(input())

# Output the corresponding nicknames
for _ in range(n):
    name = input().strip()
    # Output the nickname if found
    if name in REAL_NAMES:
        index = REAL_NAMES.index(name)
        print(NICKNAMES[index])
    # Output the real name if found
    elif name in NICKNAMES:
        index = NICKNAMES.index(name)
        print(REAL_NAMES[index])
    # Output "Not found" if neither is found
    else:
        print("Not found")
