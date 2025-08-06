<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Average ★ (
      <a href="https://drive.google.com/file/d/1qDCP0adaX9AyDZarqaKNwJpi9H2edl7t/view?usp=drive_link">
        <code>04_Loop_01</code>
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
# File Name : 04_Loop_01.py
# Problem   : Average
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Initialize total and num_count
total = 0
num_count = 0

# Input numbers until 'q' is entered
while True:
    num = input().strip()
    if num == "q":
        break
    total += float(num)
    num_count += 1

# Calculate and print the average
if num_count > 0:
    average = total / num_count
    print(round(average, 2))
else:
    print("No Data")
```
