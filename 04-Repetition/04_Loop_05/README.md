<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Count Word ★ (
      <a href="https://drive.google.com/file/d/130yj5AwIA6seHeFRHLKiJdOnV5j98Lc_/view?usp=drive_link">
        <code>04_Loop_05</code>
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
# File Name : 04_Loop_05.py
# Problem   : Count Word
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input interested word
key = input().strip()

# Input text
text = input().strip()

# Remove symbol from the text
new_text = ""
for char in text:
    if char in ['"', "(", ")", ",", ".", "'"]:
        new_text += " "
    else:
        new_text += char

# Split the new text into words
words = new_text.split()

# Count the occurrences of the interested word
count = 0
for word in words:
    if word == key:
        count += 1

# Output the count
print(count)
```
