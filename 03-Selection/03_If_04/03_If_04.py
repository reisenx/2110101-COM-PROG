# --------------------------------------------------
# File Name : 03_If_04.py
# Problem   : Mobile Number
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input the mobile number
mobile = input().strip()

# Validate the mobile number
if len(mobile) == 10 and mobile[:2] in ["06", "08", "09"]:
    print("Mobile number")
else:
    print("Not a mobile number")
