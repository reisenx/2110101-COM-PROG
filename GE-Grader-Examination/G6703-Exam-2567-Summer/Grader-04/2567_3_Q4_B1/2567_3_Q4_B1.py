# --------------------------------------------------
# File Name : 2567_3_Q4_B1.py
# Problem   : Most Common Alphabet
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Initialize a dictionary to count occurrences of each letter
letter_count = {}

# Initialize a dictionary to store the alphabet based on their counts
letter_rankings = {}

# Input the number of letter occurrences ranks to display
rank_display_limit = int(input())

# Input text
text = input().strip()

# Count occurrences of each letter in the text
# and store them in the letter_count dictionary
for char in text:
    # Initialize the alphabet character in the dictionary if not already present
    if char.isalpha() and char not in letter_count:
        letter_count[char] = 0

    # Decrement the count for each alphabet character for sorting
    if char.isalpha():
        letter_count[char] -= 1

# Iterate through the letter_count dictionary
for char, count in letter_count.items():
    # Initialize the letter_rankings dictionary if the count is not already present
    if count not in letter_rankings:
        letter_rankings[count] = []

    # Append the character to the list for its count
    letter_rankings[count].append(char)

# Output the letters sorted by their counts in descending order
for count, chars in sorted(letter_rankings.items()):
    # Stop if the rank display limit is reached
    if rank_display_limit <= 0:
        break

    # Decrement the rank display limit by the number of characters printed
    rank_display_limit -= len(chars)

    # Sort the characters alphabetically and print them with their counts
    for char in sorted(chars):
        print(char, -count)
