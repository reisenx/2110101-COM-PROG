<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Weekly Sales ★ (
      <a href="https://drive.google.com/file/d/1Pz84txEx0ZZel6BfEcsAKOvvpvj9lGHU/view?usp=drive_link">
        <code>02_StrList_05</code>
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
# File Name : 02_StrList_05.py
# Problem   : Weekly Sales
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input weekly sales data
sales = input().strip().split()

# Output the total sales for the week
print(
    int(sales[0])
    + int(sales[1])
    + int(sales[2])
    + int(sales[3])
    + int(sales[4])
    + int(sales[5])
    + int(sales[6])
)
```
