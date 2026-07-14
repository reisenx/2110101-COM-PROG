<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Department Selection ★★★ (
      <a href="https://drive.google.com/file/d/1mYbLWSQPXZ6fMd695eUBCXmvSU6TGqNN/view?usp=drive_link">
        <code>10_TSD_37</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเตรียมข้อมูลสำหรับจัดสรร**](#การเตรียมข้อมูลสำหรับจัดสรร)
-   [**การจัดลำดับตามคะแนน**](#การจัดลำดับตามคะแนน)
-   [**การจัดสรรภาควิชาแบบ Greedy**](#การจัดสรรภาควิชาแบบ-greedy)
-   [**การเรียงและแสดงผล**](#การเรียงและแสดงผล)
-   [**ข้อมูล department_ranking**](#ข้อมูล-department_ranking)
-   [**Solution**](#solution)

---

## การเตรียมข้อมูลสำหรับจัดสรร

โปรแกรมอ่านจำนวนที่นั่งของแต่ละภาควิชาเก็บใน dictionary
`department_seats` โดยใช้ชื่อภาควิชาเป็น key และจำนวนที่นั่งคงเหลือเป็น value
เช่น `{"CP": 1, "ME": 2}` ทำให้ตรวจและลดที่นั่งของภาคหนึ่งได้โดยตรง

ข้อมูลนิสิตแต่ละบรรทัดแบ่งเป็น `3` ส่วน คือ

-   `student_id` คือรหัสนิสิต ซึ่งเก็บเป็นข้อความ
-   `score` คือคะแนน ซึ่งแปลงเป็น `float`
-   `preference` คือชื่อภาควิชาที่เหลือ เรียงจากต้องการมากที่สุดไปน้อยที่สุด

โปรแกรมเก็บลำดับภาคที่นิสิตเลือกไว้ใน `student_preference[student_id]`
และเริ่มผลลัพธ์ของทุกคนเป็นข้อความว่างใน `student_to_department`
ส่วน `has_department` ใช้บอกว่านิสิตได้รับภาคแล้วหรือยัง

---

## การจัดลำดับตามคะแนน

โจทย์กำหนดให้นิสิตคะแนนสูงกว่าเลือกก่อน โปรแกรมจึงเก็บทูเพิล
`(score, student_id)` ใน `student_ranking` แล้วสั่ง

```python
student_ranking.sort(reverse=True)
```

การเรียงแบบ `reverse=True` ทำให้คะแนนมากอยู่ข้างหน้า โจทย์รับประกันว่าไม่มี
นิสิตคะแนนเท่ากัน ดังนั้นการตัดสินลำดับจริงจึงขึ้นกับคะแนนเพียงอย่างเดียว

---

## การจัดสรรภาควิชาแบบ Greedy

วิธีแบบ **Greedy** คือ เมื่อถึงคิวของนิสิตคนหนึ่ง ให้เลือกคำตอบที่ดีที่สุด
ซึ่งยังเป็นไปได้ในขณะนั้น แล้วเดินหน้าต่อโดยไม่ย้อนกลับมาเปลี่ยนผลของคนก่อนหน้า

โปรแกรมเดิน `student_ranking` จากคะแนนสูงสุดลงมา สำหรับนิสิตแต่ละคนจะตรวจ
`student_preference[student_id]` จากตัวเลือกอันดับแรกไปหาอันดับท้าย ๆ
ถ้าภาควิชานั้นยังมีที่นั่งและนิสิตยังไม่ได้รับภาค

```python
department_seats[department] > 0 and not has_department[student_id]
```

ก็จะทำงาน `3` อย่างทันที

1. บันทึกภาคลงใน `student_to_department[student_id]`
2. เปลี่ยน `has_department[student_id]` เป็น `True`
3. ลดที่นั่งด้วย `department_seats[department] -= 1` แล้ว `break`

ดังนั้นถ้าอันดับ `1` เต็ม โปรแกรมจะลองอันดับ `2`, `3` และ `4` ตามลำดับ
ตัวอย่างเช่น ผู้สมัครเลือก `PE ME CP MT` แต่ `PE` และ `ME` เต็ม จะได้รับ `CP`
ถ้า `CP` ยังมีที่ว่าง

ลำดับความชอบอาจมีชื่อภาคซ้ำกันได้ ดังตัวอย่างโจทย์ที่มี `CHE CP ME CP`
โค้ดจะตรวจค่าซ้ำตามตำแหน่งที่ปรากฏ หากภาคนั้นเต็มก็อาจตรวจซ้ำอีกครั้ง
แต่ถ้ามีที่ว่างจะจัดสรรตั้งแต่ครั้งแรก ลดที่นั่งเพียงหนึ่งที่ และออกจากลูปทันที

โจทย์รับประกันว่านิสิตทุกคนจะได้รับภาควิชา จึงไม่เหลือค่า
`student_to_department[student_id]` เป็นข้อความว่างตอนแสดงผล

---

## การเรียงและแสดงผล

การจัดสรรต้องทำตามลำดับคะแนน แต่การแสดงผลต้องเรียงตามรหัสนิสิต โปรแกรมจึงใช้

```python
sorted(student_to_department.items())
```

แต่ละ item เป็น `(student_id, department)` การเรียงจึงเริ่มจาก
`student_id` ซึ่งเก็บเป็นข้อความ แล้วพิมพ์ในรูป `รหัสนิสิต ภาควิชา`
คนละหนึ่งบรรทัด

---

## ข้อมูล department_ranking

ระหว่างอ่านข้อมูล โค้ดสร้าง `department_ranking` เพื่อรวบรวม `(score, student_id)`
ของผู้ที่เลือกแต่ละภาค และยังเรียงแต่ละลิสต์จากคะแนนสูงไปต่ำด้วย

อย่างไรก็ตาม หลังจากเรียงแล้วโปรแกรม **ไม่ได้อ่าน `department_ranking`
อีกเลย** ข้อมูลนี้จึงไม่มีผลต่อการจัดสรร ผลลัพธ์จริงเกิดจากการเดิน
`student_ranking` และตรวจ `student_preference` กับ `department_seats` เท่านั้น

---

# Solution

```python
# --------------------------------------------------
# File Name : 10_TSD_37.py
# Problem   : Department Selection
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input departments and their seats
n = int(input())
department_seats = {}
for _ in range(n):
    department, seats = input().strip().split()
    department_seats[department] = int(seats)

# Input students score and their department rankings preference
n = int(input())
student_to_department = {}
student_ranking = []
student_preference = {}
department_ranking = {}
has_department = {}
for _ in range(n):
    # Input student ID, score, and department
    data = input().strip().split()
    student_id = data[0]
    score = float(data[1])
    preference = data[2:]

    # Update student information
    student_to_department[student_id] = ""
    has_department[student_id] = False
    student_preference[student_id] = preference
    student_ranking.append((score, student_id))

    # Update department rankings
    for department in preference:
        if department not in department_ranking:
            department_ranking[department] = []
        department_ranking[department].append((score, student_id))

# Sort students by score in descending order
student_ranking.sort(reverse=True)

# Sort the department rankings by score in descending order
for _, rankings in department_ranking.items():
    rankings.sort(reverse=True)

# Assign student to departments starting from the highest score
for _, student_id in student_ranking:
    for department in student_preference[student_id]:
        # Check if the department has available seats
        # and the student hasn't been assigned to any department yet
        if department_seats[department] > 0 and not has_department[student_id]:
            # Assign student to the department
            student_to_department[student_id] = department
            has_department[student_id] = True
            department_seats[department] -= 1
            break

# Output the results
for student_id, department in sorted(student_to_department.items()):
    print(f"{student_id} {department}")
```
