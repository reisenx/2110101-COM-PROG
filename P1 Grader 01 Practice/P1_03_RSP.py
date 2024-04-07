# Input reqiured score and setup initial score to 0
win_score = int(input())
player01 = 0
player02 = 0

# Create a list of winning and losing scenario
# Given that index 0 is player1 and index 1 is player2 
# Example: 'R' wins 'S' --> Put ['R','S'] as 'winning' sublist
# Example: 'R' lose 'P' --> Put ['R','P'] as 'losing' sublist
winning = [['R','S'], ['S','P'], ['P','R']]
losing = [['S','R'], ['P','S'], ['R','P']]

# Input game for 3*win_score times
# If any player wins, then break the loop
IsWinning = False
for i in range(3*win_score):
    # Input each game
    # Example: "R P" --> ['R','P']
    game = input().strip().split()
    
    # Count player score
    if(game in winning):
        player01 += 1
    elif(game in losing):
        player02 += 1

    # Check if any player wins the game
    if(player01 == win_score):
        IsWinning = True
        print(player01, player02)
        print("Player 1 wins")
        break
    elif(player02 == win_score):
        IsWinning = True
        print(player01, player02)
        print("Player 2 wins")
        break

# In case that there's nobody wins tha game yet
if(not IsWinning):
    print(player01, player02)
    print("Tie")