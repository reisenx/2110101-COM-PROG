# --------------------------------------------------
# File Name : 03_If_08.py
# Problem   : Day of Year
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input the day, month, and year
D = int(input())
M = int(input())
Y = int(input())

# Convert the year to the year in the Gregorian calendar
Y = Y - 543

# List of total days in each month
TOTAL_DAYS = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

# Output the day of the year
if M <= 2:
    print(31 * (M - 1) + D)
else:
    # Check if the year is a leap year
    if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
        print(TOTAL_DAYS[M - 2] + D + 1)
    else:
        print(TOTAL_DAYS[M - 2] + D)
