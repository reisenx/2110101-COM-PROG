# Create a list contains Real name
realname = ["Robert", "William", "James", "John", "Margaret", "Edward", "Sarah", "Andrew", "Anthony", "Deborah"]
nickname = ["Dick", "Bill", "Jim", "Jack", "Peggy", "Ed", "Sally", "Andy", "Tony", "Debbie"]

# Input
n = int(input())
item = []
for i in range(0,n):
    item.append(input())

# Output
# If the input is in realname list, output the nickname in the same index
# If the input is in nickname list, output the realname in the same index
# Else, Output "Not found"
for i in range(0,n):
    if(item[i] in realname):
        print(nickname[realname.index(item[i])])
    elif(item[i] in nickname):
        print(realname[nickname.index(item[i])])
    else:
        print("Not found")