<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Logistic Regression ★ (
      <a href="https://drive.google.com/file/d/1NNc0lkUAzMbP7FX5Gp7vcLZzG6ODzMz9/view?usp=drive_link">
        <code>11_NumPy_13</code>
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
# File Name : 11_Numpy_13.py
# Problem   : Logistic Regression
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

import numpy as np


# Calculate the probability of a binary outcome using logistic regression
def p(x):
    logit = -3.98 + (0.1 * x[:, 0]) + (0.5 * x[:, 1])
    return 1 / (1 + np.exp(-logit))


# Execute an input string as code
exec(input().strip())
```
