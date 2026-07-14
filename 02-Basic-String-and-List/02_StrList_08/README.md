<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Decimal to Fraction ★★★ (
      <a href="https://drive.google.com/file/d/1QfmOmzJvBn66DLlNARVVvvBoOz4RsFt3/view?usp=drive_link">
        <code>02_StrList_08</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การแยกส่วนของทศนิยม**](#การแยกส่วนของทศนิยม)
-   [**การสร้างเศษและส่วน**](#การสร้างเศษและส่วน)
-   [**การทำเศษส่วนให้อยู่ในรูปอย่างต่ำ**](#การทำเศษส่วนให้อยู่ในรูปอย่างต่ำ)
-   [**Solution**](#solution)

---

## การแยกส่วนของทศนิยม

ข้อมูลนำเข้าเขียนเป็น `a,b,c` โดยแบ่งเลขทศนิยมออกเป็นสามส่วน

-   `a` คือส่วนจำนวนเต็ม
-   `b` คือเลขหลังจุดทศนิยมส่วนที่ไม่ซ้ำ
-   `c` คือชุดตัวเลขที่ซ้ำไปเรื่อย ๆ

ตัวอย่างเช่น `0,08,3` แทนจำนวน $0.08\overline{3}$ โดย `a = "0"`,
`b = "08"` และ `c = "3"` โปรแกรมใช้

```python
a, b, c = input().strip().split(",")
```

เพื่อแยกข้อความสามส่วนและนำไปเก็บในตัวแปรตามลำดับ ทุกส่วนยังเป็น `str`
จึงเชื่อมกันด้วย `+` และรักษาเลขศูนย์นำหน้าอย่าง `"08"` ไว้ได้

ถ้าทศนิยมซ้ำเริ่มทันที `b` สามารถเป็นข้อความว่างได้ เช่น `987,,987`
ส่วนจำนวนที่สิ้นสุดหรือจำนวนเต็มใช้ `c = "0"` เช่น `0,5,0` แทน `0.5`
และ `7,,0` แทน `7`

---

## การสร้างเศษและส่วน

ให้ $m = |b|$ เป็นจำนวนหลักในส่วนไม่ซ้ำ และ $n = |c|$
เป็นจำนวนหลักในส่วนซ้ำ สำหรับจำนวน
$x = a.b\overline{c}$ เมื่อนำ $x$ ไปคูณด้วย $10^{m+n}$ และ $10^m$
ตำแหน่งทศนิยมจะเลื่อนไปจนส่วนที่ซ้ำตรงกัน เมื่อนำสองสมการมาลบกัน
ส่วนทศนิยมที่ซ้ำจึงหายไป ได้ว่า

$$
(10^{m+n} - 10^m)x
= \operatorname{int}(abc) - \operatorname{int}(ab)
$$

ดังนั้นเศษ (`numerator`) และส่วน (`denominator`) ก่อนย่อคือ

$$
N = \operatorname{int}(abc) - \operatorname{int}(ab)
$$

$$
D = 10^{|b|+|c|} - 10^{|b|}
$$

ซึ่งตรงกับ Python ดังนี้

```python
numerator = int(a + b + c) - int(a + b)
denominator = 10 ** (len(b) + len(c)) - 10 ** len(b)
```

สำหรับ `0,08,3` จะได้

$$
N = \operatorname{int}(0083) - \operatorname{int}(008) = 83 - 8 = 75
$$

$$
D = 10^{2+1} - 10^2 = 1000 - 100 = 900
$$

จึงได้เศษส่วนก่อนย่อเป็น $75/900$ วิธีนี้คำนวณจากข้อความและจำนวนเต็ม
โดยตรง ไม่ต้องแปลงข้อมูลเป็น `float` จึงไม่เกิดการปัดเศษระหว่างคำนวณ

---

## การทำเศษส่วนให้อยู่ในรูปอย่างต่ำ

เศษส่วนอย่าง $75/900$ ยังย่อได้ โปรแกรมจึงใช้
`math.gcd(numerator, denominator)` หา **ตัวหารร่วมมาก** ของเศษและส่วน
ในตัวอย่างนี้ได้ `75`

จากนั้นตัวดำเนินการ `//=` หารแล้วกำหนดค่ากลับเข้าไปในตัวแปรเดิม

```python
numerator //= gcd
denominator //= gcd
```

จึงได้ $75 \mathbin{//} 75 = 1$ และ $900 \mathbin{//} 75 = 12$
ผลลัพธ์สุดท้ายคือ

```text
1 / 12
```

โปรแกรมแสดงเศษ ตามด้วยช่องว่าง เครื่องหมาย `/` ช่องว่าง และส่วน
ตามรูปแบบที่โจทย์กำหนด กรณีจำนวนเป็น `0` จะได้เศษส่วนอย่างต่ำเป็น `0 / 1`
และกรณีจำนวนเต็ม เช่น `7,,0` จะได้ `7 / 1`

---

# Solution

```python
# --------------------------------------------------
# File Name : 02_StrList_08.py
# Problem   : Decimal to Fraction
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math

# Input a decimal number in the format A,B,C
# where 'a' is the integer part,
#       'b' is the non-repeating decimal part,
#   and 'c' is the repeating decimal part.
a, b, c = input().strip().split(",")

# Convert repeating decimal to fraction
numerator = int(a + b + c) - int(a + b)
denominator = 10 ** (len(b) + len(c)) - 10 ** len(b)

# Output the fraction in its simplest form
gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd
print(f"{numerator} / {denominator}")
```
