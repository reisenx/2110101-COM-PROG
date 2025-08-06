<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Missing Digits ★ (
      <a href="https://drive.google.com/file/d/1TQnGUUCvf7KxZRCT-Q9DLiA3YMbMtkW6/view?usp=drive_link">
        <code>05_List_11</code>
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
# File Name : 05_List_11.py
# Problem   : Missing Digits
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input text
text = input().strip()

# Initialize a list of missing digits
missing_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Remove digits found in the input text
for char in text:
    if char in missing_digits:
        missing_digits.remove(char)

# Output the missing digits
if len(missing_digits) > 0:
    print(",".join(missing_digits))
else:
    print("None")
```
