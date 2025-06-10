# --------------------------------------------------
# File Name : 02_StrList_F01.py
# Problem   : Citizen ID (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------


# Create a function to calculate the last digit of a citizen ID
def check_digit(ID: str) -> int:
    val = (
        13 * int(ID[0])
        + 12 * int(ID[1])
        + 11 * int(ID[2])
        + 10 * int(ID[3])
        + 9 * int(ID[4])
        + 8 * int(ID[5])
        + 7 * int(ID[6])
        + 6 * int(ID[7])
        + 5 * int(ID[8])
        + 4 * int(ID[9])
        + 3 * int(ID[10])
        + 2 * int(ID[11])
    )
    last_digit = (11 - (val % 11)) % 10
    return last_digit


# Execute the input string as code
exec(input())
