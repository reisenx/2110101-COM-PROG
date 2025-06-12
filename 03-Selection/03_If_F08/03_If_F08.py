# --------------------------------------------------
# File Name : 03_If_F08.py
# Problem   : Day of Year (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# List of total days in each month
TOTAL_DAYS = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]


def day_of_year(D: int, M: int, Y: int) -> int:
    # Convert the year to the year in the Gregorian calendar
    Y = Y - 543

    # Output the day of the year
    if M <= 2:
        return 31 * (M - 1) + D
    else:
        # Check if the year is a leap year
        if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
            return TOTAL_DAYS[M - 2] + D + 1
        else:
            return TOTAL_DAYS[M - 2] + D


# Execute the input string as code
exec(input())
