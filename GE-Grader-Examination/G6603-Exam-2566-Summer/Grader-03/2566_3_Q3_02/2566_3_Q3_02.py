# --------------------------------------------------
# File Name : 2566_3_Q3_02.py
# Problem   : RSP Team
# Author    : Worralop Srichainont
# Date      : 2025-07-15
# --------------------------------------------------

# Initialize constants for winning and losing combinations.
WINNING = ["RS", "SP", "PR"]
LOSING = ["SR", "PS", "RP"]


# Get moves of each turn from the playing order string.
def get_moves(playing_order):
    moves = []
    for i in range(0, len(playing_order), 2):
        move = playing_order[i : i + 2]
        moves.append(move)
    return moves


# Get the match status of each turn based on the moves.
def get_match_status(playing_order):
    # Initialize match status score for both teams.
    match_status = []
    score = [0, 0]
    # Get the moves from the playing order string.
    moves = get_moves(playing_order)

    # Iterate through each move to determine the match status.
    for move in moves:
        # Initialize status as "NO CHANGE".
        status = "NO CHANGE"
        # Update the score based on the move.
        if move in WINNING:
            score[0] += 1
        elif move in LOSING:
            score[1] += 1
        # Check if either team has reached the winning score of 2.
        if score[0] == 2:
            # Reset score and change team B.
            score = [0, 0]
            status = "CHANGE TEAM B"
        elif score[1] == 2:
            # Reset score and change team A.
            score = [0, 0]
            status = "CHANGE TEAM A"
        # Append the status to the match status list.
        match_status.append(status)
    # Return the final match status list.
    return match_status


# Get the next player in the team based on the current player.
def get_next_player(current_player, team):
    idx = team.index(current_player)
    return team[(idx + 1) % len(team)]


# Get the moves made by each player in the teams based on the playing order.
def player_moves(playing_order, team_a, team_b):
    # Initialize lists to store moves for each team.
    team_a_moves = []
    team_b_moves = []

    # Get the moves and match status from the playing order.
    moves = get_moves(playing_order)
    match_status = get_match_status(playing_order)

    # Initialize players for each team.
    player_a = [team_a[0], []]
    player_b = [team_b[0], []]

    # Iterate through the moves and match status to track player moves.
    for i in range(len(moves)):
        # Append the current move to the respective player's moves.
        player_a[1].append(moves[i][0])
        player_b[1].append(moves[i][1])

        # Check the match status to determine if a team change is needed.
        if match_status[i] == "CHANGE TEAM A":
            # Append the current player's moves to team A's moves.
            team_a_moves.append(player_a)
            # Switch to the next player in team A.
            player_a = [get_next_player(player_a[0], team_a), []]

        elif match_status[i] == "CHANGE TEAM B":
            # Append the current player's moves to team B's moves.
            team_b_moves.append(player_b)
            # Switch to the next player in team B.
            player_b = [get_next_player(player_b[0], team_b), []]

    # Append the final players' moves if they have made any moves.
    if player_a[1] != []:
        team_a_moves.append(player_a)
    if player_b[1] != []:
        team_b_moves.append(player_b)
    # Return the moves made by each team.
    return team_a_moves, team_b_moves


# Execute the input string as code
exec(input().strip())
