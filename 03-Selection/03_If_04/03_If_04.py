# --------------------------------------------------
# File Name : 03_If_04.py
# Problem   : Mobile Number
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Constants
PHONE_DIGITS = 10
VALID_NUMBERS = ["06", "08", "09"]

# Input the mobile number
mobile_number = input().strip()

# Validate the mobile number
if len(mobile_number) == PHONE_DIGITS and mobile_number[:2] in VALID_NUMBERS:
    print("Mobile number")
else:
    print("Not a mobile number")
