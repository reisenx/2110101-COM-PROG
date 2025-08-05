# --------------------------------------------------
# File Name : 12_Class_22.py
# Problem   : Card
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# List of scores for each card value and their order
SCORES = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}
VALUE_ORDER = {
    "3": 0,
    "4": 1,
    "5": 2,
    "6": 3,
    "7": 4,
    "8": 5,
    "9": 6,
    "10": 7,
    "J": 8,
    "Q": 9,
    "K": 10,
    "A": 11,
    "2": 12,
}
SUIT_ORDER = {"club": 0, "diamond": 1, "heart": 2, "spade": 3}


class Card:
    # __init__ method
    # Initialize the card object with value and suit
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # __str__ method
    # Convert the card object to a string representation
    def __str__(self):
        return f"({self.value} {self.suit})"

    # getScore method
    # Get the score of the card based on its value
    def getScore(self):
        return SCORES[self.value]

    # sum method
    # Calculate the sum of scores of two cards and return the last digit
    def sum(self, other):
        return (self.getScore() + other.getScore()) % 10

    # __lt__ method
    # Compare two card objects based on their value and suit
    # Return True if self is less than rhs, otherwise return False
    def __lt__(self, rhs):
        # Compare by value first
        if VALUE_ORDER[self.value] < VALUE_ORDER[rhs.value]:
            return True
        elif VALUE_ORDER[self.value] > VALUE_ORDER[rhs.value]:
            return False
        # If values are equal, compare by suit
        return SUIT_ORDER[self.suit] < SUIT_ORDER[rhs.suit]


# Input card number
n = int(input())

# Input cards and store them in a list
cards = []
for _ in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

# Output the scores of each card
for i in range(n):
    print(cards[i].getScore())
print("----------")

# Output the sum of scores of adjacent cards
for i in range(n - 1):
    print(Card.sum(cards[i], cards[i + 1]))
print("----------")

# Output the cards sorted by value and suit
cards.sort()
for i in range(n):
    print(cards[i])
