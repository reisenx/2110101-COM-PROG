# --------------------------------------------------
# File Name : P1_01_Older.py
# Problem   : Part-I Older
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# List of month names
MONTH = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# Input first person's name and birthday
name01, m1, d1, y1 = input().strip().split()
birthday01 = [int(y1), MONTH.index(m1) + 1, int(d1.strip(","))]

# Input second person's name and birthday
name02, m2, d2, y2 = input().strip().split()
birthday02 = [int(y2), MONTH.index(m2) + 1, int(d2.strip(","))]

# Compare the two birthdays and output the older person
if birthday01 < birthday02:
    print(name01)
elif birthday01 > birthday02:
    print(name02)
else:
    print(name01, name02)
