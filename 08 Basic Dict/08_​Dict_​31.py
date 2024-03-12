# This function can return total money in a pocket
# pocket is a dictionary in the format below
# Example: pocket = {100:5, 50:2, 10:5, 1:15}
# This means we have five 100 baht bills, two 50 baht bills, five 10 baht coins and fifteen 1 baht coins
# Therefore, total(pocket) returns (100*5)+(50*2)+(10*5)+(1*15) = 665
def total(pocket):
    total_money = 0
    for money in pocket:
        total_money += money*pocket[money]
    return total_money

# This function can return dictionary "pocket" after take more money
# The money_in parameter is also a dictionary
# Example: take({100:5}, {100:2, 50:0, 1:3}) returns {100:7, 50:0, 1:3}
def take(pocket, money_in):
    for money in money_in:
        if(money in pocket):
            pocket[money] += money_in[money]
        else:
            pocket[money] = money_in[money]
    return pocket

# This function can return a dictionary of money that used for paying
# The amt parameter is an integer
# When paying a money, we used the highest value money possible first
# Example 1: pay({100:5, 50:2, 10:5, 1:15}, 57)
# In the case we pay with one 50 baht bill, then seven 1 baht coins

# If impossible to pay with that method, return empty dictionary
# Example 2: pay({10:5, 1:7}, 18) returns {}

