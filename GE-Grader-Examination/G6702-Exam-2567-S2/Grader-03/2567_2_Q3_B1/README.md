<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Graduation Ceremony ★★ (
      <a href="https://drive.google.com/file/d/1KceParo05PeXgSq9s0pC8BPWIEBHC6El/view?usp=sharing">
        <code>2567_2_Q3_B1</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ข้อมูลที่ต้องเก็บและเงื่อนไข**](#ข้อมูลที่ต้องเก็บและเงื่อนไข)
-   [**เปรียบเทียบลำดับเกรด**](#เปรียบเทียบลำดับเกรด)
-   [**แบ่งกลุ่มนิสิต**](#แบ่งกลุ่มนิสิต)
-   [**เรียงลำดับและแสดงผล**](#เรียงลำดับและแสดงผล)
-   [**Solution**](#solution)

---

## ข้อมูลที่ต้องเก็บและเงื่อนไข

โปรแกรมรับข้อมูลนิสิตทีละบรรทัด แต่ละบรรทัดมีข้อมูล 5 ค่า ได้แก่

1. รหัสนิสิต
2. เกรดเฉลี่ยสะสม (`gpax`)
3. เกรดต่ำสุดที่เคยได้
4. เคยได้ `U` หรือไม่ (`Y` หรือ `N`)
5. จำนวนปีที่ใช้เรียนจบ

เมื่ออ่านบรรทัดที่เป็น `-1` จะหยุดรับข้อมูล แล้วจึงเรียงและแสดงผลทุกกลุ่ม

ค่าคงที่สำคัญในโปรแกรมตรงกับเงื่อนไขของโจทย์ดังนี้

```python
FIRST_HONOR_GPAX = 3.60
SECOND_HONOR_GPAX = 3.25
MAX_YEARS_HONOR = 4.0
```

ดังนั้น ผู้ที่จะได้เกียรตินิยมต้องมี `gpax` ตั้งแต่ `3.25` ขึ้นไป
เรียนจบไม่เกิน `4.0` ปี ไม่เคยได้เกรดต่ำกว่า `C` และไม่เคยได้ `U`

> [!NOTE]
>
> ในโค้ดใช้ชื่อตัวแปร `has_withdrawn` และมี comment กล่าวถึงการถอนรายวิชา
> แต่ข้อมูลช่องนี้ตามโจทย์หมายถึง **เคยได้ `U` หรือไม่** โดยนิพจน์
> `data[3].strip() == "Y"` จะได้ `True` เมื่อนิสิตเคยได้ `U`

---

## เปรียบเทียบลำดับเกรด

ข้อความเกรดนำมาเปรียบเทียบมากหรือน้อยโดยตรงได้ไม่สะดวก โปรแกรมจึงสร้างลิสต์
ที่เรียงเกรดจากต่ำไปสูงก่อน

```python
GRADE_ORDER = ["F", "D", "D+", "C", "C+", "B", "B+", "A"]
MINIMUM_HONOR_GRADE = GRADE_ORDER.index("C")
```

`GRADE_ORDER.index(grade)` เปลี่ยนเกรดเป็นตำแหน่งในลิสต์ เช่น `F` ได้ `0`,
`C` ได้ `3` และ `A` ได้ `7` จึงตรวจว่าเกรดต่ำกว่า `C` ได้ด้วย

```python
minimum_grade < MINIMUM_HONOR_GRADE
```

ถ้าเงื่อนไขนี้เป็นจริง แสดงว่าเคยได้ `F`, `D` หรือ `D+`
จึงไม่มีสิทธิ์ได้เกียรตินิยม ส่วนเกรด `C` พอดียังผ่านเงื่อนไขนี้

---

## แบ่งกลุ่มนิสิต

ฟังก์ชัน `process_student_info()` ตรวจเงื่อนไขตามลำดับ โดยให้นิสิตอยู่ใน
กลุ่ม `General` ทันทีเมื่อมีอย่างน้อยหนึ่งกรณีต่อไปนี้

```python
has_withdrawn
study_years > MAX_YEARS_HONOR
minimum_grade < MINIMUM_HONOR_GRADE
gpax < SECOND_HONOR_GPAX
```

หากไม่เข้าเงื่อนไขข้างต้น จึงแบ่งตาม `gpax`

-   `gpax >= 3.60` เป็นเกียรตินิยมอันดับ 1
-   `3.25 <= gpax < 3.60` เป็นเกียรตินิยมอันดับ 2

การใช้ `if` ตามด้วย `elif` ทำให้นิสิตแต่ละคนถูกเพิ่มลงเพียงกลุ่มเดียว
ค่าขอบเขตสำคัญคือ `3.60` อยู่กลุ่มอันดับ 1, `3.25` อยู่กลุ่มอันดับ 2,
และเรียน `4.0` ปียังมีสิทธิ์ แต่ถ้ามากกว่า `4.0` ปีจะเป็น `General`

---

## เรียงลำดับและแสดงผล

กลุ่มเกียรตินิยมเก็บข้อมูลเป็น `[-gpax, student_id]` เช่น GPAX `3.80`
จะเก็บเป็น `[-3.80, student_id]` เมื่อนำไปใช้กับ `sorted()` ซึ่งเรียงจากน้อยไปมาก
ค่า `-3.80` จะมาก่อน `-3.60` จึงเท่ากับเรียง GPAX จากมากไปน้อย

ถ้า GPAX เท่ากัน `sorted()` จะเปรียบเทียบสมาชิกตัวถัดไป คือ `student_id`
ทำให้รหัสเรียงจากน้อยไปมาก ส่วนกลุ่ม `General` เก็บเฉพาะรหัสแล้วเรียงโดยตรง

> [!NOTE]
>
> โค้ดเก็บรหัสนิสิตเป็น `str` จึงเปรียบเทียบรหัสจากตัวอักษรซ้ายไปขวา
> สำหรับรหัสที่มีจำนวนหลักเท่ากัน ผลจะตรงกับการเรียงตัวเลขจากน้อยไปมาก

ฟังก์ชัน `display_students()` แสดงกลุ่มตามลำดับ `1`, `2`, `General`
และจะแสดงชื่อกลุ่มเฉพาะเมื่อมีสมาชิกเท่านั้น ดังนั้นหากไม่มีผู้ได้เกียรตินิยมอันดับ 2
จะไม่มีทั้งบรรทัด `2` และรายชื่อของกลุ่มนั้น

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_2_Q3_B1.py
# Problem   : Graduation Ceremony
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------

# Constants for GPAX thresholds
FIRST_HONOR_GPAX = 3.60
SECOND_HONOR_GPAX = 3.25

# Constants for grade order and minimum honor grade
GRADE_ORDER = ["F", "D", "D+", "C", "C+", "B", "B+", "A"]
MINIMUM_HONOR_GRADE = GRADE_ORDER.index("C")

# Constants for maximum years to qualify for honors
MAX_YEARS_HONOR = 4.0

# Initialize lists to store student info based on their honors status
first_honor_students = []
second_honor_students = []
general_students = []


# Function to process each student's information
def process_student_info(line):
    # Extract student data from the input line
    data = line.strip().split()
    student_id = data[0].strip()
    gpax = float(data[1].strip())
    # Convert grade to index in GRADE_ORDER
    minimum_grade = GRADE_ORDER.index(data[2].strip())
    # Check if the student has withdrawn any subject
    has_withdrawn = data[3].strip() == "Y"
    study_years = float(data[4].strip())

    # Check if the student qualifies for honors
    if (
        has_withdrawn
        or study_years > MAX_YEARS_HONOR
        or minimum_grade < MINIMUM_HONOR_GRADE
        or gpax < SECOND_HONOR_GPAX
    ):
        general_students.append(student_id)

    # Check if the student qualifies for first honors
    elif gpax >= FIRST_HONOR_GPAX:
        # Add the student to first honors list with negative GPAX for sorting
        first_honor_students.append([-gpax, student_id])

    # Check if the student qualifies for second honors
    elif gpax >= SECOND_HONOR_GPAX:
        # Add the student to second honors list with negative GPAX for sorting
        second_honor_students.append([-gpax, student_id])


def display_students():
    # Check if there are any first honor students
    if len(first_honor_students) > 0:
        print(1)
        # Output student IDs sorted by GPAX in descending order
        for _, student_id in sorted(first_honor_students):
            print(student_id)

    # Check if there are any second honor students
    if len(second_honor_students) > 0:
        print(2)
        # Output student IDs sorted by GPAX in descending order
        for _, student_id in sorted(second_honor_students):
            print(student_id)

    # Check if there are any general students
    if len(general_students) > 0:
        print("General")
        # Output student IDs sorted in ascending order
        for student_id in sorted(general_students):
            print(student_id)


# Main function
def main():
    # Input student information until "-1" is encountered
    while True:
        line = input().strip()
        if line == "-1":
            break
        process_student_info(line)
    # Display the categorized students
    display_students()


# Run the main function
main()
```
