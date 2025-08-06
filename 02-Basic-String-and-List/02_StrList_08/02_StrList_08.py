# --------------------------------------------------
# File Name : 02_StrList_08.py
# Problem   : Decimal to Fraction
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math

# Input a decimal number in the format A,B,C
# where 'a' is the integer part,
#       'b' is the non-repeating decimal part,
#   and 'c' is the repeating decimal part.
a, b, c = input().strip().split(",")

# Convert repeating decimal to fraction
numerator = int(a + b + c) - int(a + b)
denominator = 10 ** (len(b) + len(c)) - 10 ** len(b)

# Output the fraction in its simplest form
gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd
print(f"{numerator} / {denominator}")
