<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Registered Mail ★ (
      <a href="https://drive.google.com/file/d/1xz-1_3ylH51G0jv7eHDlA-QwxgPmTye4/view?usp=drive_link">
        <code>03_If_06</code>
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
# File Name : 03_If_06.py
# Problem   : Registered Mail
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input weight
weight = int(input())

# Calculate the cost based on weight
if weight <= 100:
    print(18)
elif weight <= 250:
    print(22)
elif weight <= 500:
    print(28)
elif weight <= 1000:
    print(38)
elif weight <= 2000:
    print(58)
else:
    print("Reject")
```
