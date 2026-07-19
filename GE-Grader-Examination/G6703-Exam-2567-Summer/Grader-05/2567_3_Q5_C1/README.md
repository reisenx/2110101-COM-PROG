<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Student Grouping ★★ (
      <a href="https://drive.google.com/file/d/18QWAzO3DB4sNp6vdtzaOhEU-TFOlXEVL/view?usp=sharing">
        <code>2567_3_Q5_C1</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**รูปแบบข้อมูลในไฟล์**](#รูปแบบข้อมูลในไฟล์)
-   [**สร้างกลุ่มทั้งสามแบบ**](#สร้างกลุ่มทั้งสามแบบ)
-   [**รักษาลำดับจากไฟล์**](#รักษาลำดับจากไฟล์)
-   [**เลือกและแสดงผลกลุ่ม**](#เลือกและแสดงผลกลุ่ม)
-   [**ข้อควรระวังเกี่ยวกับไฟล์ตัวอย่าง**](#ข้อควรระวังเกี่ยวกับไฟล์ตัวอย่าง)
-   [**Solution**](#solution)

---

## รูปแบบข้อมูลในไฟล์

โปรแกรมรับชื่อไฟล์และรูปแบบการจัดกลุ่มจากแป้นพิมพ์ เช่น

```text
data.txt 1
```

ค่า `display_type` เป็น `1`, `2` หรือ `3` ส่วนไฟล์ข้อมูลต้องมีรหัสนิสิตและ
รหัสวิชาหนึ่งคู่ต่อหนึ่งบรรทัด คั่นด้วยช่องว่าง

```text
6532345621 2110101
6631111121 2110101
6631111121 2002020
```

`open(filename)` เปิดไฟล์ตาม path ที่รับเข้ามา หากใช้ path แบบ relative เช่น
`data.txt` โปรแกรมจะค้นหาโดยอ้างอิงจากโฟลเดอร์ที่ใช้รันโปรแกรม

---

## สร้างกลุ่มทั้งสามแบบ

ในแต่ละบรรทัด โค้ดแยกข้อมูลเป็น `student_id` และ `subject` แล้วสร้าง key
สำหรับการจัดกลุ่ม

```python
year = student_id[:2]
faculty = student_id[-2:]
```

-   `student_id[:2]` คือเลขสองตัวแรก ใช้จัดกลุ่มตามปีเข้า
-   `student_id[-2:]` คือเลขสองตัวท้าย ใช้จัดกลุ่มตามคณะ
-   `subject` ใช้จัดกลุ่มตามรหัสวิชาโดยตรง

โปรแกรมสร้าง dictionary ทั้งสามชุดในรอบเดียว แม้สุดท้ายจะแสดงเพียงชุดที่ผู้ใช้
เลือก หลักการเพิ่มข้อมูลเหมือนกันทุกชุด คือสร้างลิสต์เมื่อพบกลุ่มครั้งแรก แล้ว
`append()` รหัสนิสิตลงในกลุ่มนั้น

---

## รักษาลำดับจากไฟล์

โจทย์กำหนดให้ทั้งลำดับของกลุ่มและลำดับสมาชิกตรงกับลำดับที่พบในไฟล์
dictionary ของ Python จะจำลำดับการเพิ่ม key ดังนั้นการวนด้วย `.items()`
จะแสดงกลุ่มตามการปรากฏครั้งแรก ส่วนลิสต์ของแต่ละกลุ่มเก็บรหัสตามลำดับที่
`append()` เข้ามา

หากรหัสนิสิตคนเดิมปรากฏหลายบรรทัด เช่น ลงทะเบียนหลายวิชา โค้ดจะเก็บและ
แสดงรหัสนั้นซ้ำตามข้อมูลจริง ไม่ได้ตัดค่าซ้ำออก

ตัวอย่างข้อมูลสามบรรทัดข้างต้น เมื่อจัดตามสองหลักแรก จะได้กลุ่ม `65` ก่อน
กลุ่ม `66` และในกลุ่ม `66` จะมี `6631111121` สองครั้งตามสองรายการในไฟล์

---

## เลือกและแสดงผลกลุ่ม

หลังอ่านไฟล์ครบแล้ว `display_type` กำหนด dictionary ที่นำมาแสดง

| `display_type` | วิธีจัดกลุ่ม |
| :---: | :--- |
| `1` | รหัสนิสิตสองตัวแรก |
| `2` | รหัสนิสิตสองตัวท้าย |
| `3` | รหัสวิชา |

หนึ่งกลุ่มแสดงเป็นหนึ่งบรรทัด โดยเชื่อมรหัสในลิสต์ด้วยช่องว่าง

```python
print(" ".join(student_ids))
```

ผลลัพธ์ไม่แสดง key ของกลุ่ม แสดงเฉพาะรหัสนิสิตในกลุ่มนั้น

---

## ข้อควรระวังเกี่ยวกับไฟล์ตัวอย่าง

คำสั่งนี้ต้องแยกได้ **สองค่าเท่านั้น** ในทุกบรรทัด

```python
student_id, subject = line.strip().split()
```

> [!WARNING]
>
> ไฟล์ `src/data.txt` ที่อยู่ในโฟลเดอร์โจทย์ปัจจุบันมีหลายคู่ข้อมูลรวมอยู่ใน
> บรรทัดแรก จึงไม่ตรงกับรูปแบบใน PDF และจะเกิด `ValueError` เพราะมีค่ามากกว่า
> สองค่าให้แยก เมื่อใช้กับ Solution โดยตรง การทดสอบควรใช้ไฟล์ตามข้อกำหนด คือ
> หนึ่งคู่ `student_id subject` ต่อหนึ่งบรรทัด โดยไม่แก้ตรรกะของ Solution

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_3_Q5_C1.py
# Problem   : Student Grouping
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Initialize dictionaries to store student IDs by year, faculty, and subject
students_in_year = {}
students_in_faculty = {}
students_in_subject = {}

# Input the filename and display type
data = input().strip().split()
filename = data[0].strip()
display_type = int(data[1])

# Read the file and store student IDs in the respective dictionaries
with open(filename) as file:
    # Read each line in the file
    for line in file:
        # Extract student ID, subject, year and faculty from the line
        student_id, subject = line.strip().split()
        year = student_id[:2]
        faculty = student_id[-2:]

        # Add student ID grouped on year to the dictionaries
        if year not in students_in_year:
            students_in_year[year] = []
        students_in_year[year].append(student_id)

        # Add student ID grouped on faculty to the dictionaries
        if faculty not in students_in_faculty:
            students_in_faculty[faculty] = []
        students_in_faculty[faculty].append(student_id)

        # Add student ID grouped on subject to the dictionaries
        if subject not in students_in_subject:
            students_in_subject[subject] = []
        students_in_subject[subject].append(student_id)

# Output the student IDs grouped by year in input order
if display_type == 1:
    for _, student_ids in students_in_year.items():
        print(" ".join(student_ids))

# Output the student IDs grouped by faculty in input order
elif display_type == 2:
    for _, student_ids in students_in_faculty.items():
        print(" ".join(student_ids))

# Output the student IDs grouped by subject in input order
elif display_type == 3:
    for _, student_ids in students_in_subject.items():
        print(" ".join(student_ids))
```
