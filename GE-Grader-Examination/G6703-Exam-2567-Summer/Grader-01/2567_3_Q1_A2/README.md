<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Scout ★★ (
      <a href="https://drive.google.com/file/d/1cST70loS_Wfreh2mwh7RSmKwLeR216ZH/view?usp=sharing">
        <code>2567_3_Q1_A2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิดการแบ่งหมู่**](#แนวคิดการแบ่งหมู่)
-   [**สร้างรายการสีประจำหมู่**](#สร้างรายการสีประจำหมู่)
-   [**ตอบคำถามตามลำดับ**](#ตอบคำถามตามลำดับ)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## แนวคิดการแบ่งหมู่

ข้อมูลนำเข้ามีสี่ส่วนตามลำดับ

1.  รายชื่อลูกเสือทั้งหมดในแถว คั่นด้วยช่องว่าง โดยชื่อไม่ซ้ำกัน
2.  จำนวนลูกเสือต่อหนึ่งหมู่ `group_size`
3.  สีประจำหมู่ เรียงจากหมู่แรกถึงหมู่สุดท้าย หมู่ละหนึ่งบรรทัด
4.  รายชื่อลูกเสือที่ต้องการถามสี คั่นด้วยช่องว่าง

ถ้ามีลูกเสือทั้งหมด $N$ คน และแต่ละหมู่รับได้ $S$ คน จำนวนหมู่คือ

$$
\text{group amount} = \left\lceil \frac{N}{S} \right\rceil
$$

เครื่องหมาย $\lceil\ \rceil$ หมายถึงการปัดขึ้น เพราะถึงหมู่สุดท้ายจะมีสมาชิก
ไม่ครบ $S$ คน ก็ยังต้องนับเป็นอีกหนึ่งหมู่ ในภาษา Python เขียนได้เป็น

```python
group_amount = math.ceil(len(boys) / group_size)
```

ตัวอย่างเช่น มีลูกเสือ `14` คน หมู่ละ `4` คน จะต้องรับชื่อสีทั้งหมด
`math.ceil(14 / 4) = 4` หมู่ โดยหมู่สุดท้ายมีเพียง 2 คน

---

## สร้างรายการสีประจำหมู่

โปรแกรมสร้าง `group_names` ให้ตำแหน่งของสีตรงกับตำแหน่งของชื่อลูกเสือใน
`boys` โดยอ่านสีหนึ่งครั้งแล้วทำซ้ำสีนั้น `group_size` ตำแหน่ง

```python
group_names += [input().strip()] * group_size
```

ถ้าหมู่ละ 4 คน และสามหมู่แรกมีสี `Yellow`, `Blue`, `Red` ส่วนหนึ่งของ
รายการจะมีลักษณะดังนี้

```text
ตำแหน่งลูกเสือ:  0       1       2       3       4     5     6     7
สีประจำหมู่:    Yellow  Yellow  Yellow  Yellow  Blue  Blue  Blue  Blue
```

สีของหมู่สุดท้ายอาจถูกทำซ้ำจน `group_names` ยาวเกินจำนวนลูกเสือจริง
ส่วนที่เกินไม่ก่อให้เกิดปัญหา เพราะโปรแกรมจะค้นเฉพาะตำแหน่งที่มีอยู่ใน
`boys`

---

## ตอบคำถามตามลำดับ

สำหรับชื่อที่ต้องการถามแต่ละชื่อ โปรแกรมทำงานสองขั้นตอน

1.  หาเลขตำแหน่งของชื่อในแถวด้วย `boys.index(name)`
2.  ใช้เลขตำแหน่งเดียวกันอ่านสีจาก `group_names[idx]`

ผลลัพธ์ถูกเพิ่มลงใน `query_results` ตามลำดับชื่อที่ถาม ไม่ใช่ตามลำดับหมู่
สุดท้ายใช้ `" ".join(query_results)` เชื่อมทุกสีด้วยช่องว่างและแสดงผลหนึ่ง
บรรทัด

ตามเงื่อนไขโจทย์ ชื่อลูกเสือไม่ซ้ำกันและชื่อที่นำมาถามต้องอยู่ในรายชื่อเดิม
จึงสามารถใช้ `list.index()` ระบุตำแหน่งได้แน่นอน

---

## ตัวอย่างการทำงาน

สมมติรายชื่อเป็น

```text
A B C D E F G H I J K L M N
```

กำหนดหมู่ละ 4 คนและให้สีตามลำดับเป็น `Yellow`, `Blue`, `Red`, `White`
จะได้การแบ่งหมู่ดังนี้

-   `A B C D` อยู่หมู่ `Yellow`
-   `E F G H` อยู่หมู่ `Blue`
-   `I J K L` อยู่หมู่ `Red`
-   `M N` อยู่หมู่ `White` แม้หมู่สุดท้ายมีสมาชิกไม่ครบ 4 คน

เมื่อถามชื่อ `A E G` โปรแกรมพบตำแหน่ง `0`, `4`, `6` และอ่านสีในตำแหน่ง
เดียวกัน จึงแสดงผลตามลำดับที่ถามเป็น

```text
Yellow Blue Blue
```

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_3_Q1_A2.py
# Problem   : Scout
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------

import math

# Input boys names
boys = input().strip().split()

# Input group size and calculate the number of groups
group_size = int(input())
group_amount = math.ceil(len(boys) / group_size)

# Input group names and multiply them by the group size
group_names = []
for _ in range(group_amount):
    group_names += [input().strip()] * group_size

# Input names to query
query_names = input().strip().split()

# For each queried name, find the corresponding group name
query_results = []
for name in query_names:
    idx = boys.index(name)
    query_results.append(group_names[idx])

# Output the group names for the queried names
print(" ".join(query_results))
```
