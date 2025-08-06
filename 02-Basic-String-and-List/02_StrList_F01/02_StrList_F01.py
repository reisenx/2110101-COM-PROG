# --------------------------------------------------
# File Name : 02_StrList_F01.py
# Problem   : Citizen ID (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------


# Create a function to calculate the last digit of a citizen ID
def check_digit(citizen_id):
    val = (
        13 * int(citizen_id[0])
        + 12 * int(citizen_id[1])
        + 11 * int(citizen_id[2])
        + 10 * int(citizen_id[3])
        + 9 * int(citizen_id[4])
        + 8 * int(citizen_id[5])
        + 7 * int(citizen_id[6])
        + 6 * int(citizen_id[7])
        + 5 * int(citizen_id[8])
        + 4 * int(citizen_id[9])
        + 3 * int(citizen_id[10])
        + 2 * int(citizen_id[11])
    )
    last_digit = (11 - (val % 11)) % 10
    return last_digit


# Execute the input string as code
exec(input())
