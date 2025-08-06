<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    N Digits ★ (
      <a href="https://drive.google.com/file/d/1x9TSTjfAS4zqxaoHenatkl9PoeYzBxYE/view?usp=drive_link">
        <code>02_StrList_04</code>
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
# File Name : 02_StrList_04.py
# Problem   : N Digits
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input a number
num = input().strip()

# Input number of digits
display_digits = int(input())

# Output the number with leading zeros if display digits > digits in num
print("0" * max(display_digits - len(num), 0) + num)
```
