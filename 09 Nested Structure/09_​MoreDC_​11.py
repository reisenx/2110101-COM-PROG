# Input number of code line
n = int(input())

# Input a code a append into a list
code = []
for i in range(n):
    line = input()
    code.append(line)

# Output
# Algorithm
# 1.) Use for loop to count dot (.) in front of the code
# 2.) Output '.' count//2 times then the rest of the code
# 3.) Reset count to 0 every new line of code
for line in code:
    count = 0
    for char in line:
        if(char == '.'):
            count += 1
        else:
            break
    print("."*(count//2) + line[count:])