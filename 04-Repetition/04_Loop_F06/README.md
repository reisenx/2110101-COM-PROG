<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Print Triangle (Function) ★★ (
      <a href="https://drive.google.com/file/d/1BZfEUio1oqtH8ogukO0SjbpGXvVK4ZDD/view?usp=drive_link">
        <code>04_Loop_F06</code>
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
# File Name : 04_Loop_F06.py
# Problem   : Print Triangle (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------


# Construct a function to print a triangle pattern
def print_triangle(h):
    triangle = ""
    for i in range(h - 1):
        # Add leading dots
        triangle += "." * (h - i - 1)
        # Add the first star
        triangle += "*"
        # Add dots between stars and the second star
        if i > 0:
            triangle += "." * ((2 * i) - 1)
            triangle += "*"
        # Add newline character
        triangle += "\n"
    # Add base of the triangle
    triangle += "*" * ((2 * h) - 1)

    # Output the triangle
    print(triangle)


# Execute the input string as code
exec(input())
```
