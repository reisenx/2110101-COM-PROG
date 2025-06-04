# Input initial money and amount of months
money, months = input().split()
money, months = float(money), int(months)

# Calculate money
# m = 1,5,9,13,...  (m % 4 = 1) --> Got 1% interest
# m = 2,6,10,14,... (m % 4 = 2) --> Got 2% interest
# m = 3,7,11,15,... (m % 4 = 3) --> Got 3% interest
# m = 4,8,12,16,... (m % 4 = 0) --> Got 4% interest
for m in range(1,months+1):
    if(m % 4 == 0):
        money += (money * (4/100) * (1/12))
    else:
        money += (money * ((m % 4)/100) * (1/12))

# Output
print(round(money,2))