# --------------------------------------------------
# File Name : 2566_1_Q1_01.py
# Problem   : Poker Hands Straight Flush
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------

# Initialize the order of straight and flush
STRAIGHT = "AKQJX98765432A"
ROYAL_STRAIGHT = "AKQJX"
FLUSH = ["CCCCC", "HHHHH", "DDDDD", "SSSSS"]

n = int(input())
for _ in range(n):
    # Extract values and suits from the card set
    cards = input().strip("|")
    values = cards[::3]
    suits = cards[1::3]

    # Check the values and suits for straight and flush
    is_flush = suits in FLUSH
    is_straight = values in STRAIGHT
    is_royal_straight = values == ROYAL_STRAIGHT

    # Output the type of poker hand
    if is_royal_straight and is_flush:
        print("Royal Straight Flush")
    elif is_straight and is_flush:
        print("Straight Flush")
    elif is_straight:
        print("Straight")
    elif is_flush:
        print("Flush")
    else:
        print("None")
