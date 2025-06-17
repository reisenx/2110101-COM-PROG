# --------------------------------------------------
# File Name : P2_02_Card.py
# Problem   : Part-II Card
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# List of card values and suits
VALUE = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
}
SUIT = {"C": 1, "D": 2, "H": 3, "S": 4}

# Input cards as a string
cards_str = input().strip()
# Convert the input string into a list of cards
cards = []
for i in range(0, len(cards_str), 2):
    value = cards_str[i]
    suit = cards_str[i + 1]
    cards.append([VALUE[value], SUIT[suit]])

# Compare the cards and generate the result string
result = ""
for i in range(len(cards) - 1):
    # Initialize the difference between the two cards
    diff = 0
    # Get the values and suits of the current and next cards
    value01, suit01 = cards[i]
    value02, suit02 = cards[i + 1]
    # Compare the values of the two cards
    if value01 - value02 == 0:
        diff = suit01 - suit02
    else:
        diff = value01 - value02
    # Append the result based on the comparison
    if diff > 0:
        result += "+" + str(diff)
    else:
        result += str(diff)

# Output the result
print(result)
