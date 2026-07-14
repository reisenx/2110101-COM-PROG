<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Celebrity ★★ (
      <a href="https://drive.google.com/file/d/11ysKVt-jorwWKFFLZj7iKNLzwwAtZHUK/view?usp=drive_link">
        <code>10_TSD_27</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ความสัมพันธ์แบบมีทิศทาง**](#ความสัมพันธ์แบบมีทิศทาง)
-   [**การสร้างพจนานุกรมความสัมพันธ์**](#การสร้างพจนานุกรมความสัมพันธ์)
-   [**ฟังก์ชัน knows**](#ฟังก์ชัน-knows)
-   [**ฟังก์ชัน is_celeb**](#ฟังก์ชัน-is_celeb)
-   [**ฟังก์ชัน find_celeb**](#ฟังก์ชัน-find_celeb)
-   [**การทำงานของ main**](#การทำงานของ-main)
-   [**การรับคำสั่งจาก Grader**](#การรับคำสั่งจาก-grader)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ข้อสังเกตของโค้ดต้นฉบับ**](#ข้อสังเกตของโค้ดต้นฉบับ)
-   [**Solution**](#solution)

---

## ความสัมพันธ์แบบมีทิศทาง

ข้อมูลหนึ่งบรรทัดมีชื่อสองชื่อ เช่น

```text
Ploy Pat
```

หมายถึง Ploy รู้จัก Pat แต่ไม่ได้แปลว่า Pat รู้จัก Ploy ความสัมพันธ์นี้จึงมี
**ทิศทาง** โปรแกรมเก็บข้อมูลใน dictionary ชื่อ `relation` โดย

-   key คือชื่อบุคคล
-   value คือ `set` ของคนที่บุคคลนั้นรู้จัก

ตัวอย่างเช่น

```python
relation = {
    "Ploy": {"Boy", "Pat"},
    "Pat": set(),
}
```

แปลว่า Ploy รู้จัก Boy และ Pat ส่วน Pat ไม่รู้จักใคร

ตามนิยามของโจทย์ ผู้สมัครชื่อ $x$ เป็นดาวเด่นเมื่อผ่านเงื่อนไขทั้งสองข้อ

1. $x$ ไม่รู้จักคนอื่น แต่อาจรู้จักตัวเองได้ หรือเขียนเป็น
   $R[x] \subseteq \{x\}$
2. ทุกคน $p$ ที่ไม่ใช่ $x$ ต้องรู้จัก $x$ หรือเขียนเป็น
   $x \in R[p]$ สำหรับทุก $p \ne x$

## การสร้างพจนานุกรมความสัมพันธ์

ฟังก์ชัน `read_relations()` รับความสัมพันธ์ทีละบรรทัดจนพบ `q` แต่ละบรรทัด
ถูกแยกเป็น `a` และ `b` แล้วเพิ่ม `b` เข้าเซตของ `a`

```python
a, b = line.split()
if a not in relations:
    relations[a] = set()
if b not in relations:
    relations[b] = set()
relations[a].add(b)
```

การสร้าง key ให้ทั้ง `a` และ `b` สำคัญมาก เพราะบางคนอาจปรากฏเฉพาะด้านขวา
กล่าวคือมีคนรู้จักเขา แต่เขายังไม่รู้จักใคร หากไม่สร้าง `relations[b] = set()`
บุคคลนั้นจะไม่ถูกนำไปตรวจว่าเป็นดาวเด่น

`set` ช่วยไม่ให้ความสัมพันธ์เดิมที่ป้อนซ้ำถูกเก็บซ้ำ และทำให้ตรวจว่า
ชื่อหนึ่งอยู่ในกลุ่มคนที่รู้จักหรือไม่ด้วยตัวดำเนินการ `in`

## ฟังก์ชัน knows

ฟังก์ชัน `knows(relation, a, b)` ตอบว่า `a` รู้จัก `b` หรือไม่ โดยตรวจสมาชิก
ของเซตโดยตรง

```python
return b in relation[a]
```

เช่น เมื่อ `relation["A"] == {"B"}` จะได้ `knows(relation, "A", "B")`
เป็น `True` แต่ทิศทางกลับกันจะเป็น `False` ถ้า `"A"` ไม่อยู่ใน
`relation["B"]` ข้อมูลที่ใช้เรียกฟังก์ชันต้องมี `a` เป็น key อยู่แล้ว

## ฟังก์ชัน is_celeb

ฟังก์ชัน `is_celeb()` ตรวจผู้สมัครทีละเงื่อนไข ส่วนแรกของโค้ดคือ

```python
if len(relation[candidate]) > 1:
    return False
```

ค่าที่ผ่านส่วนนี้ได้จึงต้องมีจำนวนคนในเซตไม่เกินหนึ่งคน จากนั้นโปรแกรมวนดู
ทุกคนในงาน ถ้าพบคนอื่นที่ไม่รู้จักผู้สมัคร จะคืน `False` ทันที

```python
for person, known_people in relation.items():
    if person != candidate and candidate not in known_people:
        return False
```

เงื่อนไข `person != candidate` ทำให้ผู้สมัครไม่จำเป็นต้องรู้จักตัวเอง
ถ้าไม่พบเหตุให้ปฏิเสธทั้งสองช่วง ฟังก์ชันจึงคืน `True`

> [!WARNING]
>
> ตามนิยาม ส่วนแรกควรตรวจว่าเซตของผู้สมัครไม่มีชื่อคนอื่น แต่โค้ดต้นฉบับตรวจ
> เพียง `len(...) > 1` ดังนั้นเซตที่มี “คนอื่นเพียงหนึ่งคน” ก็ผ่านช่วงแรกได้
> README นี้อธิบายพฤติกรรมจริงดังกล่าวโดยคงบล็อก Solution ไว้ตรงกับไฟล์ `.py`
> ทุกประการ

ตัวอย่างเช่น `relation["A"] == {"B"}` มีขนาดเท่ากับ `1` จึงไม่ถูกปฏิเสธ
จากเงื่อนไขแรก แม้ A จะรู้จัก B ซึ่งขัดกับนิยามดาวเด่น หากทุกคนอื่นรู้จัก A
โค้ดต้นฉบับจะตอบว่า A เป็นดาวเด่นสำหรับข้อมูลนอกเจตนาของโจทย์ลักษณะนี้

## ฟังก์ชัน find_celeb

`find_celeb()` วนผู้สมัครตามลำดับ key ใน dictionary และเรียก `is_celeb()`
กับแต่ละคน

```python
for candidate in relation:
    if is_celeb(relation, candidate):
        return candidate
return None
```

เมื่อพบผู้สมัครที่ผ่านจะคืนชื่อนั้นทันที จึงเป็นคนแรกตามลำดับการเพิ่ม key
ถ้าไม่มีใครผ่านจึงคืน `None`

## การทำงานของ main

ฟังก์ชัน `main()` เชื่อมทุกขั้นตอนเข้าด้วยกัน

1. เรียก `read_relations()` เพื่อสร้าง dictionary
2. เรียก `find_celeb()` เพื่อค้นหาดาวเด่น
3. พิมพ์ชื่อเมื่อผลไม่ใช่ `None` มิฉะนั้นพิมพ์ `Not Found`

ถ้าป้อน `q` ทันที dictionary จะว่าง `find_celeb()` ไม่มีผู้สมัครให้วน
จึงคืน `None` และ `main()` พิมพ์ `Not Found`

## การรับคำสั่งจาก Grader

บรรทัดสุดท้ายไม่ได้เรียก `main()` โดยตรง แต่รับข้อความหนึ่งบรรทัดแล้วส่งให้
`exec()`

```python
exec(input().strip())
```

วิธีนี้เปิดให้ Grader เลือกทดสอบแต่ละฟังก์ชัน เช่น

```text
main()
```

จะเริ่มรับความสัมพันธ์จนถึง `q` ส่วนคำสั่ง

```python
R = {'A': {'B'}, 'B': set()}; print(knows(R, 'A', 'B'))
```

จะทดสอบ `knows()` โดยตรงและแสดง `True`

> [!WARNING]
>
> `exec()` สามารถรันข้อความเป็นคำสั่ง Python ได้ จึงควรใช้เฉพาะกับคำสั่งจาก
> Grader ที่เชื่อถือได้ ห้ามนำรูปแบบนี้ไปใช้รันข้อมูลจากผู้ใช้ที่ไม่ไว้วางใจ

## ตัวอย่างการทำงาน

ในตัวอย่างแรก Pat ไม่รู้จักใคร เพราะปรากฏทางขวาเท่านั้นและได้ค่าเป็น
`set()` ขณะเดียวกัน Ploy, Eak, Boy และ Poom ต่างมี `"Pat"` อยู่ในเซตของตน
Pat จึงผ่านการตรวจและโปรแกรมพิมพ์

```text
Pat
```

ในตัวอย่างที่เพิ่มความสัมพันธ์ `Noo-sa Tim` ทั้ง Noo-sa และ Tim ถูกเพิ่มเป็น
บุคคลในงาน แต่ Noo-sa ไม่ได้รู้จัก Pat ทำให้ Pat ไม่ผ่านเงื่อนไข “ทุกคนรู้จัก”
และไม่มีผู้สมัครคนอื่นผ่าน โปรแกรมจึงพิมพ์ `Not Found`

## ข้อสังเกตของโค้ดต้นฉบับ

-   โครงฟังก์ชันในเอกสารโจทย์ใช้ `d = input().split()` แล้วหยุดเมื่อ
    `len(d) == 1` ซึ่งหมายถึงบรรทัดที่มีหนึ่งคำใด ๆ เป็นสัญญาณจบ ตัวอย่างใช้
    คำว่า `q`
-   ไฟล์คำตอบจริงหยุดเฉพาะเมื่อ `line == "q"` เท่านั้น ถ้าป้อนคำอื่นเพียงคำเดียว
    โค้ดจะไปทำ `a, b = line.split()` และเกิดข้อผิดพลาดจากจำนวนค่าที่ไม่ครบ
    ดังนั้นข้อมูลตามรูปแบบต้องใช้ `q` เป็นบรรทัดจบ
-   ความสัมพันธ์ไม่สมมาตร การเพิ่ม `a b` ไม่ได้เพิ่ม `a` เข้าเซตของ `b`
-   บุคคลที่ปรากฏหลายครั้งยังเก็บชื่อคนรู้จักแต่ละคนเพียงครั้งเดียวเพราะใช้
    `set`
-   comment ใน Solution ระบุว่าจะปฏิเสธผู้สมัครที่รู้จักคนอื่น แต่เงื่อนไขจริง
    คือปฏิเสธเมื่อขนาดเซตมากกว่า `1` ตามที่อธิบายในหัวข้อ
    [ฟังก์ชัน is_celeb](#ฟังก์ชัน-is_celeb)

---

# Solution

```python
# --------------------------------------------------
# File Name : 10_TSD_27.py
# Problem   : Celebrity
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------


# Check if a person 'a' knows another person 'b'
def knows(relation, a, b):
    return b in relation[a]


# Check if a candidate is a celebrity
def is_celeb(relation, candidate):
    # Return false if candidate knows anyone other than themselves
    if len(relation[candidate]) > 1:
        return False

    # Check if everyone knows the candidate
    for person, known_people in relation.items():
        if person != candidate and candidate not in known_people:
            return False
    return True


# Find the celebrity in the relations
def find_celeb(relation):
    for candidate in relation:
        if is_celeb(relation, candidate):
            return candidate
    return None


# Function to read relations from input until 'q' is entered
def read_relations():
    relations = {}
    while True:
        # Read a line of input
        line = input().strip()

        # If the line is 'q', break the loop
        if line == "q":
            break

        # Update the relations dictionary
        a, b = line.split()
        if a not in relations:
            relations[a] = set()
        if b not in relations:
            relations[b] = set()
        relations[a].add(b)

    # Return the relations dictionary
    return relations


# Main function
def main():
    relations = read_relations()
    celebrity = find_celeb(relations)
    if celebrity is not None:
        print(celebrity)
    else:
        print("Not Found")


# Execute the input string as code
exec(input().strip())
```
