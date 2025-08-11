# --------------------------------------------------
# File Name : 02_StrList_04.py
# Problem   : N Digits
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------

# Input a number
number = input().strip()

# Input number of digits to display
display_digits = int(input())

# Calculate leading zeros if the number of digits to display is greater
leading_zeros = max(0, display_digits - len(number))

# Output the number with leading zeros
print(f"{'0' * leading_zeros}{number}")
