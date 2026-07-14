<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    NumPy Functions ★★★ (
      <a href="https://drive.google.com/file/d/11DYcIuGS3OW7Lmzh3iQ9qowKcyepHfQW/view?usp=drive_link">
        <code>P3_10_Numpy1</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิด NumPy ที่ใช้**](#แนวคิด-numpy-ที่ใช้)
-   [**ฟังก์ชัน eq**](#ฟังก์ชัน-eq)
-   [**ฟังก์ชัน closest_point_indexes**](#ฟังก์ชัน-closest_point_indexes)
-   [**ฟังก์ชัน number_of_inversions**](#ฟังก์ชัน-number_of_inversions)
-   [**การรับคำสั่งจาก Grader**](#การรับคำสั่งจาก-grader)
-   [**Solution**](#solution)

---

## แนวคิด NumPy ที่ใช้

NumPy สามารถคำนวณกับสมาชิกหลายตำแหน่งของอาเรย์ได้พร้อมกัน
โจทย์นี้ใช้แนวคิดหลักสี่อย่าง

-   `a == b` เปรียบเทียบสมาชิกตำแหน่งเดียวกัน แล้วได้อาเรย์ของ `True` และ `False`
-   `points[:, 0]` เลือกข้อมูลทุกแถวของคอลัมน์ `0`
-   เงื่อนไข Boolean สามารถใช้เลือกเฉพาะสมาชิกที่ตรงเงื่อนไขได้
-   `np.mean()` และ `np.sum()` รวมผลจากสมาชิกทั้งอาเรย์

แต่ละฟังก์ชันนำแนวคิดเหล่านี้ไปใช้กับงานคนละแบบ

---

## ฟังก์ชัน eq

ฟังก์ชัน `eq(a, b, target)` ตรวจว่าอาเรย์ขนาดเท่ากันสองชุด
มีข้อมูลตำแหน่งเดียวกันเท่ากันอย่างน้อยร้อยละ `target` หรือไม่
อาเรย์จะมีกี่มิติก็ได้ และโจทย์กำหนดให้ `0 <= target <= 100`

ให้ `E` เป็นจำนวนตำแหน่งที่เท่ากัน และ `N` เป็นจำนวนช่องทั้งหมด

$$
\text{percentage} = 100 \times \frac{E}{N}
$$

เมื่อเปรียบเทียบ `a == b` ค่า `True` คิดเป็น `1` และ `False` คิดเป็น `0`
ค่าเฉลี่ยของอาเรย์ Boolean จึงเท่ากับสัดส่วนของตำแหน่งที่เท่ากัน

$$
\text{percentage} = 100 \times \operatorname{mean}(a == b)
$$

ตรงกับภาษา Python ดังนี้

```python
percentage = np.mean(a == b) * 100
return percentage >= target
```

ตัวอย่าง `[1, 2]` กับ `[1, 0]` เท่ากัน `1` จาก `2` ตำแหน่ง
จึงเท่ากันร้อยละ `50` และ `eq(..., 50)` คืน `True`
เพราะเงื่อนไขใช้ `>=` แต่ `eq(..., 51)` จะคืน `False`

ฟังก์ชันคืนเพียงค่า Boolean จึงไม่มีการปัดเศษหรือจัดรูปแบบตัวเลข
PDF ใช้ชื่อพารามิเตอร์ `A`, `B` และ `p`
ส่วน canonical solution ใช้ `a`, `b` และ `target` แต่มีความหมายเดียวกัน
โค้ดอาศัยข้อกำหนดว่าอาเรย์มีขนาดเท่ากันและมีอย่างน้อยหนึ่งช่อง

---

## ฟังก์ชัน closest_point_indexes

`points` เป็นอาเรย์สองมิติที่แต่ละแถวแทนจุดหนึ่งจุด
คอลัมน์ `0` คือพิกัด `x` และคอลัมน์ `1` คือพิกัด `y`
ส่วน `target` เป็นอาเรย์ `[x_p, y_p]` ของจุดเป้าหมาย

ระยะทางกำลังสองจากจุดลำดับที่ `i` ไปยังเป้าหมายคือ

$$
d_i^2 = (x_i - x_p)^2 + (y_i - y_p)^2
$$

ในภาษา Python คำนวณทุกจุดพร้อมกันได้ดังนี้

```python
distances_x = (points[:, 0] - target[0]) ** 2
distances_y = (points[:, 1] - target[1]) ** 2
squared_distances = distances_x + distances_y
```

ไม่จำเป็นต้องถอดรากที่สอง เพราะจุดที่มี `d_i^2` น้อยที่สุด
ย่อมเป็นจุดที่มี `d_i` น้อยที่สุดเช่นกัน

หลังหา `np.min(squared_distances)` แล้ว
โปรแกรมสร้าง index `0` ถึง `n - 1` ด้วย `np.arange()`
และใช้ Boolean indexing เลือกทุกตำแหน่งที่มีค่าน้อยที่สุด

```python
np.arange(len(squared_distances))[
    squared_distances == np.min(squared_distances)
]
```

เพราะ index เริ่มจากน้อยไปมากอยู่แล้ว
ถ้ามีหลายจุดใกล้ที่สุดเท่ากัน ผลลัพธ์จึงเรียงจากน้อยไปมากตามโจทย์ เช่น `[0 1]`

canonical solution เปรียบเทียบระยะทางด้วย `==`
ดังนั้นสำหรับพิกัดชนิดทศนิยม จะถือว่าเสมอกันเฉพาะเมื่อค่าที่คำนวณได้เท่ากันพอดี
ความคลาดเคลื่อนของ floating point อาจทำให้ค่าที่ควรใกล้กันมากไม่ถูกมองว่าเสมอกัน
นอกจากนี้โค้ดอาศัยว่า `points` มีอย่างน้อยหนึ่งแถว เพราะ `np.min()`
ใช้กับอาเรย์ว่างไม่ได้

---

## ฟังก์ชัน number_of_inversions

ฟังก์ชันนี้รับอาเรย์หนึ่งมิติที่เก็บจำนวนเต็ม
**Inversion** คือคู่ index `(i, j)` ที่

$$
i < j \quad \text{และ} \quad A[i] > A[j]
$$

กล่าวคือ สมาชิกทางซ้ายอยู่ก่อนแต่มีค่ามากกว่าสมาชิกทางขวา

โค้ดพิจารณาสมาชิก `a[i]` ทีละตัว
แล้วใช้ slice `a[i + 1 :]` เลือกสมาชิกทั้งหมดทางขวา

```python
a[i] > a[i + 1 :]
```

ผลลัพธ์เป็นอาเรย์ Boolean และ `np.sum()` จะนับจำนวน `True`
จากนั้นจึงบวกเข้ากับ `count`

ตัวอย่าง `[1, 2, 9, 4, 8, 7]` มี inversion `4` คู่ คือ

-   `9` กับ `4`
-   `9` กับ `8`
-   `9` กับ `7`
-   `8` กับ `7`

สมาชิกที่มีค่าเท่ากันไม่เป็น inversion เพราะเงื่อนไขใช้ `>` ไม่ใช่ `>=`
อาเรย์ว่างหรือมีสมาชิกตัวเดียวจึงได้ `0`
ส่วนอาเรย์เรียงจากมากไปน้อยที่มี `n` สมาชิกจะมีทุกคู่เป็น inversion

ลูปตรวจสมาชิกทางขวาของแต่ละตำแหน่ง
จึงใช้เวลาระดับกำลังสองของจำนวนสมาชิก หรือ `O(n^2)`

---

## การรับคำสั่งจาก Grader

โจทย์ไม่ได้ส่งข้อมูลธรรมดาให้แยกทีละค่า
แต่ส่งคำสั่งภาษา Python หนึ่งบรรทัด เช่น

```python
print(eq(np.array([1, 2]), np.array([1, 0]), 50))
```

บรรทัดสุดท้ายของโปรแกรม

```python
exec(input().strip())
```

รับข้อความนั้นแล้วสั่งทำงานใน namespace เดียวกับฟังก์ชันที่เขียนไว้
ตัวอย่างข้างต้นจึงเรียก `eq()` และแสดง `True`
ผลส่งออกของโปรแกรมคือผลที่คำสั่งจาก Grader สั่งให้แสดง

> [!WARNING]
>
> `exec()` สามารถรันคำสั่ง Python ใด ๆ ที่ได้รับ
> ในโจทย์นี้ใช้ได้เพราะข้อมูลมาจาก Grader ที่เชื่อถือได้เท่านั้น
> ห้ามใช้ `exec()` กับข้อความจากผู้ใช้หรือแหล่งข้อมูลที่ไม่น่าเชื่อถือ

---

# Solution

```python
# --------------------------------------------------
# File Name : P3_10_Numpy1.py
# Problem   : Part-III NumPy Functions
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------

import numpy as np


# Calculate percentage of equal elements between two arrays
# Return True if the percentage is greater than or equal to the target, otherwise False
def eq(a, b, target):
    percentage = np.mean(a == b) * 100
    return percentage >= target


# Get indexes of the closest points in a 2D array to a target point
def closest_point_indexes(points, target):
    # Calculate the distance from each point to the target
    distances_x = (points[:, 0] - target[0]) ** 2
    distances_y = (points[:, 1] - target[1]) ** 2
    squared_distances = distances_x + distances_y

    # Return the indices of the points with the minimum distance
    return np.arange(len(squared_distances))[
        squared_distances == np.min(squared_distances)
    ]


# Count the number of inversions in an array
# A pair (i, j) is an inversion if i < j and A[i] > A[j]
def number_of_inversions(a):
    count = 0
    for i in range(len(a)):
        count += np.sum(a[i] > a[i + 1 :])
    return count


# Execute an input string as code
exec(input().strip())
```
