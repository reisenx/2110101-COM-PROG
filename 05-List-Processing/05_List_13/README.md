<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Back and Front ★ (
      <a href="https://drive.google.com/file/d/1n1NhFs45L_Ckod3W0vENhqMMHnYxNO0z/view?usp=drive_link">
        <code>05_List_13</code>
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
# File Name : 05_List_13.py
# Problem   : Back and Front
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Initialize numbers list
numbers = []

# Input first set of numbers
n = int(input())
for _ in range(n):
    numbers.append(int(input()))

# Input second set of numbers
numbers += [int(num) for num in input().split()]

# Input the third set of numbers
while True:
    num = int(input())
    if num == -1:
        break
    numbers.append(num)

# Rearrange the numbers
rearranged_numbers = []
for i in range(len(numbers)):
    # Insert at the back first, then at the front
    if i % 2 == 0:
        rearranged_numbers.append(numbers[i])
    else:
        rearranged_numbers.insert(0, numbers[i])

# Output the rearranged numbers
print(rearranged_numbers)
```
