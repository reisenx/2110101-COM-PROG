<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Eavesdrop ★★★ (
      <a href="https://drive.google.com/file/d/1wwznsnM32l3HiC4QfTj-GI3czgv0MkZQ/view?usp=sharing">
        <code>2566_1_Q2_03</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**รูปแบบข้อมูลบทสนทนา**](#รูปแบบข้อมูลบทสนทนา)
-   [**การรับข้อมูลหลายบรรทัด**](#การรับข้อมูลหลายบรรทัด)
-   [**การค้นหาและตัดข้อความ**](#การค้นหาและตัดข้อความ)
-   [**การเลือกและแสดงผลบทสนทนา**](#การเลือกและแสดงผลบทสนทนา)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ข้อควรระวัง**](#ข้อควรระวัง)
-   [**Solution**](#solution)

---

## รูปแบบข้อมูลบทสนทนา

โจทย์ให้รายชื่อตัวละครที่เราสนใจจำนวน `N` ชื่อ
จากนั้นจึงตามด้วยเนื้อหานิยายหลายบรรทัด และใช้บรรทัด `END`
เป็นสัญลักษณ์บอกว่าข้อมูลนิยายจบแล้ว

บทสนทนาแต่ละครั้งมีรูปแบบดังนี้

```text
*ชื่อตัวละคร:    "บทพูด"
```

-   เครื่องหมาย `*` บอกจุดเริ่มต้นของชื่อตัวละคร
-   เครื่องหมาย `:` บอกจุดสิ้นสุดของชื่อ
-   หลัง `:` อาจมีช่องว่างกี่ช่องก็ได้ ก่อนจะพบเครื่องหมาย `"`
-   บทพูดอยู่ระหว่างเครื่องหมาย `"` คู่หนึ่ง และอาจยาวหลายบรรทัด
-   คำบรรยายที่อยู่ระหว่างบทสนทนา หรืออยู่หลังบทพูด ไม่ต้องนำมาแสดงผล

สิ่งที่ต้องแสดงคือชื่อและบทพูดของตัวละครที่อยู่ในรายชื่อที่สนใจ
โดยเรียงตามลำดับที่ปรากฏในนิยาย ไม่ใช่ลำดับของรายชื่อที่รับเข้ามา

---

## การรับข้อมูลหลายบรรทัด

เริ่มจากรับชื่อตัวละครทั้ง `N` ชื่อเก็บไว้ใน list ชื่อ `queries`
แล้วอ่านข้อความนิยายทีละบรรทัดจนกว่าจะพบ `END`

```python
raw_dialog = ""
while True:
    line = input().strip()
    if line == "END":
        break
    raw_dialog += line + "\n"
```

การเติม `"\n"` หลังแต่ละบรรทัดมีความสำคัญ เพราะทำให้ตำแหน่งที่ขึ้นบรรทัดใหม่
ภายในบทพูดยังคงอยู่ เมื่อแสดงผลบทพูดนั้นก็จะขึ้นบรรทัดใหม่ตามนิยาย

> [!NOTE]
>
> แม้ comment ใน Solution จะเรียกตัวแปร `raw_dialog` ว่า raw string
> แต่ค่าของตัวแปรนี้เป็น string ปกติที่เกิดจากการต่อข้อความด้วย `+`
> ไม่ใช่ raw string literal ที่เขียนด้วยรูปแบบ `r"..."`

---

## การค้นหาและตัดข้อความ

คำสั่ง `text.find(target, start)` ใช้ค้นหา `target` ใน `text`
โดยเริ่มค้นจากตำแหน่ง `start` หากพบจะได้ index ของตำแหน่งแรก
และหากไม่พบจะได้ค่า `-1`

โปรแกรมใช้ `find()` ค้นหาเครื่องหมายทั้ง 4 ตัวของบทสนทนาแต่ละครั้ง

| สิ่งที่ค้นหา | ตัวแปรที่เก็บ index | index ชี้ไปที่ |
|:--:|:--|:--|
| `*` | `name_start_idx` | เครื่องหมาย `*` ก่อนชื่อ |
| `:` | `name_end_idx` | เครื่องหมาย `:` หลังชื่อ |
| `"` ตัวแรก | `dialog_start_idx` | double quote เปิดบทพูด |
| `"` ตัวถัดไป | `dialog_end_idx` | double quote ปิดบทพูด |

```python
name_start_idx = raw_dialog.find("*", query_idx)
if name_start_idx == -1:
    break
name_end_idx = raw_dialog.find(":", name_start_idx + 1)
dialog_start_idx = raw_dialog.find('"', name_end_idx + 1)
dialog_end_idx = raw_dialog.find('"', dialog_start_idx + 1)
```

เมื่อหา index ครบแล้ว จึงตัดชื่อและบทพูดด้วยการ slice

```python
name = raw_dialog[name_start_idx + 1 : name_end_idx].strip()
dialog = raw_dialog[dialog_start_idx : dialog_end_idx + 1].strip()
```

การ slice ใน Python จะไม่รวม index ด้านขวา ดังนั้น
`name_start_idx + 1` จึงช่วยตัดเครื่องหมาย `*` ออกจากชื่อ
ส่วน `dialog_end_idx + 1` ทำให้บทพูดที่ตัดออกมายังคงมี double quote ปิดท้าย

หลังเก็บชื่อและบทพูดแล้ว โปรแกรมเลื่อนจุดเริ่มค้นหาไปหลังบทพูดปัจจุบัน

```python
query_idx = dialog_end_idx + 1
```

วิธีนี้ทำให้ค้นหาบทสนทนาครั้งต่อไปได้โดยไม่ย้อนกลับมาพบข้อความเดิม
และคำบรรยายหลังบทพูดจะไม่ติดมาด้วย เพราะ `dialog` สิ้นสุดที่ double quote ปิดบทพูด

---

## การเลือกและแสดงผลบทสนทนา

ทุกบทสนทนาถูกเพิ่มลงใน `dialog_list` ตามลำดับที่ค้นพบในนิยาย
โปรแกรมจึงวนดู list นี้ตามลำดับเดิม แล้วตรวจว่าชื่อผู้พูดอยู่ใน `queries` หรือไม่

```python
has_dialog = False
for name, dialog in dialog_list:
    if name in queries:
        print(f"{name}: {dialog}")
        has_dialog = True

if not has_dialog:
    print("Maybe wrong novel")
```

คำสั่ง `print(f"{name}: {dialog}")` ใส่เครื่องหมาย `:` และช่องว่างหนึ่งช่อง
ระหว่างชื่อกับบทพูด ส่วนตัวแปร `dialog` มี double quote ครบทั้งสองด้านอยู่แล้ว
หากบทพูดมี `\n` อยู่ภายใน `print()` ก็จะแสดงบรรทัดต่อไปตามเดิม
โดยไม่พิมพ์ชื่อตัวละครซ้ำหน้าบรรทัดที่ต่อเนื่อง

ตัวแปร `has_dialog` จะเปลี่ยนเป็น `True` เมื่อมีบทสนทนาที่ถูกแสดงอย่างน้อยหนึ่งครั้ง
หากวนครบแล้วยังเป็น `False` จึงแสดง `Maybe wrong novel` เพียงบรรทัดเดียว

---

## ตัวอย่างการทำงาน

สมมติว่ารายชื่อที่สนใจเรียงเป็น `Main Character` แล้วจึงเป็น `author123`
แต่ในนิยาย `author123` พูดก่อน ดังข้อความบางส่วนต่อไปนี้

```text
*author123: "I would like to send a
special gift to you as a thank you."
*Main Character: "Gift?"
```

โปรแกรมจะแยกข้อมูลได้ตามลำดับดังนี้

| ลำดับในนิยาย | `name` | `dialog` |
|:--:|:--|:--|
| 1 | `author123` | มีข้อความ 2 บรรทัด ตั้งแต่ `"I would...` ถึง `...thank you."` |
| 2 | `Main Character` | `"Gift?"` |

ชื่อทั้งสองอยู่ใน `queries` จึงได้ผลลัพธ์

```text
author123: "I would like to send a
special gift to you as a thank you."
Main Character: "Gift?"
```

จะเห็นว่า `author123` ถูกแสดงก่อน แม้จะอยู่หลัง `Main Character`
ในรายชื่อที่สนใจก็ตาม เพราะโจทย์ต้องการลำดับที่บทสนทนาปรากฏในนิยาย

---

## ข้อควรระวัง

> [!WARNING]
>
> การตรวจสอบ `name in queries` แยกตัวพิมพ์เล็กและตัวพิมพ์ใหญ่
> และต้องสะกดชื่อตรงกันทุกตัว เช่น ชื่อ `Villian` ในโจทย์ต้องใช้ตามนั้น
> ไม่ควรเปลี่ยนเป็น `Villain`

-   `input().strip()` ตัดช่องว่างด้านหน้าและด้านหลังของแต่ละบรรทัด
    โปรแกรมจึงรักษาการขึ้นบรรทัดใหม่ไว้ แต่ไม่ได้รักษาช่องว่างริมบรรทัด
-   ช่องว่างหลายช่องหลัง `:` ในข้อมูลนำเข้าไม่มีผลต่อการตัดบทพูด
    และผลลัพธ์จะมีช่องว่างหลัง `:` เพียงหนึ่งช่องเสมอ
-   หากชื่อตัวละครเดียวกันปรากฏใน `queries` ซ้ำ บทพูดจะไม่ถูกพิมพ์ซ้ำ
    เพราะ `name in queries` ให้ผลเป็นเพียง `True` หรือ `False`
-   โปรแกรมอาศัยเงื่อนไขของโจทย์ว่าเครื่องหมาย `*`, `:` และ `"`
    ถูกวางตามรูปแบบที่กำหนด จึงไม่ต้องตรวจสอบข้อมูลที่ผิดรูปแบบเพิ่มเติม

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_1_Q2_03.py
# Problem   : Eavesdrop
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------

# Input the character name queries
queries = []
n = int(input())
for _ in range(n):
    queries.append(input().strip())

# Input the novel dialog as a raw string
raw_dialog = ""
while True:
    line = input().strip()
    if line == "END":
        break
    raw_dialog += line + "\n"

# Parse the raw dialog to extract character names and their dialogs
dialog_list = []
# Initialize the index for searching
query_idx = 0
while True:
    # Find the start index of the character name
    name_start_idx = raw_dialog.find("*", query_idx)
    # Stop if no more names are found
    if name_start_idx == -1:
        break
    # Find the end index of the character name
    name_end_idx = raw_dialog.find(":", name_start_idx + 1)
    # Find the start and end index of the dialog
    dialog_start_idx = raw_dialog.find('"', name_end_idx + 1)
    dialog_end_idx = raw_dialog.find('"', dialog_start_idx + 1)

    # Extract the character name and dialog from the raw dialog
    name = raw_dialog[name_start_idx + 1 : name_end_idx].strip()
    dialog = raw_dialog[dialog_start_idx : dialog_end_idx + 1].strip()
    # Store the character name and dialog in the list
    dialog_list.append([name, dialog])

    # Update the query index to search for the next character name
    query_idx = dialog_end_idx + 1

# Output the dialogs for the queried character names
has_dialog = False
for name, dialog in dialog_list:
    if name in queries:
        print(f"{name}: {dialog}")
        has_dialog = True

if not has_dialog:
    print("Maybe wrong novel")
```
