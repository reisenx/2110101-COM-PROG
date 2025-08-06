# --------------------------------------------------
# File Name : 06_Func_23.py
# Problem   : Four Functions
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Convert a string into a list of integers
def make_int_list(numbers):
    return [int(num) for num in numbers.split()]


# Check if a number is odd
def is_odd(num):
    return num % 2 != 0


def odd_list(numbers):
    return [num for num in numbers if is_odd(num)]


# Calculate the sum of squares of a list of numbers
def sum_square(numbers):
    total = 0
    for num in numbers:
        total += num**2
    return total


# Execute a input string as code
exec(input().strip())
