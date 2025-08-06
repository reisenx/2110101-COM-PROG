<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Median 5 (Flowchart) ★ (
      <a href="https://drive.google.com/file/d/1d5UnfelndV7lFHFTRvd7f7u0Ydoza1Be/view?usp=drive_link">
        <code>03_If_001</code>
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
# File Name : 03_If_001.py
# Problem   : Median 5 (Flowchart)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a > b:
    a, b = b, a

if c > d:
    c, d = d, c

if a > c:
    b, d = d, b
    c = a

a = e

if a > b:
    a, b = b, a

if c > a:
    b, d = d, b
    a = c

if a > d:
    print(d)
else:
    print(a)
```
