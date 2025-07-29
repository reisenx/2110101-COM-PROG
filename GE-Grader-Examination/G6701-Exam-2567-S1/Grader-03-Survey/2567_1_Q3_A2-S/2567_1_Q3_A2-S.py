# --------------------------------------------------
# File Name : 2567_1_Q3_A2-S.py
# Problem   : Interest Rate
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Interest rates for each month
INTEREST_RATE = [0.04, 0.01, 0.02, 0.03]

# Extract initial money and total months from the input
data = input().split()
initial_money = float(data[0])
total_months = int(data[1])

# Initialize current money with the initial money
current_money = initial_money

# Calculate the money after each month using the interest rates
for month in range(1, total_months + 1):
    current_money += current_money * INTEREST_RATE[month % 4]

# Output
print(round(current_money, 2))
