<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Flowchart 04 ★★★ (
      <a href="https://drive.google.com/file/d/1ewNjgseKYUbSUJieJcFZ9nQlUid5RIi7/view?usp=drive_link">
        <code>P1_Flowchart_04</code>
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
# File Name : P1_Flowchart_04.py
# Problem   : Part-I Flowchart 04
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

x1 = input().strip()
x2 = input().strip()
x3 = input().strip()

x = x1 + x2 + x3

if len(x) == 9:
    win = "-"
    i = 0

    while i < 3:
        if x[3 * i] == x[3 * i + 1] == x[3 * i + 2]:
            win = x[3 * i]
            break
        elif x[i] == x[i + 3] == x[i + 6]:
            win = x[i]
            break
        else:
            i += 1

    if win == "-":
        if x[0] == x[4] == x[8]:
            win = x[0]
        elif x[3] == x[4] == x[6]:
            win = x[6]

    if win == "-":
        print("???")
    else:
        print(win)

else:
    print("ERROR")
```
