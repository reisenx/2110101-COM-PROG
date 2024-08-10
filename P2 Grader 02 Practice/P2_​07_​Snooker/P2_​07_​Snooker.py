# Create a dictionary that contains a score in each case
score_dict = {'X':0, 'Y':2, 'G':3, 'W':4, 'B':5, 'P':6, 'K':7,
              'RX':1, 'RY':3, 'RG':4, 'RW':5, 'RB':6, 'RP':7, 'RK':8}

# Calculate each player score
# Example input: "1RK" means player 1 got 8 points (RK) that round
# The game ends when a player shoot a black ball (1K or 2K)
player01 = 0
player02 = 0
while True:
    round = input().strip()
    if(round == '1K' or round == '2K'):
        if(round[0] == '1'):
            player01 += score_dict['K']
        elif(round[0] == '2'):
            player02 += score_dict['K']
        break
    else:
        if(round[0] == '1'):
            player01 += score_dict[round[1:]]
        elif(round[0] == '2'):
            player02 += score_dict[round[1:]]

# Output
print(player01, player02)
if(player01 == player02):
    print("Tie")
elif(player01 > player02):
    print("Player 1 wins")
elif(player02 > player01):
    print("Player 2 wins")