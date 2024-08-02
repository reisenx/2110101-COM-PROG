# This function can return total money in a pocket
# pocket is a dictionary in the format below
# Example: pocket = {100:5, 50:2, 10:5, 1:15}
# This means we have five 100 baht bills, two 50 baht bills, five 10 baht coins and fifteen 1 baht coins
# Therefore, total(pocket) returns (100*5)+(50*2)+(10*5)+(1*15) = 665
def total(pocket):
    total_money = 0
    for money,num in pocket.items():
        total_money += money*num
    return total_money

# This function can return dictionary "pocket" after take more money
# The "money_in" parameter is also a dictionary
# Example: take({100:5}, {100:2, 50:0, 1:3}) returns {100:7, 50:0, 1:3}
def take(pocket, money_in):
    for money,num in money_in.items():
        if(money in pocket):
            pocket[money] += num
        else:
            pocket[money] = num
    return pocket

# This function can return a dictionary of money that used for paying
# The "amt" parameter is an integer 
# Assume that the money (key) of "pocket" dictionary is always in descending order

# Example 1: pay({100:5, 50:2, 10:5, 1:15}, 57) returns {50:1, 1:7}
# When paying a money, we used the highest value money possible first
# In this case we pay with one 50 baht bill, then seven 1 baht coins
# Algorithm
# Create money_pay = {}
# Loop 1: min(57//100, 5) = 0 --> amt = 57-(100*0) = 57 --> money_pay = {}
# Loop 2: min(57//50, 2) = 1 --> amt = 57-(50*1) = 7 --> money_pay = {50:1}
# Loop 3: min(7//10, 5) = 0 --> amt = 7-(10*0) = 7 --> money_pay = {50:1}
# Loop 4: min(7//1, 15) = 7 --> amt = 7-(1*7) = 0 --> money_pay = {50:1, 1:7}
# After the loop, amt = 0 and money_pay = {50:1, 1:7}
# Subtract "pocket" with "money_pay" and we will get "pocket" = {100:5, 50:1, 10:5, 1:8}
# Returns {50:1, 1:7}

# Example 2: pay({10:5, 1:7}, 18) returns {}
# If impossible to pay with that method, return empty dictionary
# Algorithm
# Create money_pay = {}
# Loop 1: min(18//10, 5) = 1 --> amt = 18-(10*1) = 8 --> money_pay = {10:1}
# Loop 2: min(8//1, 7) = 7 --> amt = 8-(1*7) = 1 --> money_pay = {10:1, 1:7}
# After the loop, amt = 1 and money_pay = {100:0, 1:7}
# Don't subtract "pocket" with "money_pay", "pocket" remains the same
# Returns {}

def pay(pocket, amt):
    # If the total money in the pocket is less than "amt", it is impossible to pay in the first place
    if(total(pocket) < amt):
        return {}
    else:
        money_pay = {}
        for money,num in pocket.items():
            num_used = min(amt//money, num)
            amt -= money*num_used
            if(num_used > 0):
                money_pay[money] = num_used
        
        # - If it is possible to pay, amt will be 0
        if(amt == 0):
            # Subtract "pocket" with "money_pay"
            for money,num_used in money_pay.items():
                pocket[money] -= num_used
            # Returns "money_pay"
            return money_pay
        
        # - If it is impossible to pay, amt will be greater than 0
        elif(amt > 0):
            return {}

# Execute an input string
exec(input().strip())