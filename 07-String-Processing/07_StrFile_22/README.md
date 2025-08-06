<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Anagram ★★ (
      <a href="https://drive.google.com/file/d/1AXiZNOMmZwkKV2cUSMS500qbqEBiFDwQ/view?usp=drive_link">
        <code>07_StrFile_22</code>
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
# File Name : 07_StrFile_22.py
# Problem   : Anagram
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Initialize the character set
CHARACTERS = "abcdefghijklmnopqrstuvwxyz0123456789"

# Initialize character count arrays for two strings
# Index 0-25 for 'a'-'z', index 26-35 for '0'-'9'
char_count_01 = [0] * len(CHARACTERS)
char_count_02 = [0] * len(CHARACTERS)

# Input two strings and lowercase them
text01 = input().strip().lower()
text02 = input().strip().lower()

# Count characters in the first string
for char in text01:
    if char in CHARACTERS:
        index = CHARACTERS.index(char)
        char_count_01[index] += 1

# Count characters in the second string
for char in text02:
    if char in CHARACTERS:
        index = CHARACTERS.index(char)
        char_count_02[index] += 1

# Check if the two strings are anagrams
if char_count_01 == char_count_02:
    print("YES")
else:
    print("NO")
```
