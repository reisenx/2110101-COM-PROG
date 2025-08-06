<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Four Functions ★★ (
      <a href="https://drive.google.com/file/d/1s5E2eHburs33GwzIYKRjqBcq_xrRqalX/view?usp=drive_link">
        <code>06_Func_23</code>
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
# File Name : 06_Func_23.py
# Problem   : Four Functions
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Convert a string into a list of integers
def make_int_list(numbers):
    return [int(num) for num in numbers.split()]


# Check if a number is odd
def is_odd(num):
    return num % 2 != 0


def odd_list(numbers):
    return [num for num in numbers if is_odd(num)]


# Calculate the sum of squares of a list of numbers
def sum_square(numbers):
    total = 0
    for num in numbers:
        total += num**2
    return total


# Execute a input string as code
exec(input().strip())
```
