<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Winner ★ (
      <a href="https://drive.google.com/file/d/1WZFAdB_0dZ0niGUEbE1tPmyu4GFuwu3w/view?usp=drive_link">
        <code>10_TSD_13</code>
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
# File Name : 10_TSD_13.py
# Problem   : Winner
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input number of matches
n = int(input())

# Initialize sets for winners and losers
winners = set()
losers = set()

# Process each match
for _ in range(n):
    # Read the match result
    winner, loser = input().strip().split()

    # Update winners and losers sets
    winners.add(winner)
    losers.add(loser)

# Output the winner who is not in the losers set
print(sorted(winners - losers))
```
