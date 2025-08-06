<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Print Triangle ★★ (
      <a href="https://drive.google.com/file/d/1SQyDHlrG-1P4KNhaAMi-8B2NycHO0DzW/view?usp=drive_link">
        <code>04_Loop_06</code>
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
# File Name : 04_Loop_06.py
# Problem   : Print Triangle
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input the height of the triangle
n = int(input())

# Construct the triangle
triangle = ""
for i in range(n - 1):
    # Add leading dots
    triangle += "." * (n - i - 1)
    # Add the first star
    triangle += "*"
    # Add dots between stars and the second star
    if i > 0:
        triangle += "." * ((2 * i) - 1)
        triangle += "*"
    # Add newline character
    triangle += "\n"
# Add base of the triangle
triangle += "*" * ((2 * n) - 1)

# Output the triangle
print(triangle)
```
