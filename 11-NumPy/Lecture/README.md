<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

![11-numpy.png](/Z99-OTHERS/11-numpy/01-numpy.png)

# NumPy (การคำนวณด้วยอาเรย์)

# Contents

- [1. NumPy Array (อาเรย์ NumPy)](#1-numpy-array-อาเรย์-numpy)
    - [1.1. NumPy คืออะไร](#11-numpy-คืออะไร)
    - [1.2. การสร้างอาเรย์](#12-การสร้างอาเรย์)
    - [1.3. `shape` และจำนวนมิติ](#13-shape-และจำนวนมิติ)
- [2. Array Structure (โครงสร้างของอาเรย์)](#2-array-structure-โครงสร้างของอาเรย์)
    - [2.1. การเปลี่ยนรูปร่างด้วย `reshape`](#21-การเปลี่ยนรูปร่างด้วย-reshape)
    - [2.2. การสลับแกนด้วย `T`](#22-การสลับแกนด้วย-t)
    - [2.3. อาเรย์หนึ่งมิติกับอาเรย์สองมิติ](#23-อาเรย์หนึ่งมิติกับอาเรย์สองมิติ)
- [3. Indexing and Slicing (การเข้าถึงสมาชิก)](#3-indexing-and-slicing-การเข้าถึงสมาชิก)
    - [3.1. Indexing (การระบุตำแหน่ง)](#31-indexing-การระบุตำแหน่ง)
    - [3.2. Slicing (การเลือกช่วง)](#32-slicing-การเลือกช่วง)
    - [3.3. Fancy Indexing (การเลือกด้วยชุดตำแหน่ง)](#33-fancy-indexing-การเลือกด้วยชุดตำแหน่ง)
    - [3.4. การกำหนดค่าให้หลายตำแหน่ง](#34-การกำหนดค่าให้หลายตำแหน่ง)
- [4. Element-Wise Operations (การคำนวณรายสมาชิก)](#4-element-wise-operations-การคำนวณรายสมาชิก)
    - [4.1. อาเรย์กับ scalar](#41-อาเรย์กับ-scalar)
    - [4.2. อาเรย์กับอาเรย์](#42-อาเรย์กับอาเรย์)
    - [4.3. การเปรียบเทียบและ Boolean Indexing](#43-การเปรียบเทียบและ-boolean-indexing)
    - [4.4. Logical Operators (ตัวดำเนินการตรรกะ)](#44-logical-operators-ตัวดำเนินการตรรกะ)
- [5. Broadcasting (การขยายรูปร่างอัตโนมัติ)](#5-broadcasting-การขยายรูปร่างอัตโนมัติ)
    - [5.1. แนวคิดของ Broadcasting](#51-แนวคิดของ-broadcasting)
    - [5.2. การ Broadcast ตามแถวและคอลัมน์](#52-การ-broadcast-ตามแถวและคอลัมน์)
    - [5.3. การ Broadcast อาเรย์ทั้งสองตัว](#53-การ-broadcast-อาเรย์ทั้งสองตัว)
- [6. NumPy Functions (ฟังก์ชันสรุปผล)](#6-numpy-functions-ฟังก์ชันสรุปผล)
    - [6.1. `sum`, `min` และ `max`](#61-sum-min-และ-max)
    - [6.2. `argmin` และ `argmax`](#62-argmin-และ-argmax)
    - [6.3. `mean` และ `std`](#63-mean-และ-std)
    - [6.4. การคำนวณตามแกนด้วย `axis`](#64-การคำนวณตามแกนด้วย-axis)
    - [6.5. Dot Product (ผลคูณเชิงจุด)](#65-dot-product-ผลคูณเชิงจุด)

---

## 1. NumPy Array (อาเรย์ NumPy)

NumPy เป็นเครื่องมือสำหรับประมวลผลข้อมูลเชิงตัวเลข โดยเก็บข้อมูลไว้ใน
**NumPy Array** และคำนวณกับสมาชิกจำนวนมากได้ด้วยคำสั่งสั้น ๆ

## 1.1. NumPy คืออะไร

NumPy เป็น package ที่ไม่ได้มากับ Python โดยตรง หากเครื่องยังไม่มี NumPy
ต้องติดตั้งก่อน เช่น ใช้คำสั่ง `python -m pip install numpy` ใน terminal

เมื่อติดตั้งแล้ว นิยม import โดยตั้งชื่อย่อว่า `np`

```python
import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
```

ผลลัพธ์คือ

```
[1 2 3 4]
```

อาเรย์คล้ายกับ `list` ตรงที่เก็บข้อมูลเรียงต่อกัน แต่มีลักษณะสำคัญดังนี้

- สมาชิกในอาเรย์ใช้ data type เดียวกัน
- เก็บข้อมูลได้หลายมิติ เช่น vector, matrix และ tensor
- ใช้ tuple ของ index เพื่อระบุตำแหน่งในอาเรย์หลายมิติได้
- มี operators และ functions สำหรับคำนวณกับสมาชิกพร้อมกันทั้งอาเรย์

ตัวอย่างเช่น การบวก `1` ให้ทุกสมาชิกของ `list` ต้องเขียนวงวนหรือสร้าง
list ใหม่ แต่ NumPy Array คำนวณพร้อมกันได้ทันที วิธีเขียนจึงสั้นและมัก
ทำงานเร็วกว่าวงวนที่เขียนด้วย Python

```python
import numpy as np

numbers = np.array([10, 20, 30])
print(numbers + 1)
```

ผลลัพธ์คือ

```
[11 21 31]
```

> [!IMPORTANT]
>
> NumPy Array ไม่ได้ทำงานเหมือน `list` ทุกอย่าง เช่น `+` ระหว่างอาเรย์
> หมายถึงการบวกสมาชิกตำแหน่งเดียวกัน ไม่ใช่การต่อข้อมูล

## 1.2. การสร้างอาเรย์

ฟังก์ชัน `np.array()` สร้างอาเรย์จาก `list` หรือ nested list

```python
import numpy as np

vector = np.array([1, 2, 3, 4])
matrix = np.array([[1, 2], [3, 4]], dtype=float)
print(vector)
print(matrix)
```

ผลลัพธ์คือ

```
[1 2 3 4]
[[1. 2.]
 [3. 4.]]
```

อาร์กิวเมนต์ `dtype` กำหนดประเภทข้อมูลของสมาชิก เช่น `int`, `float`
หรือ `bool` ถ้าไม่ระบุ NumPy จะเลือกประเภทที่รองรับค่าทั้งหมดให้

NumPy มีฟังก์ชันสำหรับสร้างอาเรย์ตามรูปแบบที่ใช้บ่อย

| คำสั่ง | ความหมาย |
| --- | --- |
| `np.ndarray(shape, dtype)` | สร้างอาเรย์ตาม `shape` โดยยังไม่กำหนดค่าเริ่มต้น |
| `np.zeros(shape, dtype)` | สร้างอาเรย์ที่ทุกสมาชิกเป็น `0` |
| `np.ones(shape, dtype)` | สร้างอาเรย์ที่ทุกสมาชิกเป็น `1` |
| `np.zeros_like(a, dtype)` | สร้างอาเรย์ศูนย์ที่มีรูปร่างเหมือน `a` |
| `np.ones_like(a, dtype)` | สร้างอาเรย์หนึ่งที่มีรูปร่างเหมือน `a` |
| `np.identity(n, dtype)` | สร้าง identity matrix ขนาด `n` คูณ `n` |
| `np.arange(start, stop, step)` | สร้างค่าตั้งแต่ `start` แต่ไม่รวม `stop` |

```python
import numpy as np

zeros = np.zeros((2, 3), dtype=int)
ones = np.ones_like(zeros, dtype=float)
identity = np.identity(3, dtype=int)
steps = np.arange(0.0, 1.0, 0.2)

print(zeros)
print(ones)
print(identity)
print(steps)
```

ผลลัพธ์คือ

```
[[0 0 0]
 [0 0 0]]
[[1. 1. 1.]
 [1. 1. 1.]]
[[1 0 0]
 [0 1 0]
 [0 0 1]]
[0.  0.2 0.4 0.6 0.8]
```

> [!WARNING]
>
> `np.ndarray()` จองพื้นที่โดยไม่กำหนดค่าเริ่มต้น สมาชิกจึงเป็นค่าเดิมที่ค้างอยู่
> ในหน่วยความจำและคาดเดาไม่ได้ ต้องกำหนดค่าก่อนนำไปใช้ หากต้องการค่าเริ่มต้น
> ที่แน่นอนให้ใช้ `np.zeros()` หรือ `np.ones()`

## 1.3. `shape` และจำนวนมิติ

Attribute `shape` คืน tuple ที่บอกขนาดของแต่ละมิติ และ `len(a.shape)`
บอกจำนวนมิติของอาเรย์ `a`

```python
import numpy as np

a = np.ones((3, 4), dtype=int)
print(a.shape)
print(a.shape[0])
print(a.shape[1])
print(len(a.shape))
```

ผลลัพธ์คือ

```
(3, 4)
3
4
2
```

อาเรย์ `a` มี 3 แถว 4 คอลัมน์ จึงมี `shape` เป็น `(3, 4)` และมี 2 มิติ
ดังที่ผลลัพธ์บรรทัดสุดท้ายแสดง

---

## 2. Array Structure (โครงสร้างของอาเรย์)

สมาชิกชุดเดิมสามารถจัดเป็นรูปร่างใหม่หรือสลับแกนได้ โดยจำนวนสมาชิกทั้งหมด
ยังคงเดิม

## 2.1. การเปลี่ยนรูปร่างด้วย `reshape`

Method `reshape(newshape)` จัดสมาชิกของอาเรย์ลงใน `shape` ใหม่ตามลำดับเดิม

```python
import numpy as np

a = np.arange(8)
b = a.reshape((2, 4))
c = b.reshape((4, 2))

print(a)
print(b)
print(c)
```

ผลลัพธ์คือ

```
[0 1 2 3 4 5 6 7]
[[0 1 2 3]
 [4 5 6 7]]
[[0 1]
 [2 3]
 [4 5]
 [6 7]]
```

จำนวนช่องของรูปร่างใหม่ต้องเท่ากับจำนวนสมาชิกเดิม อาเรย์ 8 สมาชิกจึงเปลี่ยนเป็น
`(2, 4)` หรือ `(4, 2)` ได้ แต่เปลี่ยนเป็น `(2, 3)` ไม่ได้และจะเกิด
`ValueError`

## 2.2. การสลับแกนด้วย `T`

Attribute `T` คือ transpose ของอาเรย์ สำหรับ matrix จะเปลี่ยนแถวให้เป็นคอลัมน์
และเปลี่ยนคอลัมน์ให้เป็นแถว

```python
import numpy as np

a = np.arange(8).reshape((2, 4))
print(a)
print(a.T)
```

ผลลัพธ์คือ

```
[[0 1 2 3]
 [4 5 6 7]]
[[0 4]
 [1 5]
 [2 6]
 [3 7]]
```

ดังนั้น `a.shape` เป็น `(2, 4)` ขณะที่ `a.T.shape` เป็น `(4, 2)`

## 2.3. อาเรย์หนึ่งมิติกับอาเรย์สองมิติ

อาเรย์รูปร่าง `(8,)`, `(1, 8)` และ `(8, 1)` มีสมาชิกเท่ากัน แต่มีมิติและ
รูปร่างต่างกัน

```python
import numpy as np

vector = np.arange(4)
row = vector.reshape((1, 4))
column = row.T

print(vector.shape, vector.T.shape)
print(row.shape, column.shape)
print(column)
```

ผลลัพธ์คือ

```
(4,) (4,)
(1, 4) (4, 1)
[[0]
 [1]
 [2]
 [3]]
```

> [!IMPORTANT]
>
> การ transpose อาเรย์หนึ่งมิติไม่เปลี่ยนรูปร่าง เพราะ `(4,)` มีเพียงแกนเดียว
> หากต้องการ row หรือ column ต้องใช้ `reshape()` ให้เป็นสองมิติก่อน

---

## 3. Indexing and Slicing (การเข้าถึงสมาชิก)

Indexing เลือกสมาชิกตามตำแหน่ง ส่วน slicing เลือกช่วงข้อมูล หลักการคล้าย `list`
แต่ NumPy เลือกหลายแกนในวงเล็บเหลี่ยมคู่เดียวได้

## 3.1. Indexing (การระบุตำแหน่ง)

สำหรับอาเรย์สองมิติ ให้เขียน index ของแถวและคอลัมน์คั่นด้วย comma

```python
import numpy as np

a = np.array([[10, 20, 30], [40, 50, 60]])
print(a[0, 2])
print(a[1, 0])
print(a[(1, 1)])
```

ผลลัพธ์คือ

```
30
40
50
```

คำสั่ง `a[1, 1]` มีความหมายเดียวกับ `a[(1, 1)]` เพราะ NumPy ใช้ tuple
`(1, 1)` เป็น index ของตำแหน่งแถว 1 คอลัมน์ 1

## 3.2. Slicing (การเลือกช่วง)

Slice มีรูปแบบ `start:stop:step` เช่นเดียวกับ `list` และใช้แยกกันในแต่ละแกน

```python
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
])

print(a[::2, ::2])
print(a[::-1, ::-1])
```

ผลลัพธ์คือ

```
[[1 3]
 [7 9]]
[[12 11 10]
 [ 9  8  7]
 [ 6  5  4]
 [ 3  2  1]]
```

- `a[::2, ::2]` เลือกแถว index คู่และคอลัมน์ index คู่
- `a[::-1, ::-1]` กลับลำดับทั้งแถวและคอลัมน์

> [!WARNING]
>
> `a[::2][::2]` ใช้ slice ครั้งที่สองกับ **แถว** ของผลจากครั้งแรก จึงไม่ใช่
> การเลือกคอลัมน์ หากต้องการเลือกทั้งสองแกนให้เขียน `a[::2, ::2]`

## 3.3. Fancy Indexing (การเลือกด้วยชุดตำแหน่ง)

Fancy indexing ใช้รายการ index หรืออาเรย์ Boolean เพื่อเลือกสมาชิกที่ต้องการ

```python
import numpy as np

a = np.arange(0, 100, 10)
selected = a[[8, 1, 9, 0]]
filtered = selected[[True, False, False, True]]

print(selected)
print(filtered)
```

ผลลัพธ์คือ

```
[80 10 90  0]
[80  0]
```

เมื่อใส่รายการ index ให้ทั้งสองแกน NumPy จะจับคู่ตำแหน่งตามลำดับ ไม่ได้เลือก
พื้นที่สี่เหลี่ยม

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 1, 0]])
b = a[[1, 3, 2], [2, 0, 1]]
print(b)
```

ผลลัพธ์คือ

```
[6 0 8]
```

ผลลัพธ์มาจาก `a[1, 2]`, `a[3, 0]` และ `a[2, 1]` ตามลำดับ

## 3.4. การกำหนดค่าให้หลายตำแหน่ง

ด้านซ้ายของ `=` เป็น slice ได้ เมื่อกำหนด scalar ให้ slice ค่านั้นจะถูกใส่
ในทุกตำแหน่งที่เลือก

```python
import numpy as np

a = np.zeros((4, 4), dtype=int)
a[:, ::2] = 1
a[1::2, :] = 2
print(a)
```

ผลลัพธ์คือ

```
[[1 0 1 0]
 [2 2 2 2]
 [1 0 1 0]
 [2 2 2 2]]
```

คำสั่งแรกใส่ `1` ในคอลัมน์ index คู่ทุกแถว จากนั้นคำสั่งที่สองเขียน `2`
ทับทุกคอลัมน์ของแถว index คี่

---

## 4. Element-Wise Operations (การคำนวณรายสมาชิก)

Element-wise operation คือการนำ operation เดียวกันไปคำนวณกับสมาชิกแต่ละ
ตำแหน่ง แล้วคืนผลเป็นอาเรย์

## 4.1. อาเรย์กับ scalar

เมื่อคำนวณอาเรย์กับ scalar NumPy จะใช้ scalar เดียวกันกับสมาชิกทุกตำแหน่ง

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a + 1)
print(a**2 + 1)
print(a / 2)
```

ผลลัพธ์คือ

```
[2 3 4 5 6]
[ 2  5 10 17 26]
[0.5 1.  1.5 2.  2.5]
```

ฟังก์ชันของ NumPy หลายฟังก์ชันคำนวณแบบ element-wise เช่น `np.log10()`
และ `np.sin()`

```python
import numpy as np

powers = np.array([10, 100, 1000, 10000])
angles = np.array([np.pi / 2, np.pi, 3 * np.pi / 2])

print(np.log10(powers))
print(np.sin(angles))
```

ผลลัพธ์คือ

```
[1. 2. 3. 4.]
[ 1.0000000e+00  1.2246468e-16 -1.0000000e+00]
```

## 4.2. อาเรย์กับอาเรย์

อาเรย์ที่มีรูปร่างเท่ากันคำนวณกันตามตำแหน่งด้วย `+`, `-`, `*`, `/` และ
`**` ได้

```python
import numpy as np

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

print(u + v)
print(u * v)
```

ผลลัพธ์คือ

```
[5 7 9]
[ 4 10 18]
```

โดย `u + v` คำนวณเป็น `[1 + 4, 2 + 5, 3 + 6]` และ `u * v`
คือการคูณรายสมาชิก ไม่ใช่ dot product หรือการคูณ matrix

## 4.3. การเปรียบเทียบและ Boolean Indexing

การเปรียบเทียบอาเรย์กับ scalar ให้ผลเป็นอาเรย์ของ `True` และ `False`
ซึ่งนำกลับไปใช้เลือกสมาชิกได้

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
is_odd = a % 2 == 1
positions = np.arange(a.shape[0])

print(is_odd)
print(a[is_odd])
print(positions[is_odd])
print(np.sum(is_odd))
```

ผลลัพธ์คือ

```
[ True False  True False  True]
[1 3 5]
[0 2 4]
3
```

Boolean indexing เลือกเฉพาะตำแหน่งที่เงื่อนไขเป็น `True` และ `np.sum()`
นับจำนวน `True` ได้ เพราะ `True` มีค่าเทียบเท่า `1` และ `False` เทียบเท่า `0`

## 4.4. Logical Operators (ตัวดำเนินการตรรกะ)

เมื่อต้องรวมหลายเงื่อนไขแบบ element-wise ให้ใช้ `&` (and), `|` (or) และ
`~` (not)

```python
import numpy as np

a = np.array([9, 3, 0, 2, 6])
between = (2 < a) & (a < 5)
outside = (a <= 2) | (a >= 6)

print(a[between])
print(a[outside])
print(~between)
```

ผลลัพธ์คือ

```
[3]
[9 0 2 6]
[ True False  True  True  True]
```

> [!WARNING]
>
> ต้องใส่วงเล็บรอบเงื่อนไขแต่ละส่วน เช่น `(2 < a) & (a < 5)` ห้ามเขียน
> `2 < a < 5` หรือใช้ `and`, `or`, `not` กับอาเรย์ เพราะ operators เหล่านั้น
> ไม่ได้คำนวณรายสมาชิก

---

## 5. Broadcasting (การขยายรูปร่างอัตโนมัติ)

Broadcasting ทำให้อาเรย์ที่มีรูปร่างต่างกันบางคู่คำนวณแบบ element-wise กันได้
โดย NumPy ขยายมิติที่เข้ากันได้ให้มีขนาดเท่ากันในเชิงแนวคิด

## 5.1. แนวคิดของ Broadcasting

ตัวอย่างที่ง่ายที่สุดคือ scalar กับอาเรย์ NumPy ใช้ scalar เดิมกับทุกตำแหน่ง

```python
import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])
print(x + 2)
```

ผลลัพธ์คือ

```
[[3 4]
 [5 6]
 [7 8]]
```

เมื่อตรวจรูปร่างเพื่อ broadcasting ให้เปรียบเทียบมิติจากขวาไปซ้าย แต่ละคู่
ต้องมีขนาดเท่ากัน หรืออย่างน้อยด้านหนึ่งต้องมีขนาด `1`

> [!WARNING]
>
> Broadcasting ใช้ไม่ได้กับทุกรูปร่าง เช่น `(3,)` กับ `(2, 2)` มีมิติขวาสุด
> เป็น `3` และ `2` ซึ่งไม่เท่ากันและไม่มีด้านใดเป็น `1` จึงเกิด `ValueError`

## 5.2. การ Broadcast ตามแถวและคอลัมน์

อาเรย์รูปร่าง `(2,)` สามารถ broadcast ซ้ำไปทุกแถวของ matrix รูปร่าง `(3, 2)`

```python
import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])
row = np.array([10, 20])
print(x + row)
```

ผลลัพธ์คือ

```
[[11 22]
 [13 24]
 [15 26]]
```

หากต้องการให้ค่าต่างกันในแต่ละแถวและซ้ำไปตามคอลัมน์ ให้ใช้อาเรย์สองมิติ
รูปร่าง `(3, 1)`

```python
import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])
column = np.array([[10], [20], [30]])
print(x + column)
```

ผลลัพธ์คือ

```
[[11 12]
 [23 24]
 [35 36]]
```

ในตัวอย่างแรก `(2,)` จับคู่กับมิติสุดท้ายของ `(3, 2)` ส่วนตัวอย่างที่สอง
มิติขนาด `1` ของ `(3, 1)` ถูกขยายเป็น 2 คอลัมน์

## 5.3. การ Broadcast อาเรย์ทั้งสองตัว

NumPy อาจ broadcast อาเรย์ทั้งสองตัวพร้อมกัน เช่น column รูปร่าง `(3, 1)`
กับ row รูปร่าง `(2,)` ขยายเป็นผลลัพธ์รูปร่าง `(3, 2)`

```python
import numpy as np

column = np.array([[1], [2], [3]])
row = np.array([4, 5])
print(column + row)
```

ผลลัพธ์คือ

```
[[5 6]
 [6 7]
 [7 8]]
```

มองในเชิงแนวคิด `column` ถูกทำซ้ำไปทางขวา และ `row` ถูกทำซ้ำลงล่าง
แต่ NumPy ไม่จำเป็นต้องสร้างอาเรย์ซ้ำเหล่านั้นจริงก่อนคำนวณ

---

## 6. NumPy Functions (ฟังก์ชันสรุปผล)

NumPy มีฟังก์ชันสำหรับรวมและสรุปข้อมูลทั้งอาเรย์ หรือเลือกคำนวณตามแกนด้วย
อาร์กิวเมนต์ `axis`

## 6.1. `sum`, `min` และ `max`

- `np.sum(a)` หาผลรวม
- `np.min(a)` หาค่าน้อยที่สุด
- `np.max(a)` หาค่ามากที่สุด

```python
import numpy as np

a = np.array([[1, 2, 3], [8, 7, 6]])
print(np.sum(a))
print(np.min(a))
print(np.max(a))
```

ผลลัพธ์คือ

```
27
1
8
```

## 6.2. `argmin` และ `argmax`

`np.argmin(a)` และ `np.argmax(a)` คืน **index** ของค่าน้อยที่สุดและมากที่สุด
ไม่ใช่ค่านั้นเอง หากไม่ระบุ `axis` NumPy มองอาเรย์ที่คลี่เป็นหนึ่งมิติ

```python
import numpy as np

a = np.array([[4, 9, 2], [7, 1, 8]])
print(np.argmin(a))
print(np.argmax(a))
print(np.argmin(a, axis=1))
```

ผลลัพธ์คือ

```
4
1
[2 1]
```

ค่า `1` อยู่ที่ตำแหน่ง 4 ของลำดับ `[4, 9, 2, 7, 1, 8]` ส่วนเมื่อกำหนด
`axis=1` ผลลัพธ์บอก index ของค่าน้อยที่สุดภายในแต่ละแถว

## 6.3. `mean` และ `std`

`np.mean(a)` หาค่าเฉลี่ย และ `np.std(a)` หาส่วนเบี่ยงเบนมาตรฐาน

```python
import numpy as np

a = np.array([2, 4, 6, 8])
print(np.mean(a))
print(np.std(a))
```

ผลลัพธ์คือ

```
5.0
2.23606797749979
```

## 6.4. การคำนวณตามแกนด้วย `axis`

สำหรับ matrix สองมิติ

- `axis=0` ยุบแกนแถว จึงคำนวณลงมาตามแต่ละคอลัมน์
- `axis=1` ยุบแกนคอลัมน์ จึงคำนวณไปตามแต่ละแถว
- ถ้าไม่ระบุ `axis` จะคำนวณจากสมาชิกทั้งหมด

```python
import numpy as np

a = np.array([
    [1, 2, 3, 4, 5],
    [10, 9, 8, 7, 6],
    [11, 12, 13, 14, 15],
    [20, 19, 18, 17, 16],
])

print(np.sum(a, axis=0))
print(np.sum(a, axis=1))
print(np.mean(a, axis=0))
```

ผลลัพธ์คือ

```
[42 42 42 42 42]
[15 40 65 90]
[10.5 10.5 10.5 10.5 10.5]
```

ฟังก์ชันเหล่านี้เขียนได้ทั้งรูป `np.sum(a, axis=0)` และ method
`a.sum(axis=0)` รูปแบบเดียวกันใช้ได้กับ `min`, `max`, `argmin`, `argmax`,
`mean` และ `std`

## 6.5. Dot Product (ผลคูณเชิงจุด)

ฟังก์ชัน `np.dot(a, b)` คำนวณ dot product โดยความหมายขึ้นกับมิติของข้อมูล

- vector กับ vector ได้ scalar จากผลรวมของผลคูณตำแหน่งเดียวกัน
- vector กับ matrix ได้ vector
- matrix กับ vector ได้ vector
- matrix กับ matrix คือ matrix multiplication

```python
import numpy as np

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
matrix = np.array([[4, 7], [5, 8], [6, 9]])

print(np.dot(u, v))
print(np.dot(u, matrix))
```

ผลลัพธ์คือ

```
32
[32 50]
```

ตัวอย่าง matrix multiplication ต้องให้จำนวนคอลัมน์ของ matrix แรกเท่ากับ
จำนวนแถวของ matrix ที่สอง

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8], [9, 10], [11, 12]])

print(np.dot(a, b))
print(a.dot(b))
```

ผลลัพธ์คือ

```
[[ 58  64]
 [139 154]]
[[ 58  64]
 [139 154]]
```

> [!IMPORTANT]
>
> `a * b` คือการคูณแบบ element-wise และต้องอาศัยรูปร่างที่ broadcast กันได้
> ส่วน `np.dot(a, b)` หรือ `a.dot(b)` คำนวณ dot product จึงเป็นคนละ operation
