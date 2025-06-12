# --------------------------------------------------
# File Name : 07_StrFile_21.py
# Problem   : ROT13
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# List of lowercase and uppercase letters
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Function to encrypt text using ROT13 cipher
def ROT13(text: str) -> str:
    result = ""
    for char in text:
        # Encrypt lowercase letters
        if char in LOWERCASE:
            idx = LOWERCASE.index(char)
            result += LOWERCASE[(idx + 13) % 26]
        # Encrypt uppercase letters
        elif char in UPPERCASE:
            idx = UPPERCASE.index(char)
            result += UPPERCASE[(idx + 13) % 26]
        # Keep non-alphabetic characters unchanged
        else:
            result += char
    return result


# ROT13 encryption
while True:
    # Input a text
    text = input().strip()
    # Stop if the input is "end"
    if text == "end":
        break
    # Output the encrypted text
    print(ROT13(text))
