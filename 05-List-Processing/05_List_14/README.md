<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Peaks ★ (
      <a href="https://drive.google.com/file/d/1RgBxFsXsObus6cQxwf08QHdydE53CuDC/view?usp=drive_link">
        <code>05_List_14</code>
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
# File Name : 05_List_14.py
# Problem   : Peaks
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input a list of numbers
numbers = [float(num) for num in input().split()]

# Count the number of peaks
peak_count = 0
for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        peak_count += 1

# Output the number of peaks
print(peak_count)
```
