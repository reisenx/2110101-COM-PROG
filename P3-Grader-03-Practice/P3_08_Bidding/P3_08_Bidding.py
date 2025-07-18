# --------------------------------------------------
# File Name : P3_08_Bidding.py
# Problem   : Part-III Bidding
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# Initialize dictionaries to store products and users
products = {}
users = {}


# Bid on a product by a user with a specified price and time
def bid_product(user: str, product: str, price: int, time: int) -> None:
    # If the product or user does not exist, initialize them
    if product not in products:
        products[product] = {}
    if user not in users:
        users[user] = {"money": 0, "products": []}
    # Add or update the user's bid for the product
    products[product][user] = [price, time]


# Withdraw a user's bid for a product
def withdraw_product(user: str, product: str) -> None:
    # Ignore if the product or user does not exist
    if product not in products or user not in products[product]:
        return
    # Remove the user's bid for the product
    del products[product][user]


# Get the winner of a product based on the highest bid
def get_winner(product: str) -> tuple[str, int]:
    # If the product does not exist or has no bids
    if product not in products or len(products[product]) == 0:
        return "", -1
    # Sort the bids for the product by price (descending) and time (ascending)
    product_ranks = []
    for user, [price, time] in products[product].items():
        product_ranks.append([-price, time, user])
    product_ranks.sort()
    # The winner is the user with the highest bid
    price, user = -product_ranks[0][0], product_ranks[0][2]
    return user, price


# Update all users with the winning bids for each product
def update_all_users() -> None:
    # Iterate through each product to determine the winner
    for product, _ in products.items():
        user, price = get_winner(product)
        # Update the user's money and products if they won
        if price > 0:
            users[user]["money"] += price
            users[user]["products"].append(product)


# Report the final results of all users
def report() -> None:
    # Initialize a list to store the result of each user
    results = []
    # Iterate through each user and format their results
    for user, details in users.items():
        result = f"{user}: ${details['money']}"
        # If the user has won products
        if len(details["products"]) > 0:
            result += f" -> {' '.join(sorted(details['products']))}"
        results.append(result)
    # Sort the results alphabetically by user name
    results.sort()
    # Print the final results
    print("\n".join(results))


# Main function to read commands and process bids
def main() -> None:
    # Read the number of commands
    n = int(input())
    for time in range(n):
        line = input().strip().split()
        command, user, product = line[0], line[1], line[2]
        # Bid (B) command
        if command == "B":
            price = int(line[3])
            bid_product(user, product, price, time)
        # Withdraw (W) command
        elif command == "W":
            withdraw_product(user, product)
    # After processing all commands, update user data and report results
    update_all_users()
    report()


# Run the main function to start the bidding process
main()
