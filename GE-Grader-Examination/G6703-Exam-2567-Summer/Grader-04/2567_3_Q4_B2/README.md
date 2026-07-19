<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Student Ranking ★★☆ (
      <a href="https://drive.google.com/file/d/1ElOABGMUZv3X8ulf4nfeIjL0qHpD0mnp/view?usp=sharing">
        <code>2567_3_Q4_B2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ภาพรวมของฟังก์ชัน**](#ภาพรวมของฟังก์ชัน)
-   [**การคำนวณคะแนนเฉลี่ย**](#การคำนวณคะแนนเฉลี่ย)
-   [**การแปลงคะแนนเป็นเกรด**](#การแปลงคะแนนเป็นเกรด)
-   [**การประมวลผลนักเรียนหนึ่งคน**](#การประมวลผลนักเรียนหนึ่งคน)
-   [**การจัดอันดับนักเรียน**](#การจัดอันดับนักเรียน)
-   [**ชุดคำสั่งสำหรับ Grader**](#ชุดคำสั่งสำหรับ-grader)
-   [**Solution**](#solution)

---

## ภาพรวมของฟังก์ชัน

โจทย์ข้อนี้ไม่ได้รับข้อมูลนักเรียนด้วย `input()` แล้วคำนวณทุกอย่างในครั้งเดียว
แต่ให้เขียนฟังก์ชัน 4 ฟังก์ชันที่รับผิดชอบคนละขั้นตอน

| ฟังก์ชัน | ข้อมูลที่รับ | ผลลัพธ์ |
|---|---|---|
| `calculate_average(scores)` | ลิสต์คะแนน | คืนคะแนนเฉลี่ยเป็นจำนวนจริง |
| `get_grade(score)` | คะแนนเฉลี่ย | คืนเกรดเป็นสตริง |
| `process_student_data(student_data)` | `[ชื่อ, ลิสต์คะแนน]` | คืน `[ชื่อ, เกรด]` |
| `print_students_ranked_by_grades(list_of_student_data)` | ลิสต์ข้อมูลนักเรียน | แสดงชื่อกับเกรดตามอันดับ และไม่คืนค่า |

การแยกเป็นฟังก์ชันทำให้แต่ละขั้นตอนนำผลจากขั้นก่อนหน้าไปใช้ต่อได้ชัดเจน

```text
ลิสต์คะแนน -> คะแนนเฉลี่ย -> เกรด -> จัดกลุ่มและเรียงรายชื่อ
```

---

## การคำนวณคะแนนเฉลี่ย

ฟังก์ชัน `calculate_average(scores)` ใช้สูตรค่าเฉลี่ย

$$
\text{average} = \frac{\sum_{i=1}^{n}\text{score}_i}{n}
$$

ใน Python ผลรวมคือ `sum(scores)` และจำนวนคะแนนคือ `len(scores)`
จึงเขียนเป็น `sum(scores) / len(scores)` ตัวอย่างเช่น

```python
calculate_average([70, 72, 92, 85])
```

ได้ผลรวม `319` หารด้วย `4` จึงคืน `79.75` เครื่องหมาย `/`
ทำให้ผลลัพธ์เป็น `float` แม้ค่าเฉลี่ยจะลงตัว เช่น `[0, 0, 0, 0]` คืน `0.0`

ก่อนหาร โปรแกรมตรวจกรณีลิสต์ว่าง ถ้า `len(scores) == 0` จะคืน `0.0`
ทันที เพื่อหลีกเลี่ยงการหารด้วยศูนย์ แม้ข้อมูลตามโจทย์ปกติจะมีคะแนนสอบ 4 ครั้ง

---

## การแปลงคะแนนเป็นเกรด

ฟังก์ชัน `get_grade(score)` วนดูช่วงคะแนนใน `GRADE_CRITERIA`
แต่ละช่วงเก็บเป็น `[low, high]` และตรวจด้วย

```python
low <= score < high
```

ขอบล่างจึงรวมอยู่ในช่วง แต่ขอบบนไม่รวมอยู่ในช่วง เช่น `75.0` เป็น `B+`
ขณะที่ค่าที่ต่ำกว่า `75.0` จะไปอยู่ช่วง `B`

ช่วงคะแนนที่โค้ดใช้จริงคือ

| เงื่อนไขในโค้ด | เกรด |
|---|:---:|
| `80.0 <= score < 100.0` | `A` |
| `75.0 <= score < 80.0` | `B+` |
| `70.0 <= score < 75.0` | `B` |
| `65.0 <= score < 70.0` | `C+` |
| `60.0 <= score < 65.0` | `C` |
| `55.0 <= score < 60.0` | `D+` |
| `50.0 <= score < 55.0` | `D` |
| `0.0 <= score < 50.0` | `F` |

เมื่อพบช่วงที่ตรงกัน ฟังก์ชันจะ `return grade` ทันที ถ้าไม่ตรงกับช่วงใดเลย
จะมาถึง `return "F"` หลังลูป

> [!WARNING]
>
> PDF ระบุว่าคะแนนตั้งแต่ `80` ขึ้นไปได้ `A` ดังนั้นคะแนน `100.0`
> ควรได้ `A` ตามโจทย์ แต่ช่วง `A` ใน Solution คือ `[80.0, 100.0)`
> เพราะใช้ `< high` คะแนน `100.0` จึงไม่เข้าช่วงใดและโค้ดคืน `F`
> คำอธิบายนี้ชี้ให้เห็นพฤติกรรมจริงของโค้ด โดยยังคง Solution เดิมไว้

---

## การประมวลผลนักเรียนหนึ่งคน

ข้อมูลนักเรียนหนึ่งคนมีรูปแบบ `[name, scores]` เช่น

```python
["Nana", [70, 72, 92, 85]]
```

ฟังก์ชัน `process_student_data(student_data)` ทำงานตามลำดับดังนี้

1. อ่านชื่อจาก `student_data[0]`
2. อ่านลิสต์คะแนนจาก `student_data[1]`
3. ส่งคะแนนให้ `calculate_average()`
4. ส่งค่าเฉลี่ยต่อให้ `get_grade()`
5. คืนลิสต์ `[name, grade]`

คะแนนของ Nana มีค่าเฉลี่ย `79.75` ซึ่งอยู่ในช่วง `B+`
ฟังก์ชันจึงคืน `["Nana", "B+"]`

---

## การจัดอันดับนักเรียน

ฟังก์ชัน `print_students_ranked_by_grades()` ต้องจัดอันดับด้วยเกรดก่อน
และใช้ลำดับพจนานุกรมของชื่อเมื่อนักเรียนได้เกรดเท่ากัน

โปรแกรมสร้าง `grade_to_students` เพื่อจับคู่เกรดกับลิสต์รายชื่อ เช่น

```python
{
    "A": ["Malee", "Lisa"],
    "B+": ["Nana"],
    "B": ["Usa"],
}
```

จากนั้นวนเกรดตาม `GRADE_ORDER`

```python
["A", "B+", "B", "C+", "C", "D+", "D", "F"]
```

จึงได้เกรดสูงก่อนเสมอ สำหรับรายชื่อในเกรดเดียวกัน `sorted()` จะเรียงตาม
พจนานุกรมก่อนแสดงด้วย `print(student, grade)` ตัวอย่างข้างต้นจึงแสดง

```text
Lisa A
Malee A
Nana B+
Usa B
```

ฟังก์ชันนี้มีหน้าที่แสดงผลโดยตรงและไม่มีคำสั่ง `return`
ดังนั้นค่าที่คืนโดยปริยายคือ `None`

---

## ชุดคำสั่งสำหรับ Grader

ส่วนท้ายของโปรแกรมเป็นชุดคำสั่งสำหรับระบบตรวจคำตอบ ไม่ใช่การอ่านข้อมูลนักเรียน
ตามรูปแบบปกติ โปรแกรมอ่านคำสั่ง Python ทีละบรรทัดเก็บใน `cmd` แล้วใช้
`exec(cmd)` ให้คำสั่งนั้นทำงาน เช่น

```text
print(calculate_average([70, 72, 92, 85]));
```

คำสั่งแต่ละบรรทัดทำงานในโปรแกรมเดียวกัน ตัวแปรที่สร้างไว้ในบรรทัดก่อน
จึงนำมาใช้ในบรรทัดถัดไปได้ บรรทัดที่ลงท้ายด้วย `;` จะยังถูก `exec()` ก่อน
แล้วจึงทำให้ลูปหยุด ส่วนบรรทัดว่างทำให้เงื่อนไข `while` เป็นเท็จและหยุดเช่นกัน

> [!WARNING]
>
> `exec()` สามารถรันข้อความเป็นคำสั่ง Python ได้ทุกชนิด รูปแบบนี้เหมาะกับ
> grader ที่ส่งคำสั่งทดสอบซึ่งเชื่อถือได้เท่านั้น ห้ามนำไปใช้กับข้อความจากผู้ใช้
> หรือแหล่งข้อมูลที่ไม่น่าเชื่อถือ เพราะอาจสั่งอ่าน แก้ไข หรือลบข้อมูลได้

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_3_Q4_B2.py
# Problem   : Student Ranking
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Constants for grade criteria and order
GRADE_ORDER = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
GRADE_CRITERIA = {
    "A": [80.0, 100.0],
    "B+": [75.0, 80.0],
    "B": [70.0, 75.0],
    "C+": [65.0, 70.0],
    "C": [60.0, 65.0],
    "D+": [55.0, 60.0],
    "D": [50.0, 55.0],
    "F": [0.0, 50.0],
}


# Function to calculate the average score from a list of scores
def calculate_average(scores):
    # If the list is empty, return 0.0
    if len(scores) == 0:
        return 0.0

    # Calculate and return the average score
    return sum(scores) / len(scores)


# Function to determine the grade based on the score
def get_grade(score):
    # Check the score against the grade criteria and return the corresponding grade
    for grade, [low, high] in GRADE_CRITERIA.items():
        if low <= score < high:
            return grade
    # If the score does not match any criteria, return "F"
    return "F"


# Function to process student data and return their name and grade
def process_student_data(student_data):
    # Extract the student's name and calculate their grade from their scores
    name = student_data[0]
    grade = get_grade(calculate_average(student_data[1]))
    # Return the name and grade as a list
    return [name, grade]


# Function to print students ranked by their grades
def print_students_ranked_by_grades(list_of_student_data):
    # Initialize a dictionary to map grades to student names
    grade_to_students = {}

    # Process each student's data
    for student in list_of_student_data:
        # Get the student's name and grade
        name, grade = process_student_data(student)

        # Store the student's name in the dictionary under their grade
        if grade not in grade_to_students:
            grade_to_students[grade] = []
        grade_to_students[grade].append(name)

    # Print the students sorted by grade in the defined order
    for grade in GRADE_ORDER:
        # Check if there are students for the current grade
        if grade in grade_to_students:
            # Sort the students' names alphabetically and print them with their grade
            for student in sorted(grade_to_students[grade]):
                print(student, grade)


# Run the input string as code until it ends with a semicolon
while cmd := input().strip():
    exec(cmd)
    if cmd[-1] == ";":
        break
```
