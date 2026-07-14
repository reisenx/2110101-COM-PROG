<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Student Info ★★★ (
      <a href="https://drive.google.com/file/d/15menRq_5rcVxJTHJ2-CBhOH0zxlM_o3W/view?usp=drive_link">
        <code>10_TSD_35</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเก็บข้อมูลนิสิตและคำค้น**](#การเก็บข้อมูลนิสิตและคำค้น)
-   [**การค้นหาด้วยเซต**](#การค้นหาด้วยเซต)
-   [**การป้องกันชื่อเล่นชนกับรหัส**](#การป้องกันชื่อเล่นชนกับรหัส)
-   [**การเรียงและแสดงผล**](#การเรียงและแสดงผล)
-   [**Solution**](#solution)

---

## การเก็บข้อมูลนิสิตและคำค้น

ข้อมูลนิสิตแต่ละคนมี `4` ช่องตามลำดับ คือ ชื่อเล่น กรุ๊ป รุ่น และภาควิชา
โปรแกรมอ่านแต่ละบรรทัดด้วย `split()` แล้วเก็บลิสต์ของนิสิตทุกคนไว้ใน
`students` เช่น

```python
["Pim", "C", "99", "CP"]
```

คำค้นบรรทัดสุดท้ายอาจมีเฉพาะกรุ๊ป รุ่น ภาควิชา หรือหลายอย่างรวมกัน
และโจทย์ระบุว่าไม่จำเป็นต้องเรียงลำดับ โปรแกรมจึงแปลงคำค้นเป็นเซต

```python
query = set(input().strip().split())
```

ตัวอย่างเช่น `CP C` และ `C CP` จะได้เซตเดียวกันคือ `{"CP", "C"}`

---

## การค้นหาด้วยเซต

เมื่อพิจารณานิสิตหนึ่งคน โปรแกรมแปลงข้อมูลทั้ง `4` ช่องเป็น
`set(student)` แล้วตรวจว่าคำค้นทุกคำอยู่ในข้อมูลของนิสิตคนนั้นหรือไม่

ถ้าให้ \(Q\) เป็นเซตคำค้น และ \(S\) เป็นเซตข้อมูลนิสิต เงื่อนไขคือ

\[
Q \subseteq S
\]

เขียนใน Python ได้เป็น

```python
query.issubset(set(student))
```

เช่น `query` เป็น `{"CP", "C"}` จะตรงกับ
`["Pim", "C", "99", "CP"]` เพราะทั้ง `"CP"` และ `"C"` อยู่ในข้อมูล
แต่จะไม่ตรงกับนิสิตภาค `CE` แม้จะอยู่กรุ๊ป `C`

การใช้เซตทำให้ลำดับของคำค้นไม่มีผล และคำที่ซ้ำกันในบรรทัดคำค้นจะเหลือเพียง
ค่าเดียว อย่างไรก็ตาม **ทุกค่าที่ระบุยังต้องตรงครบทั้งหมด** จึงจะเพิ่มนิสิตคนนั้น
ลงใน `results`

---

## การป้องกันชื่อเล่นชนกับรหัส

โจทย์ให้ค้นจากกรุ๊ป รุ่น และภาควิชา ไม่ได้ให้ค้นจากชื่อเล่น แต่การใช้
`set(student)` รวมชื่อเล่นอยู่ด้วย หากมีนิสิตชื่อ `A` คำค้น `A` อาจถูกเข้าใจผิดว่า
ตรงกับกรุ๊ป ทั้งที่ `A` เป็นเพียงชื่อเล่น

โค้ดจึงประกาศ `GROUPS` และ `DEPARTMENTS` ซึ่งรวบรวมรหัสกรุ๊ปและภาควิชา
ที่รู้จัก แล้วเพิ่มเงื่อนไข

```python
(name not in GROUPS) and (name not in DEPARTMENTS)
```

> [!NOTE]
>
> เงื่อนไขนี้ทำงานตามโค้ดตรง ๆ คือ ถ้าชื่อเล่นตรงกับรหัสใดใน `GROUPS`
> หรือ `DEPARTMENTS` นิสิตคนนั้นจะไม่ถูกเพิ่มใน `results` ไม่ว่าคำค้นจะเป็นอะไร
> โค้ดไม่มีรายการลักษณะเดียวกันสำหรับค่ารุ่น

---

## การเรียงและแสดงผล

ถ้า `results` ว่าง โปรแกรมแสดง `Not Found` เพียงบรรทัดเดียว มิฉะนั้นจะเรียก
`results.sort()` การเปรียบเทียบลิสต์เริ่มจากสมาชิกตัวแรก ซึ่งก็คือชื่อเล่น
และโจทย์รับประกันว่าชื่อเล่นไม่ซ้ำกัน ผลลัพธ์จึงเรียงตามชื่อเล่นแบบพจนานุกรม

จากนั้นแยกข้อมูลกลับเป็น `name`, `group`, `generation`, `department`
แล้วพิมพ์ทั้ง `4` ค่าโดยคั่นด้วยเว้นวรรคตามรูปแบบที่โจทย์กำหนด

---

# Solution

```python
# --------------------------------------------------
# File Name : 10_TSD_35.py
# Problem   : Student Info
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# List of groups and departments
GROUPS = (
    "A",
    "B",
    "C",
    "Dog",
    "E",
    "F",
    "G",
    "H",
    "J",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
)
DEPARTMENTS = (
    "CE",
    "EE",
    "ME",
    "AE",
    "IE",
    "CHE",
    "PE",
    "GE",
    "ENV",
    "SV",
    "MT",
    "CP",
    "NT",
    "CEDT",
    "ICE",
    "NANO",
    "ADME",
    "CHPE",
    "AI",
    "AERO",
    "SEMI",
)

# Input student information
n = int(input())
students = []
for _ in range(n):
    data = input().strip().split()
    students.append(data)

# Input query as a set
query = set(input().strip().split())

# Search for students matching the query
results = []
for student in students:
    name, group, generation, department = student
    if (
        query.issubset(set(student))
        and (name not in GROUPS)
        and (name not in DEPARTMENTS)
    ):
        results.append(student)

# Output
if len(results) == 0:
    print("Not Found")
else:
    results.sort()
    for name, group, generation, department in results:
        print(name, group, generation, department)
```
