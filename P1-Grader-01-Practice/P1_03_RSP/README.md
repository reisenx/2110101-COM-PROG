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

-   [**แทนผลการแข่งขันด้วยคู่การเล่น**](#แทนผลการแข่งขันด้วยคู่การเล่น)
-   [**นับคะแนนและหยุดเมื่อมีผู้ชนะ**](#นับคะแนนและหยุดเมื่อมีผู้ชนะ)
-   [**จำกัดจำนวนรอบและตัดสินผล**](#จำกัดจำนวนรอบและตัดสินผล)
-   [**Solution**](#solution)

---

## แทนผลการแข่งขันด้วยคู่การเล่น

โจทย์ใช้ `R` แทนค้อน (rock), `S` แทนกรรไกร (scissors) และ `P` แทนกระดาษ
(paper) ในแต่ละบรรทัด อักษรตัวแรกเป็นมือของผู้เล่น 1 และตัวที่สองเป็นมือของ
ผู้เล่น 2

กติกาที่ผู้เล่น 1 ชนะมีเพียง 3 คู่ โปรแกรมจึงเก็บไว้ใน `WINNING`

| มือผู้เล่น 1 | มือผู้เล่น 2 | เหตุผล |
|:---:|:---:|:---|
| `R` | `S` | ค้อนชนะกรรไกร |
| `S` | `P` | กรรไกรชนะกระดาษ |
| `P` | `R` | กระดาษชนะค้อน |

ส่วน `LOSING` เก็บคู่ตรงข้ามทั้ง 3 คู่ ซึ่งหมายถึงผู้เล่น 2 ชนะ

```python
WINNING = [["R", "S"], ["S", "P"], ["P", "R"]]
LOSING = [["S", "R"], ["P", "S"], ["R", "P"]]
```

คำสั่ง `input().strip().split()` เปลี่ยนข้อมูลอย่าง `R P` เป็นลิสต์
`["R", "P"]` จึงนำไปตรวจด้วย `result in WINNING` และ
`result in LOSING` ได้โดยตรง

ถ้าผู้เล่นทั้งสองออกมือเหมือนกัน คู่ดังกล่าวจะไม่อยู่ในลิสต์ใดเลย
รอบนั้นจึงเสมอและไม่มีใครได้คะแนน

---

## นับคะแนนและหยุดเมื่อมีผู้ชนะ

โปรแกรมเริ่มคะแนนของทั้งสองคนที่ `0` และรับจำนวนคะแนนที่ต้องชนะเป็น
`win_score` หรือค่า $m$ จากบรรทัดแรก

ในแต่ละรอบ โปรแกรมเพิ่ม `player01` เมื่อผลอยู่ใน `WINNING` หรือเพิ่ม
`player02` เมื่อผลอยู่ใน `LOSING` จากนั้นจึงตรวจว่ามีใครได้คะแนนถึง
`win_score` แล้วหรือยัง

```python
if player01 == win_score or player02 == win_score:
    break
```

เมื่อมีคนได้คะแนนที่ $m$ คำสั่ง `break` จะออกจากลูปทันที
โปรแกรมจึงไม่อ่านหรือประมวลผลการแข่งขันรอบถัดไป เพราะผู้ชนะถูกตัดสินแล้ว

ตัวอย่าง เมื่อ `m == 1` และรอบแรกเป็น `R P` ผลอยู่ใน `LOSING`
คะแนนจึงเป็น `0 1` และผู้เล่น 2 ชนะทันที

---

## จำกัดจำนวนรอบและตัดสินผล

หากยังไม่มีผู้ชนะ โจทย์ให้แข่งขันได้ไม่เกิน $3m$ รอบ สูตรนี้เขียนใน Python
เป็น `3 * win_score`

```python
for _ in range(3 * win_score):
```

ตัวแปร `_` ใช้แทนเลขรอบที่ไม่จำเป็นต้องนำไปคำนวณ ลูปทำงานได้สูงสุด
`3 * win_score` ครั้ง โดยแต่ละรอบอ่านผลการแข่งขัน 1 บรรทัด

> [!NOTE]
>
> รอบที่เสมอยังคงนับเป็นหนึ่งในจำนวนสูงสุด $3m$ รอบ แม้คะแนนของทั้งสองคน
> จะไม่เปลี่ยนแปลง

หลังจบลูป โปรแกรมแสดงผลตามลำดับคงที่ 2 บรรทัด

1. แสดง `player01` และ `player02` คั่นด้วยช่องว่าง
2. แสดง `Player 1 wins` ถ้าผู้เล่น 1 ได้ $m$ คะแนน, แสดง
   `Player 2 wins` ถ้าผู้เล่น 2 ได้ $m$ คะแนน หรือแสดง `Tie`
   เมื่อครบ $3m$ รอบแล้วยังไม่มีใครถึง $m$ คะแนน

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
