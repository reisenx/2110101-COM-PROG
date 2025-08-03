# --------------------------------------------------
# File Name : 2567_2_Q2_A3.py
# Problem   : Snakes and Ladder 2
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Input number of rows of the table
rows = int(input())

# Initialize the game board
game_board = []

# Input the game board
for i in range(rows):
    # Input each line of the game board
    line = input().strip().split()

    # Add the line on even rows counting from the above
    if i % 2 == 0:
        game_board += line

    # Add the reversed line on odd rows counting from the above
    else:
        game_board += line[::-1]

# Input the dice rolls
dice_rolls = [int(roll) for roll in input().split()]

# Initialize the list to keep track of the game process
# and the index of the current position
game_process = []
idx = -1

# Process the game based on the dice rolls
for roll in dice_rolls:
    # Update the index based on the dice roll
    idx += roll

    # Check if the index is on snake or ladder grid
    if (idx < len(game_board) - 1) and (game_board[idx] != "."):
        # Move to the position indicated by the snake or ladder
        idx = int(game_board[idx][1:]) - 1

    # Append the current position to the game process
    if idx < len(game_board) - 1:
        game_process.append(str(idx + 1))

    # Check if the player has reached the end of the game board
    else:
        game_process.append("win")
        break

# Output the game process
print(" ".join(game_process))
