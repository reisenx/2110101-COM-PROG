# --------------------------------------------------
# File Name : 2567_1_Q3_B2-S-sol2.py
# Problem   : Card Sorting
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Initialize lists for each suit
VALUE_EX = {"J": 11, "Q": 12, "K": 13, "A": 14}
SUIT = {"S": 0, "C": 1, "D": 2, "H": 3}


# Create a class to represent a card
class Card:
    # Initialize the card with its name, value and suit
    def __init__(self, card):
        # Initialize card name
        self.name = card

        # Initialize card suit by converting to integer
        self.suit = SUIT[card[-1]]

        # Initialize card value by converting to integer
        if card[:-1] in VALUE_EX:
            self.value = VALUE_EX[card[:-1]]
            return
        self.value = int(card[:-1])

    # Convert card to string representation
    def __str__(self):
        return self.name

    # Define less than operator for sorting by comparing suit and value
    def __lt__(self, rhs):
        return (self.suit, self.value) < (rhs.suit, rhs.value)


# Create a list of Card objects from the input and sort them in ascending order
card_objects = [Card(card) for card in input().strip("| ").split("|")]
card_objects.sort()

# Convert sorted Card objects back to string representation
cards = [str(card) for card in card_objects]

# Output the sorted cards with '|' at the start and end
print(f"|{'|'.join(cards)}|")
