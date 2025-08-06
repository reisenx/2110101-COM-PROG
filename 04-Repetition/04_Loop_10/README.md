<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Bisection Log 10 [2] ★★ (
      <a href="https://drive.google.com/file/d/1JOiixtgL3MuR5bhipvUmAfFJpaPNRgSA/view?usp=drive_link">
        <code>04_Loop_10</code>
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
# File Name : 04_Loop_10.py
# Problem   : Bisection Log 10 [2]
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input a number
num = float(input())

# Initialize lower bound
lower = 0

# Calculate upper bound
upper = 0
temp = num
while temp > 0:
    temp //= 10
    upper += 1

# Initialize x as the midpoint
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
