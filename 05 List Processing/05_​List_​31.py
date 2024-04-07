# Input a list of cards
# Input a process as a string
# Given 'num' is number of the cards
cards = input().split()
num = len(cards)
process = str(input())

# Process the list
for char in process:
    # Split the cards into 2 piles
    first_half = cards[:num//2]
    second_half = cards[num//2:]
    
    # Command: Cut ('C')
    # Split the cards into 2 piles then swap
    # Example: [A,2,3,4,5,6, | 7,8,9,10,J,Q] --> [7,8,9,10,J,Q,A,2,3,4,5,6]
    if(char == 'C'):
        cards = second_half + first_half
    
    # Command: Split ('S')
    # "S" is to split the cards into 2 piles then insert a card from a pile 
    # then insert a card from other pile and so on
    # Example: [A,2,3,4,5,6, | 7,8,9,10,J,Q] --> [A,7,2,8,3,9,4,10,5,J,6,Q]
    elif(char == 'S'):
        cards = []
        for i in range(num//2):
            cards.append(first_half[i])
            cards.append(second_half[i])

# Output
# Join each item in a list with " "
print(" ".join(cards))