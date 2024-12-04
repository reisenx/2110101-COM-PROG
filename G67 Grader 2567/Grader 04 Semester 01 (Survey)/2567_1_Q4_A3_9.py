# Input solution string
sol = input().strip()
# Input correct and wrong score
correctScore, wrongScore = [int(e) for e in input().split()]
# Input answer string
ans = input().strip()

# Counting correct, wrong, No answer
correct = 0
wrong = 0
noAns = 0
for i in range(len(sol)):
    # Count no answer
    if(ans[i] == '-'):
        noAns += 1
    # Count correct-wrong
    if(sol[i] == 'X' or ans[i] == sol[i]):
        correct += 1
    elif(ans[i] != sol[i] and ans[i] != '-'):
        wrong += 1

# Calculate score
score = (correctScore * correct) + (wrongScore * wrong)
score = max(0, score)
# Output
print(correct, wrong, noAns, score)