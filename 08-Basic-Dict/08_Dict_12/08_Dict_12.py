# --------------------------------------------------
# File Name : 08_Dict_12.py
# Problem   : Nickname
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Initialize a dictionary with names and their nicknames
to_fullname = {}
to_nickname = {}

# Input name and nickname pairs
n = int(input())
for _ in range(n):
    fullname, nickname = input().strip().split()
    to_fullname[nickname] = fullname
    to_nickname[fullname] = nickname

# Search for a nickname or fullname
n = int(input())
for _ in range(n):
    name = input().strip()
    if name in to_fullname:
        print(to_fullname[name])
    elif name in to_nickname:
        print(to_nickname[name])
    else:
        print("Not found")
