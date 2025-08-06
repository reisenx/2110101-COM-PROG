<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Ice Cream Sales ★★ (
      <a href="https://drive.google.com/file/d/1hxgTFuNQ-XUr5p4xlReWOb0wvgzQSXRF/view?usp=drive_link">
        <code>08_Dict_22</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**Solution**](#solution)

---

<div align="center">
  <h2>เฉลยอย่างละเอียดจะตามมาทีหลัง</h2>
</div>

---

# Solution

```python
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
```
