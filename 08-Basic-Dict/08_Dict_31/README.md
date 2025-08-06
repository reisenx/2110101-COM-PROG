<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Cash ★★★ (
      <a href="https://drive.google.com/file/d/1pfFCHg9Yo25WSBDuLaZHa2IGHpXGuupL/view?usp=drive_link">
        <code>08_Dict_31</code>
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
# File Name : 08_Dict_31.py
# Problem   : Cash
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Calculate the total money in the pocket
def total(pocket):
    total_money = 0
    for money, quantity in pocket.items():
        total_money += money * quantity
    return total_money


# This function takes money and adds it to the pocket
def take(pocket, money_in):
    for money, quantity in money_in.items():
        if money not in pocket:
            pocket[money] = 0
        pocket[money] += quantity
    return pocket


# This function pays the money from the pocket
# The pocket must be able to pay the exact amount of money_out
# Return a dictionary of money and quantity used to pay
# If it is impossible to pay, return an empty dictionary
def pay(pocket, money_out):
    if total(pocket) >= money_out:
        # Find the money and quantity to pay
        pocket_pay = {}
        for money, quantity in pocket.items():
            quantity_used = min(money_out // money, quantity)
            money_out -= money * quantity_used
            if quantity_used > 0:
                pocket_pay[money] = quantity_used

        # If it is possible to pay, money_out will be 0
        # Subtract "pocket" with "pocket_pay"
        if money_out == 0:
            for money, quantity_used in pocket_pay.items():
                pocket[money] -= quantity_used
            return pocket_pay

    # If it is impossible to pay, return empty dictionary
    return {}


# Execute an input string as code
exec(input().strip())
```
