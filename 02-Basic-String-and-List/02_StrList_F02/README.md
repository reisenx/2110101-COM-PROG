<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Arabic Numerals (Function) ★ (
      <a href="https://drive.google.com/file/d/19JhFGiZLYESRmaPoLqC4-yg7ibpilvdB/view?usp=drive_link">
        <code>02_StrList_F02</code>
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
# File Name : 02_StrList_F02.py
# Problem   : Arabic Numerals (Function)
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


# Function to convert a number to its string representation
def number_name(num):
    return NUMBERS[int(num)]


# Execute the input string as code
exec(input())
```
