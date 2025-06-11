# --------------------------------------------------
# File Name : 03_If_09.py
# Problem   : Biorhythm
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math

# Input the birth date (bd), birth month (bm), birth year (by),
# the current day (d), month (m), and year (y)
bd, bm, by, d, m, y = [int(e) for e in input().split()]

# Convert the year to the year in the Gregorian calendar
by = by - 543
y = y - 543

# List of days in each month for common and leap years
COMMON = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Initialize the day count
days = 0

# Calculate duration from bd/bm/by to 31/12/by
# Need to check if the birth year is a leap year
if (by % 400 == 0) or (by % 4 == 0 and by % 100 != 0):
    days += (LEAP[bm - 1] - bd) + sum(LEAP[bm:])
else:
    days += (COMMON[bm - 1] - bd) + sum(COMMON[bm:])

# Calculate duration from 01/01/(by+1) to 31/12/(y-1)
# No need to check leap year for the years in between
days += (y - by - 1) * 365

# Calculate duration from 01/01/y to d/m/y
# Need to check if the current year is a leap year
if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    days += sum(LEAP[: m - 1]) + d
else:
    days += sum(COMMON[: m - 1]) + d

# Calculate biorhythm
physical = math.sin((2 * math.pi * days) / 23)
emotional = math.sin((2 * math.pi * days) / 28)
intellectual = math.sin((2 * math.pi * days) / 33)

# Output
print(
    days,
    f"{physical:.2f}",
    f"{emotional:.2f}",
    f"{intellectual:.2f}",
)
