# Input data
birth, money, months, currentMonth = input().split()
bd, bm, by = birth.split('/')
bm, money, months, currentMonth = int(bm), float(money), int(months), int(currentMonth)

# Calculate money
for n in range(1, months+1):
    # Check interest rate
    # n = 1,5,9,13,...  | n % 4 == 1 | interest = 0.01
    # n = 2,6,10,14,... | n % 4 == 2 | interest = 0.02
    # n = 3,7,11,15,... | n % 4 == 3 | interest = 0.03
    # n = 4,8,12,16,... | n % 4 == 0 | interest = 0.04
    if(n % 4 == 0):
        interest = 0.04
    else:
        interest = (n % 4)/100
    # Check birth month (Beware of bm = 12 case)
    if(currentMonth % 12 == bm % 12):
        interest += 0.01
    # Calculate money
    money += money * interest * (1/12)
    currentMonth += 1

# Output
print(round(money, 2))