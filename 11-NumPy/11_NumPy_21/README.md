<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Slicing and Element-wise Operation ★★ (
      <a href="https://drive.google.com/file/d/1w5w0mILaevnnSUQsMPd8ELhiGT-w-QF8/view?usp=drive_link">
        <code>11_NumPy_21</code>
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
# File Name : 11_Numpy_21.py
# Problem   : Slicing and Element-wise Operation
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

import numpy as np


# Sum every two rows of a 2D array
def sum_2_rows(matrix):
    return matrix[::2] + matrix[1::2]


# Split a 2D array into left and right halves, and sum the elements in each half
def sum_left_right(matrix):
    mid = matrix.shape[1] // 2
    return matrix[:, :mid] + matrix[:, mid:]


# Split a 2D array into upper and lower halves, and sum the elements in each half
def sum_upper_lower(matrix):
    mid = matrix.shape[0] // 2
    return matrix[:mid] + matrix[mid:]


# Split a 2D array into four quadrants and sum the elements in each quadrant
def sum_4_quadrants(matrix):
    mid_row = matrix.shape[0] // 2
    mid_col = matrix.shape[1] // 2
    q1 = matrix[:mid_row, :mid_col]
    q2 = matrix[:mid_row, mid_col:]
    q3 = matrix[mid_row:, :mid_col]
    q4 = matrix[mid_row:, mid_col:]
    return q1 + q2 + q3 + q4


# Sum every four cells in a 2D array by grouping them into 2x2 blocks
def sum_4_cells(matrix):
    return matrix[::2, ::2] + matrix[::2, 1::2] + matrix[1::2, ::2] + matrix[1::2, 1::2]


# Count the number of leap years in a given array of years
def count_leap_years(years):
    y = years - 543
    return np.sum((y % 400 == 0) | ((y % 100 != 0) & (y % 4 == 0)))


# Execute an input string as code
exec(input().strip())
```
