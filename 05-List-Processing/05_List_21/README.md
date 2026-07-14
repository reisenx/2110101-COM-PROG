<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Upgrade ★★ (
      <a href="https://drive.google.com/file/d/1bbLkJUrzqhrarNl3i0tO6SXG9Bkx2cmt/view?usp=drive_link">
        <code>05_List_21</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การแทนเกรดด้วยลำดับ**](#การแทนเกรดด้วยลำดับ)
-   [**การรับและจัดเก็บข้อมูล**](#การรับและจัดเก็บข้อมูล)
-   [**การปรับเกรด**](#การปรับเกรด)
-   [**การแสดงผล**](#การแสดงผล)
-   [**Solution**](#solution)

---

## การแทนเกรดด้วยลำดับ

เกรดในโจทย์เรียงจากดีที่สุดไปแย่ที่สุดดังนี้

```python
GRADES = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
```

ตำแหน่งหรือ index ของเกรดจึงบอกระดับของเกรดได้โดยตรง เช่น `"A"`
อยู่ที่ index `0`, `"B"` อยู่ที่ index `2` และ `"F"` อยู่ที่ index `7`
การปรับเกรดขึ้นหนึ่งระดับจึงเท่ากับการลด index ลง `1`

ตัวอย่างเช่น `GRADES.index("B")` ได้ `2` เมื่อลดเหลือ `1`
แล้วนำกลับไปอ่านด้วย `GRADES[1]` จะได้ `"B+"`

## การรับและจัดเก็บข้อมูล

ข้อมูลส่วนแรกมีรหัสนักเรียนและเกรดบรรทัดละหนึ่งคน โปรแกรมอ่านไปเรื่อย ๆ
จนพบบรรทัด `q` โดย `strip()` ช่วยตัดช่องว่างที่หัวและท้ายบรรทัดก่อนตรวจ
sentinel นี้

แต่ละบรรทัดถูกแยกเป็น `student_id` และ `grade` แล้วเก็บเป็นลิสต์ย่อย
`[รหัสนักเรียน, index ของเกรด]` เช่น

```python
["55555", 2]  # รหัส 55555 ได้เกรด B
```

ดังนั้น `students` เป็น nested list ที่รวมรหัสและเกรดของคนเดียวกันไว้ใน record
เดียว วิธีนี้ต่างจากข้อแนะนำใน PDF ที่เสนอให้ใช้ลิสต์ `ids` และ `grades`
แยกกัน แต่ยังเก็บความสัมพันธ์ของข้อมูลและให้ผลลัพธ์เดียวกัน

หลังจากอ่าน `q` แล้ว บรรทัดถัดไปจะถูกแยกด้วย `split()` เป็น `upgrade_ids`
ซึ่งเป็นรายการรหัสของผู้ที่ต้องปรับเกรด หากบรรทัดนี้ว่างจะได้ลิสต์ว่าง
และไม่มีใครถูกปรับเกรด

## การปรับเกรด

โปรแกรมวนผ่านนักเรียนทุกคน แล้วตรวจสมาชิกด้วย
`student_id in upgrade_ids` หากพบรหัสจึงคำนวณ index ใหม่จาก

$$
\text{new index} = \max(\text{old index} - 1, 0)
$$

ซึ่งตรงกับ Python ว่า `max(grade - 1, 0)` การใช้ `0` เป็นขอบล่างทำให้คนที่
ได้ `A` อยู่แล้ว ยังคงได้ `A` และไม่เกิด index `-1` ซึ่งจะชี้ไปที่ `F`

คำสั่ง `students[i][1] = ...` แก้เกรดใน nested list เดิมทันที
จึงไม่ต้องสร้างรายการผลลัพธ์อีกชุด

-   รหัสที่ไม่มีใน `students` จะไม่มีผลใด ๆ
-   รหัสที่ซ้ำใน `upgrade_ids` ยังปรับเพียงหนึ่งระดับ เพราะเงื่อนไขตรวจเพียงว่า
    รหัสนั้นมีอยู่หรือไม่
-   ถ้ามี record รหัสเดียวกันหลาย record ทุก record นั้นจะถูกปรับหนึ่งระดับ
    เพราะโปรแกรมวนตรวจนักเรียนทุกคน

## การแสดงผล

ลูปสุดท้ายอ่าน `students` ตามลำดับเดิมที่รับเข้ามา และแปลง index กลับเป็น
ชื่อเกรดด้วย `GRADES[grade]`

```python
for student_id, grade in students:
    print(student_id, GRADES[grade])
```

`print()` คั่นรหัสกับเกรดด้วยช่องว่างหนึ่งช่องโดยอัตโนมัติ และแสดงนักเรียน
คนละบรรทัด ลำดับผลลัพธ์จึงตรงกับลำดับข้อมูลนำเข้าตามที่โจทย์กำหนด

---

# Solution

```python
# --------------------------------------------------
# File Name : 05_List_21.py
# Problem   : Upgrade
# Author    : Worralop Srichainont
# Date      : 2025-06-11
# --------------------------------------------------

# List of letter grades
GRADES = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]

# Input student information
students = []
while True:
    student = input().strip()
    # Stop if input is 'q'
    if student == "q":
        break
    # Add student information to the list
    # Convert grade to index
    student_id, grade = student.split()
    students.append([student_id, GRADES.index(grade)])

# Upgrade student grades
upgrade_ids = input().split()
for i in range(len(students)):
    # Extract information from the list
    student_id, grade = students[i]

    # Check if the student ID is in the upgrade list
    if student_id in upgrade_ids:
        # Upgrade the grade of that student
        students[i][1] = max(grade - 1, 0)

# Output the upgraded grades
for student_id, grade in students:
    print(student_id, GRADES[grade])
```
