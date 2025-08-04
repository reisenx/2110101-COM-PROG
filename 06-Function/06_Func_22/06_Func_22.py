# --------------------------------------------------
# File Name : 06_Func_22.py
# Problem   : Distance
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Calculate the distance between two points (x1, y1) and (x2, y2)
def distance1(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# Calculate the distance between two points p1 and p2
# p1 and p2 are lists in the format [x, y]
def distance2(point_01, point_02):
    x1, y1 = point_01
    x2, y2 = point_02
    return distance1(x1, y1, x2, y2)


# Calculate the distance between two circles c1 and c2
# c1 and c2 are lists in the format [x, y, r]
# where x and y are the center coordinates and r is the radius
# # It returns a tuple (distance, is_overlapping)
def distance3(circle_01, circle_02):
    x1, y1, radius_01 = circle_01
    x2, y2, radius_02 = circle_02
    dist = distance1(x1, y1, x2, y2)

    is_overlapping = dist <= radius_01 + radius_02
    return dist, is_overlapping


# Calculate the perimeter of a polygon defined by a list of points
# points is a list of lists in the format [[x1, y1], [x2, y2], ...]
def perimeter(points):
    total = 0.0
    for i in range(1, len(points)):
        total += distance2(points[i - 1], points[i])
    total += distance2(points[-1], points[0])
    return total


# Execute a input string as code
exec(input().strip())
