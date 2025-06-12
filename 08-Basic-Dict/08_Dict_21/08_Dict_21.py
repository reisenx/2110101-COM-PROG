# --------------------------------------------------
# File Name : 08_Dict_21.py
# Problem   : Character Count
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input text and lowercase it
text = input().strip().lower()

# Initialize a dictionary to count characters
char_count = {}

# Count each character in the text
for char in text:
    if char.isalpha():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

# Sort the characters by count (descending) and then alphabetically
sorted_char_count = []
for char, count in char_count.items():
    sorted_char_count.append([-count, char])

sorted_char_count.sort()

# Output the sorted characters and their counts
for count, char in sorted_char_count:
    print(f"{char} -> {-count}")
