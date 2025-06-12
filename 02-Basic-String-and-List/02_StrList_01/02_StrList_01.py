# --------------------------------------------------
# File Name : 02_StrList_01.py
# Problem   : Citizen ID
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input citizen ID
ID = input()

# Calculate the last digit based on the first 12 digits
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

# Output the formatted ID
print(f"{ID[0]} {ID[1:5]} {ID[5:10]} {ID[10:12]} {last_digit}")
