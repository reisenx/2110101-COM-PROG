<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Compound Interest ★★ (
      <a href="https://drive.google.com/file/d/1CNrv1M8k_bTVr7CcDMwEURMhnQGlBzSb/view?usp=sharing">
        <code>2567_1_Q1_A2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การอ่านข้อมูล**](#การอ่านข้อมูล)
-   [**อัตราดอกเบี้ยแบบสี่เดือน**](#อัตราดอกเบี้ยแบบสี่เดือน)
-   [**การคิดดอกเบี้ยทบต้นรายเดือน**](#การคิดดอกเบี้ยทบต้นรายเดือน)
-   [**เดือนเกิดและการเลื่อนเดือน**](#เดือนเกิดและการเลื่อนเดือน)
-   [**การปัดเศษผลลัพธ์**](#การปัดเศษผลลัพธ์)
-   [**Solution**](#solution)

---

## การอ่านข้อมูล

ข้อมูลทั้งหมดอยู่ในบรรทัดเดียว โปรแกรมจึงใช้ `input().split()` แยกเป็นสี่ส่วน

1. วันเกิดในรูป `วัน/เดือน/ปี`
2. เงินฝากเริ่มต้น
3. จำนวนเดือนที่ฝาก
4. เลขเดือนปฏิทินที่เริ่มฝาก เช่น `3` หมายถึงเดือนมีนาคม

การให้ดอกเบี้ยพิเศษใช้เฉพาะ **เดือนเกิด** โค้ดจึงแยกข้อความวันที่ด้วย `/` แล้ว
เลือกสมาชิกตำแหน่งที่ `1`

```python
birth_month = int(data[0].split("/")[1])
```

วันและปีเกิดไม่ส่งผลต่อการคำนวณ ส่วนเงินฝากถูกอ่านเป็น `float` เพื่อรองรับ
จำนวนที่มีจุดทศนิยม

## อัตราดอกเบี้ยแบบสี่เดือน

อัตราดอกเบี้ยวนซ้ำตามลำดับเดือนที่ฝาก ไม่ใช่ตามเดือนปฏิทิน

| เดือนที่ฝาก | อัตราต่อปี | ดัชนี `month % 4` |
|---:|---:|---:|
| 1, 5, 9, ... | 1% | 1 |
| 2, 6, 10, ... | 2% | 2 |
| 3, 7, 11, ... | 3% | 3 |
| 4, 8, 12, ... | 4% | 0 |

จึงจัดลิสต์ให้ดัชนี `0` เก็บ `0.04` และดัชนี `1`, `2`, `3` เก็บ
`0.01`, `0.02`, `0.03` ตามลำดับ

```python
INITIAL_INTEREST_RATE = [0.04, 0.01, 0.02, 0.03]
interest_rate = INITIAL_INTEREST_RATE[month % 4]
```

อัตราถูกเก็บเป็นทศนิยม เช่น 1% เขียนเป็น `0.01` เพื่อใช้คูณกับเงินได้ทันที

## การคิดดอกเบี้ยทบต้นรายเดือน

ถ้าเงินต้นเดือนปัจจุบันเป็น $M$ และอัตราดอกเบี้ยต่อปีเป็น $r$ ดอกเบี้ยของหนึ่ง
เดือนคือ $M \times \dfrac{r}{12}$ ดังนั้นเงินเมื่อจบเดือนเป็น
$M_{new} = M + M \times \dfrac{r}{12}$ ซึ่งตรงกับ Python ว่า

```python
total_money += total_money * interest_rate * (1 / 12)
```

ค่าที่เพิ่มเข้า `total_money` จะกลายเป็นฐานคำนวณของเดือนถัดไป จึงเป็นดอกเบี้ย
ทบต้น ตัวอย่าง เงิน `1200000` บาทในเดือนที่ฝากลำดับแรกซึ่งได้ 1% ต่อปี
จะมีดอกเบี้ย `1200000 * 0.01 / 12 = 1000` บาท และเหลือ
`1201000.0` บาทเมื่อครบหนึ่งเดือน

## เดือนเกิดและการเลื่อนเดือน

ก่อนคิดดอกเบี้ยแต่ละรอบ โปรแกรมตรวจว่าเดือนปฏิทินปัจจุบันตรงกับเดือนเกิดหรือไม่
ถ้าตรงกันจะบวกอัตราพิเศษอีก 1% หรือ `0.01`

```python
if (current_month % 12) == (birth_month % 12):
    interest_rate += 0.01
```

การใช้ `% 12` ทำให้เดือนเดินข้ามปีได้ เช่น เดือน `13` เทียบเท่าเดือนมกราคม
เพราะ `13 % 12 == 1` และเดือน `12` เทียบกับเดือนเกิดธันวาคมได้เพราะทั้งคู่
เหลือเศษ `0` จากนั้น `current_month += 1` จะเลื่อนไปเดือนปฏิทินถัดไปสำหรับรอบหน้า

> [!NOTE]
>
> อัตราปกติเลือกจากลำดับที่ฝาก `month` แต่อัตราพิเศษเลือกจากเดือนปฏิทิน
> `current_month` ตัวแปรสองตัวนี้จึงมีหน้าที่ต่างกัน

## การปัดเศษผลลัพธ์

โจทย์กำหนดว่าไม่ต้องปัดระหว่างทาง โค้ดจึงเก็บผลที่คำนวณได้ทุกเดือนเต็มความ
ละเอียด และใช้ `round(total_money, 2)` เพียงครั้งเดียวตอนแสดงผล วิธีนี้ป้องกัน
ความคลาดเคลื่อนสะสมจากการปัดยอดเงินซ้ำทุกเดือน

`round(..., 2)` ให้เลขหลังจุดทศนิยมไม่เกิน 2 ตำแหน่ง ไม่ได้เติมศูนย์ท้ายเสมอ
จึงอาจเห็นผลลัพธ์อย่าง `1201000.0` ซึ่งเป็นค่าตัวเลขเดียวกับ `1201000.00`

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q1_A2.py
# Problem   : Compound Interest
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Initial interest rates for each month
INITIAL_INTEREST_RATE = [0.04, 0.01, 0.02, 0.03]

# Input
data = input().split()

# Get birth month, initial money, total months, and current month from input
birth_month = int(data[0].split("/")[1])
initial_money = float(data[1])
total_months = int(data[2])
current_month = int(data[3])

# Initialize total money with the initial money
total_money = initial_money

# Loop through each month to calculate the interest
for month in range(1, total_months + 1):
    # Determine interest rate based on month
    interest_rate = INITIAL_INTEREST_RATE[month % 4]

    # Check if current month matches birth month
    if (current_month % 12) == (birth_month % 12):
        interest_rate += 0.01

    # Calculate new total money amount
    total_money += total_money * interest_rate * (1 / 12)

    # Increment current month
    current_month += 1

# Output the total money rounded to two decimal places
print(round(total_money, 2))
```
