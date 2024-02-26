# Input number of card set
n = int(input())

# The card will be in the "XX" format
# The first letter is a number in the card (otherwise, Ace = "A" | King = "K" | Queen = "Q" | Jack = "J" | 10 = "X")
# The second letter is a symbol in the card (Hearts = "H" | Diamonds = "D" | Clubs = "C" | Spades = "S")
# Example: "9S" is a spades card with number 9

# A set of cards contain 5 cards and guaranteed to orded in descending order
# The format is "|XX|XX|XX|XX|XX|"
# Example: "|9S|8C|6H|5D|AH|"

# The order of the card will be in this order
# Notice that there's two 'A' in the list 
order = ['A','K','Q','J','X','9','8','7','6','5','4','3','2','A']
pattern = []

# Set of cards pattern
# Royal Straight Flush: All the symbol are the same and the order of number is exactly "A K Q J 9"
# Example: "|AH|KH|QH|JH|XH|"
# Straight Flush: The set of cards that both flush and straight
# Example: "|5H|4H|3H|2H|AH|"
# Flush: All the symbol are the same no matter what the number is
# Example: "|KH|10H|8H|6H|4H|"
# Straight: All number are in the order no matter what the symbol is
# Example: "|5H|4D|3C|2S|AH|"

# Input set of cards and check what type of the card is
for i in range(n):
    # Input the text in this format "|XX|XX|XX|XX|XX|"
    # Remove the "|" at the front and end by using .strip("|")
    # Using .split("|") the input string into a list of cards
    # Example: "|9S|8C|6H|5D|AH|" --> "9S|8C|6H|5D|AH" --> ["9S","8C","6H","5D","AH"]
    text = input().strip("|")
    cards = text.split("|")

    # Check if the card is a "Straight" or not
    IsStraight = True
    for j in range(1,5):
        # It is impossible to a set of card that start with 4,3 or 2 to be "Straight"
        if(cards[0][0] == "4" or cards[0][0] == "3" or cards[0][0] == "2"):
            IsStraight = False
            break
        # If the current character is "A", the previous card must be "2"
        # Otherwise, it is not a "Straight"
        elif(cards[j][0] == "A" and cards[j-1][0] != "2"):
            IsStraight = False
            break
        elif(cards[j][0] == "A" and cards[j-1][0] == "2"):
            IsStraight = True
        # Check If the card is not in the order
        elif(order.index(cards[j][0]) != order.index(cards[j-1][0])+1):
            IsStraight = False
            break

    # Check if the card is "Flush" or not
    if(cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1]):
        IsFlush = True
    else:
        IsFlush = False
        
    # Check a set of cards pattern, then put the result in a list
    if(IsFlush and IsStraight and cards[0][0] == 'A'):
        pattern.append("Royal Straight Flush")
    elif(IsFlush and IsStraight):
        pattern.append("Straight Flush")
    elif(IsStraight):
        pattern.append("Straight")
    elif(IsFlush):
        pattern.append("Flush")
    else:
        pattern.append("None")

# Output
for item in pattern:
    print(item)