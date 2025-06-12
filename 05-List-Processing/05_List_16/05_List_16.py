# --------------------------------------------------
# File Name : 05_List_16.py
# Problem   : Collatz
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input numbers
num = int(input())

# Initialize the Collatz sequence list
collatz = [str(num)]

# Generate the Collatz sequence
while num != 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = 3 * num + 1
    collatz.append(str(num))

# Output the Collatz sequence
print("->".join(collatz[-15:]))
