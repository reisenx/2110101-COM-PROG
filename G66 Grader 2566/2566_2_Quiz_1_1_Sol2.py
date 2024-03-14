# Solution 2: String Slicing

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
order = "AKQJX98765432A"
pattern = []

# Set of cards pattern
# Royal Straight Flush: All the symbol are the same and the order of number is exactly "A K Q J 9"
# Example: "|AH|KH|QH|JH|XH|"
# Straight Flush: The set of cards that both flush and straight
# Example: "|5H|4H|3H|2H|AH|"
# Flush: All the symbol are the same no matter what the number is
# Example: "|KH|XH|8H|6H|4H|"
# Straight: All number are in the order no matter what the symbol is
# Example: "|5H|4D|3C|2S|AH|"

# Input set of cards and check what type of the card is
for i in range(n):
    # Input the text in this format "|XX|XX|XX|XX|XX|"
    # Slice the string using [1::3] will get a string of order
    # Slice the string using [2::3] will get a string of symbol
    # Example: text = "|9S|8C|6H|5D|AH|"
    # text[1::3] = "9865A"
    # text[2::3] = "SCHDA"
    text = input()

    # Check if the card is a "Straight" or not 
    IsStraight = text[1::3] in order

    # Check if the card is "Flush" or not
    IsFlush = text[2::3] == text[2]*5

     # Check a set of cards pattern, then put the result in a list
    if(IsFlush and IsStraight and text[1] == "A"):
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