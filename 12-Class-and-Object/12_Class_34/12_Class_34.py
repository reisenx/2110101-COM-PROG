# --------------------------------------------------
# File Name : 12_Class_34.py
# Problem   : Piggy Bank 2
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------


class PiggyBank:
    # __init__ method
    def __init__(self) -> None:
        self.coins = {}

    # add method
    def add(self, value: int | float, n: int) -> bool:
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
    def total_coins(self) -> int:
        return sum(self.coins.values())

    # __float__ method
    # Calculate the total value of coins in the piggy bank
    def __float__(self) -> float:
        total_money = 0.0
        for value, quantity in self.coins.items():
            total_money += value * quantity
        return total_money

    # __str__ method
    def __str__(self) -> str:
        sorted_coins = {}
        for value, quantity in sorted(self.coins.items()):
            sorted_coins[value] = quantity
        return str(sorted_coins)


# Output
cmd1 = input().split(";")
cmd2 = input().split(";")
p1 = PiggyBank()
p2 = PiggyBank()
for c in cmd1:
    eval(c)
for c in cmd2:
    eval(c)
