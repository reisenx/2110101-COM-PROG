<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Citizen ID ★ (
      <a href="https://drive.google.com/file/d/1rrNBkLxvvoBxibKoOMcDxNEgvrYXO6wv/view?usp=drive_link">
        <code>02_StrList_01</code>
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
# File Name : 02_StrList_01.py
# Problem   : Citizen ID
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input citizen ID
id = input()

# Calculate the last digit based on the first 12 digits
val = (
    13 * int(id[0])
    + 12 * int(id[1])
    + 11 * int(id[2])
    + 10 * int(id[3])
    + 9 * int(id[4])
    + 8 * int(id[5])
    + 7 * int(id[6])
    + 6 * int(id[7])
    + 5 * int(id[8])
    + 4 * int(id[9])
    + 3 * int(id[10])
    + 2 * int(id[11])
)
last_digit = (11 - (val % 11)) % 10

# Output the formatted ID
print(f"{id[0]} {id[1:5]} {id[5:10]} {id[10:12]} {last_digit}")
```
