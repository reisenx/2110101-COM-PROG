# --------------------------------------------------
# File Name : 2567_1_Q2_A2.py
# Problem   : Positive Real Number to Continued Fraction
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input value and maximum number of terms
data = input().strip().split()
initial_value = float(data[0])
max_terms_amount = int(data[1])

# Initialize the list to store terms and the current value
terms = []
current_value = initial_value

# Generate terms
for _ in range(max_terms_amount):
    # Separate the integer and decimal parts of the current value
    integer_part = int(current_value)
    decimal_part = current_value - integer_part

    # Append the integer part to the terms list
    terms.append(str(integer_part))

    # If the decimal part is less than 1e-10, break the loop
    if decimal_part < 1e-10:
        break

    # Update the current value to be the reciprocal of the decimal part
    current_value = 1 / decimal_part

# Output the terms
print(", ".join(terms))
