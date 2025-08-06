<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Rotate String ★★★ (
      <a href="https://drive.google.com/file/d/1Ms1AhMxEaiGeOR3I9wMfwIeC27iwGTCP/view?usp=drive_link">
        <code>P1_06_RotateString</code>
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
# File Name : P1_06_RotateString.py
# Problem   : Part-I Rotate String
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input command to modify the image
cmd = input().strip()

# Input original image
row = int(input())
img = [input().strip() for _ in range(row)]

# Validate the image size
is_valid = True
col = len(img[0])
for line in img:
    if len(line) != col:
        is_valid = False
        print("Invalid size")
        break

# Modify the image based on the command
if is_valid:
    # Initialize the modified image
    modified_img = []
    # Rotate the image by 90 degrees clockwise
    if cmd == "90":
        for c in range(col):
            line = ""
            for r in range(row - 1, -1, -1):
                line += img[r][c]
            modified_img.append(line)

    # Rotate the image by 180 degrees
    elif cmd == "180":
        for r in range(row - 1, -1, -1):
            modified_img.append(img[r][::-1])

    # Flip the image horizontally
    elif cmd == "flip":
        for r in range(row):
            modified_img.append(img[r][::-1])

    # Output the modified image
    for line in modified_img:
        print(line)
```
