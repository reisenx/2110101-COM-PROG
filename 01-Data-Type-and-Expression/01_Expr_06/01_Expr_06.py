# --------------------------------------------------
# File Name : 01_Expr_06.py
# Problem   : Duration
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Constants
SECONDS_IN_MIN = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400

# Input the initial time in the format h1 : m1 : s1
h1 = int(input())
m1 = int(input())
s1 = int(input())

# Input the final time in the format h2 : m2 : s2
h2 = int(input())
m2 = int(input())
s2 = int(input())

# Convert the initial time and final time into seconds
t1 = (h1 * SECONDS_IN_HOUR) + (m1 * SECONDS_IN_MIN) + s1
t2 = (h2 * SECONDS_IN_HOUR) + (m2 * SECONDS_IN_MIN) + s2

# Calculate the duration in seconds
# Ensure that the duration is always positive by using modulo operation
dt = (SECONDS_IN_DAY + t2 - t1) % SECONDS_IN_DAY

# Convert the duration in seconds to hours, minutes, and seconds
dh = dt // SECONDS_IN_HOUR
dt %= SECONDS_IN_HOUR
dm = dt // SECONDS_IN_MIN
dt %= SECONDS_IN_MIN
ds = dt

# Output
print(f"{dh}:{dm}:{ds}")
