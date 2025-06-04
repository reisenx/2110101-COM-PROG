# Input
debt = float(input())
rate = float(input())
monthlyPay = float(input())

# ----- Formula -----
# interestMoney = debt * (rate/12)
# debt = debt - (monthlyPay - interestMoney)
# --------------------
months = 0
interestPay = 0
# Definite case (monthlyPay more than interestMoney)
if(monthlyPay > (debt*((rate/12)/100))):
    # Loop until debt = 0
    while(debt > 0):
        # Calculate interestMoney
        interestMoney = debt * ((rate/12)/100)
        # Last month
        if((debt + interestMoney) < monthlyPay):
            monthlyPay = debt + interestMoney
        # Remainder debt
        debt -= (monthlyPay - interestMoney)
        # Calculate interestPay
        interestPay += interestMoney
        months += 1
    # Output
    print(months, round(interestPay, 2))
# Indefinite case (monthlyPay not more than interestMoney)
else:
    print("indefinite")