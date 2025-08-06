# --------------------------------------------------
# File Name : 06_Func_31.py
# Problem   : Refactor
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# List of months in short form
MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

# List of days in each month
DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# List of zodiac signs with their date ranges
ZODIAC = [
    ["Aries", [3, 22], [4, 21]],
    ["Taurus", [4, 22], [5, 21]],
    ["Gemini", [5, 22], [6, 21]],
    ["Cancer", [6, 22], [7, 21]],
    ["Leo", [7, 22], [8, 21]],
    ["Virgo", [8, 22], [9, 21]],
    ["Libra", [9, 22], [10, 21]],
    ["Scorpio", [10, 22], [11, 21]],
    ["Sagittarius", [11, 22], [12, 21]],
    ["Capricorn", [12, 22], [12, 31]],
    ["Capricorn", [1, 1], [1, 20]],
    ["Aquarius", [1, 21], [2, 20]],
    ["Pisces", [2, 21], [3, 21]],
]


# Reads a date from input and returns a list [day, month, year]
def read_date():
    d, m, y = input().strip().split()
    return [int(d), MONTHS.index(m) + 1, int(y)]


# Returns the zodiac sign based on the day and month
def zodiac(d, m):
    for name, start, end in ZODIAC:
        if start <= [m, d] <= end:
            return name


# Returns the number of days in February for a given year
def days_in_feb(y):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        return 29
    else:
        return 28


# Find days in a month based on the month and year
def days_in_month(m, y):
    if m == 2:
        return days_in_feb(y)
    else:
        return DAYS_IN_MONTH[m - 1]


# Calculates the number of days between two dates
def days_in_between(d1, m1, y1, d2, m2, y2):
    # Add days from the first date to the end of that month
    days = days_in_month(m1, y1) - d1 + 1

    # Add days from month m1 + 1 to the end of the year y1
    for m in range(m1 + 1, 13):
        days += days_in_month(m, y1)

    # Add days from year y1 + 1 to year y2 - 1
    days += int((y2 - y1 - 1) * 365.25)

    # Add days from the beginning of year y2 to month m2 - 1
    for m in range(1, m2):
        days += days_in_month(m, y2)

    # Add days from the beginning of month m2 to day d2
    days += d2 - 1
    return days


# Main function
def main():
    # Read two dates
    d1, m1, y1 = read_date()
    d2, m2, y2 = read_date()

    # Output the zodiac signs of the two dates
    zodiac1 = zodiac(d1, m1)
    zodiac2 = zodiac(d2, m2)
    print(zodiac1, zodiac2)

    # Output the number of days in between the two dates
    days = days_in_between(d1, m1, y1, d2, m2, y2)
    print(days)


# Execute the input string as code
exec(input().strip())
