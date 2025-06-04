# Input cards as a list
# 1.) Remove blank space at the end using .strip()
# 2.) Remove '|' at the at the start and end using .strip('|')
# 3.) Use .split('|') to separate a string into a list
cards = input().strip().strip('|').split('|')

# Calculate a score
# 1.) Remove a symbol at the end using card[0:-1]
# 2.) Check each card and add to a score
score = 0
for card in cards:
    card = card[0:-1]
    # For A card, the score is 1
    if(card == 'A'):
        score += 1
    # For K,Q,J card, the score is 10
    elif(card in ['K','Q','J']):
        score += 10
    # For other card (2,3,4,5,...), the score is their number
    else:
        score += int(card)

# Output
print(score)