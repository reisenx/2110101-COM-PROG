<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Cartoon ★★ (
      <a href="https://drive.google.com/file/d/1-d45vrVJgudHhNZWBcjlpOO7604YnSpC/view?usp=drive_link">
        <code>10_TSD_24</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การจัดกลุ่มด้วย Dictionary และ List**](#การจัดกลุ่มด้วย-dictionary-และ-list)
-   [**การอ่านข้อมูลจนพบ q**](#การอ่านข้อมูลจนพบ-q)
-   [**การรักษาลำดับข้อมูล**](#การรักษาลำดับข้อมูล)
-   [**การจัดรูปแบบผลลัพธ์**](#การจัดรูปแบบผลลัพธ์)
-   [**กรณีพิเศษ**](#กรณีพิเศษ)
-   [**Solution**](#solution)

---

## การจัดกลุ่มด้วย Dictionary และ List

โจทย์ต้องการรวบรวมชื่อตัวการ์ตูนที่เป็นสัตว์ชนิดเดียวกันไว้ด้วยกัน
จึงใช้ dictionary ที่มีรูปแบบดังนี้

```text
ชนิดสัตว์ -> ลิสต์ชื่อตัวการ์ตูน
```

ตัวอย่างเช่น เมื่ออ่าน `Ted, bear` และ `Fozzie, bear` จะได้ข้อมูล

```python
{"bear": ["Ted", "Fozzie"]}
```

key ของ dictionary คือชนิดสัตว์ เพราะใช้ค้นหากลุ่มที่ต้องเพิ่มข้อมูล
ส่วน value ต้องเป็น `list` เพราะสัตว์หนึ่งชนิดมีตัวการ์ตูนได้หลายชื่อ
และโจทย์ต้องการรักษาลำดับที่อ่านชื่อเหล่านั้นเข้ามา

ถ้ายังไม่เคยพบชนิดสัตว์นั้น โปรแกรมสร้างลิสต์ว่างก่อน

```python
if animal not in characters:
    characters[animal] = []
```

จากนั้นจึงต่อชื่อไว้ท้ายลิสต์ด้วย

```python
characters[animal].append(name)
```

---

## การอ่านข้อมูลจนพบ q

จำนวนบรรทัดข้อมูลไม่ได้ระบุไว้ล่วงหน้า โปรแกรมจึงใช้ลูป `while True`
อ่านไปเรื่อย ๆ และหยุดเมื่อได้รับบรรทัด `q`

```python
data = input().strip()
if data == "q":
    break
```

บรรทัด `q` เป็นเพียงสัญญาณจบข้อมูล จึงถูกตรวจสอบก่อนแยกชื่อและชนิดสัตว์
และไม่ถูกเก็บลงใน dictionary

สำหรับบรรทัดทั่วไป โปรแกรมแยกข้อมูลด้วย

```python
name, animal = data.split(", ")
```

ตัวคั่นที่ implementation นี้ใช้คือ **จุลภาคตามด้วยช่องว่างหนึ่งช่อง** (`", "`)
จึงยังเก็บช่องว่างที่เป็นส่วนหนึ่งของชื่อได้ เช่น `Scooby Doo, dog`
จะได้ `name` เป็น `"Scooby Doo"` และ `animal` เป็น `"dog"`

> [!WARNING]
>
> คำอธิบายข้อมูลนำเข้าใน PDF ระบุอย่างกว้าง ๆ ว่าข้อมูลคั่นด้วยช่องว่าง
> แต่ตัวอย่างและโค้ดคำตอบใช้รูปแบบ `name, animal` และแยกด้วย `split(", ")`
> ดังนั้นข้อมูลที่โค้ดนี้รองรับต้องมีจุลภาคและช่องว่างตามรูปแบบตัวอย่าง
> เช่น `Ted, bear` ไม่ใช่ `Ted bear` หรือ `Ted,bear`

---

## การรักษาลำดับข้อมูล

โจทย์กำหนดลำดับไว้สองระดับ

1. ชนิดสัตว์ต้องเรียงตามครั้งแรกที่สัตว์ชนิดนั้นปรากฏ
2. ชื่อตัวการ์ตูนในแต่ละกลุ่มต้องเรียงตามลำดับที่อ่านเข้ามา

ใน Python 3 dictionary รักษาลำดับการเพิ่ม key ดังนั้นการวน
`characters.items()` จะแสดงชนิดสัตว์ตามครั้งแรกที่พบ ส่วนลิสต์รักษาลำดับของ
`append()` จึงแสดงชื่อตามลำดับข้อมูลนำเข้าได้เช่นกัน

ตัวอย่างข้อมูลย่อ

```text
Ted, bear
Pongo, dog
Fozzie, bear
q
```

แม้ `bear` จะปรากฏอีกครั้งหลัง `dog` แต่ key `bear` ถูกสร้างก่อน
ผลลัพธ์จึงแสดงกลุ่ม `bear` ก่อน `dog` และภายในกลุ่ม `bear` แสดง `Ted`
ก่อน `Fozzie`

---

## การจัดรูปแบบผลลัพธ์

แต่ละบรรทัดต้องมีรูปแบบ

```text
ชนิดสัตว์: ชื่อที่ 1, ชื่อที่ 2, ...
```

คำสั่ง `', '.join(names)` เชื่อมทุกชื่อในลิสต์ด้วยจุลภาคและช่องว่าง
โดยไม่เติมตัวคั่นเกินมาหลังชื่อสุดท้าย แล้ว f-string เติมชนิดสัตว์และ `: `
ไว้ด้านหน้า

```python
print(f"{animal}: {', '.join(names)}")
```

สำหรับตัวอย่างย่อจึงได้

```text
bear: Ted, Fozzie
dog: Pongo
```

---

## กรณีพิเศษ

-   ถ้าบรรทัดแรกเป็น `q` dictionary จะว่างและโปรแกรมจะไม่แสดงผล
-   ถ้าชื่อเดิมปรากฏซ้ำ โปรแกรมจะเก็บและแสดงซ้ำ เพราะ value เป็นลิสต์
    ไม่ใช่เซต
-   การพบสัตว์ชนิดเดิมภายหลังจะเพิ่มชื่อเข้า key เดิม
    จึงไม่เปลี่ยนลำดับของชนิดสัตว์

---

# Solution

```python
# --------------------------------------------------
# File Name : 10_TSD_24.py
# Problem   : Cartoon
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Initialize a dictionary to store cartoon characters.
characters = {}

# Input cartoon character names and animal types.
while True:
    # Input a line of data.
    data = input().strip()
    # If the input is "q", break the loop.
    if data == "q":
        break

    # Split the input data into name and animal type.
    name, animal = data.split(", ")

    # Update the characters dictionary.
    if animal not in characters:
        characters[animal] = []
    characters[animal].append(name)

# Output the animal types and their corresponding characters.
for animal, names in characters.items():
    print(f"{animal}: {', '.join(names)}")
```
