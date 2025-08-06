<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Day of Year ★★ (
      <a href="https://drive.google.com/file/d/1Y-dUBpKXE_nL5rr4VhvLC16gTVQh4iNN/view?usp=drive_link">
        <code>03_If_08</code>
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
# File Name : 03_If_08.py
# Problem   : Day of Year
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# List of total days in each month
TOTAL_DAYS = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

# Input the day, month, and year
d = int(input())
m = int(input())
y = int(input())

# Convert the year to the year in the Gregorian calendar
y -= 543

# Output the day of the year
if m <= 2:
    print((TOTAL_DAYS[0] * (m - 1)) + d)
else:
    # Check if the year is a leap year
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print(TOTAL_DAYS[m - 2] + d + 1)
    else:
        print(TOTAL_DAYS[m - 2] + d)
```
