# --------------------------------------------------
# File Name : 05_List_13.py
# Problem   : Back and Front
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Initialize numbers list
numbers = []

# Input first set of numbers
n = int(input())
for _ in range(n):
    numbers.append(int(input()))

# Input second set of numbers
numbers += [int(num) for num in input().split()]

# Input the third set of numbers
while True:
    num = int(input())
    if num == -1:
        break
    numbers.append(num)

# Rearrange the numbers
rearranged_numbers = []
for i in range(len(numbers)):
    # Insert at the back first, then at the front
    if i % 2 == 0:
        rearranged_numbers.append(numbers[i])
    else:
        rearranged_numbers.insert(0, numbers[i])

# Output the rearranged numbers
print(rearranged_numbers)
