# Input data here
N, M = [int(e) for e in input().split()]
column_sequence = [int(e) - 1 for e in input().split()]

# Construct a board with M x N size
#     | 0 | 1 | 2 | ... | N |
#  0  | . | . | . |  .  | . |
#  1  | . | . | . |  .  | . |
#  2  | . | . | . |  .  | . |
# ... | . | . | . |  .  | . |
# M-1 | . | . | . |  .  | . |
board = [['.'] * N for _ in range(M)]
PLAYER = ['1', '2']

# Amount of pieces in each column
column_pieces = [0] * N

# Get row index of a piece
def get_row(col):
    return M - (column_pieces[col] + 1)

# Check if the (row, col) is inside the board
def is_inside_board(row, col):
    return (0 <= row < M) and (0 <= col < N)

# Check if a pieces in (row, col) belongs to a player
# Return True,  if that piece belongs to a player
# Return False, if not belongs to a player or empty or invalid
def is_player_piece(row, col, player):
    return is_inside_board(row, col) and board[row][col] == player

# Display board
def display_board():
    for row in board:
        print(''.join(row))

# A player drop a piece into a board
# Return True,  if possible
# Return False, if the column is full
def drop_piece(row, col, player):
    if(is_inside_board(row, col)):
        board[row][col] = player
        column_pieces[col] += 1
        return True
    return False

# Directions
# - East      (0, 1)   | West      (0, -1)
# - North     (-1, 0)  | South     (1, 0)
# - Northeast (-1, 1)  | Southwest (1, -1)
# - Northwest (-1, -1) | Southeast (1, 1)
DIRECTIONS = ((0, 1), (0, -1),
              (-1, 0), (1, 0),
              (-1, 1), (1, -1),
              (-1, -1), (1, 1))

# Check if the player wins a game
def is_player_win(row, col, player):
    # Count 4 consecutive pieces in each direction
    count = 1
    for i in range(len(DIRECTIONS)):
        # Reset when count on new direction
        if(i % 2 == 0):
            count = 1
        # Counting
        dr, dc = DIRECTIONS[i]
        for n in range(1, 4):
            if(not is_player_piece(row + (dr * n), col + (dc * n), player)):
                break
            count += 1
        # The player has 4 consecutive pieces
        if(count >= 4):
            return True
    return False

# =============== Main Logic ===============
is_game_end = False
for turn in range(len(column_sequence)):
    # Get player information
    col = column_sequence[turn]
    row = get_row(col)
    player = PLAYER[turn % 2]
    
    # Drop a piece
    is_column_full = not drop_piece(row, col, player)
    
    # Check if the player wins
    if(turn >= 3 and is_player_win(row, col, player)):
        print("Player", player, "wins")
        display_board()
        is_game_end = True
        break
    # Check if the column is full
    if(turn >= M - 1 and is_column_full):
        print("Column full")
        display_board()
        is_game_end = True
        break
    # Check if the board is full
    if(turn == (M * N) - 1):
        print("Board full")
        display_board()
        is_game_end = True
        break
    
# Check if no one wins after all turns
if(not is_game_end):
    print("No more moves")
    display_board()