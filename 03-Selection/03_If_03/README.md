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

-   [**การเก็บค่าสูงสุดและต่ำสุดแบบสะสม**](#การเก็บค่าสูงสุดและต่ำสุดแบบสะสม)
-   [**การคำนวณคะแนนสุดท้าย**](#การคำนวณคะแนนสุดท้าย)
-   [**การปัดเศษ**](#การปัดเศษ)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## การเก็บค่าสูงสุดและต่ำสุดแบบสะสม

โจทย์รับคะแนนของกรรมการทั้ง 4 คนเป็นจำนวนจริงในบรรทัดเดียวกัน
โปรแกรมจึงใช้ `input().strip().split()` แยกข้อมูลด้วยช่องว่าง
แล้วแปลงคะแนนแต่ละค่าเป็น `float`

เนื่องจากโจทย์ต้องการให้ฝึกใช้คำสั่ง `if` แทน `min()` และ `max()`
เราจึงเริ่มจากสมมติว่าคะแนนแรกเป็นทั้งค่าสูงสุดและค่าต่ำสุด

```python
max_score = scores[0]
min_score = scores[0]
```

จากนั้นนำคะแนนที่เหลือมาเปรียบเทียบทีละค่า ถ้าคะแนนใหม่มากกว่าค่าสูงสุดเดิม
ก็แทนที่ `max_score` และถ้าคะแนนใหม่น้อยกว่าค่าต่ำสุดเดิม
ก็แทนที่ `min_score` วิธีนี้เรียกว่า **การเก็บค่าสูงสุดและต่ำสุดแบบสะสม**
เพราะหลังจบแต่ละรอบ ตัวแปรทั้งสองจะเก็บขอบเขตของคะแนนที่ตรวจไปแล้วเสมอ

กรณีคะแนนซ้ำกัน เครื่องหมาย `>` และ `<` จะไม่ทำให้ตัวแปรเปลี่ยนค่า
แต่ค่าที่เก็บไว้ยังคงเป็นค่าสูงสุดและค่าต่ำสุดที่ถูกต้อง เช่นเดียวกับกรณีที่คะแนนทั้ง
4 ค่าเท่ากัน

## การคำนวณคะแนนสุดท้าย

กติกาให้ตัดคะแนนสูงสุด 1 ค่าและคะแนนต่ำสุด 1 ค่า
แล้วหาค่าเฉลี่ยของคะแนนอีก 2 ค่า หากให้ `score_total` เป็นผลรวมของคะแนนทั้งหมด
จะได้สูตร

$$
\text{average score}
= \frac{\text{score total} - \text{maximum score} - \text{minimum score}}{2}
$$

ซึ่งตรงกับนิพจน์ Python ดังนี้

```python
average_score = (score_total - max_score - min_score) / 2
```

ถ้าค่าสูงสุดหรือค่าต่ำสุดปรากฏซ้ำ การลบตามสูตรจะลบออกอย่างละ 1 ค่าเท่านั้น
จึงยังตรงกับกติกา เช่น คะแนน `8 8 9 10` จะตัด `8` หนึ่งค่าและ `10` หนึ่งค่า
เหลือ `8` กับ `9` สำหรับหาค่าเฉลี่ย

## การปัดเศษ

โปรแกรมใช้ `round(average_score, 2)` เพื่อปัดค่าตัวเลขให้เหลือไม่เกิน 2
ตำแหน่งหลังจุดทศนิยม แล้วส่งค่านั้นให้ `print()`

> [!NOTE]
>
> `round(value, 2)` ปัด **ค่าตัวเลข** แต่ไม่ได้บังคับให้แสดงเลขศูนย์ท้ายครบ 2
> ตำแหน่ง ดังนั้นคำตอบ `9.50` จะแสดงเป็น `9.5`
> ซึ่งสอดคล้องกับรูปแบบผลลัพธ์ในตัวอย่างของโจทย์

## ตัวอย่างการทำงาน

เมื่อข้อมูลเข้าเป็น `9.84 9.30 9.42 9.58`

-   ผลรวมคะแนนคือ `38.14`
-   ค่าสูงสุดคือ `9.84`
-   ค่าต่ำสุดคือ `9.30`
-   คะแนนสุดท้ายคือ `(38.14 - 9.84 - 9.30) / 2` ซึ่งเท่ากับ `9.5`

โปรแกรมจึงแสดงผล `9.5`

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
