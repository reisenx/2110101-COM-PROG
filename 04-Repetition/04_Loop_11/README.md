<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    RLE ★★ (
      <a href="https://drive.google.com/file/d/1FJljyXrq98kzqLZK7o4SCWsisbRIa-wn/view?usp=drive_link">
        <code>04_Loop_11</code>
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
# File Name : 04_Loop_11.py
# Problem   : RLE
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input text
text = input().strip()

# Construct RLE string
rle = ""

# Initialize counter
char = text[0]
count = 1

# Iterate through the text
for i in range(1, len(text)):
    if text[i] == char:
        count += 1
    else:
        rle += char + " " + str(count) + " "
        char = text[i]
        count = 1

# Append the last character and its count
rle += char + " " + str(count)

# Output the RLE string
print(rle)
```
