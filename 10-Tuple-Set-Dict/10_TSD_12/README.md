<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Union Intersection ★ (
      <a href="https://drive.google.com/file/d/1oa1clo95mX24uYK4xUEI-aN3lxRzarnW/view?usp=drive_link">
        <code>10_TSD_12</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิดของเซต**](#แนวคิดของเซต)
-   [**การหา Union และ Intersection**](#การหา-union-และ-intersection)
-   [**ลำดับการทำงานของโปรแกรม**](#ลำดับการทำงานของโปรแกรม)
-   [**ข้อควรสังเกต**](#ข้อควรสังเกต)
-   [**Solution**](#solution)

---

## แนวคิดของเซต

`set` คือโครงสร้างข้อมูลที่เก็บสมาชิกโดยไม่เก็บค่าซ้ำ เช่น ข้อมูล
`2 5 4 3 3 2` เมื่อนำมาสร้างเซตจะเหลือสมาชิก `{2, 3, 4, 5}`
แม้ลำดับที่แสดงอาจไม่เหมือนเดิม แต่จำนวนสมาชิกยังคงเท่ากับ `4`

โปรแกรมอ่านจำนวนเต็มในแต่ละบรรทัดและสร้างเซตด้วย set comprehension

```python
current_set = {int(num) for num in input().split()}
```

`input().split()` แยกข้อมูลด้วยช่องว่าง, `int(num)` แปลงแต่ละค่าเป็นจำนวนเต็ม
และวงเล็บปีกกา `{...}` สร้างเป็นเซต จึงรองรับทั้งจำนวนบวก ศูนย์
และจำนวนลบ โดยค่าที่ซ้ำกันในบรรทัดเดียวจะนับเพียงครั้งเดียว

---

## การหา Union และ Intersection

กำหนดให้เซตที่รับเข้ามาคือ \(S_1, S_2, \ldots, S_n\)

-   **Union** รวมสมาชิกที่ปรากฏในอย่างน้อยหนึ่งเซต

    \[
    U = S_1 \cup S_2 \cup \cdots \cup S_n
    \]

    ใน Python ใช้ `union |= current_set` ซึ่งมีความหมายเดียวกับ
    `union = union | current_set`

-   **Intersection** เก็บเฉพาะสมาชิกที่ปรากฏอยู่ในทุกเซต

    \[
    I = S_1 \cap S_2 \cap \cdots \cap S_n
    \]

    ใน Python ใช้ `intersection &= current_set` ซึ่งมีความหมายเดียวกับ
    `intersection = intersection & current_set`

เซต union เริ่มจากเซตว่างได้ เพราะ \(\varnothing \cup S = S\)
แต่ intersection เริ่มจากเซตว่างไม่ได้ เพราะ
\(\varnothing \cap S = \varnothing\) เสมอ โปรแกรมจึงคัดลอกเซตแรกเข้า
`intersection` ก่อนด้วย `intersection |= current_set`
จากนั้นจึงค่อยใช้ `&=` กับทุกเซต

> [!NOTE]
>
> ในรอบแรก `intersection` มีค่าเท่ากับ `current_set` อยู่แล้ว
> การทำ `intersection &= current_set` ซ้ำในรอบเดียวกันจึงไม่เปลี่ยนค่า

---

## ลำดับการทำงานของโปรแกรม

สมมติรับเซตสามบรรทัดตามตัวอย่าง

```text
2 3
2 5 4 3
1 2 1 2 3 1 2 1 2 1
```

หลังตัดค่าซ้ำ จะได้ \(S_1 = \{2,3\}\),
\(S_2 = \{2,3,4,5\}\) และ \(S_3 = \{1,2,3\}\)

| หลังประมวลผล | `union` | `intersection` |
| :--: | :-- | :-- |
| เซตที่ 1 | `{2, 3}` | `{2, 3}` |
| เซตที่ 2 | `{2, 3, 4, 5}` | `{2, 3}` |
| เซตที่ 3 | `{1, 2, 3, 4, 5}` | `{2, 3}` |

โจทย์ต้องการ **ขนาด** ของทั้งสองเซต ไม่ได้ต้องการสมาชิกภายในเซต
จึงใช้ `len(union)` และ `len(intersection)` แล้วแสดงผลตามลำดับดังนี้

1. จำนวนสมาชิกของ union
2. จำนวนสมาชิกของ intersection

สำหรับตัวอย่างนี้จึงได้ `5` และ `2` คนละบรรทัด

---

## ข้อควรสังเกต

-   ลำดับของสมาชิกใน `set` ไม่แน่นอน แต่ไม่กระทบคำตอบเพราะโปรแกรมแสดงเพียง
    `len()`
-   ถ้ามีสมาชิกซ้ำหลายครั้ง เช่น `1 2 1 2` จะนับเป็นสมาชิกเพียงสองค่า
-   ถ้าไม่มีค่าใดอยู่ในทุกเซต `intersection` จะกลายเป็นเซตว่างและบรรทัดที่สอง
    จะแสดง `0`
-   จำนวนลบเป็นสมาชิกของเซตได้ตามปกติ เช่น `-1` กับ `1` เป็นคนละค่า

---

# Solution

```python
# --------------------------------------------------
# File Name : 10_TSD_12.py
# Problem   : Union Intersection
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input number of sets
n = int(input())

# Initialize sets for union and intersection
union = set()
intersection = set()

# Process each set
for i in range(n):
    # Read the current set of integers
    current_set = {int(num) for num in input().split()}

    # Update union and intersection sets
    if i == 0:
        intersection |= current_set
    union |= current_set
    intersection &= current_set

# Output length of union and intersection
print(len(union))
print(len(intersection))
```
