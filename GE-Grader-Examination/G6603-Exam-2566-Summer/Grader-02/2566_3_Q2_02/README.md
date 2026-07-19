<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Euro 2024 Sub-routing ★★☆ (
      <a href="https://drive.google.com/file/d/1bA-H_dW0TDJnl-Opur5J89TMTQz0h42Z/view?usp=sharing">
        <code>2566_3_Q2_02</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**รูปแบบข้อมูลและผลลัพธ์**](#รูปแบบข้อมูลและผลลัพธ์)
-   [**การแยกข้อความการแข่งขัน**](#การแยกข้อความการแข่งขัน)
-   [**การค้นหาคะแนนที่สลับลำดับทีม**](#การค้นหาคะแนนที่สลับลำดับทีม)
-   [**การสร้างผลลัพธ์ตามลำดับผลจริง**](#การสร้างผลลัพธ์ตามลำดับผลจริง)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**การรับข้อมูลด้วยคำสั่ง exec**](#การรับข้อมูลด้วยคำสั่ง-exec)
-   [**Solution**](#solution)

---

## รูปแบบข้อมูลและผลลัพธ์

ผลการแข่งขันหนึ่งคู่เขียนอยู่ในรูปข้อความ เช่น
`"England:Germany 2:0"` โดยแบ่งเป็น 2 ส่วน คือ

-   `England:Germany` เป็นชื่อทีมตามลำดับที่เขียนไว้
-   `2:0` เป็นคะแนนของทีมทั้งสองตามลำดับเดียวกัน

ฟังก์ชัน `extract_scores(actual_results, guess_results)` ต้องพิจารณาคู่แข่งขัน
ตามลำดับใน `actual_results` แล้วสร้างลิสต์ย่อยในรูป

```text
[ผลจริงของทีมที่ 1, ผลจริงของทีมที่ 2, ผลทายของทีมที่ 1, ผลทายของทีมที่ 2]
```

คะแนนทั้งสี่ตำแหน่งต้องเรียงทีมตามข้อความใน `actual_results` เสมอ
แม้ข้อความใน `guess_results` จะเขียนชื่อทีมสลับกันก็ตาม หากไม่มีการทายคู่นั้น
ให้ใช้ลิสต์ว่าง `[]` แทนผลของคู่นั้นทั้งชุด

---

## การแยกข้อความการแข่งขัน

ฟังก์ชัน `get_info(result)` แยกข้อความทีละระดับด้วย `split()`

```python
data = result.split()
teams = data[0].split(":")
scores = data[1].split(":")
```

เมื่อ `result` เท่ากับ `"England:Germany 2:0"` จะได้ค่าระหว่างทางดังนี้

| ตัวแปร | ค่า |
|---|---|
| `data` | `["England:Germany", "2:0"]` |
| `teams` | `["England", "Germany"]` |
| `scores` | `["2", "0"]` |

ข้อมูลจาก `split()` ยังเป็นข้อความ จึงต้องแปลงคะแนนด้วย `int()` ก่อนคืนค่า
ผลลัพธ์ของ `get_info()` ในตัวอย่างนี้คือ
`("England", "Germany", 2, 0)`

---

## การค้นหาคะแนนที่สลับลำดับทีม

ฟังก์ชัน `get_score(team01, team02, results)` เดินดูข้อความใน `results`
ทีละรายการ โดยมี 2 กรณี

1. ถ้าข้อความเขียน `team01:team02` อยู่แล้ว ให้คืน `[score01, score02]`
2. ถ้าข้อความเขียน `team02:team01` ให้สลับคะแนนก่อนคืนเป็น
   `[score02, score01]`

ตัวอย่างเช่น ต้องการคะแนนตามลำดับ `England`, `Germany` แต่ผลทายเขียนว่า

```text
Germany:England 2:1
```

คะแนน `2` เป็นของ Germany และคะแนน `1` เป็นของ England ดังนั้น
`get_score("England", "Germany", results)` ต้องคืน `[1, 2]`
เพื่อให้ลำดับกลับมาตรงกับผลจริง

หากตรวจครบทุกข้อความแล้วยังไม่พบคู่นี้ ฟังก์ชันจะคืน `[]` ส่วนคำสั่ง
`return` ที่อยู่ในลูปทำให้โค้ดเลือกคู่แรกที่พบ การค้นหาในโค้ดใช้
`f"{team01}:{team02}" in result` กับรูปแบบข้อความที่โจทย์กำหนด

---

## การสร้างผลลัพธ์ตามลำดับผลจริง

หัวใจของ `extract_scores()` คือวนลูปบน `actual_results` ไม่ใช่
`guess_results` เพราะผลลัพธ์ต้องมีจำนวนและลำดับคู่ตรงกับผลจริง

สำหรับผลจริงแต่ละคู่ โปรแกรมทำงานดังนี้

1. ใช้ `get_info(match)` หา `team01`, `team02` และคะแนนจริง
2. เก็บคะแนนจริงเป็น `exact_scores = [score01, score02]`
3. ใช้ `get_score()` หาคะแนนทายโดยจัดลำดับทีมให้ตรงกัน
4. ถ้าพบผลทาย ให้ต่อสองลิสต์ด้วย
   `exact_scores + guess_scores` จนได้ตัวเลข 4 ตัว
5. ถ้าไม่พบผลทาย ให้เพิ่ม `[]` ลงในผลลัพธ์

การเขียน `results += [exact_scores + guess_scores]` มีวงเล็บลิสต์ชั้นนอก
เพื่อเพิ่มผลการแข่งขันหนึ่งคู่เป็นสมาชิกหนึ่งตัวของ `results`

---

## ตัวอย่างการทำงาน

กำหนดผลจริงตามลำดับดังนี้

```python
actual_results = [
    "England:Germany 2:0",
    "France:Spain 1:1",
    "Portugal:Italy 0:3",
    "Netherlands:Belgium 2:1",
]
```

สมมติว่าผลทายมีคู่ England–Germany แบบสลับชื่อทีม มีอีกสองคู่ที่ชื่อทีม
เรียงตามผลจริง และไม่มีคู่ Netherlands–Belgium โปรแกรมจะจัดข้อมูลได้เป็น

| คู่ตาม `actual_results` | คะแนนจริง | คะแนนทายหลังจัดลำดับทีม | ลิสต์ย่อย |
|---|---:|---:|---|
| England–Germany | `2:0` | `1:2` | `[2, 0, 1, 2]` |
| France–Spain | `1:1` | `2:0` | `[1, 1, 2, 0]` |
| Portugal–Italy | `0:3` | `1:1` | `[0, 3, 1, 1]` |
| Netherlands–Belgium | `2:1` | ไม่มี | `[]` |

ดังนั้นค่าที่คืนจากฟังก์ชันคือ

```python
[[2, 0, 1, 2], [1, 1, 2, 0], [0, 3, 1, 1], []]
```

---

## การรับข้อมูลด้วยคำสั่ง `exec`

ข้อมูลนำเข้าของโจทย์มี 3 บรรทัด และแต่ละบรรทัดเป็นคำสั่ง Python

1. กำหนดตัวแปร `actual_results`
2. กำหนดตัวแปร `guess_results`
3. เรียกและแสดงผล `extract_scores()`

จึงมี `exec(input().strip())` สามครั้งตามลำดับ เพื่อให้ระบบตรวจคำตอบ
ประมวลผลคำสั่งทั้งสามบรรทัดได้โดยตรง

> [!WARNING]
>
> `exec()` สามารถรันคำสั่ง Python ใด ๆ ที่อยู่ในข้อความได้ วิธีนี้เหมาะกับ
> ข้อมูลจาก grader ที่โจทย์ควบคุมไว้เท่านั้น ไม่ควรใช้ `exec()` กับข้อความ
> จากผู้ใช้หรือแหล่งข้อมูลที่ไม่เชื่อถือ

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_3_Q2_02.py
# Problem   : Euro 2024 Sub-routing
# Author    : Worralop Srichainont
# Date      : 2025-07-15
# --------------------------------------------------


# Extract team names and scores from a match result string.
def get_info(result):
    data = result.split()
    teams = data[0].split(":")
    scores = data[1].split(":")
    return teams[0], teams[1], int(scores[0]), int(scores[1])


# Find the scores between two teams in a list of match results.
def get_score(team01, team02, results):
    # Iterate through the results to find the match between team01 and team02.
    for result in results:
        # Extract scores from the result string.
        _, _, score01, score02 = get_info(result)
        # Check if the order is team01:team02
        if f"{team01}:{team02}" in result:
            return [score01, score02]
        # Check if the order is team02:team01
        elif f"{team02}:{team01}" in result:
            return [score02, score01]
    # If no match is found, return an empty list.
    return []


# Extract scores from actual results and guess results.
def extract_scores(actual_results, guess_results):
    # Initialize an empty list to store the results of every match.
    results = []
    # Iterate through each match in the actual results.
    for match in actual_results:
        # Extract team names and scores from the actual match string.
        team01, team02, score01, score02 = get_info(match)

        # Get the score for the guessed match.
        exact_scores = [score01, score02]
        guess_scores = get_score(team01, team02, guess_results)
        # Add the scores to the results list.
        if guess_scores != []:
            results += [exact_scores + guess_scores]
        else:
            results += [[]]
    # Return the list of results for all matches.
    return results


# Execute the input string as code.
exec(input().strip())
exec(input().strip())
exec(input().strip())
```
