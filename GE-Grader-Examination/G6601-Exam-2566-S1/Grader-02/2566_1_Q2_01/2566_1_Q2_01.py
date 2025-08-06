# --------------------------------------------------
# File Name : 2566_1_Q2_01.py
# Problem   : Outlier
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------


# Calculate the median of a list of sorted numbers
def get_median(numbers):
    n = len(numbers)
    if n % 2 == 1:
        return float(numbers[n // 2])
    return (numbers[(n // 2) - 1] + numbers[n // 2]) / 2.0


# Input the list of numbers and sort them in ascending order
numbers = [int(num) for num in input().split()]
numbers.sort()

# Split the list into two halves
n = len(numbers)
first_half = numbers[: n // 2]
second_half = numbers[-(n // 2) :]

# Calculate the IQR
q1 = get_median(first_half)
q3 = get_median(second_half)
iqr = q3 - q1

# Calculate the lower and upper bounds for outliers
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

# Find outliers in the list of numbers
outliers = []
for num in numbers:
    if num < lower_bound or num > upper_bound:
        outliers.append(num)

# Output
print(f"L = {lower_bound} U = {upper_bound}")
# Output the outliers if any, otherwise print "Not found"
if len(outliers) > 0:
    print(" ".join([str(num) for num in outliers]))
else:
    print("Not found")
