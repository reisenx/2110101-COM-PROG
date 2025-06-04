# Input score of each quiz
Q1 = [int(e) for e in input().split()]
Q2 = [int(e) for e in input().split()]
Q3 = [int(e) for e in input().split()]

# Calculate total score
# Example:
# Q1 = [80,80,60,100]
# Q2 = [0, 0, 0, 0, 40,100]
# Q3 = [0, 0, 0, 0, 0, 0, 40,30]
# quiz 0-3 are in Q1, Q2, Q3 | len(Q1) = 4
# quiz 4-5 are in Q2, Q3     | len(Q2) = 6
# quiz 6-7 are in Q3         | len(Q3) = 8
totalScore = 0
for quiz in range(len(Q3)):
    maxScore = 0
    if(quiz < len(Q1)):
        maxScore = max(maxScore, Q1[quiz])
    if(quiz < len(Q2)):
        maxScore = max(maxScore, Q2[quiz])
    maxScore = max(maxScore, Q3[quiz])
    totalScore += maxScore
print(totalScore)