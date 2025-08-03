# --------------------------------------------------
# File Name : 2567_1_Q1_A2-W.py
# Problem   : Flowchart
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

import math

# Input
x, epsilon = [float(e) for e in input().split()]

# Initialize estimated value of cosine
cosine = 0
# Initialize term index
n = 0

# Loop until the term is less than epsilon
while True:
    # Calculate the term using Taylor series expansion
    term = (((-1) ** n) * (x ** (2 * n))) / math.factorial(2 * n)

    # Stop if the absolute value of the term is less than epsilon
    if abs(term) < epsilon:
        break

    # Add the term to the estimated value of cosine
    cosine += term

    # Increment the term index
    n += 1

# Output the estimated value of cosine rounded to 6 decimal places
print(round(cosine, 6))
