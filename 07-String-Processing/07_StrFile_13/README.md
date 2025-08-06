<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Camel Case ★ (
      <a href="https://drive.google.com/file/d/1qxebq9IQuZIsL7zibYSrSyVg3UQLRFbk/view?usp=drive_link">
        <code>07_StrFile_13</code>
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
# File Name : 07_StrFile_13.py
# Problem   : Camel Case
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input a text as lowercase string
text = input().strip().lower()

# Remove all symbols and split the text into words
new_text = ""
for char in text:
    if char.isalnum():
        new_text += char
    else:
        new_text += " "

# Convert all words to camel case
words = new_text.split()
for i in range(1, len(words)):
    words[i] = words[i][0].upper() + words[i][1:]

# Output the CamelCase string
print("".join(words))
```
