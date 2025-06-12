# --------------------------------------------------
# File Name : 07_StrFile_13.py
# Problem   : Camel Case
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input a text
text = input().strip()

# Remove all symbols and split the text into words
new_text = ""
for char in text:
    if not char.isalnum():
        new_text += " "
    else:
        new_text += char
words = new_text.split()

# Convert all words to camel case
for i in range(len(words)):
    words[i] = words[i].lower()
    if i > 0:
        words[i] = words[i][0].upper() + words[i][1:]

# Output the CamelCase string
print("".join(words))
