<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

![Basic String and List](/Z99-OTHERS/02-str-list/01-str-list.png)

# Contents

- [1. Basic String (สตริงเบื้องต้น)](#1-basic-string-สตริงเบื้องต้น)
    - [1.1. String Creation (การสร้างสตริง)](#11-string-creation-การสร้างสตริง)
    - [1.2. Escape and Unicode Characters](#12-escape-and-unicode-characters)
    - [1.3. String Indexing (การเข้าถึงตัวอักษร)](#13-string-indexing-การเข้าถึงตัวอักษร)
    - [1.4. String Slicing (การตัดสตริง)](#14-string-slicing-การตัดสตริง)
    - [1.5. String Concatenation and Repetition](#15-string-concatenation-and-repetition)
    - [1.6. String is Immutable](#16-string-is-immutable)
- [2. Basic List (ลิสต์เบื้องต้น)](#2-basic-list-ลิสต์เบื้องต้น)
    - [2.1. List Creation (การสร้างลิสต์)](#21-list-creation-การสร้างลิสต์)
    - [2.2. List Indexing (การเข้าถึงสมาชิก)](#22-list-indexing-การเข้าถึงสมาชิก)
    - [2.3. List Slicing (การตัดลิสต์)](#23-list-slicing-การตัดลิสต์)
    - [2.4. List Concatenation and Repetition](#24-list-concatenation-and-repetition)
    - [2.5. List is Mutable](#25-list-is-mutable)
- [3. String and List Methods (การดำเนินการ)](#3-string-and-list-methods-การดำเนินการ)
    - [3.1. Length with `len()`](#31-length-with-len)
    - [3.2. String Case with `.lower()` and `.upper()`](#32-string-case-with-lower-and-upper)
    - [3.3. Removing Characters with `.strip()`](#33-removing-characters-with-strip)
    - [3.4. Splitting a String with `.split()`](#34-splitting-a-string-with-split)
    - [3.5. Unpacking and Type Conversion](#35-unpacking-and-type-conversion)

---

## 1. Basic String (สตริงเบื้องต้น)

**String (สตริง)** คือข้อมูลประเภท `str` ที่ใช้เก็บข้อความ สตริงหนึ่งชุดประกอบ
ด้วยตัวอักษร เครื่องหมาย ตัวเลข หรือช่องว่างก็ได้ และ Python จะรักษาลำดับของ
ตัวอักษรเหล่านั้นไว้

## 1.1. String Creation (การสร้างสตริง)

สร้างสตริงได้โดยครอบข้อความด้วยเครื่องหมายคำพูดเดี่ยว (`'`) หรือคำพูดคู่ (`"`)
โดยเครื่องหมายเปิดและปิดต้องเป็นชนิดเดียวกัน สตริงที่ไม่มีตัวอักษรอยู่ภายใน
เรียกว่า **empty string**

```python
greeting = "Hello, World!"
food = 'Pizza'
empty_string = ""

print(greeting)
print(food)
print(empty_string)
```

ผลลัพธ์คือ

```
Hello, World!
Pizza

```

> [!WARNING]
>
> ถ้าลืมเครื่องหมายปิด หรือเปิดด้วย `"` แต่ปิดด้วย `'` โปรแกรมจะเกิด
> `SyntaxError` เพราะ Python หาจุดสิ้นสุดของสตริงไม่พบ

ข้อความหลายบรรทัดสร้างได้ด้วยเครื่องหมายคำพูดสามตัว ได้แก่ `'''` หรือ `"""`
การขึ้นบรรทัดใหม่ภายในเครื่องหมายจะเป็นส่วนหนึ่งของสตริงด้วย

```python
message = """Line one
Line two
Line three"""
print(message)
```

ผลลัพธ์คือ

```
Line one
Line two
Line three
```

## 1.2. Escape and Unicode Characters

**Escape character** คือชุดอักขระที่ขึ้นต้นด้วย backslash (`\`) เพื่อแทนตัวอักษร
ที่เขียนตรง ๆ ในสตริงได้ยาก ตัวที่ใช้บ่อยมีดังนี้

| Escape character | ความหมาย |
|---|---|
| `\"` | เครื่องหมายคำพูดคู่ |
| `\'` | เครื่องหมายคำพูดเดี่ยว |
| `\\` | backslash หนึ่งตัว |
| `\n` | ขึ้นบรรทัดใหม่ |
| `\t` | tab |

ถ้าเครื่องหมายคำพูดภายในไม่ตรงกับเครื่องหมายที่ใช้ครอบสตริง ก็เขียนได้โดย
ไม่ต้อง escape เช่น `'He said "Hello"'`

```python
print("She said, \"Hello!\"")
print("C:\\Users\\student")
print("Name\tScore")
print("Mali\t95")
```

ผลลัพธ์คือ

```
She said, "Hello!"
C:\Users\student
Name    Score
Mali    95
```

**Unicode** เป็นมาตรฐานสำหรับแทนตัวอักษรจากภาษาต่าง ๆ และสัญลักษณ์บน
คอมพิวเตอร์ ใน Python สามารถเขียนตัวอักษร Unicode ด้วยรูป `\uXXXX` โดย `XXXX`
เป็นรหัสเลขฐานสิบหกสี่หลัก

```python
print("\u0048\u0069")
print("\u0e44\u0e17\u0e22")
print("\u2660\u2663\u2665\u2666")
```

ผลลัพธ์คือ

```
Hi
ไทย
♠♣♥♦
```

## 1.3. String Indexing (การเข้าถึงตัวอักษร)

**Index** คือตัวเลขที่บอกตำแหน่งของตัวอักษรในสตริง โดย index จากด้านซ้ายเริ่มที่
`0` ส่วน index จากด้านขวาเริ่มที่ `-1`

ตัวอย่างสตริง `"PYTHON"` มีตำแหน่งดังนี้

| ตัวอักษร | `P` | `Y` | `T` | `H` | `O` | `N` |
|---|---:|---:|---:|---:|---:|---:|
| index บวก | 0 | 1 | 2 | 3 | 4 | 5 |
| index ลบ | -6 | -5 | -4 | -3 | -2 | -1 |

เข้าถึงตัวอักษรหนึ่งตัวด้วยวงเล็บสี่เหลี่ยม `string[index]`

```python
language = "PYTHON"
print(language[0])
print(language[3])
print(language[-1])
print(language[-4])
```

ผลลัพธ์คือ

```
P
H
N
T
```

> [!WARNING]
>
> ถ้าใช้ index ที่อยู่นอกสตริง เช่น `language[10]` จะเกิด
> `IndexError: string index out of range`

## 1.4. String Slicing (การตัดสตริง)

**String slicing** ใช้สร้างสตริงย่อย (substring) จากสตริงเดิม มีรูปแบบดังนี้

`string[start:stop:step]`

- `start` คือ index ของตัวอักษรแรกที่ต้องการ
- `stop` คือ index ถัดจากตัวอักษรสุดท้ายที่ต้องการ จึงไม่รวมตัวที่ `stop`
- `step` คือระยะที่เลื่อนไปในแต่ละครั้ง และมีค่าเริ่มต้นเป็น `1`

ถ้า `step` เป็นบวก การไม่ระบุ `start` หมายถึงเริ่มจากตัวแรก และการไม่ระบุ
`stop` หมายถึงไปจนจบสตริง

```python
text = "abcdefghij"
print(text[2:6])
print(text[:4])
print(text[7:])
print(text[1:9:2])
```

ผลลัพธ์คือ

```
cdef
abcd
hij
bdfh
```

ถ้า `step` เป็นลบ การตัดจะเคลื่อนจากขวาไปซ้าย การไม่ระบุ `start` และ `stop`
จึงใช้กลับลำดับสตริงได้

```python
text = "abcdefghij"
print(text[::-1])
print(text[8:2:-2])
```

ผลลัพธ์คือ

```
jihgfedcba
ige
```

> [!IMPORTANT]
>
> - `start` และ `stop` ที่เกินขอบเขตจะถูกปรับให้อยู่ในขอบเขตของสตริง
>   จึงไม่เกิด `IndexError` เช่น `text[-100:100]` ได้สตริงทั้งหมด
> - `step` ห้ามเป็น `0` มิฉะนั้นจะเกิด `ValueError`

## 1.5. String Concatenation and Repetition

**String concatenation** คือการเชื่อมสตริงด้วย `+` ส่วน `*` ใช้ทำซ้ำสตริงด้วย
จำนวนเต็ม

```python
first = "blue"
second = "berry"
word = first + second
line = "-" * 8
print(word)
print(line)
```

ผลลัพธ์คือ

```
blueberry
--------
```

> [!WARNING]
>
> ตัวดำเนินการต้องได้รับข้อมูลชนิดที่เหมาะสม เช่น `"123" + 456` และ
> `"Hello" * 2.5` เกิด `TypeError` ถ้าต้องการเชื่อมตัวเลข ให้แปลงด้วย `str()`
> ก่อน

## 1.6. String is Immutable

String เป็นข้อมูลแบบ **immutable** หมายถึงไม่สามารถแก้ตัวอักษรหรือ substring
ภายในสตริงเดิมโดยตรง คำสั่งอย่าง `text[0] = "h"` จึงเกิด `TypeError`

หากต้องการเปลี่ยนข้อความ ต้องสร้างสตริงใหม่จากส่วนที่ต้องการแล้วกำหนดกลับให้
ตัวแปร

```python
text = "Hello"
text = "h" + text[1:]
print(text)

sentence = "I like red apples."
sentence = sentence[:7] + "green" + sentence[10:]
print(sentence)
```

ผลลัพธ์คือ

```
hello
I like green apples.
```

---

## 2. Basic List (ลิสต์เบื้องต้น)

**List (ลิสต์)** คือข้อมูลที่เก็บค่าหลายค่าอย่างมีลำดับ สมาชิกแต่ละตัวอาจมี
ประเภทต่างกัน และ list สามารถแก้ไขสมาชิกหลังจากสร้างแล้วได้

## 2.1. List Creation (การสร้างลิสต์)

สร้าง list ด้วยวงเล็บสี่เหลี่ยม (`[]`) และใช้ comma (`,`) คั่นสมาชิก

```python
scores = [85, 90, 78]
fruits = ["apple", "banana", "cherry"]
mixed = [42, "hello", 3.14, True]
matrix = [[1, 2], [3, 4]]
empty_list = []

print(scores)
print(fruits)
print(mixed)
print(matrix)
print(empty_list)
```

ผลลัพธ์คือ

```
[85, 90, 78]
['apple', 'banana', 'cherry']
[42, 'hello', 3.14, True]
[[1, 2], [3, 4]]
[]
```

## 2.2. List Indexing (การเข้าถึงสมาชิก)

List ใช้ index แบบเดียวกับ string คือเริ่มจาก `0` ทางซ้าย และเริ่มจาก `-1`
ทางขวา แต่ค่าที่ได้จาก indexing คือสมาชิกหนึ่งตัว ซึ่งอาจเป็นข้อมูลชนิดใดก็ได้

```python
colors = ["red", "green", "blue", "yellow"]
print(colors[0])
print(colors[2])
print(colors[-1])
print(colors[-3])
```

ผลลัพธ์คือ

```
red
blue
yellow
green
```

> [!WARNING]
>
> การใช้ index ที่ไม่มีอยู่ใน list ทำให้เกิด `IndexError: list index out of range`

## 2.3. List Slicing (การตัดลิสต์)

**List slicing** ใช้สร้าง list ย่อย (sublist) ด้วยรูปแบบ
`list[start:stop:step]` กติกาของ `start`, `stop`, `step`, index ลบ และขอบเขต
เหมือน string slicing

```python
values = [4, 8, 15, 16, 23, 42]
print(values[1:4])
print(values[:3])
print(values[3:])
print(values[::2])
print(values[::-1])
```

ผลลัพธ์คือ

```
[8, 15, 16]
[4, 8, 15]
[16, 23, 42]
[4, 15, 23]
[42, 23, 16, 15, 8, 4]
```

ค่าที่ได้จาก slicing เป็น list ใหม่ แม้จะเลือกสมาชิกเพียงตัวเดียวก็ตาม เช่น
`values[1:2]` ได้ `[8]` แต่ `values[1]` ได้ `8`

## 2.4. List Concatenation and Repetition

List เชื่อมกันด้วย `+` และทำซ้ำด้วย `*` ได้เหมือน string โดยสมาชิกของ list
จะถูกนำมาต่อกันตามลำดับ

```python
left = [1, 2]
right = ["a", "b"]
combined = left + right
repeated = [0, 1] * 3
print(combined)
print(repeated)
```

ผลลัพธ์คือ

```
[1, 2, 'a', 'b']
[0, 1, 0, 1, 0, 1]
```

> [!WARNING]
>
> `+` ต้องเชื่อม list กับ list และ `*` ต้องใช้จำนวนเต็ม เช่น `[1, 2] + 3`
> และ `[1, 2] * 2.5` เกิด `TypeError`

## 2.5. List is Mutable

List เป็นข้อมูลแบบ **mutable** จึงเปลี่ยนสมาชิกด้วย index ได้โดยตรง

```python
numbers = [12, 24, 36, 48]
numbers[0] = 99
numbers[-1] = 77
print(numbers)
```

ผลลัพธ์คือ

```
[99, 24, 36, 77]
```

การกำหนดค่าด้วย slice ใช้แทนสมาชิกหลายตัวได้ ด้านขวาต้องเป็น iterable เช่น
list และถ้าไม่ระบุ `step` จำนวนสมาชิกใหม่ไม่จำเป็นต้องเท่ากับจำนวนที่ถูกแทน

```python
numbers = [10, 20, 30, 40, 50]
numbers[1:4] = [7, 8]
print(numbers)

numbers[2:2] = [90, 100]
print(numbers)
```

ผลลัพธ์คือ

```
[10, 7, 8, 50]
[10, 7, 90, 100, 8, 50]
```

`numbers[2] = [90, 100]` มีความหมายต่างกัน เพราะเป็นการวาง list ทั้งชุดไว้
เป็นสมาชิกเพียงตัวเดียว

ถ้าระบุ `step` ที่ไม่ใช่ `1` จำนวนค่าใหม่ต้องเท่ากับจำนวนตำแหน่งที่เลือก

```python
numbers = [10, 20, 30, 40, 50, 60]
numbers[::2] = [1, 3, 5]
print(numbers)
```

ผลลัพธ์คือ

```
[1, 20, 3, 40, 5, 60]
```

> [!WARNING]
>
> - การกำหนดค่าด้วย index ที่ไม่มีอยู่จะเกิด `IndexError`
> - การเขียน `numbers[1:3] = 0` เกิด `TypeError` เพราะค่าด้านขวาไม่ใช่
>   iterable
> - Extended slice เช่น `numbers[::2]` ที่ได้รับจำนวนค่าไม่เท่ากับจำนวน
>   ตำแหน่ง จะเกิด `ValueError`

---

## 3. String and List Methods (การดำเนินการ)

Function และ method ในส่วนนี้ใช้ตรวจสอบหรือสร้างข้อมูลจาก string และ list
โดยไม่ต้องแก้ข้อมูลเดิมโดยตรง

## 3.1. Length with `len()`

Function `len()` คืนจำนวนตัวอักษรใน string หรือจำนวนสมาชิกใน list ช่องว่างและ
เครื่องหมายต่าง ๆ ใน string นับเป็นตัวอักษรด้วย

```python
greeting = "Hello, World!"
numbers = [1, 2, 3, 4, 5]
print(len(greeting))
print(len(numbers))
```

ผลลัพธ์คือ

```
13
5
```

## 3.2. String Case with `.lower()` and `.upper()`

Method `.lower()` สร้าง string ที่ตัวอักษรเปลี่ยนเป็นตัวพิมพ์เล็ก ส่วน
`.upper()` สร้าง string ที่ตัวอักษรเปลี่ยนเป็นตัวพิมพ์ใหญ่ ทั้งสอง method
ไม่แก้ string เดิม

```python
text = "PyThOn 3"
print(text.lower())
print(text.upper())
print(text)
```

ผลลัพธ์คือ

```
python 3
PYTHON 3
PyThOn 3
```

หากต้องการเก็บผลลัพธ์ไว้ในตัวแปรเดิม ต้องกำหนดค่ากลับ เช่น
`text = text.lower()`

## 3.3. Removing Characters with `.strip()`

Method `.strip()` สร้าง string ใหม่โดยนำตัวอักษรที่กำหนดออกจากทั้งสองปลาย
ส่วน `.lstrip()` ทำเฉพาะด้านซ้าย และ `.rstrip()` ทำเฉพาะด้านขวา

ถ้าไม่ส่ง argument ทั้งสาม method จะนำ whitespace ที่ปลายออก เช่น space,
tab และ newline

```python
text = "  Hello, World!  "
print(f'"{text.strip()}"')
print(f'"{text.lstrip()}"')
print(f'"{text.rstrip()}"')
```

ผลลัพธ์คือ

```
"Hello, World!"
"Hello, World!  "
"  Hello, World!"
```

ถ้าส่ง string เข้าไป ตัวอักษรทุกตัวใน argument จะถูกมองเป็น **ชุดตัวอักษร**
ที่นำออกซ้ำ ๆ จากปลาย ไม่ได้มองเป็นคำหรือ prefix/suffix และไม่ได้นำ whitespace
ออกเองหากไม่ได้ระบุ

```python
text = "#-#Hello#--"
print(text.strip("#-"))
print(text.lstrip("-#"))
print(text.rstrip("##--"))
```

ผลลัพธ์คือ

```
Hello
Hello#--
#-#Hello
```

ลำดับและการเขียนตัวอักษรซ้ำใน argument ไม่มีผล เพราะ method ตรวจเพียงว่า
ตัวอักษรที่ปลายอยู่ในชุดนั้นหรือไม่ และ method เหล่านี้ไม่แก้ค่าของ string เดิม

## 3.4. Splitting a String with `.split()`

Method `.split()` แบ่ง string แล้วคืนผลเป็น list ของ string ถ้าไม่ระบุ separator
จะแบ่งที่ whitespace ที่ต่อเนื่องกัน และไม่นำสมาชิกว่างที่หัวหรือท้ายมาใส่ในผล

```python
text = "  red   green\tblue  "
print(text.split())
print(repr(text))
```

ผลลัพธ์คือ

```
['red', 'green', 'blue']
'  red   green\tblue  '
```

เมื่อระบุ separator, `.split(separator)` จะหา separator ทั้งชุดอย่างตรงตัว
ถ้า separator อยู่ติดกัน ผลลัพธ์จะมี empty string คั่น และถ้าไม่พบ separator
จะได้ list ที่มี string เดิมเพียงสมาชิกเดียว

```python
text = "red::green::::blue"
print(text.split("::"))
print(text.split(":::"))
print(text.split("|||"))
```

ผลลัพธ์คือ

```
['red', 'green', '', 'blue']
['red::green', ':blue']
['red::green::::blue']
```

> [!IMPORTANT]
>
> `.split()` ไม่แก้ string เดิม หากเขียน `text = text.split()` ตัวแปร `text`
> จะถูกกำหนดใหม่ให้เก็บ list ที่ method คืนมา

## 3.5. Unpacking and Type Conversion

ผลจาก `.split()` สามารถ **unpack** หรือกระจายไปยังตัวแปรหลายตัวได้ โดยจำนวน
สมาชิกต้องเท่ากับจำนวนตัวแปร

```python
text = "north south east"
first, second, third = text.split()
print(first)
print(second)
print(third)
```

ผลลัพธ์คือ

```
north
south
east
```

ข้อมูลทุกตัวที่ได้จาก `.split()` เป็น `str` หากต้องการตัวเลข ให้แปลงสมาชิก
แต่ละตัวด้วย `int()` หรือ `float()` ก่อน unpack

```python
text = "10 20 30"
a, b, c = [int(item) for item in text.split()]
x, y, z = [float(item) for item in text.split()]
print(a, b, c)
print(x, y, z)
```

ผลลัพธ์คือ

```
10 20 30
10.0 20.0 30.0
```

> [!WARNING]
>
> - ถ้าจำนวนสมาชิกไม่เท่ากับจำนวนตัวแปร จะเกิด `ValueError` ระหว่าง unpack
> - ถ้าข้อความมีรูปแบบที่แปลงไม่ได้ เช่น `int("A")` จะเกิด `ValueError`
