<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Flowchart 01 ★★ (
      <a href="https://drive.google.com/file/d/1l07PXjTYDAtB-47kj5TYaND1fjoN4aNf/view?usp=drive_link">
        <code>03_If_003</code>
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
# File Name : 03_If_003.py
# Problem   : Flowchart 01
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

a, b, c, d = [int(e) for e in input().split()]

if a > b:
    a, b = b, a

    if not d >= a:
        c = c + a
    else:
        if c > d:
            c = c - a

    b = a + c + d
else:
    if c > a >= b:
        d = d + a

    if d > c:
        b = b + 2
    else:
        b = 2 * b

print(a, b, c, d)
=
```
