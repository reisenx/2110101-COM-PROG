<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Fill in Numbers ★★★ (
      <a href="https://drive.google.com/file/d/1MGvTR5ZNjPpurG1jetgUOv__NIuNpQOu/view?usp=drive_link">
        <code>09_Nested_34</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การมองตารางด้วยดัชนีแถวและคอลัมน์**](#การมองตารางด้วยดัชนีแถวและคอลัมน์)
-   [**รูปแบบที่ 1 และ 2**](#รูปแบบที่-1-และ-2)
-   [**รูปแบบที่ 3**](#รูปแบบที่-3)
-   [**รูปแบบที่ 4**](#รูปแบบที่-4)
-   [**รูปแบบที่ 5**](#รูปแบบที่-5)
-   [**รูปแบบที่ 6**](#รูปแบบที่-6)
-   [**การรับคำสั่งทดสอบจาก Grader**](#การรับคำสั่งทดสอบจาก-grader)
-   [**Solution**](#solution)

---

## การมองตารางด้วยดัชนีแถวและคอลัมน์

ตารางในโจทย์แทนด้วย **ลิสต์ซ้อนลิสต์** โดยลิสต์ด้านนอกคือ `matrix`
และแต่ละลิสต์ด้านในคือหนึ่งแถว `row`

```python
matrix = []
row = []
row.append(num)
matrix.append(row)
```

โค้ดใช้ `i` เป็นดัชนีแถวและ `j` เป็นดัชนีคอลัมน์ โดยดัชนีของ Python
เริ่มจาก `0` แต่ตัวเลขที่เติมในตารางเริ่มจาก `1` สูตรจึงมักมี `+ 1`

ทุกฟังก์ชันคืนค่าลิสต์ซ้อนลิสต์ ไม่ได้พิมพ์ตารางโดยตรง เมื่อ Grader ใช้
`print()` ผลลัพธ์จึงอยู่ในรูป `[[...], [...]]` การคำนวณทั้งหมดเป็นจำนวนเต็ม
และไม่มีการปัดเศษ

โจทย์กำหนดให้จำนวนแถวและคอลัมน์ไม่ติดลบ กรณีมี `0` แถวจะได้ `[]`
สำหรับ `pattern1` และ `pattern2` ถ้ามีหลายแถวแต่มี `0` คอลัมน์
จะได้ลิสต์ว่างหนึ่งลิสต์ต่อแถว เช่น `pattern1(3, 0)` ได้ `[[], [], []]`
ส่วน `pattern3(0)` ถึง `pattern6(0)` ได้ `[]`

---

## รูปแบบที่ 1 และ 2

สองรูปแบบแรกสร้างตารางเต็มขนาด `rows` คูณ `cols`
แต่ต่างกันที่ทิศทางการนับเลข

**รูปแบบที่ 1 - นับจากซ้ายไปขวาทีละแถว**

ก่อนถึงแถว `i` มีตัวเลขผ่านไปแล้ว `i * cols` ตัว
ตำแหน่งคอลัมน์ `j` จึงมีค่า

$$
i \times cols + j + 1
$$

```python
num = (i * cols) + j + 1
```

**รูปแบบที่ 2 - นับจากบนลงล่างทีละคอลัมน์**

ก่อนถึงคอลัมน์ `j` มีตัวเลขผ่านไปแล้ว `j * rows` ตัว
แล้วเลื่อนลงมาตามแถว `i` จึงมีค่า

$$
j \times rows + i + 1
$$

```python
num = (j * rows) + i + 1
```

ตัวอย่างตารางขนาด `2` แถว `3` คอลัมน์

```text
pattern1(2, 3) -> [[1, 2, 3], [4, 5, 6]]
pattern2(2, 3) -> [[1, 3, 5], [2, 4, 6]]
```

แม้รูปแบบที่ 2 จะนับตามคอลัมน์ แต่โค้ดยังสร้างผลลัพธ์ทีละแถว
จึงใช้สูตรคำนวณค่าของแต่ละตำแหน่งแทนการเปลี่ยนโครงสร้างลูป

---

## รูปแบบที่ 3

ตั้งแต่รูปแบบที่ 3 เป็นต้นไป ตารางเป็นสี่เหลี่ยมจัตุรัสขนาด `rows`
และตำแหน่งใต้เส้นทแยงมุมหลักเป็น `0` ในแถวที่ `i`
จึงเริ่มสร้างแถวด้วยเลขศูนย์จำนวน `i` ตัว

```python
row = [0] * i
```

รูปแบบที่ 3 นับเลขจากซ้ายไปขวาทีละแถว เฉพาะตำแหน่งบนและเหนือ
เส้นทแยงมุม ตัวแปร `num` ถูกสร้างนอกลูปของแถว จึงนับต่อเนื่อง
และไม่กลับไปเป็น `0` เมื่อเริ่มแถวใหม่

ในแถว `i` มีช่องที่ต้องเติม `rows - i` ช่อง ซึ่งตรงกับ
`range(i, rows)` แต่ละรอบจะเพิ่ม `num` ก่อนแล้วจึง `append()`

```python
num += 1
row.append(num)
```

ตัวอย่าง `pattern3(4)` ได้

```text
[[1, 2, 3, 4],
 [0, 5, 6, 7],
 [0, 0, 8, 9],
 [0, 0, 0, 10]]
```

---

## รูปแบบที่ 4

รูปแบบนี้มองลำดับเลขเป็นการเติมแต่ละคอลัมน์จากเส้นทแยงมุมย้อนขึ้นด้านบน
เช่นคอลัมน์แรกมี `1` คอลัมน์ถัดไปมี `2, 3` และคอลัมน์ถัดไปมี `4, 5, 6`

เมื่อโค้ดสร้างผลลัพธ์ทีละแถว จึงต้องคำนวณเลขตัวแรกของแถว `i`
ด้วยจำนวนสามเหลี่ยม

$$
\frac{i(i+1)}{2} + 1
$$

```python
num = (i * (i + 1)) // 2 + 1
```

ผลคูณ `i * (i + 1)` เป็นจำนวนคู่เสมอ จึงใช้ `// 2` แล้วได้จำนวนเต็มพอดี
หลังใส่ค่าที่คอลัมน์ `j` ค่าถัดไปทางขวาจะเพิ่มขึ้น `j + 2`

```python
num += j + 2
```

ตัวอย่างในแถว `i = 1` ของ `pattern4(5)` ค่าแรกคือ `2`
แล้วเพิ่มทีละ `3`, `4` และ `5` จึงได้ `[0, 2, 5, 9, 14]`

---

## รูปแบบที่ 5

รูปแบบที่ 5 เติมเลขตามแนวทแยงที่ขนานกับเส้นทแยงมุมหลัก
โดยทุกแนวเดินจากบนลงล่าง เลขบนเส้นทแยงมุมหลักจึงเป็น
`1, 2, 3, ...` และเลขตัวแรกของแถว `i` คือ

```python
num = i + 1
```

ลูปด้านในใช้ `j` เป็นลำดับการเลื่อนไปทางขวาภายในแถว
มีทั้งหมด `rows - i` ตำแหน่ง หลังใส่แต่ละค่า โค้ดเพิ่มค่าถัดไปด้วย

$$
rows - j
$$

```python
num += rows - j
```

ตัวอย่างแถว `i = 1` ของ `pattern5(5)` เริ่มจาก `2`
แล้วเพิ่ม `5`, `4` และ `3` จึงได้ `[0, 2, 7, 11, 14]`

> [!NOTE]
>
> comment ในส่วน Pattern 05 ระบุว่าเพิ่ม `(N - i - j)` แต่โค้ดจริงเพิ่ม
> `rows - j` โดย **ไม่ได้ลบ `i`** ผลลัพธ์ในโจทย์สอดคล้องกับโค้ดจริงนี้
> จึงต้องยึด `num += rows - j` ในการอธิบาย ส่วน comment เดิมยังคงอยู่ใน
> Solution เพื่อให้ตรงกับไฟล์คำตอบ

---

## รูปแบบที่ 6

รูปแบบสุดท้ายเติมเลขตามแนวทแยงเช่นเดียวกับรูปแบบที่ 5
แต่สลับทิศทางไปมา โค้ดเริ่มแต่ละแถวด้วยเลขศูนย์ใต้เส้นทแยงมุมก่อน

```python
for i in range(rows):
    matrix.append([0] * i)
```

ลูปนอกใช้ `j` แทนลำดับของแนวทแยง แนวที่ `j` มีสมาชิก `rows - j` ตัว
จึงใช้ `range(rows - j)` ส่วน `j % 2` ตรวจว่าเป็นแนวคู่หรือแนวคี่

-   `j % 2 == 0` เติมจากแถวบนลงล่างด้วย `matrix[i].append(num)`
-   เมื่อ `j` เป็นจำนวนคี่ เติมจากแถวล่างขึ้นบนด้วย
    `matrix[rows - j - (i + 1)].append(num)`

ตัวแปร `num` เพิ่มทีละ `1` ตลอดทุกแนว จึงเกิดลำดับแบบซิกแซ็ก
ตัวอย่าง `pattern6(4)` ได้

```text
[[1, 7, 8, 10],
 [0, 2, 6, 9],
 [0, 0, 3, 5],
 [0, 0, 0, 4]]
```

---

## การรับคำสั่งทดสอบจาก Grader

บรรทัด `exec(input().strip())` รับคำสั่ง Python หนึ่งบรรทัดเพื่อให้ Grader
เรียกฟังก์ชัน เช่น `print(pattern1(3, 4))` แล้วแสดงลิสต์ซ้อนลิสต์ที่คืนมา

> [!WARNING]
>
> `exec()` สามารถสั่งทำงานโค้ดใด ๆ ที่อยู่ในข้อความได้ จึงใช้ในข้อนี้เพื่อให้
> Grader ทดสอบฟังก์ชันตามรูปแบบที่กำหนดเท่านั้น ไม่ควรใช้กับข้อมูลจากแหล่ง
> ที่ไม่เชื่อถือ

---

# Solution

```python
# --------------------------------------------------
# File Name : 09_Nested_34.py
# Problem   : Fill in Numbers
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# ---------- Patterns 01 ----------
# rows is the number of rows
# cols is the number of columns
# [[ 1,  2,  3,  4,  5,  6,  7],
#  [ 8,  9, 10, 11, 12, 13, 14],
#  [15, 16, 17, 18, 19, 20, 21]]
def pattern1(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Calculate the number based on row and column indices
            num = (i * cols) + j + 1
            row.append(num)
        # Add each row to a matrix
        matrix.append(row)
    return matrix


# ---------- Patterns 02 ----------
# rows is the number of rows
# cols is the number of columns
# [[1, 4, 7, 10, 13, 16, 19],
#  [2, 5, 8, 11, 14, 17, 20],
#  [3, 6, 9, 12, 15, 18, 21]]
def pattern2(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Calculate the number based on row and column indices
            num = (j * rows) + i + 1
            row.append(num)
        # Add each row to a matrix
        matrix.append(row)
    return matrix


# ---------- Patterns 03 ----------
# N is the number of rows and columns
# [[1, 2,  3,  4,  5],
#  [0, 6,  7,  8,  9],
#  [0, 0, 10, 11, 12],
#  [0, 0,  0, 13, 14],
#  [0, 0,  0,  0, 15]]
def pattern3(rows):
    num = 0
    matrix = []
    for i in range(rows):
        # Create a row with zeros at the beginning
        row = [0] * i
        for _ in range(i, rows):
            # Append the current number to the row
            num += 1
            row.append(num)
        # Add each row to a matrix
        matrix.append(row)
    return matrix


# ---------- Patterns 04 ----------
# N is the number of rows and columns
# [[1, 3, 6, 10, 15],
#  [0, 2, 5,  9, 14],
#  [0, 0, 4,  8, 13],
#  [0, 0, 0,  7, 12],
#  [0, 0, 0,  0, 11]]
def pattern4(rows):
    matrix = []
    for i in range(rows):
        # Create a row with zeros at the beginning
        row = [0] * i
        # Calculate the first number in the row
        num = (i * (i + 1)) // 2 + 1
        for j in range(i, rows):
            # Append the current number to the row
            row.append(num)
            # Get the next number by adding (j + 2)
            num += j + 2
        # Add each row to a matrix
        matrix.append(row)
    return matrix


# ---------- Patterns 05 ----------
# N is the number of rows and columns
# [[1, 6, 10, 13, 15],
#  [0, 2,  7, 11, 14],
#  [0, 0,  3,  8, 12],
#  [0, 0,  0,  4,  9],
#  [0, 0,  0,  0,  5]]
def pattern5(rows):
    matrix = []
    for i in range(rows):
        # Create a row with zeros at the beginning
        row = [0] * i
        # Calculate the first number in the row
        num = i + 1
        for j in range(rows - i):
            # Append the current number to the row
            row.append(num)
            # Get the next number by adding (N - i - j)
            num += rows - j
        # Add each row to a matrix
        matrix.append(row)
    return matrix


# ---------- Patterns 06 ----------
# N is the number of rows and columns
# [[1, 9, 10, 14, 15],
#  [0, 2,  8, 11, 13],
#  [0, 0,  3,  7, 12],
#  [0, 0,  0,  4,  6],
#  [0, 0,  0,  0,  5]]
def pattern6(rows):
    # Initialize the matrix with zeros
    matrix = []
    for i in range(rows):
        matrix.append([0] * i)

    # Fill the matrix with numbers
    num = 1
    for j in range(rows):
        for i in range(rows - j):
            if j % 2 == 0:
                matrix[i].append(num)
            else:
                matrix[rows - j - (i + 1)].append(num)
            num += 1
    return matrix


# Execute an input string
exec(input().strip())
```
