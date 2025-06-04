# Input number of data
n = int(input())

# Input name and their telephone number
# In each line contains [First Name] [Last Name] [Telephone]
# Example: "Anthony Stark 086-111-1111"
name_to_tel = {}
tel_to_name = {}
for i in range(n):
    first_name, last_name, telephone = input().strip().split()
    name = first_name + " " + last_name
    name_to_tel[name] = telephone
    tel_to_name[telephone] = name

# Output
n = int(input())
for i in range(n):
    search = input().strip()
    if(search in name_to_tel):
        print(search, "-->", name_to_tel[search])
    
    elif(search in tel_to_name):
        print(search, "-->", tel_to_name[search])
    
    else:
        print(search, "--> Not found")