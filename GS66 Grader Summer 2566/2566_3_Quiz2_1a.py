# Unofficial
# Summer2023 Euro2024

# Input football matches
matches = []
match_cnt = 0
while True:
    data = input().strip()
    # Stop input, if input = "-1"
    if(data == "-1"):
        break

    # Put data in 'matches'
    # Example:
    # > data = "England:Italy 3:1"
    # > matches = [[3,1,"Win"],...]
    else:
        # Get score from 'data'
        name, score = data.split()
        score1, score2 = score.split(":")
        score1, score2 = int(score1), int(score2)
        # Compare score
        if(score1 > score2):
            result = "Win"
        elif(score1 == score2):
            result = "Draw"
        elif(score1 < score2):
            result = "Lose"
        # append a data in 'matches'
        matches.append([score1, score2, result])
        match_cnt += 1

# Input user predicted football match score and calculate the user point
user_point = 0
for i in range(match_cnt):
    # Get score from user predicted football match score
    score1, score2 = input().strip().split(":")
    score1, score2 = int(score1), int(score2)
    # Get result from user predicted football match score
    # Compare score
    if(score1 > score2):
        result = "Win"
    elif(score1 == score2):
        result = "Draw"
    elif(score1 < score2):
        result = "Lose"

    # Calculate user point
    # Citeria 1: Check result Win/Draw/Lose [3 points]
    if(result == matches[i][2]):
        user_point += 3
        # Citeria 2: Check score
        # - Correctly predict 2 team [3 point]
        if(score1 == matches[i][0] and score2 == matches[i][1]):
            user_point += 3
        # - Correctly predict 1 team [1 point]
        elif(score1 == matches[i][0] or score2 == matches[i][1]):
            user_point += 1

# Output
print(user_point)

# -- Testcase Input --
# England:Italy 3:1
# Germany:France 1:1
# Portugal:Belgium 0:3
# Spain:Netherlands 2:2
# -1
# 2:1
# 0:0
# 0:0
# 2:2
# -- Testcase Output --
# 13