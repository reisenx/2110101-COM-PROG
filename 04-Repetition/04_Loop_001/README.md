<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Birthday Paradox (Flowchart) ★★ (
      <a href="https://drive.google.com/file/d/1Y9xwtuKQuA9ivybBNBocjLk1bMhSNBod/view?usp=drive_link">
        <code>04_Loop_001</code>
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
# File Name : 04_Loop_001.py
# Problem   : Birthday Paradox (Flowchart)
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

p = float(input())

k = 1
t = 1

t = (t * (365 - k + 1)) / 365

while t > 1 - p:
    k += 1
    t = (t * (365 - k + 1)) / 365

print(k)
```
