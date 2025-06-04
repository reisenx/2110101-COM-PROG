# Input number of bidding process
n = int(input())

# Create a dictionary that contains bidding details of each product
# {Product:[List of tuple (Bidder,Price)]}
# Example: products = {'p1':[('b3',11),(b1,11)], 'p2':[('b2',9)], 'p4':[('b2',1), ('b3',5)]} 
products_details = {}

# Create a dictionary that contains bidder details
# 'bidder_money' contains {Name:Money used}
# 'bidder_product' contains {Name:[List of product purchased]}
bidder_name = []
bidder_money = {}
bidder_product = {}

# Input bidding process which each line contains
# [Command] [Bidder] [Product] [Price]
# Example: "B b3 p1 11"
# Example: "W b1 p2"    (No [Price] in "W" command)
for i in range(n):
    line = input().strip().split()
    # Command: Bid (B)
    # This function add tuple (Bidder,Price) to the dictionary 'products_details'
    # NOTE: If that 'bidder' bid on the same 'product' again,
    #       delete all previous bid details and overwrite with the new one
    if(line[0] == "B"):
        bidder, product, price = line[1], line[2], int(line[3])
        # If that 'bidder' bid on the same 'product' again, delete all previous bid details first
        if(product in products_details and bidder in bidder_name):
            # Create new list of tuples which don't have 'bidder' name in each tuple
            new_details = []
            for t_bidder, t_price in products_details[product]:
                if(t_bidder != bidder):
                    new_details.append((t_bidder, t_price))
            # Change value in the 'products_details' dictionary
            products_details[product] = new_details
        
        # Add bidding details in a dictionary
        if(product not in products_details):
            products_details[product] = [(bidder, price)]
        else:
            products_details[product].append((bidder,price))
        
        # Add bidder details
        if(bidder not in bidder_name):
            bidder_name.append(bidder)
        if(bidder not in bidder_money):
            bidder_money[bidder] = 0
        if(bidder not in bidder_product):
            bidder_product[bidder] = []
    
    # Command: Withdraw (W)
    # This function remove all tuple (Bidder,Price) with the 'bidder' name in the dictionary 'products_details'
    elif(line[0] == "W"):
        bidder, product = line[1], line[2]
        # Manage bidding details in a dictionary
        # Remove all (Bidder,Price) with the 'bidder' name 
        # Ignore if 'product' is not exist in 'product_details' and 'bidder' is not exist in 'bidder_name'
        if(product in products_details and bidder in bidder_name):
            # Create new list of tuples which don't have 'bidder' name in each tuple
            new_details = []
            for t_bidder, t_price in products_details[product]:
                if(t_bidder != bidder):
                    new_details.append((t_bidder, t_price))
            # Change value in the 'products_details' dictionary
            products_details[product] = new_details

# Sort all bidder name in alphabetical order
bidder_name.sort()

# Find winning bidder and price of each product
for product, details in products_details.items():
    # Find maximum price
    max_price = 0
    for bidder, price in details:
        if(price > max_price):
            max_price = price
    # Find winning bidder and update bidder data in 'bidder_money' and 'bidder_product' dictionary
    for bidder, price in details:
        if(price == max_price):
            bidder_money[bidder] += price
            bidder_product[bidder].append(product)
            break

# Sort the product in 'bidder_product' in alphabetical order
for bidder, product_list in bidder_product.items():
    bidder_product[bidder] = sorted(product_list)

# Output
for bidder in bidder_name:
    # If that bidder doesn't buy anything
    if(len(bidder_product[bidder]) == 0):
        print(bidder + ":" + " $0")
    else:
        print(bidder + ":" + " $" + str(bidder_money[bidder]) + " -> " + " ".join(bidder_product[bidder]))