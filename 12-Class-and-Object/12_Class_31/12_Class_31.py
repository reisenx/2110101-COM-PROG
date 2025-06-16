# --------------------------------------------------
# File Name : 12_Class_31.py
# Problem   : Point in Rectangle
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------


class Point:
    # __init__ method
    # Initialize the 'Point' object with x and y coordinates
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    # __str__ method
    # Convert the 'Point' object to a string representation
    def __str__(self) -> str:
        return str((self.x, self.y))


class Rect:
    # __init__ method
    # Initialize the 'Rect' object with two points: lower left and upper right
    def __init__(self, p1: "Point", p2: "Point") -> None:
        self.lower_left = p1
        self.upper_right = p2

    # area method
    # Calculate the area of the rectangle
    def area(self) -> int:
        x1, y1 = (self.lower_left).x, (self.lower_left).y
        x2, y2 = (self.upper_right).x, (self.upper_right).y
        return (x2 - x1) * (y2 - y1)

    # contains method
    # Check if a point is inside the rectangle
    def contains(self, p: "Point") -> bool:
        x1, y1 = (self.lower_left).x, (self.lower_left).y
        x2, y2 = (self.upper_right).x, (self.upper_right).y
        x, y = p.x, p.y
        return x1 <= x <= x2 and y1 <= y <= y2


# Input lower left and upper right points of the rectangle
x1, y1, x2, y2 = [int(e) for e in input().split()]
# Create a rectangle object
lower_left = Point(x1, y1)
upper_right = Point(x2, y2)
rect = Rect(lower_left, upper_right)

# Output the area of the rectangle
print(rect.area())

# Input number of points to check
m = int(input())
# For each point, check if it is inside the rectangle
for _ in range(m):
    x, y = [int(e) for e in input().split()]
    p = Point(x, y)
    print(rect.contains(p))
