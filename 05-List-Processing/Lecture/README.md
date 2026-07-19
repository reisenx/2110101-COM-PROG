<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

![05-list.png](/Z99-OTHERS/05-list/01-list.png)

# List Processing (การประมวลผลลิสต์)

# Contents

- [1. List Basics](#1-list-basics)
    - [1.1. Creating Lists](#11-creating-lists)
    - [1.2. Basic List Operations](#12-basic-list-operations)
    - [1.3. List Methods and Membership](#13-list-methods-and-membership)
- [2. Building and Traversing Lists](#2-building-and-traversing-lists)
    - [2.1. Reading Data into a List](#21-reading-data-into-a-list)
    - [2.2. Appending Data](#22-appending-data)
    - [2.3. Traversing Values and Indices](#23-traversing-values-and-indices)
    - [2.4. Updating List Elements](#24-updating-list-elements)
- [3. Processing Adjacent Elements](#3-processing-adjacent-elements)
    - [3.1. Adjacent-Pair Loop Patterns](#31-adjacent-pair-loop-patterns)
    - [3.2. Checking an Entire List](#32-checking-an-entire-list)
- [4. Searching Lists](#4-searching-lists)
    - [4.1. Searching a Simple List](#41-searching-a-simple-list)
    - [4.2. Searching Parallel Lists](#42-searching-parallel-lists)
    - [4.3. Searching Nested Lists](#43-searching-nested-lists)
- [5. Sorting Lists](#5-sorting-lists)
    - [5.1. Basic Sorting](#51-basic-sorting)
    - [5.2. Sorting Nested Lists](#52-sorting-nested-lists)
    - [5.3. Sorting by Another Property](#53-sorting-by-another-property)
- [6. Converting between Lists and Strings](#6-converting-between-lists-and-strings)
    - [6.1. Splitting a String](#61-splitting-a-string)
    - [6.2. Joining Strings](#62-joining-strings)
- [7. Modifying Lists Safely](#7-modifying-lists-safely)
    - [7.1. Why Modification during Iteration Is Dangerous](#71-why-modification-during-iteration-is-dangerous)
    - [7.2. Building a New List](#72-building-a-new-list)
    - [7.3. Controlled Modification with `while`](#73-controlled-modification-with-while)

---

## 1. List Basics

**List (ลิสต์)** คือรายการของข้อมูลที่เรียงตามลำดับ สมาชิกแต่ละตัวมีตำแหน่ง
หรือ **index** กำกับ และสามารถแก้ไข เพิ่ม หรือลบสมาชิกได้

ลิสต์จึงเหมาะกับข้อมูลหลายค่าที่ต้องนำมาประมวลผลในรูปแบบเดียวกัน เช่น
คะแนนของนิสิต อุณหภูมิรายวัน หรือชื่อเดือน

### 1.1. Creating Lists

สร้างลิสต์ด้วยวงเล็บเหลี่ยม `[]` และใช้เครื่องหมาย `,` คั่นสมาชิก

```python
empty = []
primes = [2, 3, 5, 7, 11]
days = ["SU", "MO", "TU", "WE", "TH", "FR", "SA"]
mixed = [1, "apple", 3.14, True]
```

ลิสต์หนึ่งสามารถมีลิสต์อื่นเป็นสมาชิกได้ เรียกว่า **nested list
(ลิสต์ซ้อนลิสต์)**

```python
records = [["Mali", 82], ["Niran", 75], ["Ploy", 91]]
print(records[1])
print(records[1][0])
```

ผลลัพธ์คือ

```
['Niran', 75]
Niran
```

`records[1]` คือลิสต์ `['Niran', 75]` และ `records[1][0]` คือสมาชิกตำแหน่ง
`0` ของลิสต์ย่อยนั้น

### 1.2. Basic List Operations

การดำเนินการพื้นฐานกับลิสต์มีดังนี้

| Operation | รูปแบบ | ความหมาย |
| --- | --- | --- |
| Length | `len(x)` | จำนวนสมาชิกใน `x` |
| Concatenation | `x + y` | สร้างลิสต์ใหม่โดยนำ `y` มาต่อท้าย `x` |
| Repetition | `x * n` | สร้างลิสต์ใหม่โดยทำสมาชิกใน `x` ซ้ำ `n` รอบ |
| Indexing | `x[k]` | อ่านสมาชิกที่ index `k` |
| Slicing | `x[start:stop:step]` | สร้างลิสต์จากช่วงที่กำหนด |

```python
numbers = [10, 20, 30, 40, 50]

print(len(numbers))
print([1] + [2, 3])
print([0, 0] * 3)
print(numbers[2], numbers[-1])
print(numbers[1:4])
print(numbers[::2])
```

ผลลัพธ์คือ

```
5
[1, 2, 3]
[0, 0, 0, 0, 0, 0]
30 50
[20, 30, 40]
[10, 30, 50]
```

index เริ่มนับจาก `0` ทางซ้าย และ index ติดลบเริ่มนับจาก `-1` ทางขวา
ส่วน slicing จะเลือกตั้งแต่ `start` แต่ไม่รวม `stop`

> [!WARNING]
>
> การอ่าน index ที่ไม่มีอยู่ เช่น `[10, 20][2]` จะเกิด `IndexError` แต่ slicing
> ที่เลยขอบเขตจะหยุดที่ขอบลิสต์โดยไม่เกิดข้อผิดพลาด

### 1.3. List Methods and Membership

**List methods** เป็นคำสั่งที่เรียกผ่านลิสต์ และส่วนใหญ่แก้ไขลิสต์เดิมโดยตรง

| Method | การทำงาน |
| --- | --- |
| `x.append(e)` | เพิ่ม `e` ต่อท้าย `x` |
| `x.insert(i, e)` | แทรก `e` ก่อนตำแหน่ง `i` |
| `x.remove(e)` | ลบสมาชิกตัวแรกที่มีค่าเท่ากับ `e` |
| `x.pop(i)` | ลบและคืนค่าสมาชิกตำแหน่ง `i` |
| `x.pop()` | ลบและคืนค่าสมาชิกตัวสุดท้าย |
| `x.index(e)` | คืน index แรกที่พบ `e` |
| `x.sort()` | เรียงสมาชิกในลิสต์เดิม |

```python
data = []
for i in range(5):
    data.append(10 * i)

data.remove(20)
data.insert(2, 99)
data.insert(-1, 7)
first_removed = data.pop(1)
second_removed = data.pop(-3)
position = data.index(99)
data.sort()

print(data)
print(first_removed, second_removed, position)
print(40 in data)
```

ผลลัพธ์คือ

```
[0, 7, 40, 99]
10 30 1
True
```

ตัวดำเนินการ `in` ตรวจว่ามีค่าอยู่ในลิสต์หรือไม่ และคืนค่าเป็น `bool`
จึงควรใช้ตรวจสอบก่อนเรียก `index()` หรือ `remove()` เมื่อยังไม่แน่ใจว่าพบข้อมูล

```python
colors = ["red", "green", "blue"]
target = "yellow"

if target in colors:
    print(colors.index(target))
else:
    print("Not found")
```

ผลลัพธ์คือ

```
Not found
```

> [!WARNING]
>
> - `x.index(e)` และ `x.remove(e)` จะเกิด `ValueError` ถ้าไม่มี `e` ใน `x`
> - `x.pop(i)` จะเกิด `IndexError` ถ้า `i` อยู่นอกขอบเขต และ `x.pop()`
>   จะเกิดข้อผิดพลาดเมื่อลิสต์ว่าง

---

## 2. Building and Traversing Lists

การประมวลผลข้อมูลด้วยลิสต์มักมีสามช่วง คือ รับข้อมูลมาเก็บในลิสต์
วนอ่านสมาชิก และนำสมาชิกไปคำนวณหรือแก้ไข

### 2.1. Reading Data into a List

รูปแบบการรับข้อมูลมาเก็บในลิสต์ที่พบบ่อยมีสามแบบ

**แบบที่ 1: ระบุจำนวนข้อมูลก่อน แล้วรับข้อมูลบรรทัดละตัว**

```python
n = int(input())
data = []
for _ in range(n):
    data.append(float(input()))
```

ตัวแปร `n` กำหนดชัดเจนว่าวงวนต้องรับข้อมูลกี่รอบ

**แบบที่ 2: รับข้อมูลบรรทัดละตัวจนพบค่าที่ใช้ระบุว่าหมด**

```python
data = []
value = float(input())
while value != -1:
    data.append(value)
    value = float(input())
```

ตัวอย่างนี้ใช้ `-1` เป็น **sentinel value** ซึ่งมีหน้าที่บอกจุดสิ้นสุดและไม่ถูกเก็บ
ใน `data` รูปแบบนี้ใช้ได้เมื่อค่าที่เลือกเป็น sentinel ไม่ใช่ข้อมูลปกติ

**แบบที่ 3: รับข้อมูลหลายตัวในบรรทัดเดียว**

```python
parts = input().split()
data = []
for part in parts:
    data.append(float(part))
```

`input().split()` ให้ลิสต์ของ `str` จึงต้องแปลงสมาชิกทีละตัวหากต้องการตัวเลข

### 2.2. Appending Data

เมื่อต้องเพิ่มสมาชิกทีละตัว ควรใช้ `append()`

```python
squares = []
for number in range(1, 6):
    squares.append(number ** 2)

print(squares)
```

ผลลัพธ์คือ

```
[1, 4, 9, 16, 25]
```

รูปแบบ `data = data + [value]` สร้างลิสต์ใหม่และคัดลอกสมาชิกเดิมทุกครั้ง
จึงช้าลงมากเมื่อทำซ้ำในวงวน ส่วน `data.append(value)` เพิ่มสมาชิกท้ายลิสต์เดิม
โดยตรงและสื่อความหมายชัดเจนกว่า

`data += [value]` ก็แก้ไขลิสต์เดิมได้ แต่ `append()` เหมาะที่สุดเมื่อเพิ่มเพียง
หนึ่งค่า

### 2.3. Traversing Values and Indices

ถ้าต้องการเพียงค่าของสมาชิก ให้วนผ่านลิสต์โดยตรง

```python
prices = [12.5, 8.0, 19.5]
total = 0

for price in prices:
    total += price

print(total)
```

ผลลัพธ์คือ

```
40.0
```

ถ้าต้องการทั้งตำแหน่งและค่า ให้ใช้ index จาก `range(len(x))`

```python
names = ["Ann", "Ben", "Chet"]

for i in range(len(names)):
    print(i, names[i])
```

ผลลัพธ์คือ

```
0 Ann
1 Ben
2 Chet
```

> [!IMPORTANT]
>
> ไม่ควรหา index ด้วย `x.index(e)` ทุกครั้งใน `for e in x` เพราะต้องค้นลิสต์
> ซ้ำโดยไม่จำเป็น และหากค่าซ้ำกัน `index()` จะคืนเฉพาะตำแหน่งแรกเสมอ

### 2.4. Updating List Elements

ตัวแปรที่รับค่าจาก `for e in x` ไม่ใช่ตำแหน่งในลิสต์ การกำหนดค่าใหม่ให้ `e`
จึงไม่เปลี่ยนสมาชิกใน `x`

```python
numbers = [-4, 3, -2, 7]

for number in numbers:
    if number < 0:
        number *= -1

print(numbers)
```

ผลลัพธ์ยังคงเป็น

```
[-4, 3, -2, 7]
```

ถ้าต้องการแก้สมาชิก ให้เข้าถึงสมาชิกผ่าน index

```python
numbers = [-4, 3, -2, 7]

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] *= -1

print(numbers)
```

ผลลัพธ์คือ

```
[4, 3, 2, 7]
```

การเปลี่ยน **ค่า** ของสมาชิกผ่าน index ทำได้ระหว่างวงวนเมื่อจำนวนสมาชิกและตำแหน่ง
ต่าง ๆ ไม่เปลี่ยน แต่การเพิ่มหรือลบสมาชิกมีข้อควรระวังซึ่งจะกล่าวใน Section 7

---

## 3. Processing Adjacent Elements

งานบางประเภทต้องเปรียบเทียบสมาชิกที่อยู่ติดกัน เช่น ตรวจว่าข้อมูลเรียงเพิ่มขึ้น
หรือหาความต่างระหว่างค่าที่วัดติดต่อกัน

### 3.1. Adjacent-Pair Loop Patterns

ลิสต์ยาว `n` มีคู่ที่ติดกันทั้งหมด `n - 1` คู่ จึงเขียนวงวนได้สองรูปแบบ

```python
data = [4, 7, 9, 15]

for i in range(len(data) - 1):
    left = data[i]
    right = data[i + 1]
    print(left, right)
```

หรือเริ่ม `i` ที่สมาชิกทางขวา

```python
data = [4, 7, 9, 15]

for i in range(1, len(data)):
    left = data[i - 1]
    right = data[i]
    print(left, right)
```

ทั้งสองรูปแบบให้ผลลัพธ์เดียวกัน

```
4 7
7 9
9 15
```

ถ้าลิสต์ว่างหรือมีสมาชิกเพียงตัวเดียว `range(len(data) - 1)` และ
`range(1, len(data))` จะไม่มีรอบให้ทำงาน จึงไม่อ่าน index ที่ไม่มีอยู่

### 3.2. Checking an Entire List

ตัวอย่างต่อไปตรวจว่าตัวเลขเรียงเพิ่มขึ้นอย่างเคร่งครัดหรือไม่ นั่นคือสมาชิกทางขวา
ต้องมากกว่าสมาชิกทางซ้ายทุกคู่

```python
data = [3, 8, 12, 20]
is_increasing = True

for i in range(len(data) - 1):
    if data[i] >= data[i + 1]:
        is_increasing = False
        break

print(is_increasing)
```

ผลลัพธ์คือ

```
True
```

กำหนด `is_increasing = True` ก่อนเริ่ม แล้วเปลี่ยนเป็น `False` เมื่อพบคู่ที่ผิด
เงื่อนไข คำสั่ง `break` หยุดค้นได้ทันที เพราะพบเพียงคู่เดียวก็สรุปได้แล้ว

สำหรับลิสต์ว่างหรือลิสต์ที่มีสมาชิกตัวเดียว วงวนไม่มีรอบและผลยังเป็น `True`
เนื่องจากไม่มีคู่ใดที่ขัดเงื่อนไข

---

## 4. Searching Lists

รูปแบบการค้นขึ้นอยู่กับโครงสร้างข้อมูล ลิสต์อย่างง่ายใช้ `in` และ `index()` ได้
โดยตรง ส่วนข้อมูลที่สัมพันธ์กันหลายช่องต้องรักษาความสัมพันธ์ของตำแหน่งให้ถูกต้อง

### 4.1. Searching a Simple List

ถ้าต้องการเพียงตรวจว่ามีข้อมูลหรือไม่ ให้ใช้ `in`

```python
scores = [18, 25, 31, 25]
target = 25
print(target in scores)
```

ผลลัพธ์คือ

```
True
```

ถ้าต้องการตำแหน่งแรกที่พบ ให้ตรวจด้วย `in` ก่อนแล้วจึงใช้ `index()`

```python
scores = [18, 25, 31, 25]
target = 25

if target in scores:
    position = scores.index(target)
    print(position)
else:
    print("Not found")
```

ผลลัพธ์คือ

```
1
```

### 4.2. Searching Parallel Lists

**Parallel lists** คือลิสต์หลายลิสต์ที่ข้อมูล index เดียวกันมีความสัมพันธ์กัน
ตัวอย่างเช่น `product_codes[k]` และ `prices[k]` เป็นรหัสและราคาของสินค้าชิ้นเดียวกัน

```python
product_codes = [101, 205, 310]
prices = [12.5, 8.0, 24.0]
target = 205

if target in product_codes:
    i = product_codes.index(target)
    print(target, prices[i])
else:
    print("Not found")
```

ผลลัพธ์คือ

```
205 8.0
```

ลิสต์คู่ขนานต้องมีความยาวเท่ากันและเรียงข้อมูลให้ตรงตำแหน่งกันเสมอ
ถ้าเพิ่ม ลบ หรือเรียงเพียงลิสต์เดียว ความสัมพันธ์ของข้อมูลจะเสียไป

### 4.3. Searching Nested Lists

อีกวิธีหนึ่งคือเก็บข้อมูลที่สัมพันธ์กันไว้ในลิสต์ย่อยเดียวกัน

```python
products = [[101, 12.5], [205, 8.0], [310, 24.0]]
target = 205
found_price = None

for item in products:
    if item[0] == target:
        found_price = item[1]
        break

if found_price is None:
    print("Not found")
else:
    print(target, found_price)
```

ผลลัพธ์คือ

```
205 8.0
```

เมื่อลิสต์ย่อยทุกตัวมีจำนวนช่องแน่นอน สามารถ **unpack** สมาชิกเป็นตัวแปรได้
ทำให้ชื่อของแต่ละช่องชัดเจนขึ้น

```python
products = [[101, 12.5], [205, 8.0], [310, 24.0]]
target = 310
found_price = None

for [code, price] in products:
    if code == target:
        found_price = price
        break

print(found_price)
```

ผลลัพธ์คือ

```
24.0
```

> [!WARNING]
>
> การเขียน `for [code, price] in products` ต้องให้ลิสต์ย่อยทุกตัวมีสมาชิกสองตัว
> พอดี มิฉะนั้นจะเกิด `ValueError` ขณะ unpack

---

## 5. Sorting Lists

การเรียงข้อมูลช่วยให้ดูตามลำดับ เปรียบเทียบสมาชิกที่อยู่ติดกัน หรือเตรียมข้อมูล
สำหรับการประมวลผลขั้นต่อไป

### 5.1. Basic Sorting

เมธอด `sort()` เรียงสมาชิกจากน้อยไปมากและแก้ไขลิสต์เดิม

```python
numbers = [90, 22, 44, 20, 51, 12]
numbers.sort()
print(numbers)

names = ["Tom", "Ann", "Don"]
names.sort()
print(names)
```

ผลลัพธ์คือ

```
[12, 20, 22, 44, 51, 90]
['Ann', 'Don', 'Tom']
```

`sort()` คืนค่า `None` จึงไม่ควรเขียน `numbers = numbers.sort()` เพราะจะทำให้
`numbers` กลายเป็น `None`

> [!WARNING]
>
> สมาชิกต้องเปรียบเทียบกันได้ ใน Python 3.11 ลิสต์อย่าง `[1, "2"]`
> เรียงด้วย `sort()` ไม่ได้และเกิด `TypeError`

### 5.2. Sorting Nested Lists

เมื่อลิสต์มีลิสต์ย่อย `sort()` จะเปรียบเทียบสมาชิกช่องแรกก่อน
ถ้าช่องแรกเท่ากันจึงเปรียบเทียบช่องถัดไป

```python
data = [["A", 9], ["C", 1], ["A", 1]]
data.sort()
print(data)
```

ผลลัพธ์คือ

```
[['A', 1], ['A', 9], ['C', 1]]
```

หลักนี้เรียกว่า **lexicographic order** คล้ายการเรียงคำในพจนานุกรม

### 5.3. Sorting by Another Property

ถ้าต้องการเรียงตามช่องอื่น ให้สร้างลิสต์ชั่วคราวที่นำค่าซึ่งต้องการใช้เรียง
มาไว้ช่องแรก จากนั้นเรียงแล้วดึงข้อมูลเดิมกลับมา วิธีนี้แบ่งเป็นสามขั้นตอน

1. สร้างข้อมูลคู่ `[sort_value, original_value]`
2. เรียงลิสต์ชั่วคราว
3. นำ `original_value` ที่เรียงแล้วกลับไปใช้

ตัวอย่างต่อไปเรียงข้อความตามความยาว และใช้ตัวข้อความตัดสินเมื่อความยาวเท่ากัน

```python
words = ["pear", "fig", "banana", "kiwi", "plum"]
decorated = []

for word in words:
    decorated.append([len(word), word])

decorated.sort()

for i in range(len(decorated)):
    words[i] = decorated[i][1]

print(words)
```

ผลลัพธ์คือ

```
['fig', 'kiwi', 'pear', 'plum', 'banana']
```

เนื่องจาก `kiwi`, `pear` และ `plum` ยาวเท่ากัน จึงเรียงสามคำนี้ตามข้อความ
ซึ่งเป็นช่องที่สอง

---

## 6. Converting between Lists and Strings

เมธอด `split()` แยกสตริงให้เป็นลิสต์ ส่วน `join()` นำสตริงหลายตัวในลิสต์
มาต่อเป็นสตริงเดียว

### 6.1. Splitting a String

`s.split()` ที่ไม่ระบุตัวคั่นจะแยกด้วย whitespace และรวม whitespace
ที่อยู่ติดกันเป็นจุดแบ่งเดียว

```python
text = "11   2\t33"
print(text.split())
```

ผลลัพธ์คือ

```
['11', '2', '33']
```

ถ้าระบุ `separator` ใน `s.split(separator)` Python จะแยกด้วยข้อความนั้นตรง ๆ
ช่องว่างหรือส่วนว่างที่เหลืออยู่จะถูกเก็บไว้

```python
print("11:2: 33".split(":"))
print("a,,,b".split(","))
print("a   b".split(" "))
print("a   b".split())
print("a,,,b".split(",,"))
```

ผลลัพธ์คือ

```
['11', '2', ' 33']
['a', '', '', 'b']
['a', '', '', 'b']
['a', 'b']
['a', ',b']
```

ดังนั้น `split()` และ `split(" ")` ไม่เหมือนกัน เมื่อข้อมูลอาจมีช่องว่างหลายตัว
มักใช้ `split()` เพื่อรับคำหรือค่าหลายค่าจากหนึ่งบรรทัด

### 6.2. Joining Strings

เขียน `separator.join(items)` เพื่อนำสตริงใน `items` มาต่อกัน โดยแทรก
`separator` ระหว่างสมาชิก

```python
items = ["A", "BC", "DEF", "GH"]

print(" ".join(items))
print(",".join(items))
print("><".join(items))
```

ผลลัพธ์คือ

```
A BC DEF GH
A,BC,DEF,GH
A><BC><DEF><GH
```

`join()` ต้องการสมาชิกที่เป็น `str` ทั้งหมด ถ้ามีตัวเลข ให้แปลงเป็นข้อความ
ก่อนนำไปต่อ

```python
values = [-3, 0, 12, 7, -1]
nonnegative_text = []

for value in values:
    if value >= 0:
        nonnegative_text.append(str(value))

print(" -> ".join(nonnegative_text))
```

ผลลัพธ์คือ

```
0 -> 12 -> 7
```

สำหรับลิสต์ว่าง `separator.join([])` จะได้สตริงว่าง `""`

---

## 7. Modifying Lists Safely

การเพิ่มหรือลบสมาชิกทำให้ความยาวและตำแหน่งของสมาชิกเปลี่ยน การแก้โครงสร้างลิสต์
เดียวกับที่วงวนกำลังอ่านจึงอาจข้ามข้อมูล เกิด `IndexError` หรือไม่สิ้นสุด

### 7.1. Why Modification during Iteration Is Dangerous

ตัวอย่างนี้ดูเหมือนต้องการลบเลข `1` ทุกตัว แต่ให้ผลไม่ถูกต้อง

```python
numbers = [1, 1, 2, 3, 1]

for number in numbers:
    if number == 1:
        numbers.remove(number)

print(numbers)
```

ผลลัพธ์คือ

```
[2, 3, 1]
```

หลังลบสมาชิกตัวแรก สมาชิกที่เหลือเลื่อนมาทางซ้าย แต่วงวนเลื่อนไปตำแหน่งถัดไป
จึงข้ามเลข `1` อีกตัว และการลบครั้งต่อมายังลบเลข `1` ตัวแรกที่เหลืออยู่ ไม่ใช่
ตำแหน่งที่วงวนกำลังอ่าน

การใช้ `for i in range(len(numbers))` แล้ว `pop(i)` ก็ไม่ปลอดภัย เพราะ
`range()` กำหนด index จากความยาวเดิมไว้แล้ว แต่ลิสต์สั้นลงระหว่างทำงาน

การแทรกสมาชิกหน้าตำแหน่งที่กำลังอ่านอาจทำให้สมาชิกเดิมถูกพบซ้ำไปเรื่อย ๆ
และวงวนไม่สิ้นสุด

> [!WARNING]
>
> หลีกเลี่ยงการเพิ่มหรือลบสมาชิกจากลิสต์เดียวกับที่ `for` กำลังวนอ่าน

### 7.2. Building a New List

วิธีที่ชัดเจนคือสร้างลิสต์ใหม่ แล้วเก็บเฉพาะสมาชิกที่ต้องการ

```python
numbers = [1, 1, 2, 3, 1]
kept = []

for number in numbers:
    if number != 1:
        kept.append(number)

numbers[:] = kept
print(numbers)
```

ผลลัพธ์คือ

```
[2, 3]
```

`numbers[:] = kept` คัดลอกสมาชิกใน `kept` ไปใส่ลิสต์เดิม ส่วน
`numbers = kept` ทำให้ตัวแปร `numbers` อ้างถึงลิสต์เดียวกับ `kept`

ความแตกต่างนี้เห็นได้เมื่อมีตัวแปรอื่นอ้างถึงลิสต์เดิม

```python
numbers = [1, 2, 3]
same_list = numbers
replacement = [8, 9]

numbers[:] = replacement
print(numbers)
print(same_list)
```

ผลลัพธ์คือ

```
[8, 9]
[8, 9]
```

ตัวแปร `same_list` จึงเห็นสมาชิกใหม่ด้วย เพราะยังอ้างถึงลิสต์เดิมที่ถูกแก้ไข

### 7.3. Controlled Modification with `while`

หากจำเป็นต้องลบจากลิสต์เดิมระหว่างตรวจ สามารถควบคุม index ด้วย `while`
เมื่อลบสมาชิกแล้วไม่เพิ่ม index เพราะสมาชิกถัดไปเพิ่งเลื่อนเข้ามาที่ตำแหน่งเดิม

```python
numbers = [1, 1, 2, 3, 1]
i = 0

while i < len(numbers):
    if numbers[i] == 1:
        numbers.pop(i)
    else:
        i += 1

print(numbers)
```

ผลลัพธ์คือ

```
[2, 3]
```

อย่างไรก็ตาม การสร้างลิสต์ใหม่มักอ่านง่ายและลดความผิดพลาดได้มากกว่า
