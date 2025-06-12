# --------------------------------------------------
# File Name : 02_StrList_08.py
# Problem   : Decimal to Fraction
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math

# Input a decimal number in the format A,B,C
# where A is the integer part,
#       B is the non-repeating decimal part,
#   and C is the repeating decimal part.
A, B, C = input().strip().split(",")

# Convert repeating decimal to fraction
numerator = int(A + B + C) - int(A + B)
denominator = 10 ** (len(B) + len(C)) - 10 ** len(B)

# Output the fraction in its simplest form
gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd
print(f"{numerator} / {denominator}")
