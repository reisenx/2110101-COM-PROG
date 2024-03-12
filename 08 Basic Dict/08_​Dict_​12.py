# Input number of input name
n = int(input())

# Input name and nickname and contains it in a dict
# Example: "Robert Dick"
# nickname["Robert"] = "Dick" and name["Dick"] = "Robert"
name = {}
nickname = {}
for i in range(n):
    temp_name, temp_nickname = input().split()
    name[temp_nickname] = temp_name
    nickname[temp_name] = temp_nickname

# Input number of output name
n = int(input())

# Convert name <--> nickname and put them in a list
output_name = []
for i in range(n):
    temp_name = input()
    if(temp_name in name):
        output_name.append(name[temp_name])
    elif(temp_name in nickname):
        output_name.append(nickname[temp_name])
    else:
        output_name.append("Not found")

# Output
for i in range(n):
    print(output_name[i])