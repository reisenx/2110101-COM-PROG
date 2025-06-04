# Create a list contains Real name
realname = ["Robert", "William", "James", "John", "Margaret", "Edward", "Sarah", "Andrew", "Anthony", "Deborah"]
nickname = ["Dick", "Bill", "Jim", "Jack", "Peggy", "Ed", "Sally", "Andy", "Tony", "Debbie"]

# Input number of names
n = int(input())

# Input names
names = []
for i in range(0,n):
    names.append(input())

# Output
# If the input is in realname list, output the nickname in the same index
# If the input is in nickname list, output the realname in the same index
# Else, Output "Not found"
for name in names:
    if(name in realname):
        index = realname.index(name)
        print(nickname[index])
    elif(name in nickname):
        index = nickname.index(name)
        print(realname[index])
    else:
        print("Not found")