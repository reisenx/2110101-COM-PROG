# --------------------------------------------------
# File Name : 05_List_14.py
# Problem   : Peaks
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input a list of numbers
number = [float(e) for e in input().split()]

# Count the number of peaks
peak_count = 0
for i in range(1, len(number) - 1):
    if number[i] > number[i - 1] and number[i] > number[i + 1]:
        peak_count += 1

# Output the number of peaks
print(peak_count)
