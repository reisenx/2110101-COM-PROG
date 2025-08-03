# --------------------------------------------------
# File Name : 2567_1_Q1_A3-W.py
# Problem   : Sequence with Ellipsis
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input start, stop, and step of the sequence
start, stop, step = [int(e) for e in input().split()]

# Initialize the number of elements in the sequence
n = 0
# Calculate in case step is positive
if step > 0:
    n = max(0, (stop - start + step - 1) // step)
# Calculate in case step is negative
elif step < 0:
    n = max(0, (stop - start + step + 1) // step)

# If the number of elements is zero
if n == 0:
    print("No data")

# If the number of elements is less than or equal to 5
elif n <= 5:
    # Directly find the numbers in the sequence
    numbers = []
    for num in range(start, stop, step):
        numbers.append(str(num))
    # Output the numbers in the sequence
    print(", ".join(numbers))

# If the number of elements is greater than 5
elif n > 5:
    # Calculate the first two numbers
    first_num = start
    second_num = start + step

    # Calculate the last two numbers
    before_last_num = start + (n - 2) * step
    last_num = start + (n - 1) * step

    # Output the sequence with ellipsis
    print(f"{first_num}, {second_num}, ..., {before_last_num}, {last_num}")
