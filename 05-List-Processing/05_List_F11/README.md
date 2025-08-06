<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Missing Digits (Function) ★ (
      <a href="https://drive.google.com/file/d/1_WW9weWNWDnFKjGxdwiD39pUz6jX-JxT/view?usp=drive_link">
        <code>05_List_F11</code>
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
# File Name : 05_List_F11.py
# Problem   : Missing Digits (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


def missing_digits(text):
    # Initialize a list to track found digits
    found_digits = [False] * 10

    # Iterate through each character in the input text
    for char in text:
        if char.isdigit():
            digit = int(char)
            found_digits[digit] = True

    # Collect the missing digits
    missing = []
    for num in range(10):
        if not found_digits[num]:
            missing.append(num)

    # Return the missing digits
    return missing


# Execute the input string as code
exec(input())
```
