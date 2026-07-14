<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Nicknames ★ (
      <a href="https://drive.google.com/file/d/1uFj1SbM2w3SCE3Kwqvt1zImzjdl2rSXr/view?usp=drive_link">
        <code>08_Dict_12</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การค้นหาแบบสองทิศทางด้วยพจนานุกรม**](#การค้นหาแบบสองทิศทางด้วยพจนานุกรม)
-   [**การเก็บชื่อจริงและชื่อเล่น**](#การเก็บชื่อจริงและชื่อเล่น)
-   [**การตอบคำถาม**](#การตอบคำถาม)
-   [**ตัวอย่างการค้นหา**](#ตัวอย่างการค้นหา)
-   [**Solution**](#solution)

---

## การค้นหาแบบสองทิศทางด้วยพจนานุกรม

`dict` เหมาะกับการค้นหาข้อมูลเมื่อเรารู้คีย์ เช่น ถ้าเก็บ
`{"John": "Jack"}` เราสามารถใช้คีย์ `"John"` เพื่อค้นชื่อเล่น `"Jack"`
ได้ทันที แต่ยังใช้พจนานุกรมนี้ค้นจาก `"Jack"` กลับไปหา `"John"` โดยตรงไม่ได้

โจทย์ต้องค้นหาได้ทั้งสองทิศทาง จึงสร้างพจนานุกรม 2 ชุด

-   `fullname_to_nickname` เก็บ **ชื่อจริง → ชื่อเล่น**
-   `nickname_to_fullname` เก็บ **ชื่อเล่น → ชื่อจริง**

สำหรับคู่ชื่อ `John Jack` ข้อมูลที่เก็บจึงเป็น

```python
fullname_to_nickname["John"] = "Jack"
nickname_to_fullname["Jack"] = "John"
```

เมื่อมีพจนานุกรมทั้งสองชุด เราสามารถใช้ชื่อที่ได้รับมาเป็นคีย์ของพจนานุกรม
ชุดที่เหมาะสม แล้วหาชื่อที่จับคู่กันได้โดยไม่ต้องวนดูทุกรายชื่อ

## การเก็บชื่อจริงและชื่อเล่น

บรรทัดแรกของข้อมูลนำเข้าเป็นจำนวนคู่ชื่อ `n` จากนั้นลูปจะอ่านข้อมูลอีก `n`
บรรทัด บรรทัดละ 1 คู่

```python
n = int(input())
for _ in range(n):
    fullname, nickname = input().strip().split()
```

คำสั่ง `.split()` แยกข้อความที่คั่นด้วยช่องว่าง แล้วนำคำแรกเก็บใน
`fullname` และคำที่สองเก็บใน `nickname` ข้อมูลตามโจทย์จึงต้องมีชื่อจริงและ
ชื่อเล่นอย่างละ 1 คำในแต่ละบรรทัด

จากนั้นจึงเพิ่มคู่ชื่อเดียวกันลงในพจนานุกรมทั้งสองทิศทาง

```python
nickname_to_fullname[nickname] = fullname
fullname_to_nickname[fullname] = nickname
```

โจทย์รับประกันว่าไม่มีชื่อจริงซ้ำกัน และไม่มีชื่อเล่นซ้ำกัน ข้อมูลที่เพิ่มเข้ามา
จึงไม่เขียนทับคู่ชื่อก่อนหน้าในพจนานุกรมประเภทเดียวกัน

## การตอบคำถาม

หลังจากเก็บคู่ชื่อครบแล้ว โปรแกรมจะอ่านจำนวนคำถามและตอบทีละชื่อ
ตามลำดับที่ได้รับมา ตัวแปร `n` ถูกนำมาเก็บจำนวนคำถามแทนจำนวนคู่ชื่อเดิม
เพราะหลังสร้างพจนานุกรมเสร็จแล้ว โปรแกรมไม่ต้องใช้จำนวนคู่ชื่ออีก

```python
n = int(input())
for _ in range(n):
    name = input().strip()
```

สำหรับแต่ละชื่อ โปรแกรมตรวจสอบ 3 กรณี

1. ถ้าชื่ออยู่ใน `nickname_to_fullname` แสดงชื่อจริงที่จับคู่กัน
2. ถ้าไม่ใช่ชื่อเล่น แต่ชื่ออยู่ใน `fullname_to_nickname` แสดงชื่อเล่นที่จับคู่กัน
3. ถ้าไม่พบในพจนานุกรมทั้งสองชุด แสดงข้อความ `Not found`

การตรวจ `name in ...` และการค้นด้วย `dictionary[name]` เปรียบเทียบข้อความ
แบบตรงตัว ตัวพิมพ์เล็กและตัวพิมพ์ใหญ่จึงถือเป็นคนละชื่อ เช่น `"John"` กับ
`"john"` ไม่ใช่คีย์เดียวกัน

> [!NOTE]
>
> โค้ดตรวจพจนานุกรม `nickname_to_fullname` ก่อน หากข้อความเดียวกันปรากฏเป็น
> ทั้งชื่อเล่นของคนหนึ่งและชื่อจริงของอีกคน โค้ดจะตีความข้อความนั้นเป็นชื่อเล่น
> และแสดงชื่อจริงที่จับคู่กัน

## ตัวอย่างการค้นหา

จากข้อมูลตัวอย่างในโจทย์ โปรแกรมจะค้นหาแต่ละชื่อดังนี้

| ชื่อที่ถาม | ตำแหน่งที่พบ | ผลลัพธ์ |
| :--- | :--- | :--- |
| `John` | คีย์ใน `fullname_to_nickname` | `Jack` |
| `Jim` | คีย์ใน `nickname_to_fullname` | `James` |
| `Don` | ไม่พบในพจนานุกรมทั้งสองชุด | `Not found` |
| `Debbie` | คีย์ใน `nickname_to_fullname` | `Deborah` |

โปรแกรมแสดงผล 1 บรรทัดต่อ 1 คำถาม จึงได้ผลลัพธ์ทั้งหมดตามลำดับเดียวกับชื่อ
ที่ป้อนเข้ามา และต้องสะกด `Not found` ให้ตรงตามที่โจทย์กำหนด

---

# Solution

```python
# --------------------------------------------------
# File Name : 08_Dict_12.py
# Problem   : Nickname
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Initialize a dictionary with names and their nicknames
nickname_to_fullname = {}
fullname_to_nickname = {}

# Input name and nickname pairs
n = int(input())
for _ in range(n):
    fullname, nickname = input().strip().split()
    nickname_to_fullname[nickname] = fullname
    fullname_to_nickname[fullname] = nickname

# Search for a nickname or fullname
n = int(input())
for _ in range(n):
    name = input().strip()
    if name in nickname_to_fullname:
        print(nickname_to_fullname[name])

    elif name in fullname_to_nickname:
        print(fullname_to_nickname[name])

    else:
        print("Not found")
```
