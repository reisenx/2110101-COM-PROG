# --------------------------------------------------
# File Name : 2567_1_Q3_C1-S.py
# Problem   : Money Change
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Coins limit for 1 baht, 2 baht, and 5 baht
COINS_LIMIT = 9

# Initialize the total solution count
total_sol_count = 0

# Input total money
total_money = int(input())

# Loop through all combinations on 5 baht, 2 baht, and 1 baht coins
for fives in range(COINS_LIMIT + 1):
    for twos in range(COINS_LIMIT + 1):
        for ones in range(COINS_LIMIT + 1):
            # Calculate the remaining money after using the coins
            remaining_money = total_money - (fives * 5) - (twos * 2) - ones

            # Check if the remaining money is possible to pay with only 10 baht coins
            if remaining_money >= 0 and remaining_money % 10 == 0:
                total_sol_count += 1

# Output the total solution count
print(total_sol_count)
