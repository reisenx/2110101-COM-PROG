<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Arabic Numerals ★ (
      <a href="https://drive.google.com/file/d/19so7zJiFzwUmRbSAQhQPItIh2FfPMgkk/view?usp=drive_link">
        <code>02_StrList_02</code>
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
# File Name : 02_StrList_02.py
# Problem   : Arabic Numerals
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# List of string representations of numbers from 0 to 9
NUMBERS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

# Input a number (0-9)
num = int(input())

# Output the number and its string representation
print(f"{num} --> {NUMBERS[num]}")
```
