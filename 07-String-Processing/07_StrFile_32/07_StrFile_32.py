# --------------------------------------------------
# File Name : 07_StrFile_32.py
# Problem   : Password Strength
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# List of characters
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "01234567890"
SYMBOL = "!@#$%^&*()_+-=[]{}\\|;:'\",.<>/?`~"
PATTERNS = ["!@#$%^&*()_+", "QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]


# Check if the password has less than 8 letters
def less_than_eight_letter(password: str) -> bool:
    return len(password) < 8


# Check if the password has no lowercase letters
def no_lowercase(password: str) -> bool:
    for char in password:
        if char in LOWERCASE:
            return False
    return True


# Check if the password has no uppercase letters
def no_uppercase(password: str) -> bool:
    for char in password:
        if char in UPPERCASE:
            return False
    return True


# Check if the password has no numbers
def no_number(password: str) -> bool:
    for char in password:
        if char in NUMBER:
            return False
    return True


# Check if the password has no symbols
def no_symbol(password: str) -> bool:
    for char in password:
        if char in SYMBOL:
            return False
    return True


# Check if the password has 4 continuous same characters
def character_repetition(password: str) -> bool:
    for i in range(len(password) - 3):
        substring = password[i : i + 4].lower()
        if substring == substring[0] * 4:
            return True
    return False


# Check if there are 4 continuous numbers in password that are in order
def number_sequence(password: str) -> bool:
    for i in range(len(password) - 3):
        substring = password[i : i + 4]
        if substring in NUMBER or substring[::-1] in NUMBER:
            return True
    return False


# Check if there are 4 continuous characters in password that are in order
def letter_sequence(password: str) -> bool:
    for i in range(len(password) - 3):
        substring = password[i : i + 4].lower()
        if substring in LOWERCASE or substring[::-1] in LOWERCASE:
            return True
    return False


# Check if there are 4 continuous characters in password that are in keyboard row order
def keyboard_pattern(password: str) -> bool:
    for pattern in PATTERNS:
        for i in range(len(password) - 3):
            substring = password[i : i + 4].upper()
            if substring in pattern or substring[::-1] in pattern:
                return True
    return False


# Input a password
password = input().strip()
is_password_strong = True

# Output
OUTPUT = [
    [less_than_eight_letter(password), "Less than 8 characters"],
    [no_lowercase(password), "No lowercase letters"],
    [no_uppercase(password), "No uppercase letters"],
    [no_number(password), "No numbers"],
    [no_symbol(password), "No symbols"],
    [character_repetition(password), "Character repetition"],
    [number_sequence(password), "Number sequence"],
    [letter_sequence(password), "Letter sequence"],
    [keyboard_pattern(password), "Keyboard pattern"],
]

for condition, message in OUTPUT:
    if condition:
        print(message)
        is_password_strong = False

if is_password_strong:
    print("OK")
