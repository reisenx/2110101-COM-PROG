# Input 2 strings
# Set the initial score to 0
key = str(input())
answer = str(input())
score = 0

# Check if the answer is incomplete answer
# Incomplete answer is the length of the 'answer' is not equal to 'key'
if(len(key) != len(answer)):
    print("Incomplete answer")

# Complete answer
else:
    # Add a score by 1, if the 'answer' and 'key' in in each index is the same
    for i in range(0,len(key)):
        if(answer[i] == key[i]):
            score += 1
    # Output the score
    print(score)