# Not guarantee 100/100 points on this code
# Example testcase filename 1: color.txt
# Example testcase filename 2: song.txt

# Input 2 filenames
filename01 = input().strip()
filename02 = input().strip()

# Open 2 files
file01 = open(filename01, "r")
file02 = open(filename02, "r")

# Import data from file01 (Color file)
# Put all the color in the file into a list (Convert them all to lowercase)
color_list = []
for line in file01:
    temp = [item.lower() for item in line.strip().split()]
    for item in temp:
        if(item not in color_list):
            color_list.append(item)

# Create a function that can find and return matching color and its index as a dictionary
# Example:
# color_list = ['orange', 'yellow', 'pink', 'green']
# line = "Orange, yellow pinky blue orange BlaCkZzZ!!! and pInKiEeE???"
# In this case, this function will return
# {0:'orange', 8:'yellow', 15:'pink', 26:'orange', 49:'pink'}
# If there'are no matching color, then return empty dict {}
            
# Algorithm
# Example:
# color_list = ['orange', 'yellow', 'pink', 'green']
# line = "Orange, yellow pinky blue orange BlaCkZzZ!!! and pInKiEeE???"
# Step 1: Find 'orange'
# - Loop 1: line.lower().find('orange',0) = 0 --> append [0,'orange'] to a list --> start = 0+1 = 1 
# - Loop 2: line.lower().find('orange',1) = 26 -->  append [26,'orange'] to a list --> start = 26+1 = 27
# - Loop 3: line.lower().find('orange',27) = -1 --> break
# Step 2: Find 'yellow'
# - Loop 1: line.lower().find('yellow',0) = 8 --> append [8,'yellow'] to a list --> start = 0+1 = 1
# - Loop 2: line.lower().find('yellow',1) = -1 --> break
# Step 3: Find 'pink'
# - Loop 1: line.lower().find('pink',0) = 15 --> append [15,'pink'] to a list --> start = 15+1 = 16
# - Loop 2: line.lower().find('pink',0) = 49 --> append [49,'pink'] to a list --> start = 49+1 = 50
# - Loop 3: line.lower().find('pink',0) = -1 --> break
# Step 4: Find 'green'
# - Loop 1: line.lower().find('green',0) = -1 --> break
# Now we will get index_list = [[0,'orange'], [26,'orange'], [8,'yellow'], [15,'pink'], [49,'pink']]
# After sorting we will get index_list = [[0,'orange'], [8,'yellow'], [15,'pink'], [26,'orange'], [49,'pink']]
# Convert a index_list into index_dict
# Returns {0:'orange', 8:'yellow', 15:'pink', 26:'orange', 49:'pink'}
def find_index(line):
    index_list = []
    for color in color_list:
        start = 0
        while True:
            index = line.lower().find(color,start)
            if(index == -1):
                break
            else:
                index_list.append([index, color])
                start = index + 1
    index_list.sort()
    index_dict = {}
    for index,color in index_list:
        index_dict[index] = color
    return index_dict

# Read each line in file02 (Song file)
# Add <color> at the front and </> at the end of the color
# Example: 
# If input this, "Orange, yellow and pinky."
# The output should be like this, "<orange>Orange</>, <yellow>yellow</> and <pink>pink</>y."

# Algorithm
# Example:
# line = Orange, yellow and pinky.
# index_dict = {0:'orange', 8:'yellow', 15:'pink'}
# index_list = [0,8,15]
# index = 0
# color_l is color name in all lower case and color_n is color name in the line

# Loop index = 0: color_l = 'orange' and color_n = 'Orange'
# new_line = "<orange>Orange</>" --> index = 0 + len('orange') = 6
# Loop index = 6: new_line = "<orange>Orange</>," --> index = 6+1 = 7
# Loop index = 7: new_line = "<orange>Orange</>, " --> index = 7+1 = 8
# Loop index = 8: color_l = 'yellow' and color_n = 'yellow'
# new_line = "<orange>Orange</>, <yellow>yellow</>" --> index = 8 + len('yellow') = 14
# and so on...
for line in file02:
    line = line.strip()
    new_line = ""
    index_dict = find_index(line)
    index_list = list(index_dict.keys())
    index = 0
    while(index < len(line)):
        if(index in index_list):
            color_l = index_dict[index]
            color_n = line[index : index + len(color_l)]
            new_line += "<{}>{}</>".format(color_l, color_n)
            index += len(color_l)
        else:
            new_line += line[index]
            index += 1
    print(new_line)

# Close file
file01.close()
file02.close()