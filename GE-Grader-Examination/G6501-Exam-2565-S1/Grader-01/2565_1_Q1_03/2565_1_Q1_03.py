# Not guarantee 100/100 points on this code

# Reminder
# 1.) Import a library is prohibited
# 2.) eval() and exec() command is also prohibited

# The task is simple, just fine the answer of the input string
# The input won't have weird cases like "1+2-3.0", "1+2/3", "one+two", "1  +      2     -3"
# Example: "1+2-3+4-100+500"

# Input a string
equation = input().strip()

# Delete "+", then add a spacebar between number then split to a list of number
# Example: "1+2-3+4-100+500" --> "1 2 -3 4 -100 500" --> [1,2,-3,4,-100,500]
number = ""
for char in equation:
    if(char == '+'):
        number += " "
    elif(char == "-"):
        number += " -"
    else:
        number += char
number = number.split()
# Convert from string to integer
# ['1','2','-3','4','-100','500'] --> [1,2,-3,4,-100,500]
for i in range(len(number)):
    number[i] = int(number[i])

# Output the sum of number in a list
print(sum(number))