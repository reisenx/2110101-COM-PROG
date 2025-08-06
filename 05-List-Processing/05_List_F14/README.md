<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Peaks (Function) ★ (
      <a href="https://drive.google.com/file/d/15UrBRnCHRKq6BIs2_4niUCqOj32_6v1c/view?usp=drive_link">
        <code>05_List_F14</code>
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
# File Name : 05_List_F14.py
# Problem   : Peaks (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Create a function to find index of peaks in a list of numbers
def peaks(numbers):
    peak_indices = []
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            peak_indices.append(i)
    return peak_indices


# Execute the input string as code
exec(input())
```
