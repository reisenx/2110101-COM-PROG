<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    RLE ★★ (
      <a href="https://drive.google.com/file/d/1xbPthJmwu74ThTo_pm99cJfS2WJHIkOE/view?usp=drive_link">
        <code>P1_02_RLE</code>
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
# File Name : P1_02_RLE.py
# Problem   : Part-I RLE
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input command
cmd = input().strip()

# Initialize result variable
result = ""

# Convert string to RLE
if cmd == "str2RLE":
    # Input text
    text = input().strip()

    # Initialize counter
    char = text[0]
    count = 1

    # Iterate through the text
    for i in range(1, len(text)):
        if text[i] == char:
            count += 1
        else:
            result += f"{char} {count} "
            char = text[i]
            count = 1
    # Append the last character and its count
    result += f"{char} {count}"

# Convert RLE to string
elif cmd == "RLE2str":
    # Input text
    text = input().strip()

    # Split the input text into parts
    parts = text.split()

    # Iterate through the parts in pairs
    for i in range(0, len(parts), 2):
        char = parts[i]
        count = int(parts[i + 1])
        result += char * count
else:
    result = "Error"

# Output the result
print(result)
```
