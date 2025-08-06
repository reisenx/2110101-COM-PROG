<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Flowchart 03 ★★★ (
      <a href="https://drive.google.com/file/d/1h9FVdIoXd1Sew3hEIA2HOZn4YEAuH7Zz/view?usp=drive_link">
        <code>P1_Flowchart_03</code>
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
# File Name : P1_Flowchart_03.py
# Problem   : Part-I Flowchart 03
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

import math

x = input().split()
a, b, c, d = int(x[0]), int(x[1]), int(x[2]), int(x[3])

if a == 1:
    c, d = d, c

    if b == 1:
        c = c + d
    elif b == 2:
        c = c - d
    elif b != 3:
        c = c + (c**d)
    else:
        c = c / d

    a = (d + math.sqrt((c / b) ** 3 + d)) / (2 + b * d)

else:
    if a == 2:
        if b > 1:
            c = c + d
        if b > 2:
            c = c / d
        if b > 3:
            c = c + (c**d)
        else:
            a = math.log10(c)

    else:
        while a > d:
            a = a - 2

            if a < b:
                break
            else:
                c = c + a

print(a, b, c, d)
```
