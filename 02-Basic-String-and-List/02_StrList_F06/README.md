<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Add Vector (Function) ★★ (
      <a href="https://drive.google.com/file/d/1WYzyRZKzg7OWbNh94YhxtmMeWfrfd6x9/view?usp=drive_link">
        <code>02_StrList_F06</code>
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
# File Name : 02_StrList_F06.py
# Problem   : Add Vector (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------


# Create a function to add two vectors
def add_vector(u, v):
    total = [0.0, 0.0, 0.0]
    total[0] = float(u[0]) + float(v[0])
    total[1] = float(u[1]) + float(v[1])
    total[2] = float(u[2]) + float(v[2])
    return total


# Execute the input string as code
exec(input())
```
