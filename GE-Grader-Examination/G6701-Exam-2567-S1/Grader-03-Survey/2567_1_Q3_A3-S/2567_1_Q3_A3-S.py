# --------------------------------------------------
# File Name : 2567_1_Q3_A3-S.py
# Problem   : Total Card Score
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input cards as a list.
cards = input().strip("| ").split("|")

# Initialize score to 0
score = 0

# Convert each card to its score and sum them up.
for card in cards:
    # Remove any symbol at the end from the card.
    card = card[:-1]

    # Determine the score based on the card value.
    if card == "A":
        score += 1
    elif card in ["K", "Q", "J"]:
        score += 10
    else:
        score += int(card)

# Output the the total score.
print(score)
