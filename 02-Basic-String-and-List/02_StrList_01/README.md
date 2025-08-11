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
# Date      : 2025-08-09
# --------------------------------------------------

# Input citizen ID
citizen_id = input().strip()

# Calculate the last digit based on the first 12 digits
last_digit = (
    13 * int(citizen_id[0])
    + 12 * int(citizen_id[1])
    + 11 * int(citizen_id[2])
    + 10 * int(citizen_id[3])
    + 9 * int(citizen_id[4])
    + 8 * int(citizen_id[5])
    + 7 * int(citizen_id[6])
    + 6 * int(citizen_id[7])
    + 5 * int(citizen_id[8])
    + 4 * int(citizen_id[9])
    + 3 * int(citizen_id[10])
    + 2 * int(citizen_id[11])
)
last_digit = (11 - (last_digit % 11)) % 10

# Output the formatted ID
print(citizen_id[0], citizen_id[1:5], citizen_id[5:10], citizen_id[10:12], last_digit)
```
