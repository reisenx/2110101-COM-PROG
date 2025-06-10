# --------------------------------------------------
# File Name : 02_StrList_04.py
# Problem   : N Digits
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input a number
num = input().strip()

# Input number of digits
N = int(input())

# Output the number with leading zeros if N > digits in num
print("0" * max(N - len(num), 0) + num)
