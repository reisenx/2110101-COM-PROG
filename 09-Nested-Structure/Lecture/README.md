<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

![09-nested.png](/Z99-OTHERS/09-nested/01-nested.png)

# Nested Structures (โครงสร้างซ้อน)

# Contents

- [Section 1: Nested Loops (วงวนซ้อน)](#1-nested-loops-วงวนซ้อน)
    - [1.1. Nested `while` Loops](#11-nested-while-loops)
    - [1.2. Nested `for` Loops](#12-nested-for-loops)
    - [1.3. Iterating over Pairs](#13-iterating-over-pairs)
    - [1.4. Moving an Inner Loop into a Function](#14-moving-an-inner-loop-into-a-function)
    - [1.5. Leaving Nested Loops](#15-leaving-nested-loops)
- [Section 2: Nested Lists (ลิสต์ซ้อน)](#2-nested-lists-ลิสต์ซ้อน)
    - [2.1. Creating and Accessing Nested Lists](#21-creating-and-accessing-nested-lists)
    - [2.2. Building a Nested List Incrementally](#22-building-a-nested-list-incrementally)
    - [2.3. Sorting with Temporary Records](#23-sorting-with-temporary-records)
    - [2.4. Shared Inner Lists](#24-shared-inner-lists)
    - [2.5. Nested Lists as Matrices](#25-nested-lists-as-matrices)
    - [2.6. Reading and Printing a Matrix](#26-reading-and-printing-a-matrix)
    - [2.7. Adding Matrices](#27-adding-matrices)
- [Section 3: List Comprehensions (การสร้างลิสต์แบบย่อ)](#3-list-comprehensions-การสร้างลิสต์แบบย่อ)
    - [3.1. Transforming Values](#31-transforming-values)
    - [3.2. Filtering Values](#32-filtering-values)
    - [3.3. Filtering and Transforming](#33-filtering-and-transforming)
    - [3.4. Reading Values with a Comprehension](#34-reading-values-with-a-comprehension)
    - [3.5. Comprehensions with Nested Lists](#35-comprehensions-with-nested-lists)
    - [3.6. Readability and Performance](#36-readability-and-performance)

---

## 1. Nested Loops (วงวนซ้อน)

**Nested loop (วงวนซ้อน)** คือวงวนที่อยู่ภายในวงวนอีกชั้นหนึ่ง ในแต่ละรอบของ
วงวนนอก โปรแกรมจะทำวงวนชั้นในตั้งแต่ต้นจนจบ แล้วจึงกลับไปเริ่มรอบถัดไปของ
วงวนนอก

โครงสร้างนี้เหมาะกับงานที่มีการทำซ้ำมากกว่าหนึ่งระดับ เช่น ประมวลผลข้อมูลหลาย
กลุ่ม แจกแจงคู่ของข้อมูล หรือเดินผ่านข้อมูลที่มีแถวและคอลัมน์

## 1.1. Nested `while` Loops

`while` สามารถซ้อนกันได้ โดยแต่ละวงวนมีเงื่อนไขควบคุมของตนเอง

```python
row = 1
while row <= 3:
    column = 1
    while column <= 2:
        print(row, column)
        column += 1
    row += 1
```

ผลลัพธ์คือ

```
1 1
1 2
2 1
2 2
3 1
3 2
```

สังเกตว่าเมื่อ `row` มีค่าใหม่ ต้องกำหนด `column = 1` ใหม่ภายในวงวนนอก
มิฉะนั้นวงวนชั้นในจะทำงานครบเฉพาะรอบแรก เพราะ `column` ยังคงมีค่าที่ทำให้
เงื่อนไขเป็นเท็จอยู่

ตัวอย่างต่อไปใช้วงวนชั้นนอกอ่านจำนวนเต็มทีละคู่จนพบ `q` และใช้วงวนชั้นใน
คำนวณ ห.ร.ม. ด้วย Euclidean algorithm

```python
data = input().split()
while data[0] != "q":
    a, b = int(data[0]), int(data[1])
    while b != 0:
        a, b = b, a % b
    print(a)
    data = input().split()
```

เมื่อผู้ใช้กรอกข้อมูลดังนี้

```
5 8
143 65
q
```

ผลลัพธ์คือ

```
1
13
```

วงวนชั้นนอกไม่จำเป็นต้องมีจำนวนรอบเท่ากับวงวนชั้นใน ในตัวอย่างนี้จำนวนรอบ
ของวงวนชั้นนอกขึ้นกับจำนวนคู่ข้อมูล ส่วนจำนวนรอบของวงวนชั้นในขึ้นกับค่าของ
`a` และ `b` ในแต่ละคู่

---

## 1.2. Nested `for` Loops

เมื่อซ้อน `for` วงวนชั้นในจะเดินครบทุกค่าของมันสำหรับแต่ละค่าของวงวนนอก

```python
for i in range(3):
    for j in range(4):
        print(i, j)
```

ค่าของ `(i, j)` จะเรียงดังนี้

| รอบของ `i` | ค่าของ `j` ที่เกิดขึ้น |
| :---------: | :-------------------- |
| `0`         | `0`, `1`, `2`, `3`    |
| `1`         | `0`, `1`, `2`, `3`    |
| `2`         | `0`, `1`, `2`, `3`    |

ดังนั้น block ชั้นในทำงานทั้งหมด $3 \times 4 = 12$ ครั้ง ถ้าวงวนหนึ่งทำงาน
`m` รอบและอีกวงวนทำงาน `n` รอบ จำนวนครั้งรวมโดยทั่วไปคือ `m * n`

ขอบเขตของวงวนชั้นในอาจขึ้นกับค่าของวงวนนอกได้

```python
for i in range(3):
    for j in range(i, 4):
        print(i, j)
```

ผลลัพธ์คือ

```
0 0
0 1
0 2
0 3
1 1
1 2
1 3
2 2
2 3
```

ในที่นี้ `j` เริ่มจาก `i` จึงได้เฉพาะคู่ที่ `i <= j`

---

## 1.3. Iterating over Pairs

หากต้องการแจกแจง **ทุกคู่ของสมาชิกที่อยู่คนละตำแหน่ง** โดยไม่กลับลำดับคู่เดิม
ให้วงวนชั้นในเริ่มที่ `i + 1`

```python
values = [11, 34, 22, 34]

for i in range(len(values) - 1):
    for j in range(i + 1, len(values)):
        print(i, j, values[i], values[j])
```

ผลลัพธ์คือ

```
0 1 11 34
0 2 11 22
0 3 11 34
1 2 34 22
1 3 34 34
2 3 22 34
```

เงื่อนไข `i < j` ทำให้

- ไม่เปรียบเทียบสมาชิกกับตัวเอง
- ไม่ตรวจคู่เดิมซ้ำ เช่น ตรวจ `(0, 1)` แต่ไม่ตรวจ `(1, 0)` อีก

จึงนำรูปแบบนี้ไปใช้ตรวจข้อมูลซ้ำกันได้

```python
def has_duplicate(values):
    for i in range(len(values) - 1):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                return True
    return False


print(has_duplicate([11, 34, 22, 34]))
print(has_duplicate([11, 34, 22]))
```

ผลลัพธ์คือ

```
True
False
```

> [!IMPORTANT]
>
> สำหรับลิสต์ยาว `n` สมาชิก วิธีตรวจทุกคู่มีจำนวนคู่
> `n * (n - 1) / 2` คู่ จึงช้าลงอย่างชัดเจนเมื่อลิสต์มีขนาดใหญ่

แนวคิดเดียวกันใช้ตรวจว่า จำนวนเต็มทุกคู่ในลิสต์เป็น coprime หรือไม่ กล่าวคือ
ห.ร.ม. ของทุกคู่ต้องเท่ากับ `1`

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


def is_pairwise_coprime(values):
    for i in range(len(values) - 1):
        for j in range(i + 1, len(values)):
            if gcd(values[i], values[j]) != 1:
                return False
    return True


print(is_pairwise_coprime([21, 10, 121]))
print(is_pairwise_coprime([21, 15, 35]))
```

ผลลัพธ์คือ

```
True
False
```

---

## 1.4. Moving an Inner Loop into a Function

เมื่อวงวนชั้นในทำหน้าที่ชัดเจน การย้ายงานส่วนนั้นไปเป็นฟังก์ชันช่วยให้โค้ดหลัก
อ่านง่ายขึ้น และทดสอบงานย่อยได้แยกจากส่วนอื่น

ตัวอย่างนี้นับจำนวนตัวเลขที่ปรากฏในข้อความหลายบรรทัด

```python
def count_digits(text):
    count = 0
    for character in text:
        if "0" <= character <= "9":
            count += 1
    return count


texts = ["room 101", "floor 2", "no digits"]
total = 0
for text in texts:
    total += count_digits(text)

print(total)
```

ผลลัพธ์คือ

```
4
```

วงวนที่เดินผ่าน `texts` เป็นงานระดับหลัก ส่วนวงวนใน `count_digits()` เป็นงาน
ย่อยที่เดินผ่านอักขระของข้อความหนึ่งบรรทัด โครงสร้างการทำงานยังเป็นการวนซ้อน
เหมือนเดิม แต่แยกความรับผิดชอบชัดเจนขึ้น

---

## 1.5. Leaving Nested Loops

คำสั่ง `break` ออกจาก **วงวนที่ครอบ `break` โดยตรงเพียงชั้นเดียว** เท่านั้น

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
```

ผลลัพธ์คือ

```
0 0
1 0
2 0
```

เมื่อ `j == 1` โปรแกรมออกจากวงวนของ `j` แต่ยังกลับไปทำรอบถัดไปของวงวน `i`

หากต้องการออกจากวงวนหลายชั้น ใช้ตัวแปรสถานะ (flag) สื่อให้วงวนนอกทราบว่า
วงวนชั้นในพบสิ่งที่ต้องการแล้ว

```python
grid = [[3, 8, 1], [4, 7, 9], [2, 5, 6]]
target = 7
found = False

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == target:
            print(i, j)
            found = True
            break
    if found:
        break
```

ผลลัพธ์คือ

```
1 1
```

อีกวิธีคือแยกการค้นหาเป็นฟังก์ชัน เพราะ `return` จบการทำงานของฟังก์ชันได้ทันที
ไม่ว่าจะอยู่ในวงวนกี่ชั้น

```python
def find_position(grid, target):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == target:
                return [i, j]
    return None


grid = [[3, 8, 1], [4, 7, 9], [2, 5, 6]]
print(find_position(grid, 7))
print(find_position(grid, 0))
```

ผลลัพธ์คือ

```
[1, 1]
None
```

> [!IMPORTANT]
>
> เลือกใช้ flag เมื่อโค้ดหลังวงวนยังต้องทำงานต่อในขอบเขตเดิม และเลือกแยกเป็น
> ฟังก์ชันเมื่อขั้นตอนนั้นเป็นงานย่อยที่มีผลลัพธ์หรือเงื่อนไขจบของตนเอง

---

## 2. Nested Lists (ลิสต์ซ้อน)

**Nested list (ลิสต์ซ้อน)** คือลิสต์ที่มีสมาชิกอย่างน้อยหนึ่งตัวเป็นลิสต์อีกที
จึงใช้แทนข้อมูลที่มีโครงสร้างย่อยได้หลายแบบ เช่น

- ข้อมูลหนึ่งรายการที่มีข้อมูลย่อยเป็นลิสต์
- ข้อมูลหลายรายการที่แต่ละรายการมีหลาย field
- ข้อมูลชั่วคราวที่ใช้ประกอบการประมวลผลหรือเรียงลำดับ
- ตารางหรือ matrix ที่มีแถวและคอลัมน์

ลิสต์ชั้นในไม่จำเป็นต้องมีขนาดเท่ากัน และสมาชิกในโครงสร้างเดียวกันอาจมีประเภท
ต่างกันได้

## 2.1. Creating and Accessing Nested Lists

ตัวอย่างต่อไปเก็บชื่อ ปีเกิด และรายชื่อผลงาน โดยสมาชิกตำแหน่งที่ `2` เป็นลิสต์
อีกชั้นหนึ่ง

```python
actor = [
    "Ranee",
    1989,
    ["Plerng Boon", "Bubphe Sanniwat", "Krong Kam"],
]

print(actor[0])
print(actor[2])
print(actor[2][1])
```

ผลลัพธ์คือ

```
Ranee
['Plerng Boon', 'Bubphe Sanniwat', 'Krong Kam']
Bubphe Sanniwat
```

- `actor[2]` เข้าถึงสมาชิกของลิสต์ชั้นนอก จึงได้ลิสต์ผลงานทั้งลิสต์
- `actor[2][1]` เข้าถึงลิสต์ชั้นนอกก่อน แล้วเข้าถึงสมาชิกตำแหน่งที่ `1`
  ของลิสต์ชั้นใน

เมื่อแก้ไขสมาชิกชั้นใน ค่าในโครงสร้างหลักจะเปลี่ยนด้วย

```python
records = [["A", 10], ["B", 20]]
records[1][1] = 25
print(records)
```

ผลลัพธ์คือ

```
[['A', 10], ['B', 25]]
```

---

## 2.2. Building a Nested List Incrementally

เราสร้างลิสต์ชั้นในทีละรายการ แล้ว `append()` เข้าไปในลิสต์ชั้นนอกได้

```python
raw_students = [
    "6131001021 3.8",
    "6130020221 3.7",
    "6130150721 2.7",
]

students = []
for line in raw_students:
    student_id, gpax_text = line.split()
    gpax = float(gpax_text)
    students.append([student_id, gpax])

print(students)
```

ผลลัพธ์คือ

```
[['6131001021', 3.8], ['6130020221', 3.7], ['6130150721', 2.7]]
```

ในตัวอย่างนี้ student ID เก็บเป็น `str` เพราะเป็นรหัส ไม่ใช่ค่าที่นำไปคำนวณ
ส่วน GPAX แปลงเป็น `float`

---

## 2.3. Sorting with Temporary Records

ลิสต์ซ้อนช่วยแนบ **sorting key** ไว้หน้าข้อมูลเดิมชั่วคราวได้ เนื่องจาก Python
เปรียบเทียบลิสต์จากสมาชิกตำแหน่งแรกก่อน หากเท่ากันจึงเปรียบเทียบตำแหน่งถัดไป

ตัวอย่างนี้เรียงคำตามความยาว และเรียงตามตัวอักษรเมื่อความยาวเท่ากัน

```python
def sorted_by_length(words):
    records = []
    for word in words:
        records.append([len(word), word])

    records.sort()

    result = []
    for length, word in records:
        result.append(word)
    return result


words = ["your", "kiss", "is", "on", "my", "list"]
print(sorted_by_length(words))
```

ผลลัพธ์คือ

```
['is', 'my', 'on', 'kiss', 'list', 'your']
```

ตัวแปร `records` มีโครงสร้างชั่วคราวดังนี้ก่อนเรียง

```
[[4, 'your'], [4, 'kiss'], [2, 'is'],
 [2, 'on'], [2, 'my'], [4, 'list']]
```

หลัง `records.sort()` ค่าความยาวที่อยู่ตำแหน่ง `0` จึงเป็นเกณฑ์หลัก และคำที่อยู่
ตำแหน่ง `1` เป็นเกณฑ์รอง

---

## 2.4. Shared Inner Lists

การใช้ `*` ทำซ้ำลิสต์ชั้นในไม่ได้สร้างลิสต์ชั้นในแยกกัน แต่ทำให้ทุกตำแหน่ง
อ้างถึง **ลิสต์เดียวกัน**

```python
rows = [[0]] * 3
rows[0][0] = 9
print(rows)
```

ผลลัพธ์คือ

```
[[9], [9], [9]]
```

เมื่อแก้ `rows[0][0]` จึงเห็นการเปลี่ยนแปลงผ่านทุกตำแหน่ง วิธีสร้างลิสต์ชั้นใน
ให้เป็นคนละลิสต์คือสร้างใหม่ทีละรอบ

```python
rows = []
for i in range(3):
    rows.append([0])

rows[0][0] = 9
print(rows)
```

ผลลัพธ์คือ

```
[[9], [0], [0]]
```

> [!WARNING]
>
> รูปแบบ `[[0] * columns] * rows` มีปัญหาเดียวกัน เพราะทุกแถวอ้างถึงลิสต์
> เดียวกัน การแก้ค่าเพียงช่องเดียวอาจทำให้ค่าคอลัมน์เดียวกันเปลี่ยนทุกแถว

---

## 2.5. Nested Lists as Matrices

Matrix สามารถแทนด้วยลิสต์ซ้อน โดยลิสต์ชั้นนอกเก็บแถว และลิสต์ชั้นในแต่ละตัว
เก็บสมาชิกในแถวนั้น

```python
matrix = [
    [1, 2, 3, 0],
    [2, 3, 0, 1],
    [4, 1, 2, 2],
]

print(matrix[0])
print(matrix[2][1])
```

ผลลัพธ์คือ

```
[1, 2, 3, 0]
1
```

สำหรับ `matrix[i][j]`

- `i` คือ index ของแถว
- `j` คือ index ของคอลัมน์ภายในแถวนั้น

| ค่า             | ความหมาย                    | ผลลัพธ์       |
| :-------------- | :-------------------------- | :------------ |
| `len(matrix)`   | จำนวนแถว                    | `3`           |
| `len(matrix[0])` | จำนวนคอลัมน์ของแถวแรก      | `4`           |
| `matrix[2][1]`  | สมาชิกแถวที่ `2` คอลัมน์ `1` | `1`           |

> [!IMPORTANT]
>
> Python ไม่บังคับให้ทุกแถวมีจำนวนสมาชิกเท่ากัน ก่อนประมวลผลแบบ matrix
> จึงควรตรวจหรือกำหนดให้ทุกแถวยาวเท่ากัน

---

## 2.6. Reading and Printing a Matrix

ฟังก์ชันต่อไปอ่านจำนวนแถวก่อน แล้วอ่านตัวเลขของแต่ละแถวเป็น `float`

```python
def read_matrix():
    matrix = []
    number_of_rows = int(input())
    for i in range(number_of_rows):
        row = []
        for value in input().split():
            row.append(float(value))
        matrix.append(row)
    return matrix
```

ถ้าข้อมูลเข้าคือ

```
3
1 2 3 0
2 3 0 1
4 1 2 2
```

ฟังก์ชันจะคืนค่า

```
[[1.0, 2.0, 3.0, 0.0],
 [2.0, 3.0, 0.0, 1.0],
 [4.0, 1.0, 2.0, 2.0]]
```

เมื่อแสดง matrix ทีละแถว รูปร่างของข้อมูลจะเห็นได้ชัดกว่าการ `print()` ลิสต์
ทั้งหมดในบรรทัดเดียว

```python
def print_matrix(matrix):
    for row in matrix:
        print(row)


matrix = [[1, 2, 3, 0], [2, 3, 0, 1], [4, 1, 2, 2]]
print_matrix(matrix)
```

ผลลัพธ์คือ

```
[1, 2, 3, 0]
[2, 3, 0, 1]
[4, 1, 2, 2]
```

---

## 2.7. Adding Matrices

การบวก matrix ต้องบวกสมาชิกตำแหน่งเดียวกัน จึงใช้วงวนชั้นนอกเดินตามแถวและ
วงวนชั้นในเดินตามคอลัมน์

```python
def add_matrices(matrix_a, matrix_b):
    result = []
    number_of_rows = len(matrix_a)
    number_of_columns = len(matrix_a[0])

    for i in range(number_of_rows):
        row = []
        for j in range(number_of_columns):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)

    return result


matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[10, 20, 30], [40, 50, 60]]
print(add_matrices(matrix_a, matrix_b))
```

ผลลัพธ์คือ

```
[[11, 22, 33], [44, 55, 66]]
```

ตัวอย่างสมมติว่า matrix ทั้งสองไม่ว่าง เป็นรูปสี่เหลี่ยม และมีขนาดเท่ากัน
หากขนาดต่างกัน การเข้าถึงตำแหน่งที่ไม่มีอยู่จะเกิด `IndexError` หรืออาจได้ผล
ที่ไม่ครบตามรูปร่างของข้อมูล

---

## 3. List Comprehensions (การสร้างลิสต์แบบย่อ)

**List comprehension** เป็นรูปแบบย่อสำหรับสร้างลิสต์ใหม่จาก iterable เช่น
ลิสต์หรือ `range()` โดยเขียนนิพจน์และวงวนไว้ภายใน `[]`

รูปแบบพื้นฐานคือ

```python
result = [expression for item in iterable]
```

List comprehension เหมาะกับการสร้างลิสต์ที่แต่ละสมาชิกคำนวณได้ด้วยนิพจน์สั้น ๆ
และอ่านเข้าใจได้ทันที

## 3.1. Transforming Values

หากต้องการแปลงทุกค่าใน `values` เป็นสองเท่า สามารถเขียนด้วยวงวนปกติได้ดังนี้

```python
values = [1, 2, 3, 4]
result = []
for value in values:
    result.append(2 * value)

print(result)
```

หรือเขียนเป็น list comprehension ที่ให้ผลเหมือนกัน

```python
values = [1, 2, 3, 4]
result = [2 * value for value in values]
print(result)
```

ผลลัพธ์คือ

```
[2, 4, 6, 8]
```

ส่วน `2 * value` คือค่าที่จะนำไปเป็นสมาชิกของลิสต์ใหม่ และ
`for value in values` ระบุที่มาของแต่ละค่า

---

## 3.2. Filtering Values

ใส่เงื่อนไข `if` หลังส่วน `for` เพื่อเลือกเฉพาะค่าที่ต้องการ

```python
values = [-3, 5, -1, 0, 8]
nonnegative_values = [value for value in values if value >= 0]
print(nonnegative_values)
```

ผลลัพธ์คือ

```
[5, 0, 8]
```

เงื่อนไข `value >= 0` ตัดสินว่าสมาชิกเดิมตัวใดจะถูกนำไปใส่ในลิสต์ใหม่
โดยไม่ได้แก้ไข `values`

---

## 3.3. Filtering and Transforming

การเลือกและการแปลงค่าเขียนร่วมกันได้ นิพจน์หน้า `for` ทำหน้าที่แปลงค่า ส่วน
`if` ด้านท้ายทำหน้าที่เลือกค่า

```python
values = [-3, 5, -1, 0, 8]
doubled = [2 * value for value in values if value >= 0]
print(doubled)
```

ผลลัพธ์คือ

```
[10, 0, 16]
```

ลำดับการอ่านคือ "สำหรับ `value` แต่ละตัวใน `values` ถ้าค่านั้นไม่ติดลบ
ให้นำ `2 * value` ไปใส่ในลิสต์ใหม่"

---

## 3.4. Reading Values with a Comprehension

รูปแบบที่ใช้บ่อยคือรับข้อความหลายค่าจากหนึ่งบรรทัด แล้วแปลงแต่ละค่าเป็นตัวเลข

```python
numbers = [int(value) for value in input().split()]
print(numbers)
```

เมื่อผู้ใช้กรอก

```
10 20 -5 8
```

ผลลัพธ์คือ

```
[10, 20, -5, 8]
```

ถ้าต้องการจำนวนจริง ให้เปลี่ยน `int(value)` เป็น `float(value)`

```python
numbers = [float(value) for value in input().split()]
print(numbers)
```

เมื่อผู้ใช้กรอก `1 2.5 -0.25` ผลลัพธ์คือ

```
[1.0, 2.5, -0.25]
```

---

## 3.5. Comprehensions with Nested Lists

ขั้นตอนสร้าง record ชั่วคราวและดึงข้อมูลหลังเรียงจากหัวข้อ 2.3 เขียนให้กระชับ
ด้วย list comprehension ได้

```python
def sorted_by_length(words):
    records = [[len(word), word] for word in words]
    records.sort()
    return [word for length, word in records]


words = ["your", "kiss", "is", "on", "my", "list"]
print(sorted_by_length(words))
```

ผลลัพธ์คือ

```
['is', 'my', 'on', 'kiss', 'list', 'your']
```

List comprehension แรกสร้างลิสต์ซ้อนที่แต่ละสมาชิกเป็น `[ความยาว, คำ]`
ส่วน comprehension หลัง `sort()` unpack แต่ละ record เป็น `length` และ `word`
แล้วเก็บเฉพาะ `word` ลงในผลลัพธ์

---

## 3.6. Readability and Performance

List comprehension มักกระชับและอาจทำงานเร็วกว่าวงวนที่เรียก `append()` ทีละรอบ
ใน Python แต่ความเร็วจริงขึ้นกับข้อมูล นิพจน์ และ Python version จึงไม่ควรอาศัย
ตัวเลขเวลาจากเครื่องหนึ่งไปสรุปผลกับทุกโปรแกรม

> [!IMPORTANT]
>
> เลือก list comprehension เมื่อเป็นการสร้างลิสต์ด้วยการแปลงหรือกรองแบบสั้น
> หากมีหลายเงื่อนไข มีผลข้างเคียง หรือจำเป็นต้องอธิบายหลายขั้นตอน วงวน `for`
> ปกติมักอ่านและแก้ไขได้ง่ายกว่า

ตัวอย่างทั้งสองแบบต่อไปให้ผลเหมือนกัน

```python
values = range(6)

with_loop = []
for value in values:
    with_loop.append(value * value)

with_comprehension = [value * value for value in range(6)]

print(with_loop)
print(with_comprehension)
```

ผลลัพธ์คือ

```
[0, 1, 4, 9, 16, 25]
[0, 1, 4, 9, 16, 25]
```
