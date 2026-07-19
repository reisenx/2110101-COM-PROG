<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Loan Interest ★★ (
      <a href="https://drive.google.com/file/d/1DyMUTyMbEAQM_3bRSgrWTzRjZ0sHP4Lr/view?usp=sharing">
        <code>2567_1_Q2_A2-S</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิดดอกเบี้ยแบบลดต้นลดดอก**](#แนวคิดดอกเบี้ยแบบลดต้นลดดอก)
-   [**ลำดับการคำนวณ**](#ลำดับการคำนวณ)
-   [**เงื่อนไขที่ผ่อนไม่หมด**](#เงื่อนไขที่ผ่อนไม่หมด)
-   [**การแสดงผล**](#การแสดงผล)
-   [**Solution**](#solution)

---

## แนวคิดดอกเบี้ยแบบลดต้นลดดอก

โจทย์รับข้อมูล 3 ค่า เรียงตามบรรทัดดังนี้

1. เงินต้นเริ่มต้น `initial_debt` หรือ $P$
2. อัตราดอกเบี้ยต่อปี `interest_rate` หรือร้อยละ $R$
3. เงินที่ตั้งใจผ่อนต่อเดือน `monthly_pay` หรือ $M$

โปรแกรมเปลี่ยนอัตราร้อยละให้เป็นทศนิยม $r=R/100$ ก่อนด้วย
`interest_rate = float(input()) / 100` เช่น `15` เปลี่ยนเป็น `0.15`
จากนั้นดอกเบี้ยของเดือนที่ $t$ คำนวณจากเงินต้นคงเหลือต้นเดือน
$B_{t-1}$ ดังนี้

$$
I_t = B_{t-1} \times \frac{r}{12}
$$

เมื่อ `interest_rate` เก็บ $r$ แล้ว สูตรนี้ตรงกับ Python ว่า

```python
interest = current_debt * (interest_rate / 12)
```

เงินที่จ่ายในแต่ละเดือนจะถูกนำไปจ่ายดอกเบี้ยก่อน ส่วนที่เหลือ
$M-I_t$ จึงนำไปลดเงินต้น ทำให้เงินต้นใหม่เป็น

$$
B_t = \max(0, B_{t-1} - (M-I_t))
$$

ซึ่งตรงกับ

```python
current_debt = max(0, current_debt - (monthly_pay - interest))
```

การใช้ `max(0, ...)` ทำให้เดือนสุดท้ายมีเงินต้นคงเหลือเป็น `0`
แม้ยอดเงินต้นบวกดอกเบี้ยของเดือนนั้นจะน้อยกว่าเงินผ่อนปกติ กล่าวคือ
เดือนสุดท้ายจ่ายเพียงยอดที่เหลือจริง ไม่ทำให้หนี้กลายเป็นค่าติดลบ

---

## ลำดับการคำนวณ

เมื่อเงินผ่อนมากพอ โปรแกรมทำซ้ำตราบใดที่ `current_debt > 0`

1. คำนวณดอกเบี้ยจากเงินต้นคงเหลือ **ก่อน** ชำระของเดือนนั้น
2. หักส่วนของเงินผ่อนที่นำไปลดเงินต้น
3. บวกดอกเบี้ยเดือนนี้เข้า `total_interest`
4. เพิ่ม `total_month` อีก `1`

ตัวอย่าง เมื่อ $P=12{,}000$, $R=15\%$ ต่อปี และ $M=2{,}500$
เดือนแรกมีดอกเบี้ย
$12{,}000 \times 0.15/12 = 150$ บาท เงินต้นจึงเหลือ
$12{,}000-(2{,}500-150)=9{,}650$ บาท เดือนต่อไปจึงคิดดอกเบี้ยจาก
`9650` ไม่ใช่จากเงินต้นเริ่มต้น นี่คือเหตุผลที่ดอกเบี้ยลดลงตามยอดหนี้

> [!NOTE]
>
> ค่าระหว่างทางทั้งหมดคำนวณด้วยค่าจริงโดยไม่ปัดเศษ
> แม้ตัวอย่างในโจทย์จะแสดงตัวเลขบางค่าเพียงสองตำแหน่งก็ตาม

---

## เงื่อนไขที่ผ่อนไม่หมด

ก่อนเข้า `while` โปรแกรมคำนวณดอกเบี้ยเดือนแรก แล้วตรวจสอบ

```python
if monthly_pay > interest:
```

ถ้า $M \le I_1$ เงินที่ผ่อนจะไม่เหลือไปตัดเงินต้น หรืออาจทำให้ยอดหนี้เพิ่มขึ้น
เมื่อเงินต้นไม่ลด ดอกเบี้ยของเดือนต่อไปก็ไม่ลดจนต่ำกว่าเงินผ่อนได้
โปรแกรมจึงแสดง `indefinite` ทันที

สังเกตว่าเงื่อนไขใช้ `>` แบบเคร่งครัด ถ้าเงินผ่อน **เท่ากับ** ดอกเบี้ยพอดี
ก็ยังถือว่าผ่อนไม่หมด เพราะเงินต้นไม่ลดเลย

---

## การแสดงผล

-   กรณีผ่อนหมด แสดง `total_month` ก่อน แล้วตามด้วย
    `round(total_interest, 2)` ในบรรทัดเดียว คั่นด้วยช่องว่าง
-   กรณีผ่อนไม่หมด แสดงข้อความ `indefinite` เพียงอย่างเดียว

การปัดด้วย `round(..., 2)` เกิดขึ้นครั้งเดียวตอนแสดงผลรวมดอกเบี้ย
จึงไม่สะสมความคลาดเคลื่อนจากการปัดทุกเดือน

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q2_A2-S.py
# Problem   : Loan Interest
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input initial debt, interest rate, and monthly payment
initial_debt = float(input())
interest_rate = float(input()) / 100
monthly_pay = float(input())

# Initialize total month and total interest
total_month = 0
total_interest = 0

# Initialize current debt and calculate initial interest
current_debt = initial_debt
interest = current_debt * (interest_rate / 12)

# Check if monthly payment is greater than interest
if monthly_pay > interest:
    # Loop until the debt is paid off
    while current_debt > 0:
        # Calculate interest of the current month
        interest = current_debt * (interest_rate / 12)

        # Update current debt and total interest
        current_debt = max(0, current_debt - (monthly_pay - interest))
        total_interest += interest

        # Increment total month
        total_month += 1

    # Output total month and total interest
    print(total_month, round(total_interest, 2))

# If monthly payment is less than or equal to interest
# it's impossible to pay off the debt
else:
    print("indefinite")
```
