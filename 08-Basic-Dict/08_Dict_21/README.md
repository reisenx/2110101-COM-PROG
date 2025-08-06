<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Character Count ★★ (
      <a href="https://drive.google.com/file/d/1eojT5SxU4rf77ntGiALT98hMyYlzkops/view?usp=drive_link">
        <code>08_Dict_21</code>
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
# File Name : 08_Dict_21.py
# Problem   : Character Count
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input text and lowercase it
text = input().strip().lower()

# Initialize a dictionary to count characters
char_count = {}

# Count each character in the text
for char in text:
    if char.isalpha():
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

# Sort the characters by count (descending) and then alphabetically
sorted_char_count = []
for char, count in char_count.items():
    sorted_char_count.append([-count, char])

sorted_char_count.sort()

# Output the sorted characters and their counts
for count, char in sorted_char_count:
    print(f"{char} -> {-count}")
```
