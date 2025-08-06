<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Faculty Code ★ (
      <a href="https://drive.google.com/file/d/1gaO4DP7RnEK3iSsQxbygcjpM3MopJDBe/view?usp=drive_link">
        <code>03_If_01</code>
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
# File Name : 03_If_01.py
# Problem   : Faculty Code
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# List of valid faculty codes
FACULTIES = [
    "01",
    "02",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "51",
    "53",
    "55",
    "58",
]

# Input faculty code
code = input().strip()

# Check if the code is valid
if code in FACULTIES:
    print("OK")
else:
    print("Error")
```
