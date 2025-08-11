# --------------------------------------------------
# File Name : 03_If_07.py
# Problem   : Abbrev Num
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------

# List of symbols for abbreviations
SYMBOLS = ["", "K", "M", "B"]

# Input a number
num = int(input())

# Calculate the abbreviated number
n = 0
while num > 1000 and n < 3:
    num /= 1000
    n += 1

# Output the abbreviated number
if num < 10:
    print(f"{round(num, 1)}{SYMBOLS[n]}")
else:
    print(f"{round(num)}{SYMBOLS[n]}")
