<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Parentheses ★ (
      <a href="https://drive.google.com/file/d/1a47SEUtNOaMysUlkEDMwawdue-2c9A4A/view?usp=drive_link">
        <code>04_Loop_04</code>
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
# File Name : 04_Loop_04.py
# Problem   : Parentheses
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input text
text = input().strip()

# Construct new text by replacing parentheses
new_text = ""
for char in text:
    if char == "(":
        new_text += "["
    elif char == ")":
        new_text += "]"
    elif char == "[":
        new_text += "("
    elif char == "]":
        new_text += ")"
    else:
        new_text += char

# Output the new text
print(new_text)
```
