<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Stirling Factorial ★ (
      <a href="https://drive.google.com/file/d/1k_Apd7ovMqxXhWhAIRw3j5fCApoWKLUG/view?usp=drive_link">
        <code>01_Expr_01</code>
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
# File Name : 01_Expr_01.py
# Problem   : Stirling Factorial
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math

# Input n
n = int(input())

# Calculate the lower bound of n!
lower = (
    math.sqrt(2 * math.pi) * n ** (n + (1 / 2)) * math.e ** (-n + (1 / (12 * n + 1)))
)
print(lower)

# Calculate the upper bound of n!
upper = math.sqrt(2 * math.pi) * n ** (n + (1 / 2)) * math.e ** (-n + (1 / (12 * n)))
print(upper)
```
