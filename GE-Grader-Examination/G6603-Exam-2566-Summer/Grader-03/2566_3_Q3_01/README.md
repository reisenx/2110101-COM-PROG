<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Customized Grading ★★ (
      <a href="https://drive.google.com/file/d/19hJN0aOKbgJV4HOnwSkB2eyQrlpN-r_q/view?usp=sharing">
        <code>2566_3_Q3_01</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเก็บและเรียงเกณฑ์คะแนน**](#การเก็บและเรียงเกณฑ์คะแนน)
-   [**การเลือกเกรดจากคะแนน**](#การเลือกเกรดจากคะแนน)
-   [**การเรียงผลลัพธ์**](#การเรียงผลลัพธ์)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ข้อควรระวังของโค้ดชุดนี้**](#ข้อควรระวังของโค้ดชุดนี้)
-   [**Solution**](#solution)

---

## การเก็บและเรียงเกณฑ์คะแนน

ข้อมูลเกณฑ์หนึ่งบรรทัดประกอบด้วยชื่อเกรดและคะแนนขั้นต่ำ เช่น `B 70`
โปรแกรมแปลงคะแนนด้วย `float()` แล้วเก็บเป็น

```python
[70.0, "B"]
```

การวางคะแนนไว้ตำแหน่งแรกช่วยให้ `grade_criteria.sort(reverse=True)`
เรียงเกณฑ์จากคะแนนสูงไปต่ำได้ ตัวอย่างเช่น เกณฑ์ที่รับมาแบบไม่เรียงลำดับ

```python
[[70.0, "B"], [50.0, "D"], [65.0, "C+"], [80.0, "A"]]
```

จะถูกเรียงเป็น

```python
[[80.0, "A"], [70.0, "B"], [65.0, "C+"], [50.0, "D"]]
```

โจทย์อาจให้เกรดมาไม่ครบทุกระดับ โปรแกรมจึงใช้เฉพาะเกณฑ์ที่ได้รับ
โดยไม่ต้องสร้างเกรดที่หายไปเอง

หลังจบส่วนเกณฑ์ โปรแกรมรับจำนวนเต็ม `n` แล้วอ่านข้อมูลนักเรียนอีก `n`
บรรทัด แต่ละบรรทัดมีชื่อและคะแนนคั่นด้วยช่องว่าง เช่น `Tom 72.5`
ก่อนเก็บเป็น `[int(score), name]` เพื่อนำไปตัดเกรด

---

## การเลือกเกรดจากคะแนน

ถ้าเกณฑ์ของเกรดหนึ่งมีคะแนนขั้นต่ำเป็น $t$ นักเรียนที่มีคะแนน $s$
จะผ่านเกณฑ์นั้นเมื่อ

$$
t \leq s
$$

ซึ่งเขียนใน Python ได้เป็น

```python
if score >= criteria_score:
```

เนื่องจาก `grade_criteria` เรียงจากคะแนนสูงไปต่ำ เกณฑ์แรกที่เงื่อนไขเป็นจริง
จึงเป็นเกรดสูงที่สุดที่นักเรียนคนนั้นได้รับ โปรแกรมใช้ `break` เพื่อหยุดตรวจ
ทันทีหลังพบเกรดแล้ว

ก่อนตรวจแต่ละคน โปรแกรมกำหนดค่าเริ่มต้นเป็น
`info = [0, "F", name]` หากไม่มีเกณฑ์ใดที่คะแนนผ่าน ค่านี้จะไม่ถูกเปลี่ยน
และนักเรียนจะได้ `F` ตามเงื่อนไขของโจทย์

> [!NOTE]
>
> เครื่องหมาย `>=` รวมกรณีคะแนนเท่ากับเกณฑ์พอดี เช่น คะแนน `70`
> ผ่านเกณฑ์ `B 70` และได้เกรด `B`

---

## การเรียงผลลัพธ์

เมื่อตัดเกรดแล้ว ข้อมูลของนักเรียนแต่ละคนอยู่ในรูป

```text
[คะแนนขั้นต่ำของเกรดที่ได้, เกรด, ชื่อ]
```

เช่น `[65.0, "C+", "John"]` ส่วนผู้ที่ได้ `F` จะมีคะแนนเกณฑ์เป็น `0`
การเรียก `students_grades.sort()` จะเปรียบเทียบสมาชิกของลิสต์จากซ้ายไปขวา
จึงเกิดลำดับดังนี้

1. เรียงตามคะแนนขั้นต่ำของเกรดจากน้อยไปมาก หรือจากเกรดต่ำไปสูง
2. เมื่อได้เกรดเดียวกัน ค่าสองตำแหน่งแรกเท่ากัน จึงเรียงตาม `name`
   ตามลำดับตัวอักษร

ตอนแสดงผล โปรแกรมไม่ใช้คะแนนเกณฑ์อีก จึงแกะข้อมูลด้วย
`for _, grade, name in students_grades:` แล้วพิมพ์เพียงชื่อและเกรด

---

## ตัวอย่างการทำงาน

จากเกณฑ์ในตัวอย่างของโจทย์ โปรแกรมเรียงเกณฑ์จาก `A 80` ลงมาถึง
`D 50` แล้วพิจารณานักเรียนทีละคน เช่น

| นักเรียน | คะแนนที่โค้ดนำไปตัดเกรด | เกณฑ์แรกที่ผ่าน | เกรด |
|---|---:|---|---|
| Chokedee | `49` | ไม่มี | `F` |
| John | `65` | `C+ 65` | `C+` |
| Tom | `72` | `B 70` | `B` |
| Meesuk | `80` | `A 80` | `A` |

หลังจากเรียงผลลัพธ์ นักเรียนเกรดต่ำจะปรากฏก่อน และนักเรียนที่ได้เกรดเดียวกัน
จะเรียงตามชื่อ ตัวอย่างทางการยังได้ผลลัพธ์ตรงตามโจทย์ เพราะเกณฑ์ทั้งหมด
เป็นจำนวนเต็ม และการตัดส่วนทศนิยมของคะแนนนักเรียนไม่ได้ทำให้ใครข้ามเกณฑ์
ในตัวอย่างนั้น

---

## ข้อควรระวังของโค้ดชุดนี้

> [!WARNING]
>
> โค้ดรับคะแนนนักเรียนด้วย `float()` แต่เก็บเป็น `int(score)` จึงเป็นการ
> **ตัดส่วนทศนิยมทิ้ง ไม่ใช่การปัดเศษ** สำหรับคะแนนบวก เช่น `72.9`
> จะกลายเป็น `72` หากมีเกณฑ์ `B 72.5` และนักเรียนได้ `72.5` ตามข้อกำหนด
> นักเรียนควรผ่านเกณฑ์ แต่โค้ดจะเก็บคะแนนเป็น `72` และไม่ผ่านเกณฑ์ `72.5`
> พฤติกรรมนี้เป็นข้อจำกัดของโค้ดที่ให้มา จึงคงไว้ใน
> Solution ตามต้นฉบับ

ข้อความอธิบายใน PDF ระบุให้จบการรับเกณฑ์ด้วย `done` แต่ตัวอย่างใช้ `Done`
และโค้ดตรวจแบบตรงตัวด้วย `data == ["Done"]` ดังนั้นโค้ดชุดนี้
ยอมรับเฉพาะ `Done` ที่ตัว `D` เป็นตัวพิมพ์ใหญ่เท่านั้น

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_3_Q3_01.py
# Problem   : Customized Grading
# Author    : Worralop Srichainont
# Date      : 2025-07-15
# --------------------------------------------------

# Input customized grading criteria.
grade_criteria = []
while True:
    # Read input until "Done" is entered.
    data = input().strip().split()
    if data == ["Done"]:
        break
    # Each line contains a grade and a score threshold.
    grade = data[0]
    score = float(data[1])
    grade_criteria.append([score, grade])
grade_criteria.sort(reverse=True)

# Input student scores and names
students_scores = []
n = int(input())
for _ in range(n):
    # Read each student's name and score.
    data = input().strip().split()
    name = data[0]
    score = float(data[1])
    # Store the score and name in a list.
    students_scores.append([int(score), name])

# Initialize a list to store students' grades.
students_grades = []
# Assign grades based on the criteria.
for score, name in students_scores:
    # Default grade is "F" if no criteria match.
    info = [0, "F", name]
    # Check each grading criteria to assign the appropriate grade.
    for criteria_score, criteria_letter in grade_criteria:
        if score >= criteria_score:
            # If the score meets a criteria, update the grade and break.
            info = [criteria_score, criteria_letter, name]
            break
    # Append the student's grade information to the list.
    students_grades.append(info)
# Sort students by grade and then by name.
students_grades.sort()

# Output students with their grades.
for _, grade, name in students_grades:
    print(name, grade)
```
