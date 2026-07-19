<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Registration Data ★★ (
      <a href="https://drive.google.com/file/d/1I--JE-9RUlVGtxYaqCl41rCbGkQUlSiq/view?usp=sharing">
        <code>2566_1_Q2_02</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**โครงสร้างข้อมูลและเป้าหมาย**](#โครงสร้างข้อมูลและเป้าหมาย)
-   [**การอ่านและคัดเลือกข้อมูล**](#การอ่านและคัดเลือกข้อมูล)
-   [**การเก็บข้อมูลโดยไม่ให้ซ้ำ**](#การเก็บข้อมูลโดยไม่ให้ซ้ำ)
-   [**การจัดรูปแบบผลลัพธ์**](#การจัดรูปแบบผลลัพธ์)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## โครงสร้างข้อมูลและเป้าหมาย

โจทย์ให้รับข้อมูลทั้งหมด 2 บรรทัด โดยบรรทัดแรกเป็นชื่อแฟ้มข้อมูลการลงทะเบียน
และบรรทัดที่สองเป็นรหัสอาจารย์ที่ต้องการค้นหา เช่น

```text
2110100.txt
AAA
```

ภายในแฟ้ม ข้อมูลการลงทะเบียนหนึ่งรายการจะอยู่ในหนึ่งบรรทัด
และแบ่งเป็น 5 ส่วนด้วยเครื่องหมายจุลภาค (`,`) ตามลำดับดังนี้

| ลำดับ | ตัวแปร | ตัวอย่าง | ความหมายและการนำไปใช้ |
|:---:|:---:|:---:|---|
| 1 | `sid` | `6634000521` | เลขประจำตัวนิสิต ใช้ตรวจไม่ให้นับนิสิตคนเดิมซ้ำ |
| 2 | `sex` | `F` | รหัสเพศ `F` หรือ `M` ใช้แยกกลุ่มสำหรับนับจำนวน |
| 3 | `faculty` | `21` | รหัสคณะ โค้ดต้องอ่านไว้ให้ครบ แต่โจทย์ข้อนี้ไม่ได้นำไปคำนวณ |
| 4 | `section` | `2` | เลขตอนเรียน ใช้รวบรวมและเรียงจากน้อยไปมาก |
| 5 | `professor` | `AAA` | รหัสอาจารย์ ใช้เปรียบเทียบกับรหัสที่ต้องการค้นหา |

ตัวอย่างข้อมูลหนึ่งบรรทัดจึงมีรูปแบบดังนี้

```text
6634000521,F,21,2,AAA
```

เป้าหมายคือหาตอนเรียนทั้งหมดที่อาจารย์คนนี้สอนโดยไม่ให้ซ้ำ
เรียงเลขตอนเรียนจากน้อยไปมาก แล้วนับจำนวนนิสิตหญิงและชายที่ไม่ซ้ำกัน

---

## การอ่านและคัดเลือกข้อมูล

เริ่มจากรับชื่อแฟ้มและรหัสอาจารย์ โดยใช้ `.strip()` เพื่อตัดช่องว่าง
ที่อาจติดอยู่บริเวณหัวหรือท้ายข้อความ ส่วน `input()` จะตัดอักขระขึ้นบรรทัดใหม่
ที่เกิดจากการกด Enter ให้อยู่แล้ว

```python
filename = input().strip()
search_professor = input().strip()
```

จากนั้นเปิดแฟ้มด้วย `with open(filename) as file:` การใช้ `with`
ช่วยให้ Python ปิดแฟ้มให้อัตโนมัติเมื่ออ่านข้อมูลเสร็จ

```python
with open(filename) as file:
    for line in file:
        sid, sex, faculty, section, professor = line.strip().split(",")
```

ในแต่ละรอบ `line.strip()` จะตัด `\n` ที่ท้ายบรรทัดออก
แล้ว `.split(",")` จะแบ่งข้อความตรงเครื่องหมาย `,` ให้เป็น 5 ค่า
ก่อนกระจายค่าเหล่านั้นไปยังตัวแปรทั้ง 5 ตัวตามลำดับ
แม้จะไม่ได้ใช้ `faculty` ต่อ เราก็ยังต้องมีตัวแปรนี้เพื่อรับข้อมูลช่องที่สาม

โปรแกรมจะเก็บข้อมูลเฉพาะบรรทัดที่รหัสอาจารย์ตรงกับค่าที่ค้นหาเท่านั้น

```python
if professor == search_professor:
```

การเปรียบเทียบข้อความด้วย `==` ต้องตรงกันทุกตัวอักษร
ดังนั้น `AAA` และ `aaa` ถือเป็นคนละรหัสกัน

---

## การเก็บข้อมูลโดยไม่ให้ซ้ำ

โปรแกรมใช้ลิสต์ 3 ตัวเพื่อเก็บข้อมูลที่พบ ได้แก่

-   `sections` เก็บเลขตอนเรียน
-   `males` เก็บเลขประจำตัวนิสิตชาย
-   `females` เก็บเลขประจำตัวนิสิตหญิง

ข้อมูลหนึ่งตอนเรียนมีนิสิตหลายคน จึงพบเลขตอนเรียนเดิมได้หลายครั้ง
ก่อนเพิ่มเลขตอนเรียน โปรแกรมจึงตรวจด้วย `not in` ว่ายังไม่มีค่านี้ในลิสต์

```python
if int(section) not in sections:
    sections.append(int(section))
```

เลขตอนเรียนที่อ่านจากแฟ้มมีชนิดเป็นข้อความ จึงแปลงเป็น `int`
เพื่อให้เรียงแบบตัวเลขได้ถูกต้อง เช่น `2` ต้องมาก่อน `10`

ในทำนองเดียวกัน โปรแกรมจะเพิ่ม `sid` ลงในลิสต์ตามเพศ
เมื่อยังไม่เคยมีเลขประจำตัวนั้นอยู่ในลิสต์ จึงไม่นับนิสิตคนเดิมซ้ำ

```python
if sex == "M" and sid not in males:
    males.append(sid)
elif sex == "F" and sid not in females:
    females.append(sid)
```

เลขประจำตัวนิสิตยังคงเป็นข้อความ เพราะไม่ได้นำไปคำนวณ
สุดท้ายจำนวนของแต่ละกลุ่มหาได้โดยตรงจากความยาวของลิสต์

-   จำนวนนิสิตหญิง = `len(females)`
-   จำนวนนิสิตชาย = `len(males)`

---

## การจัดรูปแบบผลลัพธ์

เมื่ออ่านแฟ้มครบทุกบรรทัดแล้ว โปรแกรมเรียง `sections`
จากค่าน้อยไปมากด้วยคำสั่งต่อไปนี้

```python
sections.sort()
```

จากนั้นเลือกรูปแบบข้อความตามจำนวนตอนเรียนที่พบ

| จำนวนตอนเรียน | รูปแบบผลลัพธ์ |
|:---:|---|
| 0 | `Not found` |
| 1 | `Section: <เลขตอนเรียน>` |
| มากกว่า 1 | `Sections: <เลขตอนเรียนคั่นด้วยจุลภาค>` |

กรณีมีหลายตอนเรียน ต้องเปลี่ยนเลขตอนเรียนแต่ละตัวกลับเป็นข้อความ
แล้วเชื่อมด้วย `",".join(...)`

```python
",".join([str(section) for section in sections])
```

เนื่องจากตัวคั่นคือ `","` ผลลัพธ์จึงไม่มีช่องว่างหลังเครื่องหมายจุลภาค
เช่น `2,10` ไม่ใช่ `2, 10`

เมื่อพบอย่างน้อยหนึ่งตอนเรียน โปรแกรมจึงต่อท้ายจำนวนนิสิตในรูปแบบ
` --> F = <จำนวนหญิง>, M = <จำนวนชาย>` แล้วแสดง `result` หนึ่งบรรทัด

> [!WARNING]
>
> รูปแบบผลลัพธ์ต้องตรงตามโจทย์ รวมถึงคำว่า `Section` หรือ `Sections`
> ช่องว่าง เครื่องหมาย `-->` และลำดับ `F` ก่อน `M`

---

## ตัวอย่างการทำงาน

เมื่อค้นหารหัสอาจารย์ `AAA` โปรแกรมจะอ่านเฉพาะบรรทัดที่ลงท้ายด้วย
รหัสนี้ ระหว่างอ่านอาจพบตอนเรียน `2` และ `10` ซ้ำหลายครั้ง
แต่การตรวจด้วย `not in` ทำให้ `sections` เหลือเพียง `[2, 10]`

นิสิตที่ไม่ซ้ำกันในบรรทัดเหล่านี้เป็นนิสิตหญิง 8 คน
และไม่มีนิสิตชาย ดังนั้นผลลัพธ์คือ

```text
Sections: 2,10 --> F = 8, M = 0
```

ถ้าค้นหา `BBB` จะพบเพียงตอนเรียน `3` จึงใช้คำว่า `Section`
แบบเอกพจน์ แต่ถ้ารหัสอาจารย์ไม่ปรากฏในแฟ้มเลย `sections`
จะยังเป็นลิสต์ว่างและโปรแกรมจะแสดง `Not found`

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_1_Q2_02.py
# Problem   : Registration Data
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------

# Input course database filename and query professor name
filename = input().strip()
search_professor = input().strip()

# Initialize lists to store information of query professor
sections = []
males = []
females = []

# Read the file and get information of the query professor
with open(filename) as file:
    for line in file:
        # Extract data from each line
        sid, sex, faculty, section, professor = line.strip().split(",")
        # If the professor matches the search query, store the information
        if professor == search_professor:
            # Store section number of the query professor
            if int(section) not in sections:
                sections.append(int(section))
            # Store male student IDs of the query professor
            if sex == "M" and sid not in males:
                males.append(sid)
            # Store female student IDs of the query professor
            elif sex == "F" and sid not in females:
                females.append(sid)
# Sort the sections in ascending order
sections.sort()

# Determine the output based on the number of sections found
result = ""
if len(sections) == 0:
    result = "Not found"
elif len(sections) == 1:
    result = f"Section: {sections[0]}"
elif len(sections) > 1:
    result = f"Sections: {','.join([str(section) for section in sections])}"

# Add the student count to the result if there are sections found
if len(sections) > 0:
    result += f" --> F = {len(females)}, M = {len(males)}"
# Output
print(result)
```
