# --------------------------------------------------
# File Name : 03_If_F08.py
# Problem   : Day of Year (Function)
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------

# List of total days in each month
TOTAL_DAYS = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]


def day_of_year(d, m, y):
    # Convert the year to the year in the Gregorian calendar
    y = y - 543

    # Output the day of the year
    if m <= 2:
        return 31 * (m - 1) + d
    else:
        # Check if the year is a leap year
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            return TOTAL_DAYS[m - 2] + d + 1
        else:
            return TOTAL_DAYS[m - 2] + d


# Execute the input string as code
exec(input())
