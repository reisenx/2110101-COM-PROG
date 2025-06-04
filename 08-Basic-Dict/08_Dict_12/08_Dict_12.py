# Input number of input name
n = int(input())

# Input name and nickname and contains it in a dict
# Example: "Robert Dick"
# name_to_nick["Robert"] = "Dick" and nick_to_name["Dick"] = "Robert"
nick_to_name = {}
name_to_nick = {}
for i in range(n):
    name, nickname = input().split()
    nick_to_name[nickname] = name
    name_to_nick[name] = nickname

# Output
n = int(input())
for i in range(n):
    search = input()
    if(search in nick_to_name):
        print(nick_to_name[search])

    elif(search in name_to_nick):
        print(name_to_nick[search])

    else:
        print("Not found")