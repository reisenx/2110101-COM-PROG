<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Bowling ★★★ (
      <a href="https://drive.google.com/file/d/18Cp6jlm1gYagaPjU0R_lsE9imFCTqFoK/view?usp=drive_link">
        <code>P1_04_Bowling</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**Solution 1**](#solution-1)
-   [**Solution 2**](#solution-2)

---

<div align="center">
  <h2>เฉลยอย่างละเอียดจะตามมาทีหลัง</h2>
</div>

---

# Solution 1

```python
# --------------------------------------------------
# File Name : P1_04_Bowling-sol1.py
# Problem   : Part-I Bowling
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input bowling result and frame to display
result = input().strip()
display_frame = int(input())

# Initialize variables
idx = 0
frame_scores = []

# Calculate scores for each frame
for _ in range(10):
    # Initialize score for the current frame
    score = 0
    # Case 1: XXX = 30
    if result[idx : idx + 3] == "XXX":
        score = 30
        idx += 1

    # Case 2: XX? = 20 + ?
    elif result[idx : idx + 2] == "XX" and result[idx + 2].isdigit():
        score = 20 + int(result[idx + 2])
        idx += 1

    # Case 3: X?/ = 20
    elif result[idx] == "X" and result[idx + 1].isdigit() and result[idx + 2] == "/":
        score = 20
        idx += 1

    # Case 4: X?? = 10 + ? + ?
    elif result[idx] == "X" and result[idx + 1 : idx + 3].isdigit():
        score = 10 + int(result[idx + 1]) + int(result[idx + 2])
        idx += 1

    # Case 5: ?/X = 20
    elif result[idx].isdigit() and result[idx + 1 : idx + 3] == "/X":
        score = 20
        idx += 2

    # Case 6: ?/? = 10 + ?
    elif result[idx].isdigit() and result[idx + 1] == "/" and result[idx + 2].isdigit():
        score = 10 + int(result[idx + 2])
        idx += 2

    # Case 7: ?? = ? + ?
    elif result[idx : idx + 2].isdigit():
        score = int(result[idx]) + int(result[idx + 1])
        idx += 2

    # Add the score to frame scores
    frame_scores.append(score)

# Output
if 1 <= display_frame <= 10:
    print(frame_scores[display_frame - 1])
else:
    print(sum(frame_scores))
```

---

# Solution 2

```python
# --------------------------------------------------
# File Name : P1_04_Bowling-sol2.py
# Problem   : Part-I Bowling
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input bowling result and frame to display
result_str = input().strip()
display_frame = int(input())

# Convert the result string into a list of integers
result = []
for i in range(len(result_str)):
    if result_str[i] == "X":
        result.append(10)
    elif result_str[i] == "/":
        result.append(10 - int(result[i - 1]))
    else:
        result.append(int(result_str[i]))

# Initialize variables
frame_scores = []
idx = 0

# Calculate scores for each frame
for _ in range(10):
    # Initialize score for the current frame
    score = 0
    # Check for strike (X)
    if result[idx] == 10:
        score = sum(result[idx : idx + 3])
        idx += 1
    # Check for spare (/)
    elif sum(result[idx : idx + 2]) == 10:
        score = sum(result[idx : idx + 3])
        idx += 2
    # Normal case (two rolls)
    else:
        score = sum(result[idx : idx + 2])
        idx += 2
    frame_scores.append(score)

# Output
if 1 <= display_frame <= 10:
    print(frame_scores[display_frame - 1])
else:
    print(sum(frame_scores))
```
