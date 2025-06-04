# Input a number of ice cream
n = int(input())

# Input a ice cream brand and its price, then contain them in a dictionary
# Example Input:
# 5
# Magnum 50
# Cornetto 25
# PaddlePop 15
# AsianDelight 20
# Calippo 15
# > menu = {'Magnum': 50, 'Cornetto': 25, 'PaddlePop': 15, 'AsianDelight': 20, 'Calippo': 15}
# > sales = {'Magnum': 0, 'Cornetto': 0, 'PaddlePop': 0, 'AsianDelight': 0, 'Calippo': 0}
menu = {}
sales = {}
for i in range(n):
    product,price = input().split()
    menu[product] = int(price)
    sales[product] = 0

# Calculate sales of each product
# Example Input:
# 6
# Magnum 5
# Magnum 5
# Cookie 20
# MamaTomYum 3
# Cornetto 20
# AsianDelight 1
# > sales = {'Magnum': 500, 'Cornetto': 500, 'PaddlePop': 0, 'AsianDelight': 20, 'Calippo': 0}
n = int(input())
for i in range(n):
    product,quantity = input().split()
    if(product in menu):
        sales[product] += menu[product]*int(quantity)

# Calulate top sales and total sales
top_sales = 0
total_sales = 0
for icecream,money in sales.items():
    total_sales += money
    if(money > top_sales):
        top_sales = money

# Put top sales products into a list and sort it in alphabetical order
top_products = []
for icecream,money in sales.items():
    if(money == top_sales):
        top_products.append(icecream)
top_products.sort()

# Output
if(top_sales == 0):
    print("No ice cream sales")
else:
    print("Total ice cream sales:",float(total_sales))
    print("Top sales:", ", ".join(top_products))