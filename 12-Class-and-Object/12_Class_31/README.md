<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Point in Rectangle ★★★ (
      <a href="https://drive.google.com/file/d/1J4JtVByVaxCBeTAMoNvS2-byi9OLLFbC/view?usp=drive_link">
        <code>12_Class_31</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การประกอบออบเจ็กต์ `Point` และ `Rect`**](#การประกอบออบเจ็กต์-point-และ-rect)
-   [**การหาพื้นที่สี่เหลี่ยม**](#การหาพื้นที่สี่เหลี่ยม)
-   [**การตรวจว่าจุดอยู่ในสี่เหลี่ยมหรือไม่**](#การตรวจว่าจุดอยู่ในสี่เหลี่ยมหรือไม่)
-   [**ลำดับข้อมูลนำเข้าและผลลัพธ์**](#ลำดับข้อมูลนำเข้าและผลลัพธ์)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## การประกอบออบเจ็กต์ `Point` และ `Rect`

คลาส `Point` แทนจุดหนึ่งจุดบนระนาบ โดยเก็บพิกัด `x` และ `y` ไว้ใน
`self.x` และ `self.y`

สี่เหลี่ยมผืนผ้าหนึ่งรูปต้องใช้จุด 2 จุดในการระบุตำแหน่ง โจทย์จึงให้คลาส
`Rect` เก็บออบเจ็กต์ `Point` สองออบเจ็กต์ ได้แก่

-   `lower_left` คือมุมซ้ายล่าง $(x_1,y_1)$
-   `upper_right` คือมุมขวาบน $(x_2,y_2)$

นี่เป็นตัวอย่างของ **object composition** หรือการประกอบออบเจ็กต์:
ออบเจ็กต์ `Rect` มีออบเจ็กต์ `Point` เป็นส่วนประกอบ เมื่อต้องใช้พิกัดจึง
เข้าถึงต่อเนื่องได้ เช่น `self.lower_left.x`

---

## การหาพื้นที่สี่เหลี่ยม

เมื่อทราบมุมซ้ายล่างและมุมขวาบน ความกว้างคือ $x_2-x_1$ และความสูงคือ
$y_2-y_1$ ดังนั้นพื้นที่เท่ากับ

$$
\text{area} = (x_2-x_1)(y_2-y_1)
$$

ซึ่งเขียนใน Python ได้เป็น

```python
return (x2 - x1) * (y2 - y1)
```

เมท็อด `area()` อ่านพิกัดจาก `lower_left` และ `upper_right` แล้วคืนพื้นที่
ออกมา เนื่องจากข้อมูลนำเข้าเป็น `int` ผลลัพธ์จึงเป็นจำนวนเต็ม

---

## การตรวจว่าจุดอยู่ในสี่เหลี่ยมหรือไม่

จุด $(x,y)$ อยู่ในสี่เหลี่ยมเมื่อพิกัดทั้งสองแกนอยู่ในช่วงของสี่เหลี่ยม
พร้อมกัน

$$
x_1 \le x \le x_2
\quad\text{และ}\quad
y_1 \le y \le y_2
$$

ตรงกับเงื่อนไข Python

```python
x1 <= x <= x2 and y1 <= y <= y2
```

ต้องใช้ `and` เพราะจุดต้องผ่านเงื่อนไขทั้งแกน $x$ และแกน $y$
เครื่องหมาย `<=` ทำให้จุดบนเส้นขอบและจุดมุมของสี่เหลี่ยมถือว่า
**อยู่ในสี่เหลี่ยม** ด้วย เมท็อด `contains()` จึงคืนค่า `True` หรือ
`False` ตามผลของเงื่อนไขนี้

---

## ลำดับข้อมูลนำเข้าและผลลัพธ์

โปรแกรมทำงานตามลำดับดังนี้

1. รับ `x1 y1 x2 y2` สำหรับมุมซ้ายล่างและมุมขวาบน
2. สร้าง `Point` สองจุด แล้วนำมาสร้าง `Rect`
3. พิมพ์พื้นที่จาก `rect.area()` เป็นผลลัพธ์บรรทัดแรก
4. รับจำนวนจุดที่จะตรวจสอบ `m`
5. รับจุดอีก `m` บรรทัด และพิมพ์ผลจาก `rect.contains(p)` ทีละบรรทัด

ลำดับของ `True` และ `False` ในผลลัพธ์จึงตรงกับลำดับจุดที่รับเข้ามา

---

## ตัวอย่างการทำงาน

ถ้าสี่เหลี่ยมมีมุมเป็น $(2,2)$ และ $(10,10)$ จะมีพื้นที่

$$
(10-2)(10-2)=64
$$

สำหรับจุดตัวอย่าง

| จุด | ผลลัพธ์ | เหตุผล |
|---|---|---|
| $(0,0)$ | `False` | ทั้งสองพิกัดอยู่นอกช่วง |
| $(2,4)$ | `True` | อยู่บนขอบซ้าย เพราะ $x=2$ |
| $(3,5)$ | `True` | อยู่ภายในทั้งสองแกน |
| $(10,1)$ | `False` | $y=1$ ต่ำกว่าขอบล่าง |

---

# Solution

```python
# --------------------------------------------------
# File Name : 12_Class_31.py
# Problem   : Point in Rectangle
# Author    : Worralop Srichainont
# Date      : 2025-06-16
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
        return str((self.x, self.y))


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

    # contains method
    # Check if a point is inside the rectangle
    def contains(self, point):
        x1, y1 = (self.lower_left).x, (self.lower_left).y
        x2, y2 = (self.upper_right).x, (self.upper_right).y
        x, y = point.x, point.y
        return x1 <= x <= x2 and y1 <= y <= y2


# Input lower left and upper right points of the rectangle
x1, y1, x2, y2 = [int(e) for e in input().split()]
# Create a rectangle object
lower_left = Point(x1, y1)
upper_right = Point(x2, y2)
rect = Rect(lower_left, upper_right)

# Output the area of the rectangle
print(rect.area())

# Input number of points to check
m = int(input())
# For each point, check if it is inside the rectangle
for _ in range(m):
    x, y = [int(e) for e in input().split()]
    p = Point(x, y)
    print(rect.contains(p))
```
