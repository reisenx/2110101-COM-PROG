<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Quadratic Root ★ (
      <a href="https://drive.google.com/file/d/1t3sUo80oVwNc3rVWCmbVgyO69tKfFXiO/view?usp=drive_link">
        <code>01_Expr_02</code>
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
# File Name : 01_Expr_02.py
# Problem   : Quadratic Root
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math

# Input a, b and c as float
a = float(input())
b = float(input())
c = float(input())

# Calculate roots of the equation ax^2 + bx + c
x1 = (-1 * b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
x2 = (-1 * b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)

# Output
# Round the result to 3 decimal places
print(round(x1, 3), round(x2, 3))
```
