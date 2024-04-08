realname = ["Robert", "William", "James", "John", "Margaret", "Edward", "Sarah", "Andrew", "Anthony", "Deborah"]
nickname = ["Dick", "Bill", "Jim", "Jack", "Peggy", "Ed", "Sally", "Andy", "Tony", "Debbie"]

n = int(input())
names = []
for i in range(0,n):
    names.append(input())

for name in names:
    if(name in realname):
        index = realname.index(name)
        print(nickname[index])
    elif(name in nickname):
        index = nickname.index(name)
        print(realname[index])
    else:
        print("Not found")