<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Euro 2024 ★★ (
      <a href="https://drive.google.com/file/d/1cBzc4kXgbFXzY45q16TeEZBRyL9_7gH3/view?usp=sharing">
        <code>2566_3_Q2_01</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**กติกาการให้คะแนน**](#กติกาการให้คะแนน)
-   [**การอ่านและเก็บข้อมูล**](#การอ่านและเก็บข้อมูล)
-   [**การตรวจผลแพ้ชนะหรือเสมอ**](#การตรวจผลแพ้ชนะหรือเสมอ)
-   [**การตรวจคะแนนของแต่ละทีม**](#การตรวจคะแนนของแต่ละทีม)
-   [**ตัวอย่างการคำนวณ**](#ตัวอย่างการคำนวณ)
-   [**ความแตกต่างระหว่างโจทย์กับโค้ด**](#ความแตกต่างระหว่างโจทย์กับโค้ด)
-   [**ประสิทธิภาพ**](#ประสิทธิภาพ)
-   [**Solution**](#solution)

---

## กติกาการให้คะแนน

การคิดคะแนนของการแข่งขันแต่ละคู่แบ่งเป็น 2 ขั้น หากทายผลแพ้–ชนะหรือเสมอผิด
จะได้ `0` คะแนนทันที แต่ถ้าทายผลส่วนนี้ถูก จะได้คะแนนพื้นฐาน `3` คะแนน แล้ว
จึงบวกคะแนนโบนัสจากสกอร์ของทั้งสองทีม

| การทายสกอร์ เมื่อทายผลแพ้–ชนะหรือเสมอถูกแล้ว | โบนัส |
|---|---:|
| สกอร์ไม่ตรงทั้งสองทีม | 0 |
| สกอร์ตรงหนึ่งทีม | 1 |
| สกอร์ตรงทั้งสองทีม | 3 |

เขียนเป็นสูตรได้ว่า

$$
\text{คะแนนของคู่นี้} =
\begin{cases}
0, & \text{เมื่อทายผลแพ้–ชนะหรือเสมอผิด} \\
3 + \text{โบนัส}, & \text{เมื่อทายผลแพ้–ชนะหรือเสมอถูก}
\end{cases}
$$

ในภาษา Python แนวคิดของกรณีที่สองจึงตรงกับนิพจน์
`3 + get_match_scores(exact, guess)` โดยฟังก์ชัน `get_match_scores()` ในโค้ด
คืนค่าเฉพาะ **โบนัส** `0`, `1` หรือ `3`

## การอ่านและเก็บข้อมูล

คะแนนของหนึ่งคู่ถูกเก็บเป็นลิสต์สองสมาชิก `[score_team_1, score_team_2]`
เช่น `3:1` ถูกแปลงเป็น `[3, 1]` ทำให้เปรียบเทียบสกอร์ของทีมที่หนึ่งและทีมที่
สองแยกจากกันได้

โปรแกรมอ่านข้อมูลเป็น 2 ช่วง

1. ช่วงแรกอ่านบรรทัดรูปแบบ `ชื่อทีม:ชื่อทีม สกอร์:สกอร์` ไปเรื่อย ๆ จนพบ
   `-1` ตัวอย่างเช่น `England:Italy 3:1` จะถูก `split()` เป็น
   `['England:Italy', '3:1']` โค้ดใช้เฉพาะสมาชิกตำแหน่ง `1` แล้วเก็บ
   `[3, 1]` ไว้ใน `exact_scores`
2. ช่วงที่สองอ่านบรรทัดรูปแบบ `สกอร์:สกอร์` ให้ครบเท่าจำนวนคู่ในช่วงแรก
   แล้วเก็บไว้ใน `guess_scores`

> [!NOTE]
>
> คำอธิบายส่วน Input ใน PDF เรียกข้อมูลช่วงแรกว่า “ผลที่ทาย” และช่วงที่สองว่า
> “ผลการแข่งขัน” แต่ตารางอธิบายตัวอย่างและโค้ดกลับใช้ช่วงแรกเป็นผลจริง
> (`exact_scores`) และช่วงที่สองเป็นผลที่ทาย (`guess_scores`)
> คำอธิบายหน้านี้อ้างอิงพฤติกรรมของโค้ดและตารางตัวอย่าง

ชื่อทีมในช่วงแรกช่วยบอกว่าเป็นการแข่งขันคู่ใด แต่โจทย์ย่อยนี้ให้ข้อมูลทั้งสอง
ช่วงเรียงคู่ตรงกันอยู่แล้ว โค้ดจึงไม่ต้องใช้ชื่อทีมในการจับคู่

## การตรวจผลแพ้ชนะหรือเสมอ

ฟังก์ชัน `is_match_result_same(exact, guess)` ไม่ได้ตรวจว่าตัวเลขเท่ากัน แต่
ตรวจว่าเครื่องหมายเปรียบเทียบระหว่างสกอร์ของทั้งสองทีมตรงกันหรือไม่

| ผลการแข่งขัน | ผลจริง | ผลที่ทาย | เงื่อนไข Python |
|---|---|---|---|
| ทีมที่หนึ่งชนะ | `[3, 1]` | `[2, 0]` | `exact[0] > exact[1]` และ `guess[0] > guess[1]` |
| ทีมที่หนึ่งแพ้ | `[0, 2]` | `[1, 4]` | `exact[0] < exact[1]` และ `guess[0] < guess[1]` |
| เสมอ | `[1, 1]` | `[0, 0]` | `exact[0] == exact[1]` และ `guess[0] == guess[1]` |

ถ้าไม่มีกรณีใดเป็นจริง ฟังก์ชันจะคืน `False` และลูปหลักจะไม่เรียกฟังก์ชันคิด
โบนัสสำหรับคู่นั้น

## การตรวจคะแนนของแต่ละทีม

ฟังก์ชัน `get_match_scores(exact, guess)` คืนค่าโบนัสตามลำดับดังนี้

1. ถ้าลิสต์ทั้งสองเท่ากันด้วย `exact == guess` แสดงว่าสกอร์ตรงทั้งสองทีม
   จึงคืน `3`
2. มิฉะนั้น ถ้าสกอร์สมาชิกตำแหน่งเดียวกันตรงอย่างน้อยหนึ่งทีม จึงคืน `1`
3. ถ้าไม่ตรงเลย จึงคืน `0`

ต้องตรวจกรณีที่ตรงทั้งสองทีมก่อน เพราะกรณีนี้ย่อมทำให้เงื่อนไข “ตรงอย่างน้อย
หนึ่งทีม” เป็นจริงด้วย การใช้ `elif` ทำให้โปรแกรมเลือกคะแนนได้เพียงกรณีเดียว

## ตัวอย่างการคำนวณ

จากตัวอย่างใน PDF เมื่ออ่านช่วงแรกเป็นผลจริงและช่วงที่สองเป็นผลที่ทาย จะได้

| คู่ | ผลจริง | ผลที่ทาย | คะแนนตาม PDF | ค่าที่โค้ดบวกจริง |
|---|---:|---:|---:|---:|
| England–Italy | `3:1` | `2:1` | `3 + 1 = 4` | 1 |
| Germany–France | `1:1` | `0:0` | `3 + 0 = 3` | 0 |
| Portugal–Belgium | `0:3` | `0:0` | 0 | 0 |
| Spain–Netherlands | `2:2` | `2:2` | `3 + 3 = 6` | 3 |

ดังนั้นคำตอบตามกติกาใน PDF คือ $4 + 3 + 0 + 6 = 13$ คะแนน

## ความแตกต่างระหว่างโจทย์กับโค้ด

> [!WARNING]
>
> โค้ด Solution ด้านล่าง **ไม่ได้บวกคะแนนพื้นฐาน 3 คะแนน** เมื่อทายผล
> แพ้–ชนะหรือเสมอถูก ลูปหลักบวกเพียงค่าจาก `get_match_scores()` ซึ่งเป็น
> โบนัส `0`, `1` หรือ `3` เท่านั้น ด้วยข้อมูลตัวอย่าง โค้ดจึงแสดง `4`
> แทนคำตอบ `13` ที่ PDF กำหนด

คอมเมนต์เหนือ `get_match_scores()` เรียกค่าที่คืนว่า points และอธิบายว่าได้
`3` คะแนนเมื่อสกอร์ตรงทั้งหมด แต่เมื่อเทียบกับกติกาใน PDF ค่านี้เป็นเพียง
คะแนนโบนัส ยังไม่รวม 3 คะแนนจากการทายผลแพ้–ชนะหรือเสมอถูก คอมเมนต์และโค้ด
ใน Solution ถูกเก็บไว้ตามไฟล์ต้นฉบับ จึงต้องแยกพฤติกรรมจริงนี้ออกจากคำตอบที่
โจทย์ต้องการอย่างชัดเจน

## ประสิทธิภาพ

ถ้ามีการแข่งขัน $m$ คู่ โปรแกรมอ่านและเปรียบเทียบข้อมูลแต่ละคู่จำนวนคงที่
จึงใช้เวลา $O(m)$ และเก็บผลจริงกับผลที่ทายทั้งหมด จึงใช้พื้นที่เพิ่มเติม
$O(m)$

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_3_Q2_01.py
# Problem   : Euro 2024
# Author    : Worralop Srichainont
# Date      : 2025-07-15
# --------------------------------------------------


# Check if the match result of the guessed score is the same as the actual score.
# Both teams must have the same win/loss/draw status.
def is_match_result_same(exact, guess):
    return (
        ((exact[0] > exact[1]) and (guess[0] > guess[1]))
        or ((exact[0] < exact[1]) and (guess[0] < guess[1]))
        or ((exact[0] == exact[1]) and (guess[0] == guess[1]))
    )


# Compare the exact match scores with the guessed scores and return points.
# 3 points for exact match, 1 point for correct score of one team,
# and 0 points for no correct scores.
def get_match_scores(exact, guess):
    if exact == guess:
        return 3
    elif (exact[0] == guess[0]) or (exact[1] == guess[1]):
        return 1
    return 0


# Get the exact scores from the input.
exact_scores = []
while True:
    # Read input data until "-1" is entered.
    data = input().strip().split()
    if data == ["-1"]:
        break
    # Extract the scores from the input and store them in a list.
    score = data[1].split(":")
    exact_scores += [[int(score[0]), int(score[1])]]

# Get the guessed scores from the input.
guess_scores = []
for _ in range(len(exact_scores)):
    # Extract the scores from the input and store them in a list.
    score = input().strip().split(":")
    guess_scores += [[int(score[0]), int(score[1])]]

# Initialize total points to 0
total_points = 0
# Compare each exact score with the guessed score and calculate total points.
for i in range(len(exact_scores)):
    # Check if the match result is the same
    if is_match_result_same(exact_scores[i], guess_scores[i]):
        # If the match result is the same, compare scores and add points.
        total_points += get_match_scores(exact_scores[i], guess_scores[i])
# Output the total points.
print(total_points)
```
