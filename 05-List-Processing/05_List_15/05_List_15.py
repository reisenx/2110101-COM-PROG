# --------------------------------------------------
# File Name : 05_List_15.py
# Problem   : Unique Count
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input numbers and sort them in ascending order
numbers = [int(num) for num in input().split()]
numbers.sort()

# Find all unique numbers
unique_numbers = [numbers[0]]
for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1]:
        unique_numbers.append(numbers[i])

# Output
print(len(unique_numbers))
print(unique_numbers[:10])
