<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Cosine Taylor Series ★☆ (
      <a href="https://drive.google.com/file/d/1_OOLiYVtHnN-0h3iZ1udPz6MoPe3Xpna/view?usp=sharing">
        <code>2567_1_Q1_A2-W</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิดอนุกรมเทย์เลอร์**](#แนวคิดอนุกรมเทย์เลอร์)
-   [**เงื่อนไขหยุดและการรวมพจน์**](#เงื่อนไขหยุดและการรวมพจน์)
-   [**ขั้นตอนของโปรแกรม**](#ขั้นตอนของโปรแกรม)
-   [**การปัดเศษผลลัพธ์**](#การปัดเศษผลลัพธ์)
-   [**Solution**](#solution)

---

## แนวคิดอนุกรมเทย์เลอร์

ฟังก์ชัน cosine สามารถเขียนเป็นผลรวมของพจน์อนุกรมเทย์เลอร์ได้ดังนี้

$$
\cos(x) = \sum_{n=0}^{\infty}\frac{(-1)^n x^{2n}}{(2n)!}
$$

พจน์ลำดับที่ `n` จึงเป็น
$t_n = \dfrac{(-1)^n x^{2n}}{(2n)!}$ และเขียนเป็น Python ได้ตรง ๆ ว่า

```python
term = (((-1) ** n) * (x ** (2 * n))) / math.factorial(2 * n)
```

`(-1) ** n` ทำให้เครื่องหมายสลับระหว่างบวกกับลบ, `x ** (2 * n)` คือ
$x^{2n}$ และ `math.factorial(2 * n)` คือ $(2n)!$ โปรแกรมเริ่มจาก `n = 0`
จึงได้พจน์แรกเป็น `1` แล้วค่อยพิจารณาพจน์ถัดไปตามลำดับ

## เงื่อนไขหยุดและการรวมพจน์

โจทย์กำหนดให้หยุดเมื่อพบพจน์แรกที่มีค่าสัมบูรณ์น้อยกว่า `epsilon` และไม่รวม
พจน์นั้นในคำตอบ โค้ดจึงตรวจเงื่อนไขก่อนคำสั่ง `cosine += term`

```python
if abs(term) < epsilon:
    break
cosine += term
```

> [!WARNING]
>
> เงื่อนไขเป็น `<` ไม่ใช่ `<=` ถ้า `abs(term)` เท่ากับ `epsilon` พอดี
> พจน์นั้นยังต้องถูกรวม แล้วโปรแกรมจึงไปตรวจพจน์ถัดไป

ตัวอย่างเมื่อ `x = 1.0` และ `epsilon = 0.02` มีพจน์ช่วงแรกเป็น
`1`, `-0.5`, `0.041666...` และ `-0.001388...` พจน์ที่สี่มีค่าสัมบูรณ์
น้อยกว่า `0.02` จึงไม่ถูกนำมาบวก ผลรวมที่ใช้คือ
`1 - 0.5 + 0.041666... = 0.541666...`

## ขั้นตอนของโปรแกรม

1. อ่าน `x` และ `epsilon` เป็นจำนวนจริงด้วย `float`
2. กำหนดผลรวมเริ่มต้น `cosine = 0` และดัชนีพจน์ `n = 0`
3. คำนวณ `term` ของดัชนีปัจจุบัน
4. ถ้า `abs(term) < epsilon` ให้ออกจากวงวนทันที
5. มิฉะนั้นบวกพจน์เข้า `cosine`, เพิ่ม `n` ขึ้น `1` แล้ววนกลับไปคำนวณ
   พจน์ใหม่

การใช้ `while True` เหมาะกับกรณีนี้ เพราะจำนวนรอบไม่ได้กำหนดล่วงหน้า แต่มี
`break` เป็นจุดจบตามค่าของพจน์ สำหรับข้อมูลตามข้อกำหนด `epsilon` เป็นค่าบวก
จึงหยุดได้เมื่อขนาดของพจน์เล็กลงเพียงพอ เช่น ถ้า `x == 0` โปรแกรมจะรวมพจน์
แรก `1` และหยุดที่พจน์ถัดไปซึ่งมีค่า `0`

## การปัดเศษผลลัพธ์

โปรแกรมเก็บผลรวมด้วยค่าจริงเต็มความละเอียดระหว่างคำนวณ แล้วเรียก
`round(cosine, 6)` เฉพาะตอนแสดงผล จึงได้เลขหลังจุดทศนิยมไม่เกิน 6 ตำแหน่ง
ตัวอย่างข้างต้นจะแสดงเป็น `0.541667`

`round(..., 6)` ไม่ได้บังคับให้แสดงศูนย์ท้ายครบ 6 หลัก ดังนั้นค่าที่ปัดแล้วเป็น
จำนวนเต็มอาจแสดงเป็น `-1.0` ได้ ซึ่งตรงกับรูปแบบที่โจทย์ต้องการ

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q1_A2-W.py
# Problem   : Cosine Taylor Series
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

import math

# Input
x, epsilon = [float(e) for e in input().split()]

# Initialize estimated value of cosine
cosine = 0
# Initialize term index
n = 0

# Loop until the term is less than epsilon
while True:
    # Calculate the term using Taylor series expansion
    term = (((-1) ** n) * (x ** (2 * n))) / math.factorial(2 * n)

    # Stop if the absolute value of the term is less than epsilon
    if abs(term) < epsilon:
        break

    # Add the term to the estimated value of cosine
    cosine += term

    # Increment the term index
    n += 1

# Output the estimated value of cosine rounded to 6 decimal places
print(round(cosine, 6))
```
