# Input a list of cards
# Input a process as a string
# Given num is a number of the cards
cards = input().split()
num = len(cards)
process = str(input())

# Process the list
# "C" is to split the cards into 2 piles then swap
# Example: [A,2,3,4,5,6,7,8,9,10,J,Q] --> [7,8,9,10,J,Q,A,2,3,4,5,6]
# "S" is to split the cards into 2 piles then insert a card from a pile 
# then insert a card from other pile and so on
# Example: [A,2,3,4,5,6,7,8,9,10,J,Q] --> [A,7,2,8,3,9,4,10,5,J,6,Q]
temp = []
temp1 = []
temp2 = []
for char in process:
    if(char == 'C'):
        temp = cards[int(num/2):] + cards[:int(num/2)]
        cards = temp
        temp = []
    elif(char == 'S'):
        temp1 = cards[:int(num/2)]
        temp2 = cards[int(num/2):]
        for i in range(0,int(num/2)):
            temp.append(temp1[i])
            temp.append(temp2[i])
        cards = temp
        temp = []
        temp1 = []
        temp2 = []

# Create a string of the new card order
card_shuffle = ""
for i in range(0,num):
    card_shuffle += cards[i] + " "

# Output
print(card_shuffle)