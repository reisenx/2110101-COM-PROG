# --------------------------------------------------
# File Name : 2567_2_Q3_C1.py
# Problem   : Connect Four
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------

# Constants for directions
# East      ( 0,  1) | West      (0, -1)
# North     (-1,  0) | South     (1,  0)
# Northeast (-1,  1) | Southwest (1, -1)
# Northwest (-1, -1) | Southeast (1,  1)
DIRECTIONS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1))

# Game Configuration
PLAYER = ["1", "2"]
WINNING_PIECE_COUNT = 4

# Input amount of rows and columns of the board
cols, rows = [int(num) for num in input().split()]

# Initialize the game board and pieces on each column
board = [["."] * cols for _ in range(rows)]
pieces_on_column = [0] * cols

# Input the order of dropping pieces to each columns
drop_on_column_order = [int(num) - 1 for num in input().split()]


# Check if the given row and column are inside the board
def is_inside_board(row, col):
    return (0 <= row < rows) and (0 <= col < cols)


# Calculate the row to drop a piece in the given column
def get_drop_piece_row(col):
    return rows - (pieces_on_column[col] + 1)


# Check if the piece at the given row and column is the player's piece
def is_player_piece(row, col, player):
    return is_inside_board(row, col) and board[row][col] == player


# Drop a piece in the given row and column for the player
# Return True if the piece is dropped successfully, otherwise return False
def drop_piece(row, col, player):
    if is_inside_board(row, col):
        board[row][col] = player
        pieces_on_column[col] += 1
        return True
    return False


# Check if the player has won by connecting 4 pieces in a row
def is_player_win(row, col, player):
    # Initialize the piece count
    piece_count = 1

    # Check all 8 directions for a win
    for i in range(len(DIRECTIONS)):
        # Get the current direction
        dr, dc = DIRECTIONS[i]
        # Reset piece count when resetting direction
        if i % 2 == 0:
            piece_count = 1

        # Count pieces in the current direction
        for n in range(1, WINNING_PIECE_COUNT):
            if not is_player_piece(row + (dr * n), col + (dc * n), player):
                break
            piece_count += 1

        # Check if the player has connected enough pieces
        if piece_count >= WINNING_PIECE_COUNT:
            return True
    # If no direction has enough pieces, return False
    return False


# Display the game board
def display_board():
    for row in board:
        print("".join(row))


# Main function to play the game
def play_game():
    # Initialize the game state
    is_game_end = False

    # Process each turn in the order of dropping pieces
    for turn in range(len(drop_on_column_order)):
        # Get the row and column to drop the piece
        col = drop_on_column_order[turn]
        row = get_drop_piece_row(col)
        player = PLAYER[turn % 2]

        # Player drops a piece in the specified column
        # If the column is full, the piece cannot be dropped
        is_column_full = not drop_piece(row, col, player)

        # If the player has won, display the board and end the game
        if turn >= 3 and is_player_win(row, col, player):
            print("Player", player, "wins")
            display_board()
            is_game_end = True
            break

        # If the column is full, display a message and end the game
        if turn >= rows - 1 and is_column_full:
            print("Column full")
            display_board()
            is_game_end = True
            break

        # If the board is full, display a message and end the game
        if turn == (rows * cols) - 1:
            print("Board full")
            display_board()
            is_game_end = True
            break

    # If the game has not ended after all turns, display a message
    if not is_game_end:
        print("No more moves")
        display_board()


# Run the function to play the game
play_game()
