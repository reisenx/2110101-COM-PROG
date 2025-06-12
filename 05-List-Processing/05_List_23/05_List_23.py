# --------------------------------------------------
# File Name : 05_List_23.py
# Problem   : Third Closest
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input number of points
n = int(input())

# Input points
points = []
for order in range(n):
    x, y = [float(num) for num in input().split()]
    # Calculate distance from origin
    distance = (x**2 + y**2) ** 0.5
    # Store point with its distance and order
    points.append([distance, order + 1, x, y])

# Sort points by distance from origin
points.sort()

# Output the third closest point
order, x, y = points[2][1:]
print(f"#{order}: {(x, y)}")

