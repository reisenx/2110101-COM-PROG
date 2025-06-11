# --------------------------------------------------
# File Name : 04_Loop_04.py
# Problem   : Parentheses
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input text
text = input().strip()

# Construct new text by replacing parentheses
new_text = ""
for char in text:
    if char == "(":
        new_text += "["
    elif char == ")":
        new_text += "]"
    elif char == "[":
        new_text += "("
    elif char == "]":
        new_text += ")"
    else:
        new_text += char

# Output the new text
print(new_text)
