# --------------------------------------------------
# File Name : P2_07_Snooker.py
# Problem   : Part-II Snooker
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# Initialize the score mapping for snooker balls
SCORES = {
    "X": 0,
    "Y": 2,
    "G": 3,
    "W": 4,
    "B": 5,
    "P": 6,
    "K": 7,
    "RX": 1,
    "RY": 3,
    "RG": 4,
    "RW": 5,
    "RB": 6,
    "RP": 7,
    "RK": 8,
}

# Initialize player scores
player_scores = [0, 0]

# Both players start the game
while True:
    # Read input data
    data = input().strip()
    player = int(data[0]) - 1
    ball = data[1:]
    # Update the score for the current player
    player_scores[player] += SCORES[ball]
    # The game ends when a player pots the black ball
    if ball == "K":
        break

# Output the scores and the winner
print(player_scores[0], player_scores[1])
if player_scores[0] == player_scores[1]:
    print("Tie")
elif player_scores[0] > player_scores[1]:
    print("Player 1 wins")
else:
    print("Player 2 wins")
