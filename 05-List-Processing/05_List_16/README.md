<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Collatz ★☆ (
      <a href="https://drive.google.com/file/d/1PKXPExf_DPAlKwaGvQaZ3vqMd54RpVJ2/view?usp=drive_link">
        <code>05_List_16</code>
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
# File Name : 05_List_16.py
# Problem   : Collatz
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input numbers
num = int(input())

# Initialize the Collatz sequence list
collatz = [str(num)]

# Generate the Collatz sequence
while num != 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = 3 * num + 1
    collatz.append(str(num))

# Output the Collatz sequence
print("->".join(collatz[-15:]))
```
