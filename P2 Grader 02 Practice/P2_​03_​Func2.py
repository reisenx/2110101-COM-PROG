# Reminder
# All function must not change the value of parameters

# This function can find an area of a polygon
# 'p' parameter is a list that contains coordinates (x,y) of a polygon
# Assume that coordinates (x,y) are already sorted in clockwise or counterclockwise order
# Area of the polygon = 1/2[(x1*y2 + x2*y3 + ... + xn*y1) - (y1*x2 + y2*x3 + ... + yn*x1)]
# If the coordinates (x,y) are in clockwise order the value will be negative so we need to absolute the value
def convex_polygon_area(p):
    # Seperate list p into 2 list which are X list and Y list
    # Example: [[0,0], [0,3], [4,0]] --> X = [0,0,4] and Y = [0,3,0]
    X = []
    Y = []
    for x,y in p:
        X.append(x)
        Y.append(y)
    # Calculate the area
    # Given sum1 = x1*y2 + x2*y3 + ... + xn*y1
    # And given sum2 = y1*x2 + y2*x3 + ... + yn*x1
    sum1 = 0
    sum2 = 0
    for i in range(len(p)-1):
        sum1 += X[i]*Y[i+1]
        sum2 += Y[i]*X[i+1]
    sum1 += X[len(p)-1]*Y[0]
    sum2 += Y[len(p)-1]*X[0]
    area = abs(0.5*(sum1 - sum2))
    return area

# This function can check if the string is heterogram
# Heterogram occurs when all english letter in a string are all difference
# Consider lowercase and uppercase are the same letter
# Example: "Python" is heterogram but "Java" is not heterogram
def is_heterogram(s):
    # Convert all letter in string 's' to uppercase
    text = s.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Count a letter and put them in a dictionary 'letter_count'
    letter_count = {}
    for letter in text:
        if(letter in alphabet):
            if(letter not in letter_count):
                letter_count[letter] = 1
            elif(letter in letter_count):
                letter_count[letter] += 1
    # If the string 's' is heterogram, maximum value of 'count_list' must be 1
    if(max(letter_count.values()) == 1):
        return True
    else:
        return False

# This function can replace a substring 'a' with substring 'b' in string 's'
# Consider lowercase and uppercase are the same letter
# Example 1: replace_ignorecase("Python is hard", "Hard", "easy")
# In this case, we will see a string "Hard" here "Python is [hard]". Replace it with "easy"
# and you got a new string which is "Python is easy"

# Example 2: replace_ignorecase("AAabaAA", "Aa", "Aaa")
# Algorithm
# Convert string 's' and substring 'a' to uppercase
# a = 'Aa' --> check = 'AA', check_s = "AAABAAA"
# Use function find() to indicate the index of the 'check' in 'check_s' then put all the index in the list
# Since find() can indicate only substring that has the smallest index, so we need to delete a substring after find()

# Repeat the process until we can't find it anymore (check_s.find(check) == -1)
# Loop 1: "AAABAAA".find('AA') = 0 --> index = 0 --> index_list = [0]
# Delete "[AA]ABAAA" --> "ABAAA"
# Loop 2: "ABAAA".find('AA') = 2 --> index = 0+2+2 --> index_list = [0,4]
# Delete "[ABAA]A" --> "A"
# Loop 3: "A".find('AA') = -1 --> Break loop

# Modify a new string
# len("AAABAAA") = 7 --> loop from i=0 to i=6
# len("Aa") = 2 --> increase i by 2 when i in index_list
# Loop i=0: i=0 in index_list --> Add substring b --> new_s = "Aaa" --> i += 2
# Loop i=2: i=2 not in index_list --> Add s[2] = 'a' --> new_s = "Aaaa" --> i += 1
# Loop i=3: i=3 not in index_list --> Add s[3] = 'b' --> new_s = "Aaaab" --> i += 1
# Loop i=4: i=4 in index_list --> Add substring b --> new_s = "AaaabAaa" --> i += 2
# Loop i=6: i=6 not in index_list --> Add s[6] = 'A' --> new_s = "AaaabAaaA" --> i += 1
# Loop i=7: i>6 --> Break loop
# The function returns "AaaabAaaA"
def replace_ignorecase(s,a,b):
    check = a.upper()
    check_s = s.upper()
    # Create and find an index list
    index_list = []
    while(check_s.find(check) != -1):
        index = check_s.find(check)
        if(len(index_list) == 0):
            index_list.append(index)
            check_s = check_s[index + len(a):]
        else:
            index_list.append(index_list[-1] + len(a) + index)
            check_s = check_s[index + len(a):]
    # Modify a new string
    new_s = ""
    i = 0
    while(i < len(s)):
        if(i in index_list):
            new_s += b
            i += len(a)
        else:
            new_s += s[i]
            i += 1
    return new_s

# This function can return a list contains top 3 names
# 'votes' parameter is a dictionary
# If there are people with same score, sort them in alphabetical order
# Example: top3({"A": 8888, "B": 6666, "C": 7777, "X":6666}) returns ['A','C','B']
def top3(votes):
    # Create and find a list of votes and sort it in descending order
    # {"A": 8888, "B": 6666, "C": 7777, "X":6666} --> [8888,7777,6666]
    vote_list = []
    for name in votes:
        if(votes[name] not in vote_list):
            vote_list.append(votes[name])
    vote_list.sort(reverse = True)

    # Find rank 1,2 and 3 names
    rank1_name = []
    rank2_name = []
    rank3_name = []
    for name in votes:
        if(votes[name] == vote_list[0]):
            rank1_name.append(name)
        elif(votes[name] == vote_list[1]):
            rank2_name.append(name)
        elif(votes[name] == vote_list[2]):
            rank3_name.append(name)
    
    # Sort and select the first 3 person
    rank1_name.sort()
    rank2_name.sort()
    rank3_name.sort()
    top3_name = rank1_name + rank2_name + rank3_name
    return top3_name[0:3]

# Execute an input string 2 times
for k in range(2):
    exec(input().strip())