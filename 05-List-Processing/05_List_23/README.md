<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Third Closet ★★ (
      <a href="https://drive.google.com/file/d/1qCZ0wgD0tv7KWyG36SdAVo_qwJY7flCR/view?usp=drive_link">
        <code>05_List_23</code>
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
# File Name : 05_List_23.py
# Problem   : Third Closest
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input number of points
n = int(input())

# Input points
points = []
for order in range(n):
    x, y = [float(num) for num in input().split()]
    # Calculate distance from origin
    distance = (x**2 + y**2) ** 0.5
    # Store point with its distance and order
    points.append([distance, order + 1, x, y])

# Sort points by distance from origin
points.sort()

# Output the third closest point
order, x, y = points[2][1:]
print(f"#{order}: {(x, y)}")
```
