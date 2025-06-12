# --------------------------------------------------
# File Name : 08_Dict_22.py
# Problem   : Ice Cream Sales
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Initialize dictionaries for menu and sales
menu = {}
sales = {}
total_revenue = 0.0

# Input the menu items and their prices
n = int(input())
for _ in range(n):
    item, price = input().strip().split()
    menu[item] = float(price)
    sales[item] = 0.0

# Input the sales data
n = int(input())
for _ in range(n):
    item, quantity = input().strip().split()
    if item in menu:
        sales[item] += menu[item] * int(quantity)

# Sort the sales items by total sales amount (descending) and then alphabetically
sorted_sales = []
for item, revenue in sales.items():
    if revenue > 0:
        total_revenue += revenue
        sorted_sales.append([-revenue, item])
sorted_sales.sort()

# Output
if len(sorted_sales) > 0:
    # Find the top sales items and their total sales
    highest_revenue = sorted_sales[0][0]
    top_items = []
    for revenue, item in sorted_sales:
        if revenue == highest_revenue:
            top_items.append(item)

    # Output the top sales items
    print(f"Total ice cream sales: {total_revenue}")
    print("Top sales:", ", ".join(top_items))
else:
    print("No ice cream sales")
