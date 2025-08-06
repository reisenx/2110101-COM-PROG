<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Scalar and Array ★ (
      <a href="https://drive.google.com/file/d/1kd8NY1_YIXGCZkje78AvSlWdJuLAW6Nw/view?usp=drive_link">
        <code>11_NumPy_12</code>
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
# File Name : 11_Numpy_12.py
# Problem   : Scalar and Array
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

import numpy as np


# Convert Fahrenheit to Celsius
def toCelsius(fahrenheit):
    return (fahrenheit - 32) / 1.8


# Calculate Body Mass Index (BMI)
def BMI(weight_and_height):
    weight = weight_and_height[:, 0]
    height = weight_and_height[:, 1] / 100
    return weight / (height**2)


# Calculate the distance from a point to all points in an array
def distanceTo(point, all_points):
    distance_x = all_points[:, 0] - point[0]
    distance_y = all_points[:, 1] - point[1]
    return ((distance_x**2) + (distance_y**2)) ** 0.5


# Execute an input string as code
exec(input().strip())
```
