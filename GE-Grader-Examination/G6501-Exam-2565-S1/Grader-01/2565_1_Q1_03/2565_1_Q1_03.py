# --------------------------------------------------
# File Name : 2565_1_Q1_03.py
# Problem   : Simple Expression Calculator
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

# Input equation and add spaces before operators
equation = ""
for char in input().split():
    if char in "+-":
        equation += " "
    equation += char

# Split the equation string into numbers
numbers = []
for num in equation.split():
    numbers += [int(num)]

# Calculate the sum of the numbers and print the result
print(sum(numbers))
