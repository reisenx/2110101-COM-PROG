<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Flowchart 01 ★★ (
      <a href="https://drive.google.com/file/d/1LTZjlET9UDzyOCV-XCcw5ukS03xLicy8/view?usp=drive_link">
        <code>P1_Flowchart_01</code>
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
# File Name : P1_Flowchart_01.py
# Problem   : Part-I Flowchart 01
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

x1, x2, x3, x4, x5 = [int(e) for e in input().split()]

if x1 - x5 > x2:
    if x2 > x3 + x1:
        if x3 + x5 > x4:
            print("C5")
        else:
            if x3 < x5:
                print("C6")
            else:
                print("C7")
            print("C8")

else:
    if x2 - x1 > x3:
        pass
    else:
        if x4 < x5 + x1:
            if x3 + x2 > x5:
                print("C3")
            else:
                print("C2")
            print("C4")
        else:
            print("C1")
```
