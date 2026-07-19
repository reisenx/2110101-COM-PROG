<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Grader Score ★★ (
      <a href="https://drive.google.com/file/d/1xH6vj4ppOagjY1tbTkR5sUHK3JA6TzU5/view?usp=sharing">
        <code>2567_1_Q3_A3</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การจับคู่ข้อสอบเดิม**](#การจับคู่ข้อสอบเดิม)
-   [**การปรับรายการให้ยาวเท่ากัน**](#การปรับรายการให้ยาวเท่ากัน)
-   [**การเลือกคะแนนที่ดีที่สุด**](#การเลือกคะแนนที่ดีที่สุด)
-   [**ตัวอย่างการคำนวณ**](#ตัวอย่างการคำนวณ)
-   [**ลำดับการทำงานของโปรแกรม**](#ลำดับการทำงานของโปรแกรม)
-   [**Solution**](#solution)

---

## การจับคู่ข้อสอบเดิม

ข้อสอบมีทั้งหมด 3 Quiz โดย Quiz ครั้งหลังมีทั้งข้อใหม่และข้อแก้ตัวจากครั้งก่อน
คะแนนที่ตำแหน่งเดียวกันของทั้งสามบรรทัดจึงเป็นคะแนนของข้อเดียวกันในแต่ละครั้ง
ที่นิสิตได้ทำข้อนั้น

โปรแกรมอ่านคะแนนแต่ละ Quiz เป็นรายการจำนวนเต็ม `q1_scores`, `q2_scores`
และ `q3_scores` ลำดับของคะแนนต้องคงเดิม เพราะดัชนี `i` ใช้จับคู่ข้อสอบ
เดียวกันข้าม Quiz

ข้อที่เพิ่งปรากฏใน Quiz ครั้งหลังจะไม่มีคะแนนในรายการของ Quiz ก่อนหน้า
จึงต้องทำให้รายการทั้งสามยาวเท่ากันก่อนเปรียบเทียบ

---

## การปรับรายการให้ยาวเท่ากัน

จำนวนตำแหน่งข้อสอบทั้งหมดหาได้จากความยาวมากที่สุด

```python
total_quizzes = max(len(q1_scores), len(q2_scores), len(q3_scores))
```

จากนั้นเติม `0` ต่อท้ายรายการที่สั้นกว่า เช่น ถ้าความยาวสูงสุดเป็น `5`
แต่ `q1_scores` มี `2` ค่า นิพจน์
`[0] * (total_quizzes - len(q1_scores))` จะสร้างเลขศูนย์อีก `3` ค่า

คะแนนเต็มของแต่ละข้ออยู่ในช่วง `0` ถึง `100` ดังนั้น `0`
แทนการที่ข้อนั้นยังไม่มีใน Quiz ก่อนหน้าได้ และจะไม่ชนะคะแนนจริงที่มากกว่า

> [!NOTE]
>
> แม้ตัวแปรชื่อ `total_quizzes` และความเห็นใน Solution จะกล่าวถึงจำนวน Quiz
> แต่ค่าที่คำนวณจริงคือ **จำนวนตำแหน่งข้อสอบทั้งหมด** หลัง Quiz ครั้งที่ 3
> ส่วนจำนวนครั้งของ Quiz มีค่าเท่ากับ `3` ตามโจทย์เสมอ

---

## การเลือกคะแนนที่ดีที่สุด

สำหรับข้อสอบตำแหน่งที่ $i$ คะแนนที่นำมาคิดคือคะแนนสูงสุดจากทั้งสาม Quiz

$$
best_i = \max(q1_i, q2_i, q3_i)
$$

ตรงกับ Python คือ

```python
max(q1_scores[i], q2_scores[i], q3_scores[i])
```

โปรแกรมวน `i` ตั้งแต่ `0` ถึง `total_quizzes - 1` แล้วบวกคะแนนที่ดีที่สุด
ของแต่ละข้อเข้า `total_score` กล่าวคือ

$$
total\_score = \sum_i best_i
$$

ถ้าการแก้ตัวได้คะแนนน้อยลง คะแนนครั้งเดิมยังคงถูกเลือกด้วย `max()`

---

## ตัวอย่างการคำนวณ

สมมติคะแนนสามบรรทัดเป็น

```text
50 60
55 40 100
45 90 0 66
```

ความยาวสูงสุดคือ `4` หลังเติมศูนย์จะเปรียบเทียบได้ดังนี้

| ตำแหน่งข้อ | Quiz 1 | Quiz 2 | Quiz 3 | คะแนนที่เลือก |
|---:|---:|---:|---:|---:|
| 1 | `50` | `55` | `45` | `55` |
| 2 | `60` | `40` | `90` | `90` |
| 3 | `0` | `100` | `0` | `100` |
| 4 | `0` | `0` | `66` | `66` |

คะแนนรวมจึงเป็น `55 + 90 + 100 + 66 = 311`

---

## ลำดับการทำงานของโปรแกรม

1. อ่านคะแนนของ Quiz 1, 2 และ 3 ตามลำดับ
2. หาความยาวมากที่สุดของสามรายการ
3. เติม `0` ต่อท้ายรายการที่สั้นกว่าให้ยาวเท่ากัน
4. ใช้ `max()` เลือกคะแนนสูงสุดของทุกตำแหน่งและสะสมผลรวม
5. แสดง `total_score` เป็นจำนวนเต็มหนึ่งบรรทัด

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q3_A3.py
# Problem   : Grader Score
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input grader scores for three quizzes
q1_scores = [int(score) for score in input().split()]
q2_scores = [int(score) for score in input().split()]
q3_scores = [int(score) for score in input().split()]

# Calculate the total number of quizzes
total_quizzes = max(len(q1_scores), len(q2_scores), len(q3_scores))

# Ensure all lists have the same length by padding with zeros
q1_scores += [0] * (total_quizzes - len(q1_scores))
q2_scores += [0] * (total_quizzes - len(q2_scores))
q3_scores += [0] * (total_quizzes - len(q3_scores))

# Initialize total score to 0
total_score = 0

# Calculate the total score by taking the maximum score from each quiz
for i in range(total_quizzes):
    total_score += max(q1_scores[i], q2_scores[i], q3_scores[i])

# Output the total score
print(total_score)
```
