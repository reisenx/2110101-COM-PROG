# --------------------------------------------------
# File Name : 12_Class_23.py
# Problem   : Next Card
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# List of orders for each card value and suit
VALUE_TO_ORDER = {
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
SUIT_TO_ORDER = {"club": 0, "diamond": 1, "heart": 2, "spade": 3}
ORDER_TO_VALUE = {
    0: "3",
    1: "4",
    2: "5",
    3: "6",
    4: "7",
    5: "8",
    6: "9",
    7: "10",
    8: "J",
    9: "Q",
    10: "K",
    11: "A",
    12: "2",
}
ORDER_TO_SUIT = {0: "club", 1: "diamond", 2: "heart", 3: "spade"}


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

    # next1 method
    # This method will return the next card in order as a new Card object
    def next1(self):
        # Get the current order of the card
        value_order = VALUE_TO_ORDER[self.value]
        suit_order = SUIT_TO_ORDER[self.suit]
        card_order = (value_order * 4) + suit_order
        # Calculate the next card's order
        card_order = (card_order + 1) % 52
        value_order = card_order // 4
        suit_order = card_order % 4
        # Return the next card as a new Card object
        return Card(ORDER_TO_VALUE[value_order], ORDER_TO_SUIT[suit_order])

    # next2 method
    # This method will update the current card to the next card in order
    def next2(self):
        next_card = self.next1()
        self.value = next_card.value
        self.suit = next_card.suit


# Input card number
n = int(input())

# Input cards and store them in a list
cards = []
for _ in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

# Output the next card for each card in the list
for i in range(n):
    print(cards[i].next1())
print("----------")

# Output the current cards
for i in range(n):
    print(cards[i])
print("----------")

# Update each card to the next card in order and print the updated cards
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
