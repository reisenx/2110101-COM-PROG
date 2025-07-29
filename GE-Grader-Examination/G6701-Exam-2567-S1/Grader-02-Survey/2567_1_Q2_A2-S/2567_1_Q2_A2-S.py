# --------------------------------------------------
# File Name : 2567_1_Q2_A2-S.py
# Problem   : Loan Debt
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input initial debt, interest rate, and monthly payment
initial_debt = float(input())
interest_rate = float(input()) / 100
monthly_pay = float(input())

# Initialize total month and total interest
total_month = 0
total_interest = 0

# Initialize current debt and calculate initial interest
current_debt = initial_debt
interest = current_debt * (interest_rate / 12)

# Check if monthly payment is greater than interest
if monthly_pay > interest:
    # Loop until the debt is paid off
    while current_debt > 0:
        # Calculate interest of the current month
        interest = current_debt * (interest_rate / 12)

        # Update current debt and total interest
        current_debt = max(0, current_debt - (monthly_pay - interest))
        total_interest += interest

        # Increment total month
        total_month += 1

    # Output total month and total interest
    print(total_month, round(total_interest, 2))

# If monthly payment is less than or equal to interest
# it's impossible to pay off the debt
else:
    print("indefinite")
