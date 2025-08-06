<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Next 15 Days (Flowchart) ★★ (
      <a href="https://drive.google.com/file/d/1GrvuJt4-An6P7JUJnEC1XjJx5QD10qkE/view?usp=drive_link">
        <code>03_If_002</code>
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
# File Name : 03_If_002.py
# Problem   : Next 15 Days (Flowchart)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

d, m, y = [int(e) for e in input().split()]

y = y - 543

n = 31

if m in [4, 6, 9, 11]:
    n = 30
else:
    if m == 2:
        n = 28
        if y % 400 == 0:
            n = 29
        if y % 4 == 0 and y % 100 != 0:
            n = 29

d = d + 15

if d > n:
    d = d - n
    m = m + 1

if m > 12:
    m = m - 12
    y = y + 1

y = y + 543

print(f"{d}/{m}/{y}")
```
