<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Nicknames ★ (
      <a href="https://drive.google.com/file/d/1Uh5SmLFLn4k6F0RzaVNpBY2iHL5t9Jfb/view?usp=drive_link">
        <code>05_List_12</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ลิสต์คู่ขนาน**](#ลิสต์คู่ขนาน)
-   [**การค้นหาชื่อทั้งสองทิศทาง**](#การค้นหาชื่อทั้งสองทิศทาง)
-   [**ลำดับการรับและแสดงผล**](#ลำดับการรับและแสดงผล)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## ลิสต์คู่ขนาน

ชื่อจริงกับชื่อเล่นในโจทย์จับคู่กันตามตำแหน่ง โปรแกรมจึงเก็บข้อมูลไว้ในลิสต์
สองชุดที่มีลำดับตรงกัน เรียกว่า **ลิสต์คู่ขนาน** (parallel lists)

ตัวอย่างเช่น

-   `REAL_NAMES[0]` คือ `"Robert"` และ `NICKNAMES[0]` คือ `"Bob"`
-   `REAL_NAMES[3]` คือ `"John"` และ `NICKNAMES[3]` คือ `"Jack"`
-   `REAL_NAMES[9]` คือ `"Deborah"` และ `NICKNAMES[9]` คือ `"Debbie"`

เมื่อรู้ตำแหน่งของชื่อในลิสต์หนึ่ง เราจึงใช้ตำแหน่งเดียวกันอ่านชื่อที่เป็นคู่กัน
จากอีกลิสต์ได้ โดยไม่ต้องเขียน `if...elif...` แยกทุกชื่อ

---

## การค้นหาชื่อทั้งสองทิศทาง

แต่ละชื่อที่รับเข้ามามีความเป็นไปได้สามกรณี

1. ถ้า `name in REAL_NAMES` ให้หา index ด้วย `REAL_NAMES.index(name)`
   แล้วแสดง `NICKNAMES[idx]`
2. ถ้าไม่ใช่ชื่อจริง แต่ `name in NICKNAMES` ให้หา index ด้วย
   `NICKNAMES.index(name)` แล้วแสดง `REAL_NAMES[idx]`
3. ถ้าไม่อยู่ในทั้งสองลิสต์ ให้แสดง `Not found`

โปรแกรมตรวจด้วย `in` ก่อนเรียก `.index()` เสมอ เพราะ `.index()` จะเกิด
`ValueError` หากไม่มีชื่อนั้นอยู่ในลิสต์

> [!NOTE]
>
> การเปรียบเทียบสตริงของ Python แยกตัวพิมพ์เล็กและตัวพิมพ์ใหญ่ เช่น `"Jack"`
> ค้นพบในลิสต์ แต่ `"jack"` ไม่ตรงกับชื่อที่กำหนดและจะแสดง `Not found`

---

## ลำดับการรับและแสดงผล

บรรทัดแรกรับจำนวนเต็ม `n` ซึ่งบอกจำนวนชื่อที่จะตามมา จากนั้นลูปทำงาน `n`
รอบ แต่ละรอบรับหนึ่งชื่อและแสดงคำตอบทันที จึงได้ผลลัพธ์ทั้งหมด `n` บรรทัด
และเรียงตามลำดับเดียวกับข้อมูลนำเข้า

การใช้ `.strip()` ตัดช่องว่างที่หัวและท้ายบรรทัดออก แต่ข้อความชื่อด้านในยังต้อง
ตรงกับชื่อในตารางทุกตัวอักษร

---

## ตัวอย่างการทำงาน

หากได้รับชื่อเรียงกันเป็น `Jack`, `James`, `Don` และ `Deborah`

-   `Jack` อยู่ที่ index `3` ของ `NICKNAMES` จึงได้ `John`
-   `James` อยู่ที่ index `2` ของ `REAL_NAMES` จึงได้ `Jim`
-   `Don` ไม่อยู่ในทั้งสองลิสต์ จึงได้ `Not found`
-   `Deborah` อยู่ที่ index `9` ของ `REAL_NAMES` จึงได้ `Debbie`

ผลลัพธ์จึงเป็น

```text
John
Jim
Not found
Debbie
```

---

# Solution

```python
# --------------------------------------------------
# File Name : 05_List_12.py
# Problem   : Nicknames
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------

# List of real names and their corresponding nicknames
REAL_NAMES = [
    "Robert",
    "William",
    "James",
    "John",
    "Margaret",
    "Edward",
    "Sarah",
    "Andrew",
    "Anthony",
    "Deborah",
]
NICKNAMES = [
    "Bob",
    "Bill",
    "Jim",
    "Jack",
    "Peggy",
    "Ed",
    "Sally",
    "Andy",
    "Tony",
    "Debbie",
]

# Input amount of names
n = int(input())

# Output the corresponding nicknames
for _ in range(n):
    name = input().strip()
    # Output the nickname if found
    if name in REAL_NAMES:
        idx = REAL_NAMES.index(name)
        print(NICKNAMES[idx])
    # Output the real name if found
    elif name in NICKNAMES:
        idx = NICKNAMES.index(name)
        print(REAL_NAMES[idx])
    # Output "Not found" if neither is found
    else:
        print("Not found")
```
