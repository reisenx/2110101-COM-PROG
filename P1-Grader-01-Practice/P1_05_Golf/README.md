<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Golf ★★ (
      <a href="https://drive.google.com/file/d/1wTfOJEajV7A6x-R_k33MWWbuWgFoDuwP/view?usp=drive_link">
        <code>P1_05_Golf</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**อ่านข้อมูลและเก็บผลรวม**](#อ่านข้อมูลและเก็บผลรวม)
-   [**คำนวณสโตรคปรับปรุง**](#คำนวณสโตรคปรับปรุง)
-   [**คำนวณแต้มต่อและคะแนนสุทธิ**](#คำนวณแต้มต่อและคะแนนสุทธิ)
-   [**ลำดับการแสดงผล**](#ลำดับการแสดงผล)
-   [**Solution**](#solution)

---

## อ่านข้อมูลและเก็บผลรวม

โจทย์ให้ข้อมูลการเล่นกอล์ฟทั้งหมด `9` หลุม หลุมละหนึ่งบรรทัด แต่ละบรรทัดมี
จำนวนเต็มสามจำนวนตามลำดับ ได้แก่

-   `par` คือพาร์ของหลุม
-   `stroke` คือจำนวนครั้งที่ผู้เล่นตีจริง
-   `select` เป็น `1` เมื่อเลือกหลุมนี้มาคำนวณแต้มต่อ และเป็น `0`
    เมื่อไม่เลือก

คำสั่งต่อไปนี้แยกข้อมูลในหนึ่งบรรทัด แปลงแต่ละค่าเป็น `int`
แล้วเก็บลงในตัวแปรทั้งสาม

```python
par, stroke, select = [int(num) for num in input().split()]
```

ก่อนเริ่มอ่านข้อมูล โปรแกรมกำหนดผลรวมทั้งสามค่าให้เป็น `0`
จากนั้นใช้ลูป `for _ in range(9)` อ่านข้อมูลครบเก้าหลุม
แล้วสะสมค่าด้วยตัวดำเนินการ `+=`

-   `total_par` เก็บผลรวมพาร์ของทุกหลุม
-   `total_stroke` เก็บผลรวมจำนวนครั้งที่ตีจริงของทุกหลุม
-   `total_modified_stroke` เก็บผลรวมสโตรคปรับปรุงของหลุมที่ถูกเลือก

## คำนวณสโตรคปรับปรุง

สำหรับหลุมหนึ่ง สโตรคปรับปรุงคือค่าที่น้อยกว่าระหว่างจำนวนครั้งที่ตีจริงกับ
พาร์บวกสอง เขียนเป็นสูตรได้ว่า

$$
m_i = \min(\text{stroke}_i,\ \text{par}_i + 2)
$$

ใน Python ตรงกับ `min(stroke, par + 2)` แต่เราต้องนำมารวมเฉพาะหลุมที่
`select` เป็น `1` ด้วย จึงคูณด้วย `select`

```python
total_modified_stroke += select * min(stroke, par + 2)
```

การคูณนี้ทำหน้าที่เหมือนสวิตช์: ถ้า `select` เป็น `1` ค่าที่คำนวณได้จะถูกนำไป
รวม แต่ถ้าเป็น `0` ผลคูณจะเป็น `0` และไม่กระทบผลรวม

| `par` | `stroke` | `select` | `min(stroke, par + 2)` | ค่าที่นำไปรวม |
|---:|---:|---:|---:|---:|
| `3` | `6` | `1` | `5` | `1 * 5 = 5` |
| `5` | `6` | `0` | `6` | `0 * 6 = 0` |

## คำนวณแต้มต่อและคะแนนสุทธิ

ให้ $P$ เป็นพาร์รวม, $T$ เป็นสโตรครวม และ $M$ เป็นผลรวมสโตรคปรับปรุง
ของหลุมที่ถูกเลือก แต้มต่อ $H$ คำนวณจาก

$$
H = \left\lfloor 0.8(1.5M - P) \right\rfloor
$$

ส่วนคะแนนสุทธิ $S$ คือ

$$
S = T - H
$$

สูตรทั้งสองตรงกับคำสั่ง Python ดังนี้

```python
handicap = math.floor(0.8 * (1.5 * total_modified_stroke - total_par))
total_score = total_stroke - handicap
```

ตัวอย่างในคำอธิบายโจทย์มี $T = 43$, $P = 36$ และ $M = 28$ จึงได้
`handicap = math.floor(0.8 * (1.5 * 28 - 36))` เท่ากับ `4`
และได้คะแนนสุทธิ `43 - 4` เท่ากับ `39`

> [!WARNING]
>
> `math.floor(x)` หาจำนวนเต็มที่มากที่สุดซึ่งไม่เกิน `x`
> จึงไม่ใช่การปัดเป็นจำนวนเต็มที่ใกล้ที่สุด โดยเฉพาะเมื่อค่าเป็นลบ
> เช่น `math.floor(-4.8)` ได้ `-5` ไม่ใช่ `-4`

## ลำดับการแสดงผล

โจทย์กำหนดผลลัพธ์สามบรรทัด โปรแกรมจึงเรียก `print()` ตามลำดับนี้

1.  `total_stroke` — สโตรครวม
2.  `handicap` — แต้มต่อ
3.  `total_score` — คะแนนสุทธิ

---

# Solution

```python
# --------------------------------------------------
# File Name : P1_05_Golf.py
# Problem   : Part-I Golf
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

import math

# Initialize variables
total_par = 0
total_stroke = 0
total_modified_stroke = 0

# Read score of each hole
for _ in range(9):
    par, stroke, select = [int(num) for num in input().split()]
    # Calculate total par stroke and modified stroke
    total_par += par
    total_stroke += stroke
    total_modified_stroke += select * min(stroke, par + 2)

# Calculate the score
handicap = math.floor(0.8 * (1.5 * total_modified_stroke - total_par))
total_score = total_stroke - handicap

# Output the result
print(total_stroke)
print(handicap)
print(total_score)
```
