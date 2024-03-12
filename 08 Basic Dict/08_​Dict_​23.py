# Input number of data
n = int(input())

# Input name and their telephone number
# In each line, it will split in to 3 string. 
# The first and second (data[0] and data[1]) are name and third one (data[2]) is telephone number
# Example: "Anthony Stark 086-111-1111"
# "Anthony Stark 086-111-1111" --> "Anthony", "Stark", "086-111-1111"
# name = "Anthony" + " " + "Stark"
# telephone = "086-111-1111"
name = {}
telephone = {}
for i in range(n):
    data = input().strip().split()
    name[data[2]] = data[0] + " " + data[1]
    telephone[data[0] + " " + data[1]] = data[2]

# Input number of output data
n = int(input())

# Put output data in a list
output_data = []
for i in range(n):
    data = input().strip()
    output_data.append(data)
    
# Output
# Don't forget to convert name <--> telephone before print()
for i in range(n):
    if(output_data[i] in name):
        print(output_data[i], "-->", name[output_data[i]])
    elif(output_data[i] in telephone):
        print(output_data[i], "-->", telephone[output_data[i]])
    else:
        print(output_data[i], "-->", "Not found")