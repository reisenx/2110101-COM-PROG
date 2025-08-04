# --------------------------------------------------
# File Name : 07_StrFile_11.py
# Problem   : Plural
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# List of vowels
VOWELS = ["a", "e", "i", "o", "u"]

# Input a word
word = input().strip()

# Add -es if the word ends with 's', 'x', or 'ch'
if word[-1] in ["s", "x"] or word[-2:] == "ch":
    word += "es"

# Add -ies if the word ends with 'y' and the second last character is a vowel
elif word[-1] == "y" and word[-2] not in VOWELS:
    word = word[:-1] + "ies"

# Otherwise, just add -s
else:
    word += "s"

# Output the plural form of the word
print(word)
