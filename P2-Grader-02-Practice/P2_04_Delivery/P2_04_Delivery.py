# --------------------------------------------------
# File Name : P2_04_Delivery.py
# Problem   : Part-II Delivery
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# List of days in each month for common and leap years
COMMON = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Delivery types and their corresponding days
DELIVERY = {"E": 1, "Q": 3, "N": 7, "F": 14}


# Check if the year is a leap year
def is_leap_year(year):
    return ((year - 543) % 400 == 0) or (
        (year - 543) % 100 != 0 and (year - 543) % 4 == 0
    )


# This function checks if the order is valid
def is_order_valid(o_id, o_type, day, month, year):
    # Case 1: Invalid order year
    if year < 2558:
        print(f"Error: {o_id} {o_type} {day} {month} {year} --> Invalid year")
        return False

    # Case 2: Invalid order month
    if month < 1 or month > 12:
        print(f"Error: {o_id} {o_type} {day} {month} {year} --> Invalid month")
        return False

    # Case 3: Invalid order date
    if (
        day < 1
        or (not is_leap_year(year) and day > COMMON[month - 1])
        or (is_leap_year(year) and day > LEAP[month - 1])
    ):
        print(f"Error: {o_id} {o_type} {day} {month} {year} --> Invalid date")
        return False

    # Case 4: Invalid delivery type
    if o_type not in DELIVERY:
        print(f"Error: {o_id} {o_type} {day} {month} {year} --> Invalid delivery type")
        return False

    # The order is valid
    return True


# This function adds the delivery days to the order date
def add_date(day, month, year, o_type):
    # Initialize total days in the year and the new date variables
    total_days = 0
    new_day, new_month, new_year = day, month, year
    # Add the delivery days to the order date and adjust the year
    if is_leap_year(year):
        total_days = sum(LEAP[: month - 1]) + day
        total_days += DELIVERY[o_type]
        if total_days > 366:
            new_year = year + 1
            total_days -= 366
    else:
        total_days = sum(COMMON[: month - 1]) + day
        total_days += DELIVERY[o_type]
        if total_days > 365:
            new_year = year + 1
            total_days -= 365

    # Determine the new month and day after adding delivery days
    for m in range(13):
        if is_leap_year(year):
            if total_days <= sum(LEAP[:m]):
                new_month = m
                new_day = total_days - sum(LEAP[: m - 1])
                break
        else:
            if total_days <= sum(COMMON[:m]):
                new_month = m
                new_day = total_days - sum(COMMON[: m - 1])
                break
    # Return the new date as a list [day, month, year]
    return [new_day, new_month, new_year]


# Input orders until "END" is entered
successful_orders = []
while True:
    # Read the order input
    order = input().strip().split()
    # Stop if "END" is entered
    if order[0] == "END":
        break

    # Extract order details
    o_id, o_type = order[:2]
    day, month, year = int(order[2]), int(order[3]), int(order[4])
    # Check if the order is valid
    if is_order_valid(o_id, o_type, day, month, year):
        # Add the delivery days to the order date
        day, month, year = add_date(day, month, year, o_type)
        # Append the successful order to the list
        successful_orders.append([year, month, day, o_id])

# Sort the successful orders by year, month, day, and ID
successful_orders.sort()

# Output the successful orders
for year, month, day, o_id in successful_orders:
    print(f"{o_id}: delivered on {day}/{month}/{year}")
