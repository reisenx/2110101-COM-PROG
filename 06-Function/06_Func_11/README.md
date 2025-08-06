<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Binary Adder ★ (
      <a href="https://drive.google.com/file/d/18WhSghzPMPQRwFrjsYxGYeNEnU8G9dYB/view?usp=drive_link">
        <code>06_Func_11</code>
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
# File Name : 06_Func_11.py
# Problem   : Binary Adder
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input numbers in binary format
numbers = [int(num, 2) for num in input().split()]

# Output the sum of the binary numbers
print(bin(sum(numbers))[2:])
```
