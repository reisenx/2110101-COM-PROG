# --------------------------------------------------
# File Name : 05_List_F11.py
# Problem   : Missing Digits (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


def missing_digits(text):
    # Initialize a list to track found digits
    found_digits = [False] * 10

    # Iterate through each character in the input text
    for char in text:
        if char.isdigit():
            digit = int(char)
            found_digits[digit] = True

    # Collect the missing digits
    missing = []
    for num in range(10):
        if not found_digits[num]:
            missing.append(num)

    # Return the missing digits
    return missing


# Execute the input string as code
exec(input())
