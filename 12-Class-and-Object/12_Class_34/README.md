<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Piggy Bank 2 ★★★ (
      <a href="https://drive.google.com/file/d/1F6onEA6o4ffyH7_50jcqVq4D8vcVRn5n/view?usp=drive_link">
        <code>12_Class_34</code>
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
# File Name : 12_Class_34.py
# Problem   : Piggy Bank 2
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------


class PiggyBank:
    # __init__ method
    def __init__(self):
        self.coins = {}

    # add method
    def add(self, value, n):
        # Total coins cannot exceed 100
        if self.total_coins() + n > 100:
            return False
        # Add coins to the piggy bank
        if value not in self.coins:
            self.coins[float(value)] = n
        else:
            self.coins[float(value)] += n
        return True

    # total_coins method
    # Calculate the total number of coins in the piggy bank
    def total_coins(self):
        return sum(self.coins.values())

    # __float__ method
    # Calculate the total value of coins in the piggy bank
    def __float__(self):
        total_money = 0.0
        for value, quantity in self.coins.items():
            total_money += value * quantity
        return total_money

    # __str__ method
    def __str__(self):
        ordered_coins = []
        for value, quantity in sorted(self.coins.items()):
            ordered_coins.append(f"{value}:{quantity}")
        return "{" + ", ".join(ordered_coins) + "}"


# Output
cmd1 = input().split(";")
cmd2 = input().split(";")
p1 = PiggyBank()
p2 = PiggyBank()
for c in cmd1:
    eval(c)
for c in cmd2:
    eval(c)
```
