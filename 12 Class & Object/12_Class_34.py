class piggybank:
    # __init__ method
    # Create 'piggybank' object and setup initial dictionary
    # The dictionary tell us how many coins in that 'piggybank' object
    def __init__(self):
        self.coins = {}
    
    # add method
    # Add n 'v' baht coins to a dictionary
    # 'v' is a float and 'n' is an integer
    # - If total coins not exceed 100 coins after added, return True 
    # - If total coins exceed 100 coins after added, return False
    def add(self,v,n):
        # Total coins not exceed 100 coins
        if(self.total_coins() + n <= 100):
            if(v not in self.coins):
                self.coins[float(v)] = n
            else:
                self.coins[float(v)] += n
            return True
        # total coins exceed 100 coins
        else:
            return False
    
    # total_coins method
    # This method can calculate total coins in 'piggybank' object
    def total_coins(self):
        return sum(self.coins.values())
    
    # __float__ method
    # Calculate total money in that 'piggybank' object
    def __float__(self):
        total = 0.0
        for value, quantity in self.coins.items():
            total += value*quantity
        return total
    
    # __str__ method
    # Return a dictionary but as a string
    # Sort in ascending order
    def __str__(self):
        # Sort and convert dictionary into a list
        # Example: self.coins = {20.5:9, 0.25:4, 10.0:1, 0.5:1}
        # sorted(self.coins.items()) = [(0.25,4), (0.5,1), (10.0,1), (20.5,9)]
        sorted_coins = sorted(self.coins.items())

        # Construct a string
        length = len(sorted_coins)
        # Case 1: Non-empty dictionary
        if(length > 0):
            string = "{"
            for i in range(length):
                value, quantity = sorted_coins[i][0], sorted_coins[i][1]
                # Between a string
                if(i < length-1):
                    string += str(value) + ":" + str(quantity) + ", "
                # End of a string
                else:
                    string += str(value) + ":" + str(quantity) + "}"
        # Case 2: Empty dictionary
        else:
            string = "{}"
        
        # Return a string
        return string

# Output
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
