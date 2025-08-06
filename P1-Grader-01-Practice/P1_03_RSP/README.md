<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Rock Scissor Paper ★★ (
      <a href="https://drive.google.com/file/d/12H-09gh_qRohC_q6lgplcSfxFSmCxuY0/view?usp=drive_link">
        <code>P1_03_RSP</code>
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
# File Name : P1_03_RSP.py
# Problem   : Part-I Rock Scissors Paper
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Initialize winning and losing conditions
WINNING = [["R", "S"], ["S", "P"], ["P", "R"]]
LOSING = [["S", "R"], ["P", "S"], ["R", "P"]]

# Initialize each player's score
player01 = 0
player02 = 0

# Input the winning score
win_score = int(input())

# Process each game result for 3 times the winning score
for _ in range(3 * win_score):
    # Input the result of the game
    result = input().strip().split()
    # Count scores for each player
    if result in WINNING:
        player01 += 1
    elif result in LOSING:
        player02 += 1
    # Check if either player has reached the winning score
    if player01 == win_score or player02 == win_score:
        break

# Output the final scores and the winner
print(player01, player02)
if player01 == win_score:
    print("Player 1 wins")
elif player02 == win_score:
    print("Player 2 wins")
else:
    print("Tie")
```
