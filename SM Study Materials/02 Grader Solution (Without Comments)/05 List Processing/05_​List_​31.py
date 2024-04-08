cards = input().split()
num = len(cards)
process = str(input())

for char in process:
    first_half = cards[:num//2]
    second_half = cards[num//2:]
    
    if(char == 'C'):
        cards = second_half + first_half
    elif(char == 'S'):
        cards = []
        for i in range(num//2):
            cards.append(first_half[i])
            cards.append(second_half[i])

print(" ".join(cards))