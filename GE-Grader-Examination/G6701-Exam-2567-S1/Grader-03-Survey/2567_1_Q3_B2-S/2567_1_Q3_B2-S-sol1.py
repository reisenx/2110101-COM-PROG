# --------------------------------------------------
# File Name : 2567_1_Q3_B2-S-sol1.py
# Problem   : Card Sorting
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Initialize lists for each suit
VALUE_EX = {"J": 11, "Q": 12, "K": 13, "A": 14}
SUIT = {"S": 0, "C": 1, "D": 2, "H": 3}

# Input cards as a list of strings
cards_str = input().strip("| ").split("|")

# Initialize a list to hold card sublist
cards = []

# Iterate through each card string
for card in cards_str:
    # Extract value from the card string
    value = 0
    if card[:-1] in VALUE_EX:
        value = VALUE_EX[card[:-1]]
    else:
        value = int(card[:-1])

    # Extract suit from the card string
    suit = SUIT[card[-1]]

    # Append the card sublist for sorting
    cards.append([suit, value, card])

# Sort the cards based on suit and value in ascending order
cards.sort()

# Construct the output string
output = "|"
for _, _, card in cards:
    output += f"{card}|"

# Output the output string
print(output)
