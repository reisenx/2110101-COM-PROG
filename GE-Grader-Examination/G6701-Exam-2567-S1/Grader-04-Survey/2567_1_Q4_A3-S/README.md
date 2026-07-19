<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    MCQ ★☆ (
      <a href="https://drive.google.com/file/d/1-AYbnJMeKUlmUY6LSnm5LZwU2DRU2UwG/view?usp=sharing">
        <code>2567_1_Q4_A3-S</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ความหมายของเฉลยและคำตอบ**](#ความหมายของเฉลยและคำตอบ)
-   [**การนับคำตอบแต่ละข้อ**](#การนับคำตอบแต่ละข้อ)
-   [**การคำนวณคะแนนรวม**](#การคำนวณคะแนนรวม)
-   [**ตัวอย่างการไล่ค่า**](#ตัวอย่างการไล่ค่า)
-   [**รูปแบบผลลัพธ์**](#รูปแบบผลลัพธ์)
-   [**Solution**](#solution)

---

## ความหมายของเฉลยและคำตอบ

โปรแกรมรับข้อมูลสามบรรทัดตามลำดับ

1. `solution_answer` เป็นสตริงเฉลย ประกอบด้วย `A` ถึง `E` หรือ `X`
2. `correct_score` และ `incorrect_score` เป็นคะแนนเมื่อตอบถูกและตอบผิด
3. `candidate_answer` เป็นคำตอบของผู้สอบ โดย `-` หมายถึงไม่ได้ตอบ

สตริงเฉลยและคำตอบยาวเท่ากัน ตำแหน่ง `i` ของทั้งสองสตริงจึงแทนข้อสอบ
ข้อเดียวกัน ตัว `X` ในเฉลยเป็น wildcard หมายถึงคำตอบใด ๆ รวมถึง `-`
ก็ถือว่าถูก

---

## การนับคำตอบแต่ละข้อ

โปรแกรมวนตั้งแต่ตำแหน่ง `0` ถึง `len(solution_answer) - 1` แล้วตรวจสองเรื่อง
แยกกัน

เงื่อนไขแรกนับถูกหรือผิด

```python
if solution_answer[i] == "X" or candidate_answer[i] == solution_answer[i]:
```

ถ้าเฉลยเป็น `X` หรือคำตอบตรงกับเฉลย ให้เพิ่ม `correct_count` มิฉะนั้นเพิ่ม
`incorrect_count`

จากนั้นโปรแกรมใช้ `if` อีกคำสั่งเพื่อตรวจ `candidate_answer[i] == "-"`
และเพิ่ม `no_answer_count` การตรวจนี้ไม่ใช่ `elif` จึงเกิดการนับซ้อนกันได้

| เฉลย | คำตอบ | นับถูก | นับผิด | นับไม่ตอบ |
|:---:|:---:|:---:|:---:|:---:|
| `A` | `A` | ✓ |  |  |
| `A` | `-` |  | ✓ | ✓ |
| `X` | `B` | ✓ |  |  |
| `X` | `-` | ✓ |  | ✓ |

ดังนั้น `correct_count + incorrect_count` เท่ากับจำนวนข้อทั้งหมดเสมอ
แต่ `no_answer_count` เป็นข้อมูลอีกมิติหนึ่งและไม่ควรนำไปบวกกับสองค่านั้น

> [!NOTE]
>
> ข้อที่ไม่ตอบและเฉลยเป็น `X` จะเพิ่มทั้ง `correct_count` และ
> `no_answer_count` ตามกติกาของโจทย์

---

## การคำนวณคะแนนรวม

เมื่อได้จำนวนข้อถูกและผิดแล้ว คะแนนก่อนจำกัดค่าคือ

$$
score = (correct\_count \times correct\_score)
      + (incorrect\_count \times incorrect\_score)
$$

ตรงกับ Python ดังนี้

```python
total_score = (correct_count * correct_score) + (incorrect_count * incorrect_score)
```

จำนวนข้อไม่ตอบไม่มีพจน์คะแนนแยกต่างหาก เพราะข้อไม่ตอบถูกจัดเป็นข้อถูกเมื่อเฉลย
เป็น `X` และเป็นข้อผิดในกรณีอื่นอยู่แล้ว

`incorrect_score` อาจเป็นค่าติดลบ หากคะแนนที่คำนวณได้ต่ำกว่า `0`
โปรแกรมใช้ `max(0, total_score)` เพื่อเปลี่ยนผลลัพธ์เป็น `0`

---

## ตัวอย่างการไล่ค่า

สมมติเฉลยเป็น `AXD`, คะแนนถูก/ผิดเป็น `2 -1` และคำตอบเป็น `--D`

1. ข้อ 1 เฉลย `A` แต่ไม่ตอบ: ผิดและไม่ตอบ
2. ข้อ 2 เฉลย `X` และไม่ตอบ: ถูกและไม่ตอบ
3. ข้อ 3 ตอบ `D` ตรงกับเฉลย: ถูก

จึงได้ถูก `2` ข้อ ผิด `1` ข้อ ไม่ตอบ `2` ข้อ และคะแนน
`(2 * 2) + (1 * -1) = 3`

---

## รูปแบบผลลัพธ์

โปรแกรมแสดงจำนวนเต็มสี่ค่าบนบรรทัดเดียว คั่นด้วยช่องว่าง และเรียงตามนี้

```text
จำนวนข้อถูก จำนวนข้อผิด จำนวนข้อไม่ตอบ คะแนนรวม
```

ต้องรักษาลำดับดังกล่าว แม้จำนวนข้อไม่ตอบจะซ้อนอยู่ในจำนวนข้อถูกหรือผิดแล้วก็ตาม

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q4_A3-S.py
# Problem   : MCQ
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Input solution answer of the exam
solution_answer = input().strip()

# Input score gained or deducted for correct and incorrect answers
correct_score, incorrect_score = [int(score) for score in input().split()]

# Input candidate's answer
candidate_answer = input().strip()

# Initialize counters
correct_count = 0
incorrect_count = 0
no_answer_count = 0

# Calculate scores based on answers
for i in range(len(solution_answer)):
    # Candidate answered correctly
    if solution_answer[i] == "X" or candidate_answer[i] == solution_answer[i]:
        correct_count += 1

    # Candidate answered incorrectly
    else:
        incorrect_count += 1

    # Candidate did not answer
    if candidate_answer[i] == "-":
        no_answer_count += 1

# Calculate total score
total_score = (correct_count * correct_score) + (incorrect_count * incorrect_score)
# Ensure score is not negative
total_score = max(0, total_score)

# Output the results
print(correct_count, incorrect_count, no_answer_count, total_score)
```
