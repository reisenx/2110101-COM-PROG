<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Abbrev Num ★★ (
      <a href="https://drive.google.com/file/d/1mDTCZmWLDeGtuSMLp3g2CcJFYdxafpjL/view?usp=drive_link">
        <code>03_If_07</code>
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
# File Name : 03_If_07.py
# Problem   : Abbrev Num
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# List of symbols for abbreviations
SYMBOLS = ["", "K", "M", "B"]

# Input a number
num = float(input())

# Calculate the abbreviated number
n = 0
while num > 1000 and n < 3:
    num /= 1000
    n += 1

# Output the abbreviated number
if num < 10:
    print(f"{round(num, 1)}{SYMBOLS[n]}")
else:
    print(f"{round(num)}{SYMBOLS[n]}")
```
