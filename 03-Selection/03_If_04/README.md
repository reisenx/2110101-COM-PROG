<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Mobile Number ★ (
      <a href="https://drive.google.com/file/d/1uZSbjfMcACfcXKunBZOUlSJ9o_u8f6dI/view?usp=drive_link">
        <code>03_If_04</code>
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
# File Name : 03_If_04.py
# Problem   : Mobile Number
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Constants
PHONE_DIGITS = 10
VALID_NUMBERS = ["06", "08", "09"]

# Input the mobile number
mobile_number = input().strip()

# Validate the mobile number
if len(mobile_number) == PHONE_DIGITS and mobile_number[:2] in VALID_NUMBERS:
    print("Mobile number")
else:
    print("Not a mobile number")
```
