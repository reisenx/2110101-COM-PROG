# --------------------------------------------------
# File Name : 02_StrList_04.py
# Problem   : N Digits
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input a number
num = input().strip()

# Input number of digits
display_digits = int(input())

# Output the number with leading zeros if display digits > digits in num
print("0" * max(display_digits - len(num), 0) + num)
