<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    An Expression ★★ (
      <a href="https://drive.google.com/file/d/1QjFbvlGZVW_DvMut1K-ZNRXlswoMD_Lt/view?usp=drive_link">
        <code>01_Expr_03</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การแยกนิพจน์เป็นเศษและส่วน**](#การแยกนิพจน์เป็นเศษและส่วน)
-   [**การแปลงฟังก์ชันคณิตศาสตร์เป็น Python**](#การแปลงฟังก์ชันคณิตศาสตร์เป็น-python)
-   [**รากที่สามและเลขชี้กำลังซ้อน**](#รากที่สามและเลขชี้กำลังซ้อน)
-   [**การคำนวณคำตอบและปัดเศษ**](#การคำนวณคำตอบและปัดเศษ)
-   [**Solution**](#solution)

---

## การแยกนิพจน์เป็นเศษและส่วน

โจทย์ไม่มีข้อมูลนำเข้า และต้องคำนวณนิพจน์เพียงค่าเดียว
นิพจน์มีรูปเป็นเศษส่วนขนาดใหญ่ดังนี้

$$
\frac{
    \pi - \frac{10!}{8^8}
    + (\ln 9.7)^{\frac{7}{\sqrt{71}} - \sin(40^\circ)}
}{
    (1.2)^{\sqrt[3]{2.3}}
}
$$

การแยกตัวเศษเก็บใน `numerator` และตัวส่วนเก็บใน `denominator`
ช่วยให้มองวงเล็บและลำดับการคำนวณได้ชัดเจน ก่อนนำสองค่านี้มาหารกัน

---

## การแปลงฟังก์ชันคณิตศาสตร์เป็น Python

แต่ละส่วนของตัวเศษมีคำสั่งในโมดูล `math` ที่ตรงกับสูตร

-   $\pi$ ใช้ `math.pi`
-   $10!$ ใช้ `math.factorial(10)`
-   $\ln(9.7)$ ใช้ `math.log(9.7)` ซึ่งเป็นลอการิทึมธรรมชาติฐาน $e$
-   $\sqrt{71}$ ใช้ `math.sqrt(71)`
-   $\sin(40^\circ)$ ใช้ `math.sin(math.radians(40))`

เมื่อนำทุกส่วนมารวมกัน จะได้ตัวเศษดังนี้

```python
numerator = (
    math.pi
    - (math.factorial(10) / (8**8))
    + (math.log(9.7)) ** ((7 / math.sqrt(71)) - math.sin(math.radians(40)))
)
```

> [!NOTE]
>
> `math.sin()` รับมุมหน่วยเรเดียน แต่โจทย์ให้มุม $40^\circ$
> จึงต้องแปลงองศาด้วย `math.radians(40)` ก่อนส่งค่าให้ `math.sin()`

---

## รากที่สามและเลขชี้กำลังซ้อน

ตัวส่วนมีรากที่สามอยู่ในตำแหน่งเลขชี้กำลัง โดยแปลงรากที่สามเป็น
เลขชี้กำลังเศษส่วนได้ว่า

$$
\sqrt[3]{2.3} = 2.3^{\frac{1}{3}}
$$

ดังนั้น $(1.2)^{\sqrt[3]{2.3}}$ จึงเขียนเป็น Python ได้ว่า

```python
denominator = 1.2 ** (2.3 ** (1 / 3))
```

วงเล็บแสดงลำดับของเลขชี้กำลังซ้อนอย่างชัดเจน: คำนวณ
`2.3 ** (1 / 3)` ก่อน แล้วใช้ผลนั้นเป็นเลขชี้กำลังของ `1.2`
ซึ่งไม่เหมือนกับการคำนวณ `(1.2 ** 2.3) ** (1 / 3)`

---

## การคำนวณคำตอบและปัดเศษ

ขั้นสุดท้ายคือนำตัวเศษหารด้วยตัวส่วน แล้วใช้ `round(..., 6)`
ปัดผลลัพธ์ให้เหลือทศนิยมไม่เกิน 6 ตำแหน่งก่อนแสดงผล

```python
print(round(numerator / denominator, 6))
```

โปรแกรมจึงแสดงผลเพียงหนึ่งค่าในหนึ่งบรรทัด โดยไม่ต้องเรียก `input()`

---

# Solution

```python
# --------------------------------------------------
# File Name : 01_Expr_03.py
# Problem   : An Expression
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math

# Calculate numerator and denominator of a fraction
numerator = (
    math.pi
    - (math.factorial(10) / (8**8))
    + (math.log(9.7)) ** ((7 / math.sqrt(71)) - math.sin(math.radians(40)))
)
denominator = 1.2 ** (2.3 ** (1 / 3))

# Output
# Round the result to 6 decimal places
print(round(numerator / denominator, 6))
```
