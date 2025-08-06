<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    File Min-Max-Average ★★ (
      <a href="https://drive.google.com/file/d/1g8qEXc7_TKpAVXmD9HZSHeysBDMZwiv4/view?usp=drive_link">
        <code>07_StrFile_23</code>
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
# File Name : 07_StrFile_23.py
# Problem   : File Min Max Average
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input filename and year (extract last two digits)
filename, year = input().strip().split()
year = year[-2:]

# Initialize lists to store scores
scores = []

# Read the file and extract scores for the specified year
with open(filename) as file:
    for line in file:
        student_id, score = line.strip().split()
        if student_id[:2] == year:
            scores.append(float(score))

if len(scores) > 0:
    # Calculate min, max, and average
    min_score = min(scores)
    max_score = max(scores)
    avg_score = sum(scores) / len(scores)

    # Print the results
    print(min_score, max_score, avg_score)
else:
    print("No data")
```
