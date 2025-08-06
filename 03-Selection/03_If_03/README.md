<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Gymnastic Score ★ (
      <a href="https://drive.google.com/file/d/1p7OQvLjJEf3w8mZ927Vc2ImtmJTkadFw/view?usp=drive_link">
        <code>03_If_03</code>
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
# File Name : 03_If_03.py
# Problem   : Gymnastic Score
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

# Input the scores of 4 judges
raw_scores = input().strip().split()
scores = [
    float(raw_scores[0]),
    float(raw_scores[1]),
    float(raw_scores[2]),
    float(raw_scores[3]),
]

# Find the maximum and minimum scores
max_score = scores[0]
min_score = scores[0]

if scores[1] > max_score:
    max_score = scores[1]
if scores[1] < min_score:
    min_score = scores[1]

if scores[2] > max_score:
    max_score = scores[2]
if scores[2] < min_score:
    min_score = scores[2]

if scores[3] > max_score:
    max_score = scores[3]
if scores[3] < min_score:
    min_score = scores[3]

# Calculate the average score
score_total = scores[0] + scores[1] + scores[2] + scores[3]
average_score = (score_total - max_score - min_score) / 2

# Output the average score
print(round(average_score, 2))
```
