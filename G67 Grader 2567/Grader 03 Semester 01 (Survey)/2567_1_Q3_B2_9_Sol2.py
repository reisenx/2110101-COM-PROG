# Object Oriented Programming in Python
# Create a class makes it a lot easier to sort them
class Card:
    def __init__(self, card):
        val = {'J':11, 'Q':12, 'K':13, 'A':14}
        suit = {'S':0, 'C':1, 'D':2, 'H':3}
        if(card[0:-1] in val):
            self.value = val[card[0:-1]]
        else:
            self.value = int(card[0:-1])

        self.suit = suit[card[-1]]
    
    def __str__(self):
        val = {11:'J', 12:'Q', 13:'K', 14:'A'}
        suit = {0:'S', 1:'C', 2:'D', 3:'H'}
        if(self.value in val):
            return val[self.value] + suit[self.suit]
        else:
            return str(self.value) + suit[self.suit]
    
    def __lt__(self, rhs):
        if(self.suit == rhs.suit):
            return self.value < rhs.value
        return self.suit < rhs.suit

cards = input().strip().strip('|').split('|')
cards = [Card(item) for item in cards]
cards.sort()
cards = [str(item) for item in cards]
print('|' + '|'.join(cards) + '|')