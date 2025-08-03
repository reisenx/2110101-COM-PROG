# --------------------------------------------------
# File Name : 2567_3_Q3_B1.py
# Problem   : Survival game
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------

# Constants for the number of top players to display
DISPLAY_LIMIT = 3

# Initialize a dictionary to store survival times of each player
survival_time = {}

# Input raw data
data = input().strip().split()

# Process the input data to calculate total survival time for each player
for i in range(0, len(data), 2):
    # Extract player name and time from the input data
    player = data[i]
    time = int(data[i + 1])

    # Update the survival time for the player
    if player not in survival_time:
        survival_time[player] = 0
    survival_time[player] += time

# Sort players by survival time in descending order and then by name in ascending order
sorted_survival_time = []
for player, time in survival_time.items():
    sorted_survival_time.append([-time, player])
sorted_survival_time.sort()

# Extract the top players based on survival time
top_player_names = []
for _, player in sorted_survival_time[:DISPLAY_LIMIT]:
    top_player_names.append(player)

# Output the names of the top players
print(" ".join(top_player_names))
