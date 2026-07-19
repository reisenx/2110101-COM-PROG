<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Students in Course ★★ (
      <a href="https://drive.google.com/file/d/1RaqjKrdRqYq1Q_4bk1QxuT5OdIz_muvG/view?usp=sharing">
        <code>2567_1_Q3_C2-S</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**โครงสร้างข้อมูลแบบพจนานุกรมซ้อนกัน**](#โครงสร้างข้อมูลแบบพจนานุกรมซ้อนกัน)
-   [**การบันทึกข้อมูลการลงทะเบียน**](#การบันทึกข้อมูลการลงทะเบียน)
-   [**การตอบคำถามแต่ละวิชา**](#การตอบคำถามแต่ละวิชา)
-   [**เงื่อนไขเกี่ยวกับข้อมูลซ้ำ**](#เงื่อนไขเกี่ยวกับข้อมูลซ้ำ)
-   [**Solution**](#solution)

---

## โครงสร้างข้อมูลแบบพจนานุกรมซ้อนกัน

โจทย์ต้องนับนิสิตแยกทั้งตาม **รหัสวิชา** และ **ปีการศึกษาแรกเข้า**
จึงเหมาะกับ dictionary สองชั้นที่มีรูปแบบ

```text
รหัสวิชา -> ปีแรกเข้า -> จำนวนนิสิต
```

ตัวอย่างข้อมูลอาจมีหน้าตาเช่น

```python
{
    "2110101": {"2566": 1, "2567": 2},
    "2110102": {"2567": 4},
}
```

รหัสนิสิตและรหัสวิชาถูกเก็บเป็น `str` เพราะไม่ต้องนำไปคำนวณทางคณิตศาสตร์

---

## การบันทึกข้อมูลการลงทะเบียน

สองหลักแรกของรหัสนิสิตคือสองหลักท้ายของปีแรกเข้า
โปรแกรมจึงเติม `"25"` ข้างหน้า

```python
academic_year = f"25{student_id[:2]}"
```

เช่น `student_id` ที่ขึ้นต้นด้วย `67` จะได้ปี `2567`

สำหรับแต่ละวิชา โปรแกรมสร้าง dictionary ของวิชาและปีเมื่อพบเป็นครั้งแรก
จากนั้นเพิ่มตัวนับของคู่นั้นหนึ่งครั้ง

```python
subjects_registration[subject][academic_year] += 1
```

จึงไม่จำเป็นต้องวนค้นหารายชื่อนิสิตทั้งหมดใหม่ทุกครั้งที่มีคำถาม

---

## การตอบคำถามแต่ละวิชา

รหัสวิชาในบรรทัดสุดท้ายถูกวนตามลำดับเดิม ทำให้บรรทัดผลลัพธ์เรียงตรงกับ
ลำดับคำถาม ไม่ใช่เรียงรหัสวิชาใหม่

ถ้าพบวิชา โปรแกรมใช้

```python
sorted(subjects_registration[subject].items())
```

เพื่อเรียงปีจากน้อยไปมาก การเรียงข้อความปีสี่หลักให้ผลเหมือนการเรียงตัวเลข
จากนั้นจัดแต่ละคู่เป็น `ปี:จำนวน` และเชื่อมด้วย `", "`

ถ้าไม่มีรหัสวิชานั้นในข้อมูลเลย จะแสดง

```text
รหัสวิชา None
```

---

## เงื่อนไขเกี่ยวกับข้อมูลซ้ำ

> [!NOTE]
>
> ข้อกำหนดระบุว่ารหัสวิชาของนิสิตหนึ่งคนไม่ซ้ำกัน
> แต่ข้อความตัวอย่างใน PDF มีบรรทัดหนึ่งที่เขียน `2110105` ซ้ำ
> โค้ดนับทุก token ที่ได้รับ ดังนั้นถ้าป้อนข้อมูลซ้ำซึ่งอยู่นอกเงื่อนไข
> จะนับวิชานั้นซ้ำสองครั้ง โปรแกรมไม่ได้แปลงรายการวิชาเป็น `set`

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q3_C2-S.py
# Problem   : Students in Course
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Initialize a dictionary to store subjects and their registration information
subjects_registration = {}

# Input the number of students
n = int(input())

# Input student student registration data
for _ in range(n):
    # Extract student ID and subjects they are registered for from input
    data = input().strip().split()
    student_id = data[0].strip()
    subjects = data[1:]

    # Concatenate the digits from the student ID with '25' to form the academic year
    academic_year = f"25{student_id[:2]}"

    # Update each subject to the dictionary
    for subject in subjects:
        # Initialize the subject in the dictionary if not already exists
        if subject not in subjects_registration:
            subjects_registration[subject] = {}

        # Initialize the academic year in the subject's dictionary if not already exists
        if academic_year not in subjects_registration[subject]:
            subjects_registration[subject][academic_year] = 0
        # Increment the count of the current academic year for the current subject
        subjects_registration[subject][academic_year] += 1

# Input query subjects
query_subjects = input().strip().split()

# Iterate through each query subject
for subject in query_subjects:
    # Check if the subject exists in the registration dictionary
    if subject in subjects_registration:
        # Initialize a list to store the years and their counts
        year_enrolled = []

        # Sort the years and format them with their counts
        for year, count in sorted(subjects_registration[subject].items()):
            year_enrolled.append(f"{year}:{count}")

        # Output the subject with the years and their counts
        print(f"{subject} {', '.join(year_enrolled)}")

    # If the subject does not exist, print the subject with 'None'
    else:
        print(f"{subject} None")
```
