<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Body Surface Area ★★ (
      <a href="https://drive.google.com/file/d/19WB4pcdU4XHMoAIHkf7DW2LBYjxIbLaX/view?usp=drive_link">
        <code>01_Expr_04</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ข้อมูลที่โจทย์ให้**](#ข้อมูลที่โจทย์ให้)
-   [**แปลงสูตรเป็น Python**](#แปลงสูตรเป็น-python)
-   [**ลำดับการคำนวณและแสดงผล**](#ลำดับการคำนวณและแสดงผล)
-   [**Solution**](#solution)

---

## ข้อมูลที่โจทย์ให้

โจทย์ต้องการคำนวณพื้นที่ผิวร่างกาย (body surface area) จากข้อมูล 2 ค่า ได้แก่

-   `w` คือ **น้ำหนัก** หน่วยกิโลกรัม รับด้วย `float(input())`
-   `h` คือ **ส่วนสูง** หน่วยเซนติเมตร รับด้วย `float(input())`

การรับเป็น `float` ทำให้โปรแกรมรองรับทั้งจำนวนเต็มอย่าง `56` และจำนวนจริงอย่าง
`56.5`

> [!NOTE]
>
> comment ใน source code เขียนว่า `Input width and height` แต่ตามโจทย์ `w`
> ย่อมาจาก **weight (น้ำหนัก)** ไม่ใช่ width (ความกว้าง)

---

## แปลงสูตรเป็น Python

สูตรทั้งสามมีรากที่สอง เลขยกกำลังทศนิยม และลอการิทึม จึงต้อง `import math`
เพื่อใช้ `math.sqrt()` และ `math.log10()` ส่วนเครื่องหมายยกกำลังใน Python คือ
`**`

**1. สูตร Mosteller**

$$
BSA_{Mosteller} = \frac{\sqrt{w h}}{60}
$$

เขียนเป็น Python ได้ตรง ๆ ว่า

```python
math.sqrt(w * h) / 60
```

**2. สูตร Haycock**

$$
BSA_{Haycock} = 0.024265 \times w^{0.5378} \times h^{0.3964}
$$

เลขชี้กำลัง `0.5378` และ `0.3964` เป็นเลขทศนิยม แต่ใช้ `**` ได้เหมือน
เลขชี้กำลังจำนวนเต็ม

```python
0.024265 * (w**0.5378) * (h**0.3964)
```

**3. สูตร Boyd**

$$
BSA_{Boyd}
= 0.0333 \times
w^{\left(0.6157 - 0.0188\log_{10}(w)\right)} \times h^{0.3}
$$

สูตรนี้ต่างจากสองสูตรแรกตรงที่เลขชี้กำลังของ `w` เปลี่ยนตามค่าน้ำหนัก
จึงต้องคำนวณ `math.log10(w)` ก่อน แล้วครอบเลขชี้กำลังทั้งหมดด้วยวงเล็บ

```python
0.0333 * (w ** (0.6157 - (0.0188 * math.log10(w)))) * (h**0.3)
```

> [!WARNING]
>
> `math.log10(w)` นิยามได้เมื่อ `w > 0` เท่านั้น การส่งน้ำหนักเป็นศูนย์หรือติดลบ
> จะทำให้โปรแกรมเกิด error

---

## ลำดับการคำนวณและแสดงผล

เมื่ออ่าน `w` และ `h` แล้ว โปรแกรมคำนวณสูตรตามลำดับ Mosteller, Haycock และ
Boyd จากนั้น `print()` คำตอบแต่ละค่าออกมาคนละบรรทัด

```text
<ผลจากสูตร Mosteller>
<ผลจากสูตร Haycock>
<ผลจากสูตร Boyd>
```

ผลลัพธ์ไม่มีชื่อสูตรนำหน้าและโจทย์ไม่ได้กำหนดให้ปัดเศษ จึงพิมพ์ค่า `float`
ที่คำนวณได้โดยตรง สิ่งสำคัญคือห้ามสลับลำดับทั้งสามบรรทัด

---

# Solution

```python
# --------------------------------------------------
# File Name : 01_Expr_04.py
# Problem   : Body Surface Area
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math

# Input width and height
w = float(input())
h = float(input())

# Mosteller's formula for body surface area
mosteller = math.sqrt(w * h) / 60
print(mosteller)

# Haycock's formula for body surface area
haycock = 0.024265 * (w**0.5378) * (h**0.3964)
print(haycock)

# Boyd's formula for body surface area
boyd = 0.0333 * (w ** (0.6157 - (0.0188 * math.log10(w)))) * (h**0.3)
print(boyd)
```
