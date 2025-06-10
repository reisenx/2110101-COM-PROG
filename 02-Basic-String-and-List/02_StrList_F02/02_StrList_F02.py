# --------------------------------------------------
# File Name : 02_StrList_F02.py
# Problem   : Arabic Numerals (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

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


# Function to convert a number to its string representation
def number_name(num: int | float | str) -> str:
    return NUMBERS[int(num)]


# Execute the input string as code
exec(input())
