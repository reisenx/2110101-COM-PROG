<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Sequence with Ellipsis ★★ (
      <a href="https://drive.google.com/file/d/1BsL2WmqcA0Zi5Jt8rX0YuHeto6Sjdkxg/view?usp=sharing">
        <code>2567_1_Q1_A3-W</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ทำความเข้าใจ range**](#ทำความเข้าใจ-range)
-   [**การหาจำนวนสมาชิก**](#การหาจำนวนสมาชิก)
-   [**การเลือกรูปแบบผลลัพธ์**](#การเลือกรูปแบบผลลัพธ์)
-   [**การหาสมาชิกโดยไม่สร้างทั้งลำดับ**](#การหาสมาชิกโดยไม่สร้างทั้งลำดับ)
-   [**Solution**](#solution)

---

## ทำความเข้าใจ range

`range(start, stop, step)` สร้างลำดับที่เริ่มจาก `start` แล้วเพิ่มด้วย `step`
ทุกครั้ง โดยค่า `stop` เป็นขอบเขตที่ **ไม่ถูกรวม** ในลำดับ เช่น
`range(0, 5, 1)` ให้ `0, 1, 2, 3, 4`

-   เมื่อ `step > 0` ลำดับเดินขึ้นและมีข้อมูลต่อเมื่อ `start < stop`
-   เมื่อ `step < 0` ลำดับเดินลงและมีข้อมูลต่อเมื่อ `start > stop`
-   โจทย์รับประกันว่า `step != 0` เพราะลำดับที่มีระยะก้าวเป็นศูนย์ไม่มีนิยาม

สิ่งสำคัญของข้อนี้คือ `start`, `stop` และ `step` อาจมีขนาดใหญ่มาก เราจึงไม่ควร
สร้างสมาชิกทั้งหมดเพียงเพื่อจะนับจำนวน

## การหาจำนวนสมาชิก

ให้ `n` เป็นจำนวนสมาชิกในลำดับ กรณี `step > 0` จำนวนสมาชิกทางคณิตศาสตร์คือ
$\left\lceil\dfrac{stop-start}{step}\right\rceil$ เมื่อ `start < stop`
สูตรปัดขึ้นนี้เขียนด้วยเลขจำนวนเต็มใน Python ได้เป็น

```python
n = max(0, (stop - start + step - 1) // step)
```

ถ้าทิศทางไม่ถูกต้อง ผลในวงเล็บอาจไม่เป็นจำนวนบวก จึงใช้ `max(0, ...)`
เพื่อให้จำนวนสมาชิกต่ำสุดเป็นศูนย์

สำหรับ `step < 0` ต้องนับในทิศทางลดลง โค้ดใช้สูตรที่จัดเครื่องหมายให้เหมาะกับ
การหารปัดลงของ Python ดังนี้

```python
n = max(0, (stop - start + step + 1) // step)
```

เช่น `start = 100`, `stop = 12`, `step = -7` ได้ `n = 13` สมาชิกคือ
`100, 93, ...` ไปจนถึง `16` ส่วน `9 9 1` ได้ `n = 0` เพราะค่าเริ่มต้น
อยู่ที่ขอบเขต `stop` ซึ่งไม่ถูกรวม

## การเลือกรูปแบบผลลัพธ์

เมื่อทราบ `n` แล้ว โปรแกรมแยกผลลัพธ์เป็นสามกรณี

1. `n == 0` แสดงข้อความ `No data`
2. `1 <= n <= 5` วนผ่าน `range(...)` เพื่อเก็บสมาชิกเป็นข้อความ แล้วใช้
   `", ".join(numbers)` เชื่อมด้วย comma ตามด้วยช่องว่างหนึ่งช่อง
3. `n > 5` แสดงเพียงสองสมาชิกแรก, `...` และสองสมาชิกสุดท้าย

กรณีที่มี 5 สมาชิกพอดียังแสดงครบทั้ง 5 ค่า ส่วน 6 สมาชิกขึ้นไปจึงเริ่มย่อด้วย
`...` รูปแบบจึงเป็นไปตามจำนวนสมาชิก ไม่ได้ขึ้นกับขนาดของตัวเลข

## การหาสมาชิกโดยไม่สร้างทั้งลำดับ

สมาชิกตำแหน่งที่ `i` เมื่อนับตำแหน่งแรกเป็น `i = 0` มีค่า
$start + i \times step$ หรือ `start + i * step` ใน Python ดังนั้นเมื่อ `n > 5`
เราหาค่าที่ต้องแสดงได้โดยตรง

```python
first_num = start
second_num = start + step
before_last_num = start + (n - 2) * step
last_num = start + (n - 1) * step
```

วิธีนี้ใช้หน่วยความจำคงที่ ไม่ว่าจะมีสมาชิกจริงกี่ตัว ตัวอย่าง
`0 10000000000000000000 1` จึงคำนวณเฉพาะสี่ค่าที่ต้องใช้ และแสดง
`0, 1, ..., 9999999999999999998, 9999999999999999999` โดยไม่สร้างลิสต์
ขนาดมหาศาล

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q1_A3-W.py
# Problem   : Sequence with Ellipsis
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input start, stop, and step of the sequence
start, stop, step = [int(e) for e in input().split()]

# Initialize the number of elements in the sequence
n = 0
# Calculate in case step is positive
if step > 0:
    n = max(0, (stop - start + step - 1) // step)
# Calculate in case step is negative
elif step < 0:
    n = max(0, (stop - start + step + 1) // step)

# If the number of elements is zero
if n == 0:
    print("No data")

# If the number of elements is less than or equal to 5
elif n <= 5:
    # Directly find the numbers in the sequence
    numbers = []
    for num in range(start, stop, step):
        numbers.append(str(num))
    # Output the numbers in the sequence
    print(", ".join(numbers))

# If the number of elements is greater than 5
elif n > 5:
    # Calculate the first two numbers
    first_num = start
    second_num = start + step

    # Calculate the last two numbers
    before_last_num = start + (n - 2) * step
    last_num = start + (n - 1) * step

    # Output the sequence with ellipsis
    print(f"{first_num}, {second_num}, ..., {before_last_num}, {last_num}")
```
