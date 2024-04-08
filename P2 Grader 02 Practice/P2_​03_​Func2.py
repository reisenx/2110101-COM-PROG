# == Reminder ==
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
    for char in text:
        if(char in alphabet):
            if(char not in letter_count):
                letter_count[char] = 1
            elif(char in letter_count):
                letter_count[char] += 1
    # If the string 's' is heterogram, maximum value of 'letter_count' must be 1
    return max(letter_count.values()) == 1

# This function can replace a substring 'a' with substring 'b' in string 's'
# Consider lowercase and uppercase are the same letter
# Example 1: replace_ignorecase("Python is hard", "Hard", "easy")
# In this case, we will see a string "Hard" here "Python is [hard]". Replace it with "easy"
# and you got a new string which is "Python is easy"

# == Algorithm ==
# Create a new string 'replaced'
# Check if s[start:end] is 'b' until the end of the string 's' 
# - If yes, replace with substring 'b' and increase start and end by len(a)
# - If no, add s[start] to 'replaced' and increase start and end by 1

# Example 2: replace_ignorecase("AAabaAA", "Aa", "Aaa")
# Loop 1: t[0:2] = "[AA]abaAA" --> replaced = "Aaa"         <-- Add b = "Aaa"
# Loop 2: t[2:4] = "AA[ab]aAA" --> replaced = "Aaaa"   
# Loop 3: t[3:5] = "AAa[ba]AA" --> replaced = "Aaaab"  
# Loop 4: t[4:6] = "AAab[aA]A" --> replaced = "AaaabAaa"    <-- Add b = "Aaa"
# Loop 5: t[7:9] = "AAabaA[A]" --> replaced = "AaaabAaaA"  
# Loop 6: t[8:10] --> break (start = 8 and len(s) = 8)
def replace_ignorecase(s,a,b):
    replaced = ""
    start = 0
    end = len(a)
    while(start < len(s)):
        if(s[start:end].lower() == a.lower()):
            replaced += b
            start += len(a)
            end += len(a)
        else:
            replaced += s[start]
            start += 1
            end += 1
    return replaced

# This function can return a list contains top 3 names
# 'votes' parameter is a dictionary
# If there are people with same score, sort them in alphabetical order
# Example: top3({"A": 8888, "B": 6666, "C": 7777, "X":6666}) returns ['A','C','B']
def top3(votes):
    # Find unique top 3 scores
    # Example: {"A":8888, "B":6666, "C":7777, "X":6666} --> [8888,7777,6666]
    top3_scores = []
    for name,score in votes.items():
        if(score not in top3_scores):
            top3_scores.append(score)
    top3_scores.sort(reverse = True)
    top3_scores = top3_scores[0:3]

    # Find all top3 names
    top3_names = []
    for t_score in top3_scores:
        # Find a score of each rank, sort them and put all of them in 'top3_names' 
        temp = []
        for name,score in votes.items():
            if(score == t_score):
                temp.append(name)
        temp.sort()
        for item in temp:
            top3_names.append(item)    
    
    # Return first 3 names in 'top3_names'
    return top3_names[0:3]

# Execute an input string 2 times
for k in range(2):
    exec(input().strip())