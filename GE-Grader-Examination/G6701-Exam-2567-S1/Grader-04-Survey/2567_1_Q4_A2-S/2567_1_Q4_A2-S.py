# --------------------------------------------------
# File Name : 2567_1_Q4_A2-S.py
# Problem   : Benefit from Sales
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Input benefits percentage for each type
BENEFITS = [0.0, 0.0, 0.0, 0.0]
for i in range(4):
    BENEFITS[i] = float(input().strip()) / 100

# Initialize total benefit money
total_benefit = 0.0

# Input sales records
n = int(input().strip())
for _ in range(n):
    # Extract sales type and money gained
    data = input().strip().split()
    type = int(data[1]) - 1
    sales = float(data[2])

    # Calculate benefit for this sale and add to total
    total_benefit += BENEFITS[type] * sales

# Output total benefit rounded to 2 decimal places
print(round(total_benefit, 2))
