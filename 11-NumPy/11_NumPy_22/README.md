<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Outer Product ★★ (
      <a href="https://drive.google.com/file/d/1xqJl_9dvPZ2AvS6nRSVAnRTCY1PbMId7/view?usp=drive_link">
        <code>11_NumPy_22</code>
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
# File Name : 11_Numpy_22.py
# Problem   : Outer Product
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

import numpy as np


# Calculate the multiplication table of size rows x cols
def mult_table(rows, cols):
    row = np.arange(1, rows + 1).reshape(-1, 1)
    col = np.arange(1, cols + 1)
    return row * col


# Execute an input string as code
exec(input().strip())
```
