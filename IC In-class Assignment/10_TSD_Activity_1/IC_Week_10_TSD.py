# Input number of person
n = int(input())

# Input each person sport details which contains
# [Name] [Sport1],[Sport2],[Sport3]
# Example: Shane Swimming,Soccer,Golf,Badminton
# Put a data in 'sports' dictionary in the format
# {Name:{Set of sport}}
# Example: sports = {'Shane':{'Swimming','Soccer','Golf','Badminton'}} 
sports = {}
for i in range(n):
    name,sport = input().strip().split()
    sport = set(sport.split(','))
    sports[name] = sport

# Input 2 name and find what sport they both play
while(True):
    data = input().strip()
    # Input until 'q'
    if(data == 'q'):
        break
    else:
        # Get 2 names
        name01, name02 = data.split()
        # Find intersection of set of sport of both
        match_sport = sports[name01] & sports[name02]
        # Convert to a list, then sort them in alphabetical order
        match_sport = sorted(match_sport)
        # Output
        print(match_sport)
