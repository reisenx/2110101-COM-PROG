# --------------------------------------------------
# File Name : 10_TSD_12.py
# Problem   : Union Intersection
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input number of sets
n = int(input())

# Initialize sets for union and intersection
union = set()
intersection = set()

# Process each set
for _ in range(n):
    # Read the current set of integers
    current_set = {int(num) for num in input().split()}

    # Update union and intersection
    if len(union) == 0:
        union = current_set
        intersection = current_set
    else:
        union |= current_set
        intersection &= current_set

# Output length of union and intersection
print(len(union))
print(len(intersection))
