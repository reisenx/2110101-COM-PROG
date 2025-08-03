# --------------------------------------------------
# File Name : 2567_3_Q4_A2.py
# Problem   : Computer Price
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Constants for computer components amount and types
COMPONENT_AMOUNT = 5
COMPONENT_TYPES = ["A", "B", "C", "D", "E"]

# Input each component's price
component_prices = [int(price) for price in input().split()]

# Initialize the maximum price and corresponding room
max_price_room = [0, "room"]

while True:
    # Input room and its computer components until "END" is entered
    data = input().split()
    if data == ["END"]:
        break

    # Extract room name and computer components from input
    room = data[0]
    computers = data[1]

    # Initialize total price for the current room
    total_price = 0

    # Calculate the total price of components in the room
    for i in range(COMPONENT_AMOUNT):
        component_count = computers.count(COMPONENT_TYPES[i])
        total_price += component_count * component_prices[i]

    # Update the maximum price and room if the current total price is higher
    if total_price > max_price_room[0]:
        max_price_room = [total_price, room]

# Output the room with the maximum total price
print(max_price_room[1])
