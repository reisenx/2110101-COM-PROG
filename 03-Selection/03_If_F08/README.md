<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Day of Year (Function) ★★ (
      <a href="https://drive.google.com/file/d/1RVKPo_LIe7Rztuj5s4-bM5jrY8qpN_vG/view?usp=drive_link">
        <code>03_If_F08</code>
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
# File Name : 03_If_F08.py
# Problem   : Day of Year (Function)
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------

# List of total days in each month
TOTAL_DAYS = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]


def day_of_year(d, m, y):
    # Convert the year to the year in the Gregorian calendar
    y = y - 543

    # Output the day of the year
    if m <= 2:
        return 31 * (m - 1) + d
    else:
        # Check if the year is a leap year
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            return TOTAL_DAYS[m - 2] + d + 1
        else:
            return TOTAL_DAYS[m - 2] + d


# Execute the input string as code
exec(input())
```
