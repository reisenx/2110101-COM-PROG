# --------------------------------------------------
# File Name : 07_StrFile_13.py
# Problem   : Camel Case
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input a text as lowercase string
text = input().strip().lower()

# Remove all symbols and split the text into words
new_text = ""
for char in text:
    if char.isalnum():
        new_text += char
    else:
        new_text += " "

# Convert all words to camel case
words = new_text.split()
for i in range(1, len(words)):
    words[i] = words[i][0].upper() + words[i][1:]

# Output the CamelCase string
print("".join(words))
