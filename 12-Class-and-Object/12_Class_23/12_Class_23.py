class Card:
    # __init__ method
    # Create 'Card' object by given
    # 'value' is ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
    # 'suit' is ("club", "diamond", "heart", "spade")
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    # __str__ method
    # Convert 'Card' object to string
    # A string must be in the format: "([Value] [Suit])"
    # Example: "(7 diamond)"
    def __str__(self):
        value = self.value
        suit = self.suit
        line = "(" + value + " " + suit + ")"
        return line
    
    # == How to compare a card ==
    # 'value' order are '3' < '4' < '5' < '6' < '7' < '8' < '9' < '10' < 'J' < 'Q' < 'K' < 'A' < '2'
    # 'suit' order are "club" < "diamond" < "heart" < "spade"

    # == The next card ==
    # Consider 'value' first, then consider 'suit'
    # - The next card of (5 diamond) is (5 heart)
    # - The next card of (10 spade) is (J club)
    # - The next card of (2 spade) is (3 club)

    # == The card order value ==
    # It is easier to compare, if we convert a card to a number. 
    # Given that
    # value_to_order = {'3':0, '4':1, '5':2, '6':3, '7':4, '8':5, '9':6, '10':7, 'J':8, 'Q':9, 'K':10, 'A':11, '2':12}
    # suit_to_order = {"club":0, "diamond":1, "heart":2, "spade":3}
    # card_order = (value_order * 4) + suit_order
    # Example:
    # (3 club)      = (0*4) + 0 = 0
    # (3 diamond)   = (0*4) + 1 = 1
    # (3 heart)     = (0*4) + 2 = 2
    # (3 spade)     = (0*4) + 3 = 3
    # (4 club)      = (1*4) + 0 = 4
    # ...
    # (2 spade)     = (12*4) + 3 = 51

    # next1 method
    # This method will create new 'Card' object that next to the 'self' card
    def next1(self):
        # Calculate card order
        value_to_order = {'3':0, '4':1, '5':2, '6':3, '7':4, '8':5, '9':6, '10':7, 'J':8, 'Q':9, 'K':10, 'A':11, '2':12}
        suit_to_order = {"club":0, "diamond":1, "heart":2, "spade":3}
        card_order = (value_to_order[self.value] * 4) + suit_to_order[self.suit]
        
        # Find the next card
        if(card_order == 51):
            card_order = 0
        else:
            card_order += 1
        
        # Convert 'card_order' to 'value' and 'suit'
        order_to_value = {0:'3', 1:'4', 2:'5', 3:'6', 4:'7', 5:'8', 6:'9', 7:'10', 8:'J', 9:'Q', 10:'K', 11:'A', 12:'2'}
        order_to_suit = {0:'club', 1:'diamond', 2:'heart', 3:'spade'}
        Value = order_to_value[card_order // 4]
        Suit = order_to_suit[card_order % 4]

        # Return new 'Card' object
        return Card(Value, Suit)
    
    # next2 method
    # This method will edit input object to the card that next to itself
    def next2(self):
        next_card = self.next1()
        self.value = next_card.value
        self.suit = next_card.suit

# Input number of cards
n = int(input())

# Input cards details which each line contains
# [Value] [Suit]
# Example: "10 spade"
# Create each 'Card' object using input in each line and put in 'cards' list
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

# Output
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
