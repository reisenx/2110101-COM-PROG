<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

![01-tsd.png](/Z99-OTHERS/10-tsd/01-tsd.png)

# Contents

- [1. Tuple](#1-tuple)
    - [1.1. Creating a Tuple](#11-creating-a-tuple)
    - [1.2. Tuple Operations](#12-tuple-operations)
    - [1.3. Tuple vs. List](#13-tuple-vs-list)
- [2. Set](#2-set)
    - [2.1. Creating a Set](#21-creating-a-set)
    - [2.2. Membership and Iteration](#22-membership-and-iteration)
    - [2.3. Set Operations](#23-set-operations)
    - [2.4. Adding and Removing Members](#24-adding-and-removing-members)
- [3. Converting and Sorting Collections](#3-converting-and-sorting-collections)
    - [3.1. Converting between Collections](#31-converting-between-collections)
    - [3.2. `sort()` vs. `sorted()`](#32-sort-vs-sorted)
- [4. More on Dict](#4-more-on-dict)
    - [4.1. List vs. Dict](#41-list-vs-dict)
    - [4.2. Collection Values](#42-collection-values)
    - [4.3. `keys()`, `values()`, and `items()`](#43-keys-values-and-items)
    - [4.4. Reverse Mapping](#44-reverse-mapping)
- [5. Choosing a Collection](#5-choosing-a-collection)
    - [5.1. Comparison](#51-comparison)

---

## 1. Tuple

**Tuple (ทูเพิล)** เป็น collection ที่เก็บข้อมูลหลายค่าเรียงตามลำดับ
คล้ายกับ `list` แต่เมื่อสร้างแล้วจะเปลี่ยนสมาชิก เพิ่มสมาชิก
หรือลบสมาชิกโดยตรงไม่ได้ คุณสมบัตินี้เรียกว่า **immutable**

## 1.1. Creating a Tuple

เขียน tuple โดยครอบสมาชิกด้วยวงเล็บ `()` และคั่นสมาชิกด้วยเครื่องหมายจุลภาค
`,`

```python
point = (3, 5)
empty = ()
one_item = ("Python",)

print(point)
print(empty)
print(one_item)
```

ผลลัพธ์คือ

```
(3, 5)
()
('Python',)
```

> [!IMPORTANT]
>
> tuple ที่มีสมาชิกหนึ่งค่าต้องมี `,` เช่น `(9,)` เพราะ `(9)` เป็นเพียง
> จำนวนเต็มที่เขียนในวงเล็บ ไม่ใช่ tuple

Python สามารถ **pack** หลายค่าเป็น tuple และ **unpack** สมาชิกของ tuple
ใส่ตัวแปรหลายตัวได้

```python
record = "Ada", 36, "engineer"
name, age, occupation = record

print(record)
print(name)
print(age)
print(occupation)
```

ผลลัพธ์คือ

```
('Ada', 36, 'engineer')
Ada
36
engineer
```

จำนวนตัวแปรทางซ้ายต้องเท่ากับจำนวนสมาชิกใน tuple จึงจะ unpack ได้พอดี

## 1.2. Tuple Operations

tuple ใช้ operation ที่ไม่แก้ไขข้อมูลได้คล้าย `list` เช่น `len()` การเข้าถึง
ด้วย index การ slice การค้นหาด้วย `in` และ method `index()`

```python
values = (11, 22, 33, 44)

print(len(values))
print(values[0], values[-1])
print(values[1:3])
print(33 in values)
print(values.index(33))
```

ผลลัพธ์คือ

```
4
11 44
(22, 33)
True
2
```

แต่คำสั่งอย่าง `values[0] = 99` ใช้ไม่ได้และทำให้เกิด `TypeError`
หากต้องการข้อมูลที่เปลี่ยนไป ต้องสร้าง tuple ใหม่

```python
values = (11, 22, 33)
values = (99,) + values[1:]
print(values)
```

ผลลัพธ์คือ

```
(99, 22, 33)
```

## 1.3. Tuple vs. List

โดยทั่วไปควรเลือก collection ให้สื่อความหมายของข้อมูล

- ใช้ `list` เมื่อสมาชิกมีความหมายคล้ายกัน และรายการอาจเปลี่ยนค่าหรือขนาด
  เช่น รายการอุณหภูมิที่วัดทุกชั่วโมง
- ใช้ `tuple` เมื่อแต่ละตำแหน่งมีความหมายเฉพาะ และโครงสร้างไม่ควรเปลี่ยน
  เช่น พิกัด `(x, y)` หรือข้อมูล `(name, year)`

tuple จึงช่วยป้องกันการเปลี่ยนสมาชิกโดยไม่ตั้งใจ และสามารถเก็บ tuple
หลายรายการใน list ได้

```python
locations = [("library", 13.738), ("station", 13.746)]

for place, latitude in locations:
    print(place, latitude)
```

ผลลัพธ์คือ

```
library 13.738
station 13.746
```

> [!WARNING]
>
> ความ immutable ของ tuple ใช้กับช่องสมาชิกของ tuple เท่านั้น
> ถ้าสมาชิกภายในเป็น object ที่แก้ไขได้ เช่น `list` เนื้อหาของ list นั้น
> ยังเปลี่ยนได้

```python
data = ([1, 2], "ready")
data[0].append(3)
print(data)
```

ผลลัพธ์คือ

```
([1, 2, 3], 'ready')
```

---

## 2. Set

**Set (เซต)** เป็น collection ที่สมาชิกไม่ซ้ำกัน และไม่มีลำดับตายตัว
จึงเหมาะกับการตรวจว่ามีข้อมูลอยู่หรือไม่ และการดำเนินการทางเซต

## 2.1. Creating a Set

ใช้วงเล็บปีกกา `{}` สร้าง set ที่มีสมาชิก หรือใช้ `set()` สร้าง set ว่าง

```python
numbers = {4, 3, 1, 2, 3}
empty = set()

print(sorted(numbers))
print(len(numbers))
print(empty)
```

ผลลัพธ์คือ

```
[1, 2, 3, 4]
4
set()
```

สมาชิก `3` ที่เขียนซ้ำถูกเก็บเพียงครั้งเดียว ส่วน `{}` ไม่ใช่ set ว่าง
แต่เป็น `dict` ว่าง

```python
print(type({}))
print(type(set()))
```

ผลลัพธ์คือ

```
<class 'dict'>
<class 'set'>
```

สมาชิกของ set ต้องเป็น **hashable** ซึ่งโดยทั่วไปหมายถึงค่าที่ไม่เปลี่ยนแปลง
เช่น `int`, `float`, `bool`, `str` และ tuple ที่สมาชิกภายในทั้งหมด hashable
ส่วน `list`, `dict` และ `set` เป็นสมาชิกของ set ไม่ได้

> [!WARNING]
>
> ไม่ใช่ tuple ทุกตัวจะ hashable เช่น `([1, 2], 3)` มี `list` อยู่ภายใน
> จึงนำไปใส่ใน set ไม่ได้

## 2.2. Membership and Iteration

ใช้ `in` ตรวจสมาชิก ใช้ `len()` นับสมาชิก และใช้ `for` แจกแจงสมาชิกได้
การค้นหาสมาชิกใน set โดยทั่วไปเร็วกว่าใน list มาก โดยเฉพาะเมื่อข้อมูลมีจำนวนมาก

```python
allowed_codes = {200, 201, 204}

print(200 in allowed_codes)
print(404 in allowed_codes)
print(len(allowed_codes))
```

ผลลัพธ์คือ

```
True
False
3
```

ลำดับการวนซ้ำและการแสดง set ไม่ควรถูกนำไปใช้เป็นลำดับข้อมูล
ถ้าต้องการผลลัพธ์ที่เรียงแน่นอน ให้ใช้ `sorted()`

```python
letters = {"C", "A", "B"}

for letter in sorted(letters):
    print(letter)
```

ผลลัพธ์คือ

```
A
B
C
```

set ยังช่วยตรวจข้อมูลซ้ำได้ เพราะการสร้าง set จะเก็บแต่ละค่าเพียงครั้งเดียว

```python
codes = [7, 4, 7, 9]
has_duplicate = len(set(codes)) != len(codes)
print(has_duplicate)
```

ผลลัพธ์คือ

```
True
```

## 2.3. Set Operations

กำหนดให้ `A` และ `B` เป็น set ดังนี้

```python
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
```

operation สำคัญมีดังนี้

| Operation | Method | Operator | ความหมาย |
| :-- | :-- | :--: | :-- |
| Union | `A.union(B)` | `A \| B` | สมาชิกที่อยู่ใน `A` หรือ `B` |
| Intersection | `A.intersection(B)` | `A & B` | สมาชิกที่อยู่ในทั้ง `A` และ `B` |
| Difference | `A.difference(B)` | `A - B` | สมาชิกที่อยู่ใน `A` แต่ไม่อยู่ใน `B` |
| Symmetric difference | `A.symmetric_difference(B)` | `A ^ B` | สมาชิกที่อยู่ใน set ใด set หนึ่งเท่านั้น |

```python
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

print(sorted(A | B))
print(sorted(A & B))
print(sorted(A - B))
print(sorted(B - A))
print(sorted(A ^ B))
```

ผลลัพธ์คือ

```
[1, 2, 3, 4, 5, 6, 7]
[3, 4, 5]
[1, 2]
[6, 7]
[1, 2, 6, 7]
```

**Subset (สับเซต)** หมายถึง set ที่สมาชิกทุกตัวอยู่ในอีก set หนึ่ง
ตรวจได้ด้วย `<=` หรือ `issubset()`

```python
A = {1, 2}
B = {1, 2, 3}
C = {2, 4}

print(A <= B, A.issubset(B))
print(C <= B, C.issubset(B))
```

ผลลัพธ์คือ

```
True True
False False
```

## 2.4. Adding and Removing Members

set เปลี่ยนแปลงได้ ใช้ `add()` เพิ่มสมาชิกหนึ่งค่า และใช้ `remove()`
ลบสมาชิกที่มีอยู่

```python
active = {1, 2}
active.add(9)
active.remove(1)
print(sorted(active))
```

ผลลัพธ์คือ

```
[2, 9]
```

> [!WARNING]
>
> `remove()` จะเกิด `KeyError` ถ้าสมาชิกที่ต้องการลบไม่มีอยู่ใน set
> จึงควรตรวจด้วย `in` ก่อนเมื่อไม่แน่ใจ

---

## 3. Converting and Sorting Collections

constructor `list()`, `tuple()` และ `set()` รับ iterable แล้วสร้าง collection
ชนิดใหม่ได้ การแปลงชนิดอาจเปลี่ยนทั้งลำดับและจำนวนสมาชิก

## 3.1. Converting between Collections

```python
data = [1, 2, 3, 1]

print(list(data))
print(tuple(data))
print(sorted(set(data)))
```

ผลลัพธ์คือ

```
[1, 2, 3, 1]
(1, 2, 3, 1)
[1, 2, 3]
```

- `list()` และ `tuple()` รักษาสมาชิกซ้ำและลำดับของ iterable ที่มีลำดับ
- `set()` ตัดสมาชิกซ้ำ และไม่รับประกันลำดับ
- เมื่อแปลง `str` จะได้อักขระทีละตัว
- เมื่อแปลง `dict` โดยตรง จะได้เฉพาะ key

```python
word = "Mono"
scores = {"A": 2, "B": 5}

print(tuple(word))
print(sorted(set(word)))
print(list(scores))
print(tuple(scores))
```

ผลลัพธ์คือ

```
('M', 'o', 'n', 'o')
['M', 'n', 'o']
['A', 'B']
('A', 'B')
```

## 3.2. `sort()` vs. `sorted()`

`list.sort()` เรียงสมาชิกภายใน list เดิมและใช้ได้เฉพาะกับ `list`
ส่วน built-in function `sorted()` รับ iterable ได้หลายชนิด คืนผลเป็น `list` ใหม่
และไม่แก้ไขข้อมูลต้นฉบับ

```python
numbers = [4, 1, 3, 2]
result = numbers.sort()

print(numbers)
print(result)
```

ผลลัพธ์คือ

```
[1, 2, 3, 4]
None
```

`sort()` คืนค่า `None` เพราะหน้าที่ของ method นี้คือแก้ไข list เดิม

```python
values = (4, 1, 3, 2)
ordered = sorted(values)

print(ordered)
print(values)
print(sorted({22: 2, 90: 3, 3: 23}))
```

ผลลัพธ์คือ

```
[1, 2, 3, 4]
(4, 1, 3, 2)
[3, 22, 90]
```

ตัวอย่างสุดท้ายเรียง key ของ `dict` เพราะการวนข้อมูลใน `dict` โดยตรง
จะได้ key

---

## 4. More on Dict

**Dict (dictionary)** เก็บข้อมูลเป็นคู่ **key-value** และใช้ key เข้าถึง value
แทนการใช้ index แบบ `list` หรือ `tuple`

## 4.1. List vs. Dict

สมมติว่าต้องเก็บราคาสินค้าตามรหัส การใช้ list สองรายการทำให้ต้องค้นหา index
ของรหัสก่อน และต้องรักษาให้ข้อมูลในสอง list ตรงตำแหน่งกันเสมอ

```python
codes = ["P01", "P02", "P03"]
prices = [35, 50, 20]

code = "P02"
if code in codes:
    print(prices[codes.index(code)])
```

ผลลัพธ์คือ

```
50
```

dict แสดงความสัมพันธ์นี้ได้โดยตรง จึงค้นและเรียงเพื่อแสดงผลได้สะดวกกว่า

```python
prices = {"P01": 35, "P02": 50, "P03": 20}

code = "P02"
if code in prices:
    print(prices[code])

for code in sorted(prices):
    print(code, prices[code])
```

ผลลัพธ์คือ

```
50
P01 35
P02 50
P03 20
```

ใน Python 3.11 dict รักษาลำดับที่เพิ่ม key แต่ลำดับดังกล่าวไม่ใช่ลำดับตามขนาด
หรือตามตัวอักษร หากต้องการเรียง key ให้ใช้ `sorted(d)` อย่างชัดเจน

## 4.2. Collection Values

value ของ dict เป็นข้อมูลชนิดใดก็ได้ รวมถึง `list`, `tuple`, `set` หรือ `dict`
จึงใช้สร้างโครงสร้างข้อมูลที่แสดงความสัมพันธ์ได้หลายแบบ

tuple เหมาะกับ value ที่มีตำแหน่งแน่นอน เช่น `(day, month, year)`

```python
released = {
    "alpha": (3, 4, 2024),
    "beta": (18, 9, 2025),
}

print(released["alpha"])
print(released["alpha"][2])
```

ผลลัพธ์คือ

```
(3, 4, 2024)
2024
```

set เหมาะกับ value ที่ต้องเก็บสมาชิกไม่ซ้ำและไม่สนใจลำดับ

```python
skills = {
    "Mali": {"Python", "SQL"},
    "Niran": {"Python"},
}

skills["Niran"].add("Git")
print(sorted(skills["Niran"]))
```

ผลลัพธ์คือ

```
['Git', 'Python']
```

> [!IMPORTANT]
>
> `{name}` สร้าง set ที่มีข้อความ `name` เป็นสมาชิกหนึ่งค่า แต่ `set(name)`
> จะแยกข้อความออกเป็นอักขระ จึงให้ผลต่างกัน

## 4.3. `keys()`, `values()`, and `items()`

dict มี method สำหรับเลือกส่วนที่ต้องการวนซ้ำ

- `d.keys()` แจกแจง key
- `d.values()` แจกแจง value
- `d.items()` แจกแจงคู่ `(key, value)` ซึ่ง unpack ใน `for` ได้

```python
vehicles = {
    "Vios": "Toyota",
    "Wave": "Honda",
    "Civic": "Honda",
}

for model in vehicles.keys():
    print(model)

for brand in vehicles.values():
    print(brand)

for model, brand in vehicles.items():
    print(model, brand)
```

ผลลัพธ์ตามลำดับที่เพิ่ม key ใน Python 3.11 คือ

```
Vios
Wave
Civic
Toyota
Honda
Honda
Vios Toyota
Wave Honda
Civic Honda
```

การเขียน `for key in d` ให้ผลเหมือน `for key in d.keys()` ดังนั้นมักเขียน
รูปที่สั้นกว่าเมื่อใช้เฉพาะ key

## 4.4. Reverse Mapping

**Reverse mapping** คือการสลับให้ value เดิมกลายเป็น key ของ dict ใหม่
ถ้า value เดิมไม่ซ้ำ แต่ละ key ใหม่เก็บค่าเดิมเพียงค่าเดียวได้

```python
room_by_course = {"Calculus": "A1", "Physics": "B2"}
course_by_room = {}

for course, room in room_by_course.items():
    course_by_room[room] = course

print(course_by_room)
```

ผลลัพธ์คือ

```
{'A1': 'Calculus', 'B2': 'Physics'}
```

ถ้า value เดิมอาจซ้ำ key ใหม่หนึ่งตัวต้องเก็บหลายค่า จึงใช้ set เป็น value
และสร้าง set ว่างก่อนเรียก `add()` ครั้งแรก

```python
category_by_product = {
    "pen": "stationery",
    "book": "stationery",
    "mug": "kitchen",
}
products_by_category = {}

for product, category in category_by_product.items():
    if category not in products_by_category:
        products_by_category[category] = set()
    products_by_category[category].add(product)

for category in sorted(products_by_category):
    products = sorted(products_by_category[category])
    print(category, products)
```

ผลลัพธ์คือ

```
kitchen ['mug']
stationery ['book', 'pen']
```

---

## 5. Choosing a Collection

การเลือก collection ควรเริ่มจากความหมายของข้อมูล ต้องรักษาลำดับหรือไม่
ต้องแก้ไขข้อมูลหรือไม่ และต้องเข้าถึงข้อมูลด้วยตำแหน่งหรือ key

## 5.1. Comparison

| ชนิด | ลักษณะข้อมูล | การเข้าถึง | การค้นด้วย `in` | การเปลี่ยนแปลง |
| :-- | :-- | :-- | :-- | :-- |
| `list` | มีลำดับ สมาชิกซ้ำได้ | ใช้ integer index เช่น `d[i]` | ค้นตามสมาชิกในรายการ | เพิ่ม ลบ หรือแก้สมาชิกได้ |
| `tuple` | มีลำดับ สมาชิกซ้ำได้ | ใช้ integer index เช่น `d[i]` | ค้นตามสมาชิกในรายการ | แก้ไม่ได้ ต้องสร้าง tuple ใหม่ |
| `dict` | เก็บคู่ key-value | ใช้ key เช่น `d[key]` | ตรวจ key และโดยทั่วไปเร็ว | เพิ่ม ลบ หรือแก้คู่ข้อมูลได้ |
| `set` | สมาชิกไม่ซ้ำ ไม่มีลำดับตายตัว | ไม่มี index ต้องแจกแจงหรือค้นสมาชิก | ตรวจสมาชิกและโดยทั่วไปเร็ว | เพิ่มหรือลบสมาชิกได้ |

ตัวอย่างรูปแบบการสร้างและเพิ่มข้อมูลคือ

| ชนิด | การสร้าง | การเพิ่มข้อมูล |
| :-- | :-- | :-- |
| `list` | `x = [1, 2, 3]` | `x.append(4)` |
| `tuple` | `t = (1, 2, 3)` | สร้างใหม่ เช่น `t = t + (4,)` |
| `dict` | `d = {"k1": 1}` | `d["k2"] = 2` |
| `set` | `s = {1, 2, 3}` | `s.add(4)` |

ไม่มี collection ชนิดใดดีที่สุดในทุกสถานการณ์ การเลือกชนิดที่ตรงกับความสัมพันธ์
ของข้อมูลจะทำให้โปรแกรมอ่านง่าย และลดขั้นตอนการค้นหาหรือจัดการข้อมูล
