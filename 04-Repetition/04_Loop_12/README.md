<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Zig Zag 1 ★★ (
      <a href="https://drive.google.com/file/d/1qVnA8Sd9Yx741Ud-dvpnS1oX8wLMuh4F/view?usp=drive_link">
        <code>04_Loop_12</code>
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
# File Name : 04_Loop_12.py
# Problem   : Zig Zag 1
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input number of rows
n = int(input())

# Initialize lists
a = []
b = []

# Loop to read input values
for i in range(n):
    x, y = [int(e) for e in input().split()]
    if i % 2 == 0:
        a += [x]
        b += [y]
    else:
        a += [y]
        b += [x]

# Output the results
cmd = input().strip()
if cmd == "Zig-Zag":
    print(min(a), max(b))
elif cmd == "Zag-Zig":
    print(min(b), max(a))
```
