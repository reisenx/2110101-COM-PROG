<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Upgrade 2 ★★ (
      <a href="https://drive.google.com/file/d/17bzTOp0JyiwwKGzB0KJzAgcDDvdY1g52/view?usp=drive_link">
        <code>05_List_22</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเก็บระดับเกรดและข้อมูลนักเรียน**](#การเก็บระดับเกรดและข้อมูลนักเรียน)
-   [**การปรับเกรด**](#การปรับเกรด)
-   [**การเรียงตามรหัสนักเรียน**](#การเรียงตามรหัสนักเรียน)
-   [**การแสดงผล**](#การแสดงผล)
-   [**Solution**](#solution)

---

## การเก็บระดับเกรดและข้อมูลนักเรียน

โจทย์นี้ต้องปรับเกรดเหมือนโจทย์ Upgrade แต่เพิ่มการเรียงผลลัพธ์ตามรหัส
นักเรียน โปรแกรมจึงเริ่มจากเรียงชื่อเกรดจากดีที่สุดไปแย่ที่สุด

```python
GRADES = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
```

เมื่อเก็บเกรดเป็น index ในลิสต์นี้ เกรดที่ดีกว่าจะมี index น้อยกว่า เช่น
`"B"` มี index `2` ส่วน `"B+"` มี index `1`

โปรแกรมอ่านข้อมูลบรรทัดละหนึ่งคนจนพบบรรทัด `q` แล้วเก็บแต่ละคนเป็น
ลิสต์ย่อย `[student_id, grade_index]` ภายใน `students` เช่น

```python
["55555", 2]  # รหัส 55555 และเกรด B
```

การรวมข้อมูลของคนเดียวกันในลิสต์ย่อยทำให้ปรับเกรดและเรียง record ทั้งก้อน
ได้สะดวก หลัง `q` โปรแกรมอ่านรหัสที่จะได้รับการปรับเกรดจากอีกหนึ่งบรรทัด
ด้วย `input().split()`

## การปรับเกรด

โปรแกรมวนดู record ของนักเรียนทุกคน ถ้า `student_id in upgrade_ids`
จะปรับเกรดขึ้นหนึ่งระดับตามสูตร

$$
\text{new index} = \max(\text{old index} - 1, 0)
$$

ซึ่งเขียนใน Python เป็น `max(grade - 1, 0)` และบันทึกกลับที่
`students[i][1]` โดยตรง ค่า `0` ทำหน้าที่เป็นขอบเขต ทำให้ `A` ยังเป็น `A`
แทนที่จะลด index ต่อไปเป็น `-1`

รหัสที่ไม่อยู่ในข้อมูลนักเรียนจะไม่มีผล ส่วนรหัสที่เขียนซ้ำใน
`upgrade_ids` ไม่ได้ทำให้เกรดเลื่อนหลายระดับ เพราะ `in` ให้เพียงผลว่า
“พบ” หรือ “ไม่พบ” หากข้อมูลนักเรียนมีรหัสเดียวกันหลาย record
ทุก record ที่มีรหัสนั้นจะถูกปรับหนึ่งระดับ

## การเรียงตามรหัสนักเรียน

หลังปรับเกรดครบแล้ว โปรแกรมเรียก `students.sort()` ลิสต์ย่อยแต่ละตัวมี
รหัสนักเรียนเป็นสมาชิกตัวแรก Python จึงเปรียบเทียบรหัสก่อน และเรียง
record ทั้งหมดตามรหัสจากน้อยไปมาก

รหัสถูกเก็บเป็น `str` จึงเป็นการเรียงข้อความแบบ lexicographic
สำหรับตัวอย่างในโจทย์ รหัสทุกตัวเป็นตัวเลขและมีจำนวนหลักเท่ากัน
ลำดับนี้จึงตรงกับการเรียงค่าตัวเลข เช่น

```text
"11111" < "33333" < "55555"
```

> [!NOTE]
>
> ถ้ารหัสมีจำนวนหลักไม่เท่ากัน การเรียงสตริงอาจต่างจากการเรียงจำนวน เช่น
> `"10"` จะมาก่อน `"2"` ซึ่งเป็นพฤติกรรมจริงของโค้ดเพราะไม่ได้แปลงรหัส
> เป็นจำนวนเต็มก่อนเรียง

หากรหัสตัวแรกเท่ากัน Python จะใช้สมาชิกถัดไปคือ index ของเกรดช่วยตัดสิน
ลำดับ เพราะ `sort()` เปรียบเทียบสมาชิกของลิสต์ย่อยจากซ้ายไปขวา

## การแสดงผล

ลูปสุดท้ายอ่าน record ที่เรียงแล้ว แปลง index กลับเป็นชื่อเกรดด้วย
`GRADES[grade]` และใช้ `print(student_id, GRADES[grade])`
แสดงรหัสกับเกรดคั่นด้วยช่องว่าง คนละหนึ่งบรรทัด

---

# Solution

```python
# --------------------------------------------------
# File Name : 05_List_22.py
# Problem   : Upgrade 2
# Author    : Worralop Srichainont
# Date      : 2025-06-12
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

# Sort students by id in ascending order
students.sort()

# Output the upgraded grades
for student_id, grade in students:
    print(student_id, GRADES[grade])
```
