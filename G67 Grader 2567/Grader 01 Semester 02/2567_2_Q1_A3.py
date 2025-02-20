# Input row amount
row = int(input())

# Input Snakes and Ladder Table
table = []
for i in range(row):
    # Input each row, and split to a list
    data = input().strip().split()
    # Reverse row when 'row-i-1' is odd number
    if((row-i-1) % 2 == 1):
        data = data[::-1]
    # Add a sublist into the table
    table.append(data)
# Reverse the entire table
table = table[::-1]
# Find columns amount
col = len(table[0])

# Roll a dice and play the game
dice_rolls = [int(e) for e in input().split()]
winning_grid = row * col
current_grid = 0
game_process = ""
for point in dice_rolls:
    # Calculate current position on a table
    current_grid += point
    i = (current_grid - 1) // col
    j = (current_grid - 1) % col
    
    # Player is on a ladder or eaten by a snake
    while(1 <= current_grid < winning_grid and table[i][j][0] in ['L', 'S']):
        current_grid = int(table[i][j][1:])
        i = (current_grid - 1) // col
        j = (current_grid - 1) % col
    
    # Update game process
    if(current_grid >= winning_grid):
        game_process += "win"
        break
    else:
        game_process += (str(current_grid) + " ")

# Output
print(game_process)

# ========== Snakes and Ladder Table ==========
# Example: 5 x 4 Table
# > For loop from i = 0 to i = 4 (row = 5)
# > For loop from j = 0 to j = 3 (col = 4)
# ---------------------------------------------
#             | j = 0 | j = 1 | j = 2 | j = 3 |
# row-i-1 = 4 |   17  |   18  |   19  |   20  |
# row-i-1 = 3 |   16  |   15  |   14  |   13  |
# row-i-1 = 2 |   9   |   10  |   11  |   12  |
# row-i-1 = 1 |   8   |   7   |   6   |   5   |
# row-i-1 = 0 |   1   |   2   |   3   |   4   |
# ---------------------------------------------
# Reverse row when 'row-i-1' is odd number
# ---------------------------------------------
#             | j = 0 | j = 1 | j = 2 | j = 3 |
# row-i-1 = 4 |   17  |   18  |   19  |   20  |
# row-i-1 = 3 |   13  |   14  |   15  |   16  | <-- Reverse row
# row-i-1 = 2 |   9   |   10  |   11  |   12  |
# row-i-1 = 1 |   5   |   6   |   7   |   8   | <-- Reverse row
# row-i-1 = 0 |   1   |   2   |   3   |   4   |
# ---------------------------------------------
# Reverse entire table
# ---------------------------------------
#       | j = 0 | j = 1 | j = 2 | j = 3 |
# i = 0 |   1   |   2   |   3   |   4   |
# i = 1 |   5   |   6   |   7   |   8   |
# i = 2 |   9   |   10  |   11  |   12  |
# i = 3 |   13  |   14  |   15  |   16  |
# i = 4 |   17  |   18  |   19  |   20  |
# ---------------------------------------