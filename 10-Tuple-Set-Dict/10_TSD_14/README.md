<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Database ★☆ (
      <a href="https://drive.google.com/file/d/1sVM1L8WTU6poZMnUgH2q4Ru3ynjeVz0j/view?usp=drive_link">
        <code>10_TSD_14</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**โครงสร้างฐานข้อมูลสามไฟล์**](#โครงสร้างฐานข้อมูลสามไฟล์)
-   [**การสร้างตารางค้นหาด้วย Dictionary**](#การสร้างตารางค้นหาด้วย-dictionary)
-   [**การประมวลผลฐานข้อมูล**](#การประมวลผลฐานข้อมูล)
-   [**ตัวอย่างการติดตามผล**](#ตัวอย่างการติดตามผล)
-   [**ข้อควรสังเกต**](#ข้อควรสังเกต)
-   [**Solution**](#solution)

---

## โครงสร้างฐานข้อมูลสามไฟล์

แทนที่จะเขียนรหัสวิชาและชื่อผู้สอนซ้ำกันทุกระเบียน โจทย์แยกข้อมูลออกเป็น
สามไฟล์ โดยรับชื่อไฟล์ตามลำดับดังนี้

1. ไฟล์รายวิชา เช่น `courses.txt`
2. ไฟล์ผู้สอน เช่น `teachers.txt`
3. ไฟล์ฐานข้อมูลที่จับคู่รหัสภายในของวิชาและผู้สอน เช่น `database.txt`

ตัวอย่างข้อมูลที่สัมพันธ์กันมีลักษณะดังนี้

| ไฟล์ | ข้อมูลหนึ่งบรรทัด | ความหมาย |
| :-- | :-- | :-- |
| `courses.txt` | `1,2110101` | รหัสภายใน `1` หมายถึงวิชา `2110101` |
| `teachers.txt` | `9,Somchai` | รหัสภายใน `9` หมายถึงผู้สอน `Somchai` |
| `database.txt` | `1,9` | วิชารหัสภายใน `1` สอนโดยผู้สอนรหัสภายใน `9` |

ดังนั้นระเบียน `1,9` ต้องถูกแปลงกลับเป็น

```text
2110101,Somchai
```

---

## การสร้างตารางค้นหาด้วย Dictionary

โปรแกรมอ่านสองไฟล์แรกเพื่อสร้าง dictionary สำหรับค้นหาค่าจากรหัสภายใน

```python
course_num, course_code = line.strip().split(",")
courses[course_num] = course_code
```

`line.strip()` ตัดอักขระขึ้นบรรทัดใหม่ที่ท้ายบรรทัด และ `split(",")`
แยกข้อความตรงจุลภาค จากนั้น `courses` จะเก็บความสัมพันธ์
`รหัสภายในของวิชา -> รหัสวิชา`

ไฟล์ผู้สอนทำงานแบบเดียวกัน

```python
prof_num, prof_name = line.strip().split(",")
professors[prof_num] = prof_name
```

โดย `professors` เก็บความสัมพันธ์
`รหัสภายในของผู้สอน -> ชื่อผู้สอน` แม้ไฟล์ตัวอย่างในโจทย์ใช้ชื่อ
`teachers.txt` แต่ตัวแปร `professor_filename` และ `professors` ในโปรแกรม
หมายถึงข้อมูลผู้สอนชุดเดียวกัน

> [!NOTE]
>
> รหัสภายในถูกเก็บเป็น `str` ไม่ได้แปลงเป็น `int` เพราะโปรแกรมใช้รหัสเพื่อ
> ค้นหาข้อมูลเท่านั้น ไม่ได้นำไปคำนวณ

---

## การประมวลผลฐานข้อมูล

โปรแกรมอ่านไฟล์ที่สามทีละบรรทัด แล้วแยกรหัสภายในสองค่า

```python
course_num, prof_num = line.strip().split(",")
```

ระเบียนจะแปลงเป็นข้อมูลที่อ่านได้ต่อเมื่อค้นพบ **ทั้ง** รหัสวิชาและรหัสผู้สอน

```python
if course_num in courses and prof_num in professors:
```

เมื่อทั้งสองรหัสถูกต้อง โปรแกรมค้นหารหัสวิชาและชื่อผู้สอน แล้วใช้ f-string
เชื่อมด้วยจุลภาคโดยไม่มีช่องว่าง

```python
course_code = courses[course_num]
prof_name = professors[prof_num]
print(f"{course_code},{prof_name}")
```

ถ้าขาดรหัสใดรหัสหนึ่ง โปรแกรมแสดงข้อความตรงตามที่โจทย์กำหนด

```text
record error
```

โปรแกรมวนผ่าน `database_file` โดยตรง จึงแสดงผลหนึ่งบรรทัดต่อหนึ่งระเบียน
และรักษาลำดับเดิมของไฟล์ฐานข้อมูล ไม่ได้เรียงตามรหัสหรือชื่อ

---

## ตัวอย่างการติดตามผล

เมื่อใช้ไฟล์รายวิชาและผู้สอนจากตัวอย่างกับ `database2.txt`

```text
1,4
3,9
4,5
5,1
```

จะประมวลผลได้ดังนี้

| ระเบียน | ผลการค้นหา | ข้อมูลส่งออก |
| :--: | :-- | :-- |
| `1,4` | มีวิชา `1` แต่ไม่มีผู้สอน `4` | `record error` |
| `3,9` | วิชา `2100111` และผู้สอน `Somchai` | `2100111,Somchai` |
| `4,5` | วิชา `2110200` และผู้สอน `Nattee` | `2110200,Nattee` |
| `5,1` | ไม่มีวิชา `5` | `record error` |

จะเห็นว่าระเบียนผิดพลาดไม่ทำให้โปรแกรมหยุด ระเบียนถัดไปยังถูกตรวจสอบและ
แสดงผลตามปกติ

---

## ข้อควรสังเกต

-   ลำดับชื่อไฟล์สามบรรทัดต้องเป็นไฟล์วิชา ไฟล์ผู้สอน และไฟล์จับคู่ตามลำดับ
-   โปรแกรมคาดว่าแต่ละบรรทัดมีข้อมูลสองส่วนคั่นด้วยจุลภาค `,`
-   การตรวจสมาชิกด้วย `in` ต้องทำก่อนเข้าถึง `courses[course_num]` หรือ
    `professors[prof_num]` เพื่อหลีกเลี่ยงการค้นหา key ที่ไม่มีอยู่
-   `with open(...)` ทำให้ไฟล์ถูกปิดโดยอัตโนมัติเมื่ออ่านเสร็จ

---

# Solution

```python
# --------------------------------------------------
# File Name : 10_TSD_14.py
# Problem   : Database
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input filenames
course_filename = input().strip()
professor_filename = input().strip()
database_filename = input().strip()

# Initialize dictionaries for courses and professors
courses = {}
professors = {}

# Read courses from the course file
with open(course_filename) as course_file:
    for line in course_file:
        course_num, course_code = line.strip().split(",")
        courses[course_num] = course_code

# Read professors from the professor file
with open(professor_filename) as professor_file:
    for line in professor_file:
        prof_num, prof_name = line.strip().split(",")
        professors[prof_num] = prof_name

# Read the database file and process each entry
with open(database_filename) as database_file:
    for line in database_file:
        course_num, prof_num = line.strip().split(",")
        if course_num in courses and prof_num in professors:
            course_code = courses[course_num]
            prof_name = professors[prof_num]
            print(f"{course_code},{prof_name}")
        else:
            print("record error")
```
