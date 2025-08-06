<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    RLE (Function) ★★ (
      <a href="https://drive.google.com/file/d/1TFt7ByWF1iL5RG1q5c2kTaf2cv7yKsWl/view?usp=drive_link">
        <code>04_Loop_F11</code>
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
# File Name : 04_Loop_F11.py
# Problem   : RLE (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------


def RLE(text: str) -> list:
    # Empty string check
    if text == "":
        return []

    # Construct RLE list
    rle = []

    # Initialize counter
    char = text[0]
    count = 1

    # Iterate through the text
    for i in range(1, len(text)):
        if text[i] == char:
            count += 1
        else:
            rle += [[char, count]]
            char = text[i]
            count = 1

    # Append the last character and its count
    rle += [[char, count]]
    # Return the RLE list
    return rle


# Execute input string as code
exec(input())
```
