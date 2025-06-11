# --------------------------------------------------
# File Name : 04_Loop_01.py
# Problem   : Average
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Initialize total and num_count
total = 0
num_count = 0

# Input numbers until 'q' is entered
while True:
    num = input().strip()
    if num == "q":
        break
    total += float(num)
    num_count += 1

# Calculate and print the average
if num_count > 0:
    average = total / num_count
    print(round(average, 2))
else:
    print("No Data")
