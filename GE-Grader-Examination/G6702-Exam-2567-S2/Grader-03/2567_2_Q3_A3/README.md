<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Red Ball ★☆ (
      <a href="https://drive.google.com/file/d/1xhNd3hF-0datqyz816erb_OIuLOHxJ79/view?usp=sharing">
        <code>2567_2_Q3_A3</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**อ่านและเก็บลำดับลูกบอล**](#อ่านและเก็บลำดับลูกบอล)
-   [**แปลงช่วงหมายเลขถ้วยเป็น slicing**](#แปลงช่วงหมายเลขถ้วยเป็น-slicing)
-   [**ย้ายช่วงที่เลือกไปทางขวาสุด**](#ย้ายช่วงที่เลือกไปทางขวาสุด)
-   [**ลำดับการทำงานและกรณีพิเศษ**](#ลำดับการทำงานและกรณีพิเศษ)
-   [**Solution**](#solution)

---

## อ่านและเก็บลำดับลูกบอล

บรรทัดแรกเป็นสีของลูกบอลที่คั่นด้วยเครื่องหมายจุลภาค `,` และไม่มีช่องว่าง
โปรแกรมใช้

```python
balls = input().strip().split(",")
```

`strip()` ตัดช่องว่างหรืออักขระขึ้นบรรทัดใหม่ที่อาจติดอยู่ตรงหัวและท้ายข้อความ
ส่วน `split(",")` แบ่งข้อความให้เป็นลิสต์ เช่น
`"blue,red,green"` กลายเป็น `['blue', 'red', 'green']`

หลังจากนั้นรับจำนวนครั้งที่โจทย์เรียก `m` มาเก็บในตัวแปร `n` และทำการย้ายถ้วย
ตามคำสั่งอีก `n` บรรทัด

---

## แปลงช่วงหมายเลขถ้วยเป็น slicing

โจทย์นับถ้วยจาก `1` ถึงจำนวนถ้วยทั้งหมด และให้ย้ายช่วงตั้งแต่ถ้วยที่ `a` ถึง `b`
โดยรวมปลายทั้งสองข้าง แต่ index ของลิสต์ Python เริ่มจาก `0` และการ slice
จะไม่รวมตำแหน่งขวาสุด

ช่วงแบบหนึ่ง-based $[a,b]$ จึงตรงกับ slice ต่อไปนี้

```python
balls[a - 1 : b]
```

โปรแกรมทำให้ `start_idx` เท่ากับ `a - 1` ด้วย `start_idx -= 1` แต่ไม่ลบ
`end_idx` เพราะค่า `b` เดิมทำหน้าที่เป็นขอบขวาแบบไม่รวมของ slice ได้พอดี

ตัวอย่าง ถ้าเลือกถ้วยที่ `2` ถึง `4` จะใช้ `balls[1:4]` ซึ่งได้สมาชิกที่
index `1`, `2` และ `3` หรือถ้วยหมายเลข `2`, `3` และ `4` ครบถ้วน

---

## ย้ายช่วงที่เลือกไปทางขวาสุด

การย้ายหนึ่งครั้งแบ่งลิสต์ปัจจุบันเป็นสามส่วน

-   ส่วนก่อนช่วงที่เลือก: `balls[:start_idx]`
-   ส่วนที่เลือก: `balls[start_idx:end_idx]`
-   ส่วนหลังช่วงที่เลือก: `balls[end_idx:]`

เมื่อต้องนำส่วนที่เลือกไปไว้ท้ายสุด ลำดับใหม่จึงเป็น

```python
balls = balls[:start_idx] + balls[end_idx:] + balls[start_idx:end_idx]
```

ดังนั้นการทำงานนี้คือการ **ย้ายช่วงที่เลือก** ไปท้ายลิสต์ ไม่ใช่การสลับสมาชิก
ทีละคู่

เช่น เริ่มจาก

```text
[blue, red, green, purple, skyblue]
```

และเลือกถ้วยที่ `1` ถึง `3` จะได้ส่วนก่อนเป็นลิสต์ว่าง ส่วนหลังเป็น
`[purple, skyblue]` และส่วนที่เลือกเป็น `[blue, red, green]` เมื่อนำมาต่อกัน
จึงได้

```text
[purple, skyblue, blue, red, green]
```

---

## ลำดับการทำงานและกรณีพิเศษ

ทุกคำสั่งอ้างอิงลำดับ **ปัจจุบัน** หลังจากคำสั่งก่อนหน้าทำงานแล้ว โปรแกรมจึง
แทนค่า `balls` ด้วยลิสต์ใหม่ในแต่ละรอบ ก่อนอ่านช่วงของรอบถัดไป

-   ถ้าเลือกตั้งแต่ถ้วยแรกถึงถ้วยสุดท้าย ลิสต์จะไม่เปลี่ยน เพราะย้ายสมาชิก
    ทั้งหมดไปท้ายลิสต์เดิม
-   ถ้าเลือกช่วงที่ลงท้ายด้วยถ้วยสุดท้าย ส่วนที่เลือกอยู่ท้ายลิสต์อยู่แล้ว
    ลำดับจึงไม่เปลี่ยน
-   ถ้า `a == b` จะย้ายถ้วยเพียงใบเดียวไปไว้ขวาสุด
-   ถ้าไม่มีการย้าย (`n == 0`) ลูปไม่ทำงานและลำดับเริ่มต้นจะถูกแสดงตามเดิม

สุดท้าย `",".join(balls)` เชื่อมสีทุกสีด้วย `,` จึงได้ผลลัพธ์หนึ่งบรรทัด
โดยไม่มีช่องว่าง เช่น `purple,skyblue,blue,red,green`

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_2_Q3_A3.py
# Problem   : Red Ball
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------

# Input initial balls order
balls = input().strip().split(",")

# Swap balls operations
n = int(input())
for _ in range(n):
    # Input start and end indices for the swap operation in 1-based indexing
    start_idx, end_idx = [int(idx) for idx in input().split()]

    # Convert to 0-based indexing
    # NOTE: No need to decrement end_idx because the operation includes the end index
    start_idx -= 1

    # Swap the balls in range to the end of the list
    balls = balls[:start_idx] + balls[end_idx:] + balls[start_idx:end_idx]

# Output the final order of balls
print(",".join(balls))
```
