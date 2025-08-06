<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    US Date ★ (
      <a href="https://drive.google.com/file/d/1nSQvpgBMvO2dFyuGitJZUQQvNWmx34Ko/view?usp=drive_link">
        <code>02_StrList_03</code>
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
# File Name : 02_StrList_03.py
# Problem   : US Date
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# List of month names in English
MONTH = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# Input a date in the format DD/MM/YYYY
date = input().strip()

# Split the input date into day, month, and year
d, m, y = date.split("/")

# Output the date in the format "Month Day, Year"
print(f"{MONTH[int(m) - 1]} {d}, {y}")
```
