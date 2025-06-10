# --------------------------------------------------
# File Name : 02_StrList_03.py
# Problem   : US Date
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input a date in the format DD/MM/YYYY
date = input().strip()

# Split the input date into day, month, and year
d, m, y = date.split("/")

# List of month names in English
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

# Output the date in the format "Month Day, Year"
print(MONTH[int(m) - 1], (d + ", " + y))
