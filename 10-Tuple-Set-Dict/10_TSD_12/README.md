<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Union Intersection ★ (
      <a href="https://drive.google.com/file/d/1oa1clo95mX24uYK4xUEI-aN3lxRzarnW/view?usp=drive_link">
        <code>10_TSD_12</code>
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
# File Name : 10_TSD_12.py
# Problem   : Union Intersection
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input number of sets
n = int(input())

# Initialize sets for union and intersection
union = set()
intersection = set()

# Process each set
for i in range(n):
    # Read the current set of integers
    current_set = {int(num) for num in input().split()}

    # Update union and intersection sets
    if i == 0:
        intersection |= current_set
    union |= current_set
    intersection &= current_set

# Output length of union and intersection
print(len(union))
print(len(intersection))
```
