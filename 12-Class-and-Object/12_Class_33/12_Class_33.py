# --------------------------------------------------
# File Name : 12_Class_33.py
# Problem   : Piggy Bank 1
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------


class PiggyBank:
    # __init__ method
    # Initialize the 'PiggyBank' object with a dictionary to store coins
    def __init__(self):
        self.coins = {1: 0, 2: 0, 5: 0, 10: 0}

    # add1 method
    # This method adds 'n' coins of 1 baht to the piggy bank
    def add1(self, n):
        self.coins[1] += n

    # add2 method
    # This method adds 'n' coins of 2 baht to the piggy bank
    def add2(self, n):
        self.coins[2] += n

    # add5 method
    # This method adds 'n' coins of 5 baht to the piggy bank
    def add5(self, n):
        self.coins[5] += n

    # add10 method
    # This method adds 'n' coins of 10 baht to the piggy bank
    def add10(self, n):
        self.coins[10] += n

    # __int__ method
    # This calculates the total amount of money in the piggy bank
    def __int__(self):
        return (
            (10 * self.coins[10])
            + (5 * self.coins[5])
            + (2 * self.coins[2])
            + (1 * self.coins[1])
        )

    # __lt__ method
    # This compares two PiggyBank objects based on their total amount of money
    def __lt__(self, rhs):
        return int(self) < int(rhs)

    # __str__ method
    # This converts the PiggyBank object to a string representation of its coins
    def __str__(self):
        result = []
        for coin_type, coin_count in self.coins.items():
            result.append(f"{coin_type}:{coin_count}")
        return "{" + ", ".join(result) + "}"

# Output
cmd1 = input().split(";")
cmd2 = input().split(";")
p1 = PiggyBank()
p2 = PiggyBank()
for c in cmd1:
    eval(c)
for c in cmd2:
    eval(c)
