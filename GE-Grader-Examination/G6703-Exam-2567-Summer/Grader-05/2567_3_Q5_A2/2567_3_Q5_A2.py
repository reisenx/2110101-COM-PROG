# --------------------------------------------------
# File Name : 2567_3_Q5_A2.py
# Problem   : Computer Price 2
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Constants for computer components amount and types
COMPONENT_AMOUNT = 5
COMPONENT_TYPES = ["A", "B", "C", "D", "E"]

# Input each component's price
component_prices = [int(price) for price in input().split()]

component_total_price = [0] * COMPONENT_AMOUNT

all_computers = ""
while True:
    # Input room and its computer components until "END" is entered
    data = input().split()
    if data == ["END"]:
        break

    # Extract room name and computer components from input
    room = data[0]
    computers = data[1]

    # Add the current room's computers to the total string
    all_computers += computers

# Calculate the total price for each component type
for i in range(COMPONENT_AMOUNT):
    component_count = all_computers.count(COMPONENT_TYPES[i])
    component_total_price[i] = component_count * component_prices[i]

# Find and output the component with the maximum total price
idx = component_total_price.index(max(component_total_price))
print(COMPONENT_TYPES[idx], component_total_price[idx])
