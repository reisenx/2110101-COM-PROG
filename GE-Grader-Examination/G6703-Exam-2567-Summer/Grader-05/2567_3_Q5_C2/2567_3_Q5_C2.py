# --------------------------------------------------
# File Name : 2567_3_Q5_C2.py
# Problem   : Top Sales Hour
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Initialize a dictionary to store sales by hour
hourly_sales = {}

while True:
    # Read input until "END" is encountered
    data = input().strip().split()
    if data == ["END"]:
        break

    # Extract hour and sale amount from the input
    sale = float(data[3])
    hour = data[2].split(":")[0]

    # Add the sale amount to the corresponding hour in the dictionary
    if hour not in hourly_sales:
        hourly_sales[hour] = 0.0
    hourly_sales[hour] += sale

# Initialize variables to find the hour with the highest sales
top_hour = ""
top_sale = 0.0

# Find the hour with the highest sales
for hour, sale in hourly_sales.items():
    if sale > top_sale:
        top_sale = sale
        top_hour = hour

# Output the hour with the highest sales
print(top_hour, round(top_sale, 2))
