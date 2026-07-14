<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    ASCII Text ★★★ (
      <a href="https://drive.google.com/file/d/19OKv5YMBBL2tA_5PuhJFt6fX69pJdM4d/view?usp=drive_link">
        <code>P3_04_Ascii</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**มอง ASCII Text เป็นตาราง**](#มอง-ascii-text-เป็นตาราง)
-   [**หาคอลัมน์ที่เป็นจุดล้วน**](#หาคอลัมน์ที่เป็นจุดล้วน)
-   [**เลือกคอลัมน์ที่จะลบตามคำสั่ง**](#เลือกคอลัมน์ที่จะลบตามคำสั่ง)
-   [**แสดงภาพจากหน้ากากคอลัมน์**](#แสดงภาพจากหน้ากากคอลัมน์)
-   [**ลำดับการทำงานของโปรแกรม**](#ลำดับการทำงานของโปรแกรม)
-   [**Solution**](#solution)

---

## มอง ASCII Text เป็นตาราง

แฟ้มในโจทย์เก็บภาพด้วยอักขระหลายบรรทัด โดยใช้จุด (`.`) แทนช่องว่าง
และทุกบรรทัดมีความยาวเท่ากัน เราจึงมองข้อมูลเป็นตารางที่มี
`rows` แถว และ `cols` คอลัมน์ได้

```text
..A..B.
..A..B.
```

เมื่อนำแต่ละบรรทัดมาเก็บในลิสต์ `image` จะเข้าถึงอักขระที่แถว `row`
และคอลัมน์ `col` ได้ด้วย `image[row][col]` โดยจำนวนแถวและคอลัมน์คือ

$$
R = \texttt{len(image)}
\qquad
C = \texttt{len(image[0])}
$$

ฟังก์ชัน `extract_image_from_file()` เปิดแฟ้มและสร้างลิสต์ของบรรทัดด้วย
`line.strip()` ในข้อมูลตามโจทย์ ช่องว่างถูกแทนด้วยจุดอยู่แล้ว
จึงเหลือเพียงภาพที่พร้อมนำมาพิจารณาทีละคอลัมน์

---

## หาคอลัมน์ที่เป็นจุดล้วน

คอลัมน์หนึ่งจะเป็นช่องว่างที่ลบได้ ก็ต่อเมื่ออักขระในคอลัมน์นั้น
เป็นจุดทุกแถว เขียนเป็นเงื่อนไขทางคณิตศาสตร์ได้ว่า

$$
\texttt{is\_all\_dots[c]}
=
\bigwedge_{r=0}^{R-1}
\left(\texttt{image[r][c] == "."}\right)
$$

ในภาษา Python โค้ดสร้างลิสต์ `result` ที่เริ่มต้นด้วย `True`
ทุกคอลัมน์ แล้วใช้ลูปซ้อนตรวจอักขระจากบนลงล่าง

```python
result = [True] * cols
for col in range(cols):
    for row in range(rows):
        if image[row][col] != ".":
            result[col] = False
            break
```

เมื่อพบอักขระที่ไม่ใช่จุดเพียงตัวเดียว คอลัมน์นั้นห้ามถูกลบ
จึงเปลี่ยนค่าเป็น `False` และใช้ `break` หยุดตรวจคอลัมน์นั้นได้ทันที

จากภาพตัวอย่างข้างต้น จะได้หน้ากากคอลัมน์ดังนี้

```text
คอลัมน์             0     1     2      3     4     5      6
is_all_dots       True  True  False  True  True  False  True
```

---

## เลือกคอลัมน์ที่จะลบตามคำสั่ง

ลิสต์ Boolean ที่ใช้บอกว่าคอลัมน์ใดต้องถูกลบ เรียกว่า
**หน้ากากคอลัมน์** ถ้าค่าในตำแหน่งหนึ่งเป็น `True`
`print_image()` จะข้ามคอลัมน์นั้น

| คำสั่ง | คอลัมน์ที่มีค่า `True` ในหน้ากาก |
| :-- | :-- |
| `LSTRIP` | คอลัมน์จุดล้วนที่เรียงต่อกันจากขอบซ้าย |
| `RSTRIP` | คอลัมน์จุดล้วนที่เรียงต่อกันจากขอบขวา |
| `STRIP` | คอลัมน์จุดล้วนที่อยู่ติดขอบซ้ายหรือขอบขวา |
| `STRIP_ALL` | ทุกคอลัมน์ที่เป็นจุดล้วน แม้อยู่ระหว่างตัวอักษรใหญ่ |

`get_column_left_strip()` เดินจากซ้ายไปขวาจนพบคอลัมน์แรกที่ไม่ใช่จุดล้วน
ส่วน `get_column_right_strip()` ทำแบบเดียวกันจากขวาไปซ้าย
สำหรับ `STRIP` โค้ดนำหน้ากากทั้งสองด้านมารวมกันด้วย `or`

```python
is_strip = [
    left_strip[i] or right_strip[i]
    for i in range(cols)
]
```

ถ้าใช้ภาพตัวอย่างเดิม ผลลัพธ์หนึ่งบรรทัดของแต่ละคำสั่งจะเป็นดังนี้

| คำสั่ง | ผลลัพธ์ |
| :-- | :-- |
| `LSTRIP` | `A..B.` |
| `RSTRIP` | `..A..B` |
| `STRIP` | `A..B` |
| `STRIP_ALL` | `AB` |

สังเกตว่า `STRIP_ALL` ไม่ได้ลบจุดทุกตัว แต่ลบเฉพาะคอลัมน์ที่
**ทุกแถว** เป็นจุดเท่านั้น ถ้าคอลัมน์หนึ่งมีส่วนของตัวอักษรอยู่แม้เพียงแถวเดียว
คอลัมน์นั้นจะยังคงอยู่

---

## แสดงภาพจากหน้ากากคอลัมน์

`print_image(image, is_strip)` อ่านภาพตามลำดับเดิมจากแถวบนลงแถวล่าง
และจากคอลัมน์ซ้ายไปขวา หาก `is_strip[col]` เป็น `False`
จึงนำอักขระในคอลัมน์นั้นมาต่อท้าย `line`

```python
for row in image:
    line = ""
    for col in range(len(row)):
        if not is_strip[col]:
            line += row[col]
    print(line)
```

โปรแกรมจึงไม่สลับลำดับอักขระ ไม่เติมช่องว่าง และไม่เปลี่ยนอักขระอื่น
เพียงตัดคอลัมน์ตามหน้ากาก แล้วพิมพ์ผลลัพธ์ทีละบรรทัดเท่านั้น

---

## ลำดับการทำงานของโปรแกรม

1. รับชื่อแฟ้มจากข้อมูลนำเข้าบรรทัดแรก และรับคำสั่งจากบรรทัดที่สอง
2. อ่านภาพทั้งหมดเป็นลิสต์ `image`
3. สร้าง `is_all_dots` เพื่อบอกว่าคอลัมน์ใดเป็นจุดล้วน
4. เลือกหน้ากากให้ตรงกับ `STRIP_ALL`, `STRIP`, `LSTRIP`
   หรือ `RSTRIP`
5. พิมพ์ภาพหลังตัดคอลัมน์ หรือพิมพ์ `Invalid command`
   เมื่อคำสั่งไม่ตรงกับทั้งสี่แบบ

คำสั่งต้องสะกดด้วยตัวพิมพ์ใหญ่ตามที่กำหนด เช่น `strip`
ไม่ใช่คำสั่งเดียวกับ `STRIP`

โจทย์รับประกันว่าแฟ้มทดสอบจะไม่เป็นจุดล้วนทั้งแฟ้ม
เงื่อนไขนี้ทำให้ฟังก์ชันที่ค้นจากขอบซ้ายและขอบขวา
พบคอลัมน์ที่ไม่ใช่จุดล้วนก่อนจบลูปเสมอ
ส่วนแฟ้มว่างหรือบรรทัดที่ยาวไม่เท่ากันก็อยู่นอกเงื่อนไขของโจทย์

---

# Solution

```python
# --------------------------------------------------
# File Name : P3_04_Ascii.py
# Problem   : Part-III ASCII Text
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------


# Extract text from a file and return it as a list of lines.
def extract_image_from_file(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


# Check if all characters in each column of the image are dots ('.')
def get_column_all_dots(image):
    rows, cols = len(image), len(image[0])
    result = [True] * cols
    for col in range(cols):
        for row in range(rows):
            if image[row][col] != ".":
                result[col] = False
                break
    return result


# Get the left strip of columns where all characters are dots ('.').
def get_column_left_strip(is_all_dots):
    cols = len(is_all_dots)
    for idx in range(cols):
        if not is_all_dots[idx]:
            break
    return [True] * idx + [False] * (cols - idx)


# Get the right strip of columns where all characters are dots ('.').
def get_column_right_strip(is_all_dots):
    cols = len(is_all_dots)
    for idx in range(cols):
        if not is_all_dots[-idx - 1]:
            break
    return [False] * (cols - idx) + [True] * idx


# Get the strip of columns where all characters are dots ('.') on either side.
def get_column_strip(is_all_dots):
    cols = len(is_all_dots)
    left_strip = get_column_left_strip(is_all_dots)
    right_strip = get_column_right_strip(is_all_dots)
    return [left_strip[i] or right_strip[i] for i in range(cols)]


# Output the image without the columns that are all dots ('.').
def print_image(image, is_strip):
    for row in image:
        line = ""
        for col in range(len(row)):
            if not is_strip[col]:
                line += row[col]
        print(line)


# Input filename and command
filename = input().strip()
command = input().strip()

# Extract the image from the file
image = extract_image_from_file(filename)
# Get the columns where all characters are dots ('.')
is_all_dots = get_column_all_dots(image)
# Print the image based on the command
if command == "STRIP_ALL":
    print_image(image, is_all_dots)
elif command == "STRIP":
    is_strip = get_column_strip(is_all_dots)
    print_image(image, is_strip)
elif command == "LSTRIP":
    is_strip = get_column_left_strip(is_all_dots)
    print_image(image, is_strip)
elif command == "RSTRIP":
    is_strip = get_column_right_strip(is_all_dots)
    print_image(image, is_strip)
else:
    print("Invalid command")
```
