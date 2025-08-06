# --------------------------------------------------
# File Name : 05_List_31.py
# Problem   : Cut & Shuffle
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input card deck
deck = input().split()
half_idx = len(deck) // 2

# Input commands
commands = input().strip()

# Cut & Shuffle the deck
for cmd in commands:
    # Split the deck into two halves
    first_half = deck[:half_idx]
    second_half = deck[half_idx:]

    # Cut the deck
    if cmd == "C":
        deck = second_half + first_half
    # Shuffle the deck
    elif cmd == "S":
        deck = []
        for i in range(half_idx):
            deck.append(first_half[i])
            deck.append(second_half[i])

# Output the final deck
print(" ".join(deck))
