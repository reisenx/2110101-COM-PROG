# --------------------------------------------------
# File Name : 02_StrList_02.py
# Problem   : Arabic Numerals
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input a number (0-9)
num = int(input())

# List of string representations of numbers from 0 to 9
NUMBERS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

# Output the number and its string representation
print(num, "-->", NUMBERS[num])
