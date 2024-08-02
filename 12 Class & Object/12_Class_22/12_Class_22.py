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

    # getScore method
    # Get 'value' from object and convert to score using a dictionary
    def getScore(self):
        scores = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
        value = self.value
        return scores[value]
    
    # sum method
    # Find a sum of score of 2 cards and mod by 10
    def sum(self, other):
        score01 = self.getScore()
        score02 = other.getScore()
        return (score01+score02)%10
    
    # __lt__ method
    # This method can compare that 'self' is less than 'rhs' or not
    # 'value' order are '3' < '4' < '5' < '6' < '7' < '8' < '9' < '10' < 'J' < 'Q' < 'K' < 'A' < '2'
    # 'suit' order are "club" < "diamond" < "heart" < "spade"
    # Sort by 'value' first then sort by 'suit'
    def __lt__(self, rhs):
        # Create a dictionary that can convert 'value' to 'suit' to make it easier to compare
        value_order = {'3':0, '4':1, '5':2, '6':3, '7':4, '8':5, '9':6, '10':7, 'J':8, 'Q':9, 'K':10, 'A':11, '2':12}
        suit_order = {"club":0, "diamond":1, "heart":2, "spade":3}
        
        # Get order number of each object
        value_order01 = value_order[self.value]
        suit_order01 = suit_order[self.suit]
        value_order02 = value_order[rhs.value]
        suit_order02 = suit_order[rhs.suit]

        # Compare and return a boolean value
        if(value_order01 < value_order02):
            return True
        elif(value_order01 == value_order02):
            if(suit_order01 < suit_order02):
                return True
            else:
                return False
        else:
            return False
        

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

# Output a score of each card in a list
for i in range(n):
    print(cards[i].getScore())
print("----------")

# Output a sum of 2 cards that close to each other
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")

# Sorting a card
cards.sort()

# Output 'Card' object as a string
for i in range(n):
    print(cards[i])