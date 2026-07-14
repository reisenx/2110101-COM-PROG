<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Rectangle Sorted by Area ★★★ (
      <a href="https://drive.google.com/file/d/14_CYL0hMMiWPds7FrDK4JLUAMASWH-vB/view?usp=drive_link">
        <code>12_Class_32</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การสร้าง `Point` และ `Rect`**](#การสร้าง-point-และ-rect)
-   [**รูปแบบข้อความของออบเจ็กต์**](#รูปแบบข้อความของออบเจ็กต์)
-   [**การเปรียบเทียบด้วยพื้นที่**](#การเปรียบเทียบด้วยพื้นที่)
-   [**การเรียงลำดับสี่เหลี่ยม**](#การเรียงลำดับสี่เหลี่ยม)
-   [**ลำดับข้อมูลนำเข้าและผลลัพธ์**](#ลำดับข้อมูลนำเข้าและผลลัพธ์)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## การสร้าง `Point` และ `Rect`

คลาส `Point` เก็บพิกัด `x` และ `y` ของจุดหนึ่งจุด ส่วนคลาส `Rect`
แทนสี่เหลี่ยมผืนผ้าด้วยออบเจ็กต์ `Point` สองจุด

-   `lower_left` คือมุมซ้ายล่าง $(x_1,y_1)$
-   `upper_right` คือมุมขวาบน $(x_2,y_2)$

การให้ออบเจ็กต์หนึ่งเก็บออบเจ็กต์อื่นเป็นส่วนประกอบเรียกว่า
**object composition** ในข้อนี้ `Rect` จึงอ่านพิกัดได้ผ่าน
`self.lower_left.x`, `self.lower_left.y` และพิกัดของ `upper_right`

พื้นที่คำนวณจาก

$$
\text{area} = (x_2-x_1)(y_2-y_1)
$$

และเขียนใน Python เป็น `(x2 - x1) * (y2 - y1)`

---

## รูปแบบข้อความของออบเจ็กต์

เมท็อด `__str__` บอก Python ว่าต้องแสดงออบเจ็กต์เป็นข้อความอย่างไร
เมื่อส่งออบเจ็กต์ให้ `print()`

-   `Point.__str__` คืนข้อความรูปแบบ `(x,y)`
-   `Rect.__str__` นำจุดสองจุดมาต่อด้วย `-` เป็น `(x1,y1)-(x2,y2)`

รูปแบบนี้ **ไม่มีช่องว่าง** รอบตัวเลข เครื่องหมายจุลภาค หรือเครื่องหมาย
`-` เช่น สี่เหลี่ยมจาก $(2,2)$ ถึง $(3,3)$ จะแสดงเป็น
`(2,2)-(3,3)`

---

## การเปรียบเทียบด้วยพื้นที่

ตามปกติ Python ยังไม่ทราบว่าออบเจ็กต์ `Rect` ใดควรมากหรือน้อยกว่า
อีกออบเจ็กต์หนึ่ง คลาสจึงกำหนดเมท็อดพิเศษ `__lt__` ซึ่งทำงานเมื่อ Python
ต้องตรวจสอบเครื่องหมาย `<`

```python
return self.area() < other.area()
```

ดังนั้น `rect_a < rect_b` จะเป็น `True` ก็ต่อเมื่อพื้นที่ของ `rect_a`
น้อยกว่าพื้นที่ของ `rect_b` เท่านั้น พิกัด ตำแหน่ง ความกว้าง และความสูง
ไม่ได้ถูกใช้เป็นเงื่อนไขแยกต่างหาก

---

## การเรียงลำดับสี่เหลี่ยม

คำสั่ง `rectangles.sort()` เรียงลิสต์จากน้อยไปมาก โดยใช้ `__lt__` ของ
`Rect` เปรียบเทียบสมาชิก ผลลัพธ์จึงเรียงตามพื้นที่จากน้อยไปมาก

Python ใช้การเรียงลำดับแบบ **stable** หากสี่เหลี่ยมสองรูปมีพื้นที่เท่ากัน
`__lt__` จะคืน `False` เมื่อเปรียบเทียบทั้งสองทิศทาง และสี่เหลี่ยมคู่นั้น
จะยังเรียงตามลำดับเดิมที่รับเข้ามา

---

## ลำดับข้อมูลนำเข้าและผลลัพธ์

บรรทัดแรกรับจำนวนสี่เหลี่ยม `n` จากนั้นอีก `n` บรรทัดรับ
`x1 y1 x2 y2` ตามลำดับ โปรแกรมสร้าง `Point` สองจุด สร้าง `Rect`
แล้วเก็บไว้ใน `rectangles`

เมื่อรับครบ โปรแกรมเรียก `rectangles.sort()` เพียงครั้งเดียว แล้วพิมพ์
สี่เหลี่ยมทั้งหมดตามลำดับพื้นที่จากน้อยไปมาก ผลลัพธ์มี `n` บรรทัดและ
แสดงเฉพาะพิกัดตามรูปแบบของ `__str__` ไม่ได้แสดงค่าพื้นที่

---

## ตัวอย่างการทำงาน

สี่เหลี่ยมสามรูปต่อไปนี้มีพื้นที่ต่างกัน

| สี่เหลี่ยม | พื้นที่ |
|---|---:|
| `(1,1)-(3,3)` | $(3-1)(3-1)=4$ |
| `(0,0)-(10,10)` | $(10-0)(10-0)=100$ |
| `(2,2)-(3,3)` | $(3-2)(3-2)=1$ |

หลังเรียงลำดับ โปรแกรมจึงพิมพ์

```text
(2,2)-(3,3)
(1,1)-(3,3)
(0,0)-(10,10)
```

---

# Solution

```python
# --------------------------------------------------
# File Name : 12_Class_32.py
# Problem   : Rectangle Sorted by Area
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------


class Point:
    # __init__ method
    # Initialize the 'Point' object with x and y coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __str__ method
    # Convert the 'Point' object to a string representation
    def __str__(self):
        return f"({self.x},{self.y})"


class Rect:
    # __init__ method
    # Initialize the 'Rect' object with two points: lower left and upper right
    def __init__(self, point_01, point_02):
        self.lower_left = point_01
        self.upper_right = point_02

    # area method
    # Calculate the area of the rectangle
    def area(self):
        x1, y1 = (self.lower_left).x, (self.lower_left).y
        x2, y2 = (self.upper_right).x, (self.upper_right).y
        return (x2 - x1) * (y2 - y1)

    # __str__ method
    # Convert the 'Rect' object to a string representation
    def __str__(self):
        return f"{self.lower_left}-{self.upper_right}"

    # __lt__ method
    # Compare rectangles based on their area for sorting
    def __lt__(self, other):
        return self.area() < other.area()


# Input number of rectangles
n = int(input())

# Input rectangles and store them in a list
rectangles = []
for _ in range(n):
    x1, y1, x2, y2 = [int(e) for e in input().split()]
    rectangles.append(Rect(Point(x1, y1), Point(x2, y2)))

# Sort rectangles by area in ascending order
rectangles.sort()

# Output the rectangles in sorted order
for i in range(n):
    print(rectangles[i])
```
