<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Bisection Log 10 ★☆ (
      <a href="https://drive.google.com/file/d/1kxFsi7BjNGh9YDjNnzYRKDESZPJ2eX0S/view?usp=drive_link">
        <code>04_Loop_02</code>
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
# File Name : 04_Loop_02.py
# Problem   : Bisection Log 10
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input a number
num = float(input())

# Initialize variables
lower = 0
upper = num
x = (lower + upper) / 2

# Bisection method
while abs(num - 10**x) > (10**-10) * max(num, 10**x):
    if 10**x > num:
        upper = x
    else:
        lower = x
    x = (lower + upper) / 2

# Output the result
print(round(x, 6))
```
