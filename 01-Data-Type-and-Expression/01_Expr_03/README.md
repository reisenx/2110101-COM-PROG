<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    An Expression ★★ (
      <a href="https://drive.google.com/file/d/1QjFbvlGZVW_DvMut1K-ZNRXlswoMD_Lt/view?usp=drive_link">
        <code>01_Expr_03</code>
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
# File Name : 01_Expr_03.py
# Problem   : An Expression
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math

# Calculate numerator and denominator of a fraction
numerator = (
    math.pi
    - (math.factorial(10) / (8**8))
    + (math.log(9.7)) ** ((7 / math.sqrt(71)) - math.sin(math.radians(40)))
)
denominator = 1.2 ** (2.3 ** (1 / 3))

# Output
# Round the result to 6 decimal places
print(round(numerator / denominator, 6))
```
