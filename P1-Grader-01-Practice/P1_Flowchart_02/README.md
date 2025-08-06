<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Flowchart 02 ★★★ (
      <a href="https://drive.google.com/file/d/10ygmFflkrf_beWnxtfczsVP6onvTbVPt/view?usp=drive_link">
        <code>P1_Flowchart_02</code>
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
# File Name : P1_Flowchart_02.py
# Problem   : Part-I Flowchart 02
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

n, k = [int(e) for e in input().split()]

if n % 2 != 0:
    sum_a, sum_b, sum_c, m = 0, 0, 0, 0

    while m < k:
        a, b, c = [int(e) for e in input().split()]

        if a == b:
            if a == b == c:
                if a + b > k:
                    sum_a += 1
                    sum_b += 2
                    sum_c -= 3
                else:
                    sum_a -= 3
                    sum_b -= 2
                    sum_c += 1
            else:
                sum_a += 2
                sum_b -= 3
        m += 1
    print(sum_a, sum_b, sum_c)

else:
    s, t = [int(e) for e in input().split()]

    x = s
    y = t

    if s > t:
        x = s - t
    else:
        if s < t:
            y = 2 * (t - s)

    if x + y > k:
        x, y = y, x
        x = y + (s**2)

    print(x, y)
```
