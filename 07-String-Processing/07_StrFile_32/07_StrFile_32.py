# This function can check if the password is less than 8 letter
def less_than_eight_letter(password):
    if(len(password) < 8):
        return True
    else:
        return False

# This function can check if the password have no lowercase
def no_lowercase(password):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    NoLower = True
    for char in password:
        if(char in lowercase):
            NoLower = False
            break
    return NoLower

# This function can check if the password have no uppercase
def no_uppercase(password):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NoUpper = True
    for char in password:
        if(char in uppercase):
            NoUpper = False
            break
    return NoUpper

# This function can check if the password have no number
def no_number(password):
    number = "0123456789"
    NoNumber = True
    for char in password:
        if(char in number):
            NoNumber = False
            break
    return NoNumber

# This function can check if the password have no symbol
def no_symbol(password):
    symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '=', '[', '{', ']', '}', '\\', '|'
              , ';', ':', '\'', '\"', ',', '<', '.', '>', '/', '?']
    NoSymbol = True
    for char in password:
        if(char in symbol):
            NoSymbol = False
            break
    return NoSymbol

# This function can check if there are 4 continuous letters that are the same letter
# Example: aaaa, BbbB, CCCC
def character_repetition(password):
    length = len(password)
    IsCharRepeat = False

    password = password.upper()
    if(length < 4):
        return IsCharRepeat
    else:
        for i in range(length-3):
            if(password[i] == password[i+1] == password[i+2] == password[i+3]):
                IsCharRepeat = True
                break
        return IsCharRepeat

# This function can check if there are 4 continuous numbers in password that are in order
# Example: 0123, 2345, 7890, 0987
def number_sequence(password):
    number = "01234567890"
    number_reversed = "09876543210"
    length = len(password)
    IsNumberOrder = False

    if(length < 4):
        return IsNumberOrder
    else:
        for i in range(length-3):
            if(password[i:i+4] in number):
                IsNumberOrder = True
                break
            elif(password[i:i+4] in number_reversed):
                IsNumberOrder = True
                break
        return IsNumberOrder
    
# This function can check if there are 4 continuous characters in password that are in order
# Example: abcd, wXYZ, ZYxW
def letter_sequence(password):
    charcter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charcter_reversed = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    length = len(password)
    IsCharOrder = False

    password = password.upper()
    if(length < 4):
        return IsCharOrder
    else:
        for i in range(length-3):
            if(password[i:i+4] in charcter):
                IsCharOrder = True
                break
            elif(password[i:i+4] in charcter_reversed):
                IsCharOrder = True
                break
        return IsCharOrder

# This function can check if there are 4 continuous characters in password that are in keyboard row order
# Example: ASDF, qwer, REWq, !@#$
def keyboard_pattern(password):
    ROW1 = "!@#$%^&*()_+"
    ROW2 = "QWERTYUIOP"
    ROW3 = "ASDFGHJKL"
    ROW4 = "ZXCVBNM"
    length = len(password)
    IsKeyboardOrder = False

    password = password.upper()
    if(length < 4):
        return IsKeyboardOrder
    else:
        for i in range(length-3):
            # Check keyboard order on row 1
                # Check ascending order (Example: "!@#$")
                if(password[i:i+4] in ROW1):
                    IsKeyboardOrder = True
                    break
                # Check descending order (Example: ")(*&")
                elif(password[i:i+4] in ROW1[::-1]):
                    IsKeyboardOrder = True
                    break

            # Check keyboard order on row 2
                # Check ascending order (Example: "QwEr")
                if(password[i:i+4] in ROW2):
                    IsKeyboardOrder = True
                    break
                # Check descending order (Example: "OiuY")
                elif(password[i:i+4] in ROW2[::-1]):
                    IsKeyboardOrder = True
                    break
            
            # Check keyboard order on row 3
                # Check ascending order (Example: "AsdF")
                if(password[i:i+4] in ROW3):
                    IsKeyboardOrder = True
                    break
                # Check descending order (Example: "LkJh")
                elif(password[i:i+4] in ROW3[::-1]):
                    IsKeyboardOrder = True
                    break

            # Check keyboard order on row 4
                # Check ascending order (Example: "ZxCv")
                if(password[i:i+4] in ROW4):
                    IsKeyboardOrder = True
                    break
                # Check descending order (Example: "MnbV")
                elif(password[i:i+4] in ROW4[::-1]):
                    IsKeyboardOrder = True
                    break
        return IsKeyboardOrder

# Input a password
password = input().strip()

# Check condition
C1 = less_than_eight_letter(password)
C2 = no_lowercase(password)
C3 = no_uppercase(password)
C4 = no_number(password)
C5 = no_symbol(password)
C6 = character_repetition(password)
C7 = number_sequence(password)
C8 = letter_sequence(password)
C9 = keyboard_pattern(password)
# C1-C9 must be False to make "ALL" be True
ALL = not(C1 or C2 or C3 or C4 or C5 or C6 or C7 or C8 or C9)

# Output
# Condition 01: Password has less than 8 letters
if(C1):
    print("Less than 8 characters")
# Condition 02: Password has no lowercase letters
if(C2):
    print("No lowercase letters")
# Condition 03: Password has no uppercase letters
if(C3):
    print("No uppercase letters")
# Condition 04: Password has no numbers
if(C4):
    print("No numbers")
# Condition 05: Password has no symbols
if(C5):
    print("No symbols")
# Condition 06: Password has 4 continuous letters that are the same letter
# Example: aaaa, BbbB, CCCC
if(C6):
    print("Character repetition")
# Condition 07: Password has 4 continuous numbers in password that are in order
# Example: 0123, 2345, 7890, 0987
if(C7):
    print("Number sequence")
# Condition 08: Password has 4 continuous characters in password that are in order
# Example: abcd, wXYZ, ZYxW
if(C8):
    print("Letter sequence")
# Condition 09: Password has 4 continuous characters in password that are in keyboard row order
# Example: ASDF, qwer, REWq, !@#$
if(C9):
    print("Keyboard pattern")
# If those previous condition are not met, that means the password is strong
if(ALL):
    print("OK")