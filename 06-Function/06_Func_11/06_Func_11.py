# --------------------------------------------------
# File Name : 06_Func_11.py
# Problem   : Binary Adder
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input numbers in binary format
numbers = [int(num, 2) for num in input().split()]

# Output the sum of the binary numbers
print(bin(sum(numbers))[2:])
