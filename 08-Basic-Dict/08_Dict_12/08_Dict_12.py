# --------------------------------------------------
# File Name : 08_Dict_12.py
# Problem   : Nickname
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Initialize a dictionary with names and their nicknames
nickname_to_fullname = {}
fullname_to_nickname = {}

# Input name and nickname pairs
n = int(input())
for _ in range(n):
    fullname, nickname = input().strip().split()
    nickname_to_fullname[nickname] = fullname
    fullname_to_nickname[fullname] = nickname

# Search for a nickname or fullname
n = int(input())
for _ in range(n):
    name = input().strip()
    if name in nickname_to_fullname:
        print(nickname_to_fullname[name])

    elif name in fullname_to_nickname:
        print(fullname_to_nickname[name])

    else:
        print("Not found")
