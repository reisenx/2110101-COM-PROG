# --------------------------------------------------
# File Name : 08_Dict_23.py
# Problem   : Telephone Directory
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Initialize the telephone directory
to_telephone = {}
to_name = {}

# Input the entries in the directory
n = int(input())
for _ in range(n):
    first_name, last_name, telephone = input().strip().split()
    name = f"{first_name} {last_name}"
    to_telephone[name] = telephone
    to_name[telephone] = name

# Search queries in the directory
n = int(input())
for _ in range(n):
    query = input().strip()
    if query in to_telephone:
        print(f"{query} --> {to_telephone[query]}")
    elif query in to_name:
        print(f"{query} --> {to_name[query]}")
    else:
        print(f"{query} --> Not found")
