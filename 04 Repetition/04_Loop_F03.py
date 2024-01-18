# Create function grade_mcq(sol,ans)
def grade_mcq(sol,ans):
    # Set the initial score to 0
    score = 0
    
    # Check if the answer is incomplete answer
    # Incomplete answer is the length of the string is not equal
    if(len(sol) != len(ans)):
        return -1
    # Complete answer
    else:
        # If the answer string and key string in index i is the same, add score by 1
        for i in range(0,len(sol)):
         if(ans[i] == sol[i]):
             score = score+1
        return score

# Execute input string
exec(input())