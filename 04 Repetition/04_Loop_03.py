# Input 2 strings
# Set the initial score to 0
key = str(input())
answer = str(input())
score = 0

# Check if the answer is incomplete answer
# Incomplete answer is the length of the string is not equal
if(len(key) != len(answer)):
    print("Incomplete answer")
# Complete answer
else:
    # If the answer string and key string in index i is the same, add score by 1
    for i in range(0,len(key)):
        if(answer[i] == key[i]):
            score = score+1
    # Output the score
    print(score)