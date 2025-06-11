# --------------------------------------------------
# File Name : 03_If_F04.py
# Problem   : Mobile Number (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------


# This function checks if a given string is a valid mobile number.
def is_mobile_number(number: str) -> bool:
    return len(number) == 10 and number[:2] in ["06", "08", "09"]


# Execute the input string as code
exec(input())
