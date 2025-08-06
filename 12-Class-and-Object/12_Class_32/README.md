<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Rectangle Sorted by Area ★★★ (
      <a href="https://drive.google.com/file/d/14_CYL0hMMiWPds7FrDK4JLUAMASWH-vB/view?usp=drive_link">
        <code>12_Class_32</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**Solution**](#solution)

---

<div align="center">
  <h2>เฉลยอย่างละเอียดจะตามมาทีหลัง</h2>
</div>

---

# Solution

```python
# --------------------------------------------------
# File Name : 12_Class_32.py
# Problem   : Rectangle Sorted by Area
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------


class Point:
    # __init__ method
    # Initialize the 'Point' object with x and y coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __str__ method
    # Convert the 'Point' object to a string representation
    def __str__(self):
        return str((self.x, self.y))


class Rect:
    # __init__ method
    # Initialize the 'Rect' object with two points: lower left and upper right
    def __init__(self, point_01, point_02):
        self.lower_left = point_01
        self.upper_right = point_02

    # area method
    # Calculate the area of the rectangle
    def area(self):
        x1, y1 = (self.lower_left).x, (self.lower_left).y
        x2, y2 = (self.upper_right).x, (self.upper_right).y
        return (x2 - x1) * (y2 - y1)

    # __str__ method
    # Convert the 'Rect' object to a string representation
    def __str__(self):
        return f"{self.lower_left}-{self.upper_right}"

    # __lt__ method
    # Compare rectangles based on their area for sorting
    def __lt__(self, other):
        return self.area() < other.area()


# Input number of rectangles
n = int(input())

# Input rectangles and store them in a list
rectangles = []
for _ in range(n):
    x1, y1, x2, y2 = [int(e) for e in input().split()]
    rectangles.append(Rect(Point(x1, y1), Point(x2, y2)))

# Sort rectangles by area in ascending order
rectangles.sort()

# Output the rectangles in sorted order
for i in range(n):
    print(rectangles[i])
```
