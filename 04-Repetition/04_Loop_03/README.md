<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    MCQ ★ (
      <a href="https://drive.google.com/file/d/1045T9kHbNpOkVWQG6D0URf3tx7AYj9Zq/view?usp=drive_link">
        <code>04_Loop_03</code>
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
# File Name : 04_Loop_03.py
# Problem   : MCQ
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# Input answer and solution
answer = input().strip()
solution = input().strip()

# Initialize score
score = 0

# Output the score
if len(answer) == len(solution):
    for i in range(len(answer)):
        if answer[i] == solution[i]:
            score += 1
    print(score)
else:
    print("Incomplete answer")
```
