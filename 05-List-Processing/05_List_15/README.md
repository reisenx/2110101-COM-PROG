<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Unique Count ★★ (
      <a href="https://drive.google.com/file/d/15BrwiOGvTgNx3yN0tho9532OSx83o4YG/view?usp=drive_link">
        <code>05_List_15</code>
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
# File Name : 05_List_15.py
# Problem   : Unique Count
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input numbers and sort them in ascending order
numbers = [int(num) for num in input().split()]
numbers.sort()

# Find all unique numbers
unique_numbers = [numbers[0]]
for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1]:
        unique_numbers.append(numbers[i])

# Output
print(len(unique_numbers))
print(unique_numbers[:10])
```
