<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    ROT13 ★★ (
      <a href="https://drive.google.com/file/d/1TO8vz37m9d83js4X4iks1d9j4NRwG50a/view?usp=drive_link">
        <code>07_StrFile_21</code>
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
# File Name : 07_StrFile_21.py
# Problem   : ROT13
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# List of lowercase and uppercase letters
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Function to encrypt text using ROT13 cipher
def rot13(text):
    result = ""
    for char in text:
        # Encrypt lowercase letters
        if char in LOWERCASE:
            idx = LOWERCASE.index(char)
            result += LOWERCASE[(idx + 13) % 26]

        # Encrypt uppercase letters
        elif char in UPPERCASE:
            idx = UPPERCASE.index(char)
            result += UPPERCASE[(idx + 13) % 26]

        # Keep non-alphabetic characters unchanged
        else:
            result += char
    # Return the encrypted text
    return result


# ROT13 encryption
while True:
    # Input a text
    text = input().strip()
    # Stop if the input is "end"
    if text == "end":
        break
    # Output the encrypted text
    print(rot13(text))
```
