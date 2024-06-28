# Unofficial
# Summer 2023 Euro2024 Subrouting

# -- Example --
# actual_results = ["England:Germany 2:0", "France:Spain 1:1", "Protugal:Italy 0:3", "Netherlands:Belgium 2:1"]
# guess_results  = ["Germany:England 2:1", "Portugal:Italy 1:1", "France:Spain 2:0"]
# f(actual_results, guess_results) = [[2,0,1,2], [1,1,2,0], [0,3,1,1], []]

# 'text_to_score' function
# Example: text_to_score("England:Germany 2:0")
# > returns ["England", 2, "Germany", 0] 
def text_to_score(text):
    team, score = text.strip().split()
    team1, team2 = team.split(":")
    score1, score2 = score.split(":")
    score1, score2 = int(score1), int(score2)
    return [team1, score1, team2, score2]

# 'getscore' function
# Example: getscore(team1, team2, guess_results)
# > team1 = "England"
# > team2 = "Germany"
# > guess_results = ["Germany:England 2:1", "Portugal:Italy 1:1", "France:Spain 2:0"]
# > returns [1,2]
# Condition
# - If found returns a list of score
# - If not found returns -1
def getscore(team1, team2, guess_results):
    # Find a text in guess_results that has team1 and team2 in it
    for text in guess_results:
        match = text_to_score(text)
        # If found returns a list of score
        if((team1 in match) and (team2 in match)):
            # Get a predicted score from 'match'
            guess_score1 = match[match.index(team1) + 1]
            guess_score2 = match[match.index(team2) + 1]
            return [guess_score1, guess_score2]
    # If not found returns -1
    return -1

def f(d1, d2):
    answer = []
    for text in d1:
        team1, score1, team2, score2 = text_to_score(text)
        # If not found team1 and team2 in 'd2', just append an empty list
        if(getscore(team1, team2, d2) == -1):
            answer.append([])
        else:
            guess_score1, guess_score2 = getscore(team1, team2, d2)
            answer.append([score1, score2, guess_score1, guess_score2])
    return answer

# DON'T REMOVE THIS LINE
# Execute an input string
exec(input())

# -- Testcase 1 INPUT --
# print(f(["England:Germany 2:0", "France:Spain 1:1", "Protugal:Italy 0:3", "Netherlands:Belgium 2:1"], ["England:Germany 2:0", "France:Spain 1:1", "Protugal:Italy 0:3", "Netherlands:Belgium 2:1"]))
# -- Testcase 1 OUTPUT --
# [[2, 0, 2, 0], [1, 1, 1, 1], [0, 3, 0, 3], [2, 1, 2, 1]]

# -- Testcase 2 INPUT --
# print(f(["England:Germany 2:0", "France:Spain 1:1", "Protugal:Italy 0:3", "Netherlands:Belgium 2:1"], ["Germany:England 1:2", "Spain:France 2:1", "Italy:Protugal 3:2", "Belgium:Netherlands 2:1"]))
# -- Testcase 2 OUTPUT --
# [[2, 0, 2, 1], [1, 1, 1, 2], [0, 3, 2, 3], [2, 1, 1, 2]]

# -- Testcase 3 INPUT --
# print(f(["England:Germany 2:0", "France:Spain 1:1", "Protugal:Italy 0:3", "Netherlands:Belgium 2:1"], ["Germany:England 2:1", "Protugal:Italy 1:1", "France:Spain 2:0"]))
# -- Testcase 3 OUTPUT --
# [[2, 0, 1, 2], [1, 1, 2, 0], [0, 3, 1, 1], []]