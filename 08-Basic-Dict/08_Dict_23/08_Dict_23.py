# --------------------------------------------------
# File Name : 08_Dict_23.py
# Problem   : Telephone Directory
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Initialize the telephone directory
name_to_telephone = {}
telephone_to_name = {}

# Input the entries in the directory
n = int(input())
for _ in range(n):
    first_name, last_name, telephone = input().strip().split()
    name = f"{first_name} {last_name}"
    name_to_telephone[name] = telephone
    telephone_to_name[telephone] = name

# Search queries in the directory
n = int(input())
for _ in range(n):
    query = input().strip()
    if query in name_to_telephone:
        print(f"{query} --> {name_to_telephone[query]}")

    elif query in telephone_to_name:
        print(f"{query} --> {telephone_to_name[query]}")

    else:
        print(f"{query} --> Not found")
