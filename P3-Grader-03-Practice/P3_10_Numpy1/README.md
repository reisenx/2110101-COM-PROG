<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    NumPy Functions ★★★ (
      <a href="https://drive.google.com/file/d/11DYcIuGS3OW7Lmzh3iQ9qowKcyepHfQW/view?usp=drive_link">
        <code>P3_10_Numpy1</code>
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
# File Name : P3_10_Numpy1.py
# Problem   : Part-III NumPy Functions
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

import numpy as np


# Calculate percentage of equal elements between two arrays
# Return True if the percentage is greater than or equal to the target, otherwise False
def eq(a, b, target):
    percentage = np.mean(a == b) * 100
    return percentage >= target


# Get indexes of the closest points in a 2D array to a target point
def closest_point_indexes(points, target):
    # Calculate the distance from each point to the target
    distance_x = points[:, 0] - target[0]
    distance_y = points[:, 1] - target[1]
    distances = ((distance_x**2) + (distance_y**2)) ** 0.5
    # Find the indices of the points with the minimum distance
    indices = np.arange(len(distances))[distances == np.min(distances)]
    return indices


# Count the number of inversions in an array
# A pair (i, j) is an inversion if i < j and A[i] > A[j]
def number_of_inversions(a):
    count = 0
    for i in range(len(a)):
        count += np.sum(a[i] > a[i + 1 :])
    return count


# Execute an input string as code
exec(input().strip())
```
