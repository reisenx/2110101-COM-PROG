<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    MCQ (Function) ★ (
      <a href="https://drive.google.com/file/d/1FiT8lFWI6pDnFiyKGCfqsoO6aFQHRNsn/view?usp=drive_link">
        <code>04_Loop_F03</code>
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
# File Name : 04_Loop_F03.py
# Problem   : MCQ (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------


# Create a function to grade multiple-choice questions (MCQ)
def grade_mcq(sol, ans):
    # Initialize score
    score = 0

    # Returns a score
    if len(ans) == len(sol):
        for i in range(len(ans)):
            if ans[i] == sol[i]:
                score += 1
        return score
    return -1


# Execute the input string as code
exec(input())
```
