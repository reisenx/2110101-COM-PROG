<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Partition (Flowchart) ★★ (
      <a href="https://drive.google.com/file/d/17o5HGkHrFkwV8cdCDwyzej8z9jdYetMZ/view?usp=drive_link">
        <code>04_Loop_002</code>
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
# File Name : 04_Loop_002.py
# Problem   : Partition (Flowchart)
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

d = [int(e) for e in input().split()]

p = d[-1]
i = -1
j = 0
n = len(d)

while j < n - 1:
    if d[j] <= p:
        i += 1
        d[i], d[j] = d[j], d[i]
    j += 1

d[i + 1], d[-1] = d[-1], d[i + 1]

print(d)
```
