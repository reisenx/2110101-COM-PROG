<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Compound Interest ★☆ (
      <a href="https://drive.google.com/file/d/1DmAZ8jdqgMcyNonBr82crODpALnPiDP-/view?usp=sharing">
        <code>2567_1_Q3_A2-S</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ดอกเบี้ยทบต้นตามโจทย์**](#ดอกเบี้ยทบต้นตามโจทย์)
-   [**การเลือกอัตราดอกเบี้ย**](#การเลือกอัตราดอกเบี้ย)
-   [**พฤติกรรมของโค้ดต้นฉบับ**](#พฤติกรรมของโค้ดต้นฉบับ)
-   [**การแสดงผล**](#การแสดงผล)
-   [**Solution**](#solution)

---

## ดอกเบี้ยทบต้นตามโจทย์

เงินฝากของแต่ละเดือนคิดดอกเบี้ยจากยอดเงินล่าสุด
ดอกเบี้ยที่ได้รับจึงถูกนำไปรวมเป็นเงินต้นของเดือนถัดไป หรือที่เรียกว่า
**ดอกเบี้ยทบต้น**

ถ้าเงินก่อนคิดดอกเบี้ยคือ $M$ และอัตราดอกเบี้ยต่อปีคือ $r$
โจทย์กำหนดให้คิดดอกเบี้ยหนึ่งเดือนเป็น

$$
\text{interest} = M \times r \times \frac{1}{12}
$$

ดังนั้นยอดใหม่ตามข้อกำหนดใน PDF คือ

$$
M_{\text{next}} = M + M \times r \times \frac{1}{12}
$$

ระหว่างคำนวณต้องเก็บค่าทศนิยมเต็มไว้ และปัดเศษเฉพาะตอนแสดงผลครั้งสุดท้าย

---

## การเลือกอัตราดอกเบี้ย

อัตราดอกเบี้ยวนซ้ำทุกสี่เดือนเป็น `1%`, `2%`, `3%`, `4%`
โค้ดจัดรายการให้ตำแหน่ง `0` เป็น `4%` เพื่อใช้เศษจากการหารเดือนด้วย `4`

```python
INTEREST_RATE = [0.04, 0.01, 0.02, 0.03]
```

จึงได้การจับคู่ดังนี้

| เดือนที่ | `month % 4` | อัตราที่เลือก |
|---:|---:|---:|
| 1 | 1 | `0.01` |
| 2 | 2 | `0.02` |
| 3 | 3 | `0.03` |
| 4 | 0 | `0.04` |

เดือนที่ `5` จะกลับมาใช้ตำแหน่ง `1` อีกครั้ง ทำให้วงรอบดำเนินต่อไปได้

---

## พฤติกรรมของโค้ดต้นฉบับ

> [!WARNING]
>
> PDF ระบุว่าอัตรา `1%` ถึง `4%` เป็นอัตรา **ต่อปี** และต้องหารด้วย `12`
> ก่อนคิดดอกเบี้ยหนึ่งเดือน แต่โค้ดต้นฉบับใช้คำสั่ง
> `current_money += current_money * INTEREST_RATE[month % 4]`
> โดยไม่มีตัวคูณ `1 / 12`
>
> ตัวอย่างเช่น เงิน `12000` บาทเป็นเวลา `1` เดือน ตาม PDF ควรได้ `12010.0`
> แต่โค้ดชุดนี้คำนวณจริงเป็น `12000 + 12000 * 0.01 = 12120.0`

ส่วน Solution ด้านล่างคงโค้ดต้นฉบับไว้ตามไฟล์ `.py`
คำอธิบายนี้จึงแยกข้อกำหนดของโจทย์ออกจากพฤติกรรมที่โปรแกรมทำจริงอย่างชัดเจน

---

## การแสดงผล

หลังวนครบ `total_months` รอบ โปรแกรมใช้

```python
print(round(current_money, 2))
```

`round(..., 2)` ปัดให้มีทศนิยมอย่างมากสองตำแหน่ง ไม่ได้บังคับให้พิมพ์ศูนย์
ท้ายจำนวนเสมอ เช่นอาจแสดง `12120.0` แทน `12120.00`

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q3_A2-S.py
# Problem   : Compound Interest
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Interest rates for each month
INTEREST_RATE = [0.04, 0.01, 0.02, 0.03]

# Extract initial money and total months from the input
data = input().split()
initial_money = float(data[0])
total_months = int(data[1])

# Initialize current money with the initial money
current_money = initial_money

# Calculate the money after each month using the interest rates
for month in range(1, total_months + 1):
    current_money += current_money * INTEREST_RATE[month % 4]

# Output
print(round(current_money, 2))
```
