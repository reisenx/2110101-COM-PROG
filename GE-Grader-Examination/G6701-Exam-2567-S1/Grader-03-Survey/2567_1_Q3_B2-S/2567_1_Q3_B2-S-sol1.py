# Input cards as a list
# 1.) Remove blank space at the end using .strip()
# 2.) Remove '|' at the at the start and end using .strip('|')
# 3.) Use .split('|') to separate a string into a list
cards = input().strip().strip('|').split('|')

# For each card in cards list
# - card number is card[0:-1] (Example: '10H' --> '10')
# - card suit is card[-1]     (Example: '10H' --> 'H')
# - Categorize card by its suit
# For card number we will indicate
# - 'J' is 11
# - 'Q' is 12
# - 'K' is 13
# - 'A' is 14
spades = []
clubs = []
diamonds = []
hearts = []
for card in cards:
    # Get card information
    cardNumber = card[0:-1]
    cardSuit = card[-1]
    # Convert cardNumber to int
    if(cardNumber == 'J'): cardNumber = 11
    elif(cardNumber == 'Q'): cardNumber = 12
    elif(cardNumber == 'K'): cardNumber = 13
    elif(cardNumber == 'A'): cardNumber = 14
    else: cardNumber = int(cardNumber)
    # Categorize card by its suit
    if(cardSuit == 'S'): spades.append(cardNumber)
    if(cardSuit == 'C'): clubs.append(cardNumber)
    if(cardSuit == 'D'): diamonds.append(cardNumber)
    if(cardSuit == 'H'): hearts.append(cardNumber)

# Sorting each suit by card number in ascending order
spades.sort()
clubs.sort()
diamonds.sort()
hearts.sort()

# Clear cards list
cards.clear()
# Put spades into cards list
for card in spades:
    # Convert back to string (Example: 13 --> "KS")
    if(card == 11): cards.append("JS")
    elif(card == 12): cards.append("QS")
    elif(card == 13): cards.append("KS")
    elif(card == 14): cards.append("AS")
    else: cards.append(str(card) + "S")

# Put clubs into cards list
for card in clubs:
    # Convert back to string (Example: 13 --> "KC")
    if(card == 11): cards.append("JC")
    elif(card == 12): cards.append("QC")
    elif(card == 13): cards.append("KC")
    elif(card == 14): cards.append("AC")
    else: cards.append(str(card) + "C")

# Put diamonds into cards list
for card in diamonds:
    # Convert back to string (Example: 13 --> "KD")
    if(card == 11): cards.append("JD")
    elif(card == 12): cards.append("QD")
    elif(card == 13): cards.append("KD")
    elif(card == 14): cards.append("AD")
    else: cards.append(str(card) + "D")

# Put hearts into cards list
for card in hearts:
    # Convert back to string (Example: 13 --> "KH")
    if(card == 11): cards.append("JH")
    elif(card == 12): cards.append("QH")
    elif(card == 13): cards.append("KH")
    elif(card == 14): cards.append("AH")
    else: cards.append(str(card) + "H")

# Output
print('|' + '|'.join(cards) + '|')