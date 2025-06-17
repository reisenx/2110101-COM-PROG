# --------------------------------------------------
# File Name : P2_05_Anagram2.py
# Problem   : Part-II Anagram 2
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# Input two strings
texts = []
for _ in range(2):
    texts.append(input().strip())

# Initialize dictionaries to count characters in both strings
char_counts = [{}, {}]

# Count characters in both strings
for i in range(2):
    for char in texts[i].lower():
        if char.isalpha() and char not in char_counts[i]:
            char_counts[i][char] = 1
        elif char.isalpha() and char in char_counts[i]:
            char_counts[i][char] += 1

# Initialize lists to store characters to be removed from each string
remove_chars = [{}, {}]

# Compare character counts and determine which characters to remove
for i in range(2):
    for char, count in char_counts[i].items():
        # The character exists in both strings
        if char in char_counts[1 - i]:
            diff = count - char_counts[1 - i][char]
            if diff > 0:
                remove_chars[i][char] = diff
        # The character exists only in the current string
        else:
            remove_chars[i][char] = count

# Output the characters to be removed from each string
for i in range(2):
    # Output the current string
    print(texts[i])
    # Output the characters to be removed
    if len(remove_chars[i]) > 0:
        for char, count in sorted(remove_chars[i].items()):
            if count > 1:
                print(f" - remove {count} {char}'s")
            else:
                print(f" - remove {count} {char}")
    else:
        print(" - None")
