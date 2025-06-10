# --------------------------------------------------
# File Name : 02_StrList_05.py
# Problem   : Weekly Sales
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input weekly sales data
sales = input().strip().split()

# Output the total sales for the week
print(
    int(sales[0])
    + int(sales[1])
    + int(sales[2])
    + int(sales[3])
    + int(sales[4])
    + int(sales[5])
    + int(sales[6])
)
