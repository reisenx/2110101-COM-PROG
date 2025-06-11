# --------------------------------------------------
# File Name : 04_Loop_05.py
# Problem   : Count Word
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input interested word
key = input().strip()

# Input text
text = input().strip()

# Remove symbol from the text
new_text = ""
for char in text:
    if char in ['"', "(", ")", ",", ".", "'"]:
        new_text += " "
    else:
        new_text += char

# Split the new text into words
words = new_text.split()

# Count the occurrences of the interested word
count = 0
for word in words:
    if word == key:
        count += 1

# Output the count
print(count)
