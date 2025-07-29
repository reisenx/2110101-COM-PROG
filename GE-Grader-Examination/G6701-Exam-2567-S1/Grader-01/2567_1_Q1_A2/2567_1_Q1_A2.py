# --------------------------------------------------
# File Name : 2567_1_Q1_A2.py
# Problem   : Interest Rate
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Initial interest rates for each month
INITIAL_INTEREST_RATE = [0.04, 0.01, 0.02, 0.03]

# Input
data = input().split()

# Get birth month, initial money, total months, and current month from input
birth_month = int(data[0].split("/")[1])
initial_money = float(data[1])
total_months = int(data[2])
current_month = int(data[3])

# Initialize total money with the initial money
total_money = initial_money

# Loop through each month to calculate the interest
for month in range(1, total_months + 1):
    # Determine interest rate based on month
    interest_rate = INITIAL_INTEREST_RATE[month % 4]

    # Check if current month matches birth month
    if (current_month % 12) == (birth_month % 12):
        interest_rate += 0.01

    # Calculate new total money amount
    total_money += total_money * interest_rate * (1 / 12)

    # Increment current month
    current_month += 1

# Output the total money rounded to two decimal places
print(round(total_money, 2))
