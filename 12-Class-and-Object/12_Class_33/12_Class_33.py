class piggybank:
    # __init__ method
    # Create 'piggybank' object and setup initial dictionary
    # The dictionary tell us how many 1,2,5,10 baht coins in that 'piggybank' object
    def __init__(self):
        self.coins = {1:0, 2:0, 5:0, 10:0}
    
    # add1 method
    # Add 'n' 1 baht coins to a dictionary
    def add1(self, n):
        self.coins[1] += n
    
    # add2 method
    # Add 'n' 2 baht coins to a dictionary
    def add2(self, n):
        self.coins[2] += n
    
    # add5 method
    # Add 'n' 5 baht coins to a dictionary
    def add5(self, n):
        self.coins[5] += n
        
    # add10 method
    # Add 'n' 10 baht coins to a dictionary
    def add10(self, n):
        self.coins[10] += n
    
    # __int__ method
    # Returns total money in a piggybank
    # Example: {1:1, 2:2, 5:3, 10:4} --> 60
    def __int__(self):
        one = self.coins[1]
        two = self.coins[2]
        five = self.coins[5]
        ten = self.coins[10]
        return one + (two * 2) + (five * 5) + (ten * 10)
    
    # __lt__ method
    # This method can compare 2 'piggybank' object by their total money
    def __lt__(self, rhs):
        total01 = int(self)
        total02 = int(rhs)
        return total01 < total02
    
    # __str__ method
    # Returns a dictionary but as a string
    def __str__(self):
        one = self.coins[1]
        two = self.coins[2]
        five = self.coins[5]
        ten = self.coins[10]
        return "{1:" + str(one) + ", 2:" + str(two) + ", 5:" + str(five) + ", 10:" + str(ten) + "}"

# Output
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
