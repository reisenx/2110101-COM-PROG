<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Continued Fraction ★★ (
      <a href="https://drive.google.com/file/d/1tpVYDDJD990Q14XT2uEONHCwzBXefI4N/view?usp=sharing">
        <code>2567_1_Q2_A2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิดเศษส่วนต่อเนื่อง**](#แนวคิดเศษส่วนต่อเนื่อง)
-   [**การสร้างแต่ละพจน์**](#การสร้างแต่ละพจน์)
-   [**เงื่อนไขหยุด**](#เงื่อนไขหยุด)
-   [**รูปแบบผลลัพธ์**](#รูปแบบผลลัพธ์)
-   [**Solution**](#solution)

---

## แนวคิดเศษส่วนต่อเนื่อง

อินพุตบรรทัดเดียวประกอบด้วยจำนวนจริงบวก $C$ และจำนวนเต็มบวก `n`
ซึ่งเป็นจำนวนพจน์มากที่สุดที่ต้องการ โปรแกรมเก็บสองค่านี้เป็น
`initial_value` และ `max_terms_amount`

ในการหาพจน์ของเศษส่วนต่อเนื่อง ให้เริ่มจาก $x_0=C$ แล้วแยกค่าปัจจุบัน
$x_k$ เป็นส่วนจำนวนเต็ม $a_k$ และส่วนเศษ $r_k$

$$
a_k = \lfloor x_k \rfloor, \qquad r_k = x_k-a_k
$$

ถ้ายังมีเศษ ให้นำส่วนกลับของเศษไปเป็นค่ารอบถัดไป

$$
x_{k+1}=\frac{1}{r_k}
$$

เมื่อทำซ้ำจะได้ $a_0,a_1,a_2,\ldots$ ตามลำดับที่โจทย์ต้องการ

---

## การสร้างแต่ละพจน์

ในแต่ละรอบ โปรแกรมใช้

```python
integer_part = int(current_value)
decimal_part = current_value - integer_part
```

โจทย์รับประกันว่า $C$ เป็นจำนวนบวก และส่วนกลับของเศษก็เป็นบวกเสมอ
ดังนั้น `int(current_value)` จึงให้ค่าเดียวกับการปัดลง
$\lfloor x_k \rfloor$ จากนั้นแปลงจำนวนเต็มเป็นข้อความแล้วเก็บใน `terms`

ถ้าเศษยังมีค่ามากพอ จึงคำนวณรอบถัดไปด้วย
`current_value = 1 / decimal_part`

ตัวอย่าง $C=1.25$ และ `n = 4`

1. $1.25=1+0.25$ จึงได้พจน์แรกเป็น `1`
2. ส่วนกลับของ `0.25` คือ `4.0` จึงได้พจน์ถัดไปเป็น `4`
3. `4.0` ไม่มีส่วนเศษที่มีนัยสำคัญ โปรแกรมจึงหยุด ได้ผลลัพธ์ `1, 4`

---

## เงื่อนไขหยุด

ลูป `for` ทำงานได้ไม่เกิน `max_terms_amount` รอบ จึงไม่มีทางสร้างเกิน `n` พจน์
นอกจากนี้ หลังเพิ่มพจน์ปัจจุบันแล้ว โปรแกรมตรวจว่า

```python
if decimal_part < 1e-10:
    break
```

ถ้าเศษน้อยกว่า $10^{-10}$ จะถือว่าเล็กพอที่จะจบการคำนวณ
และหยุดก่อนนำเศษนั้นไปหารกลับ ซึ่งช่วยหลีกเลี่ยงการหารด้วยศูนย์หรือจำนวนที่เล็กมาก

> [!WARNING]
>
> เงื่อนไขในโค้ดเป็น `< 1e-10` ไม่ใช่ `<= 1e-10`
> และจำนวนจริงใน Python อาจมีความคลาดเคลื่อนเล็กน้อยจากการเก็บแบบ floating-point
> จึงต้องใช้ค่าที่โปรแกรมคำนวณได้จริงในการตัดสินใจหยุด

จำนวนเต็มบวก เช่น `99.0` มีเศษ `0.0` จึงหยุดหลังพจน์แรกทันที
แม้ `n` จะมีค่ามากกว่านั้น

---

## รูปแบบผลลัพธ์

พจน์ทุกตัวถูกเก็บเป็นข้อความ แล้วนำมาต่อด้วย `", ".join(terms)`
ผลลัพธ์จึงคั่นแต่ละจำนวนด้วยเครื่องหมายจุลภาคตามด้วยช่องว่าง เช่น
`3, 7, 15, 1` โดยไม่มีวงเล็บเหลี่ยมและไม่มีจุลภาคต่อท้าย

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q2_A2.py
# Problem   : Continued Fraction
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input value and maximum number of terms
data = input().strip().split()
initial_value = float(data[0])
max_terms_amount = int(data[1])

# Initialize the list to store terms and the current value
terms = []
current_value = initial_value

# Generate terms
for _ in range(max_terms_amount):
    # Separate the integer and decimal parts of the current value
    integer_part = int(current_value)
    decimal_part = current_value - integer_part

    # Append the integer part to the terms list
    terms.append(str(integer_part))

    # If the decimal part is less than 1e-10, break the loop
    if decimal_part < 1e-10:
        break

    # Update the current value to be the reciprocal of the decimal part
    current_value = 1 / decimal_part

# Output the terms
print(", ".join(terms))
```
