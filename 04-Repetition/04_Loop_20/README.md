<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Zig Zag 2 ★★★ (
      <a href="https://drive.google.com/file/d/1uqvOHaGO9mRZmolJCEQUttyfUHyWmnai/view?usp=drive_link">
        <code>04_Loop_20</code>
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
# File Name : 04_Loop_20.py
# Problem   : Zig Zag 2
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Initialize variables
line = 0
min_a, max_a = 0, 0
min_b, max_b = 0, 0

# Loop to read input values
while True:
    # Read input data
    data = input().strip().split()

    # Output the result
    if len(data) == 1:
        cmd = data[0]
        if cmd == "Zig-Zag":
            print(min_a, max_b)
        elif cmd == "Zag-Zig":
            print(min_b, max_a)
        break

    # Get the numbers
    x, y = int(data[0]), int(data[1])

    # Update min and max values based on the line number
    if line == 0:
        min_a, max_a = x, x
        min_b, max_b = y, y
    else:
        if line % 2 == 0:
            min_a, max_a = min(min_a, x), max(max_a, x)
            min_b, max_b = min(min_b, y), max(max_b, y)
        else:
            min_a, max_a = min(min_a, y), max(max_a, y)
            min_b, max_b = min(min_b, x), max(max_b, x)

    # Increment the line number
    line += 1
```
