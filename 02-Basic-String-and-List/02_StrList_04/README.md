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
# Date      : 2025-08-09
# --------------------------------------------------

# Input a number
number = input().strip()

# Input number of digits to display
display_digits = int(input())

# Calculate leading zeros if the number of digits to display is greater
leading_zeros = max(0, display_digits - len(number))

# Output the number with leading zeros
print(f"{'0' * leading_zeros}{number}")
```
