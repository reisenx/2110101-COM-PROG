<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Telephone Dictionary ★★ (
      <a href="https://drive.google.com/file/d/1tFaiW-9R_dVhyP72g_SaPjIFcmkQfcXa/view?usp=drive_link">
        <code>08_Dict_23</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การค้นข้อมูลสองทิศทางด้วย Dictionary**](#การค้นข้อมูลสองทิศทางด้วย-dictionary)
-   [**การสร้างสมุดโทรศัพท์**](#การสร้างสมุดโทรศัพท์)
-   [**การตอบคำค้นหา**](#การตอบคำค้นหา)
-   [**รูปแบบการแสดงผล**](#รูปแบบการแสดงผล)
-   [**Solution**](#solution)

---

## การค้นข้อมูลสองทิศทางด้วย Dictionary

Dictionary เหมาะสำหรับการค้นค่าจาก key แต่โจทย์ข้อนี้ต้องค้นได้ 2 ทิศทาง
คือค้นหมายเลขโทรศัพท์จากชื่อ และค้นชื่อจากหมายเลขโทรศัพท์
โปรแกรมจึงสร้าง Dictionary 2 ตัวที่สลับหน้าที่ของ key และ value กัน

| Dictionary | Key | Value | ใช้เมื่อค้นหา |
|---|---|---|---|
| `name_to_telephone` | ชื่อและนามสกุล | หมายเลขโทรศัพท์ | หมายเลขจากชื่อ |
| `telephone_to_name` | หมายเลขโทรศัพท์ | ชื่อและนามสกุล | ชื่อจากหมายเลข |

ตัวอย่างเช่น ข้อมูล `Henry Pym 087-222-2222` จะทำให้เกิดคู่ข้อมูล

```python
name_to_telephone["Henry Pym"] = "087-222-2222"
telephone_to_name["087-222-2222"] = "Henry Pym"
```

> [!NOTE]
>
> หมายเลขโทรศัพท์ถูกเก็บเป็น `str` ไม่ใช่ตัวเลข จึงรักษาเลข `0` ด้านหน้า
> และเครื่องหมาย `-` ไว้ได้ครบถ้วน และโจทย์ข้อนี้ไม่มีการคำนวณหรือปัดเศษตัวเลข

---

## การสร้างสมุดโทรศัพท์

ข้อมูลผู้ใช้บริการแต่ละบรรทัดมี 3 ส่วน ได้แก่ ชื่อ นามสกุล และหมายเลขโทรศัพท์
โปรแกรมแยกทั้ง 3 ส่วนแล้วนำชื่อกับนามสกุลมาต่อกันโดยมีช่องว่าง 1 ช่อง

```python
first_name, last_name, telephone = input().strip().split()
name = f"{first_name} {last_name}"
```

จากนั้นจึงบันทึกข้อมูลทั้งสองทิศทาง

```python
name_to_telephone[name] = telephone
telephone_to_name[telephone] = name
```

การรับข้อมูลแบบนี้หมายความว่าแต่ละรายการต้องมีชื่อ 1 คำ นามสกุล 1 คำ
และหมายเลขโทรศัพท์ 1 คำตามรูปแบบของโจทย์

> [!NOTE]
>
> การกำหนดค่าให้ key เดิมใน Dictionary จะเขียนทับค่าเก่า
> โจทย์ไม่ได้กำหนดวิธีจัดการชื่อหรือหมายเลขที่ซ้ำกัน
> ดังนั้นโค้ดชุดนี้อาศัยข้อมูลสมุดโทรศัพท์ที่แต่ละชื่อและหมายเลขไม่ซ้ำกัน

---

## การตอบคำค้นหา

คำค้นหาอาจเป็นหมายเลขโทรศัพท์ 1 คำ หรือชื่อและนามสกุลที่มีช่องว่างคั่นกลาง
โปรแกรมจึงอ่านทั้งบรรทัดด้วย `input().strip()` โดยไม่เรียก `.split()`

```python
query = input().strip()
```

จากนั้นตรวจสอบ Dictionary ตามลำดับ

1. ถ้า `query in name_to_telephone` ให้แสดงหมายเลขโทรศัพท์ของชื่อนั้น
2. ถ้าไม่พบชื่อ แต่ `query in telephone_to_name` ให้แสดงชื่อของหมายเลขนั้น
3. ถ้าไม่พบทั้งสอง Dictionary ให้แสดง `Not found`

เพราะโปรแกรมใช้ `if` ตามด้วย `elif` การค้นชื่อจะถูกตรวจสอบก่อนการค้นหมายเลข
แต่ข้อมูลปกติมีรูปแบบชื่อและหมายเลขต่างกัน จึงไม่เกิดความกำกวม

ตัวอย่างในโจทย์ให้ผลการค้นหาดังนี้

| คำค้นหา | Dictionary ที่พบ | คำตอบ |
|---|---|---|
| `087-222-2222` | `telephone_to_name` | `Henry Pym` |
| `Steven Rogers` | `name_to_telephone` | `089-444-4444` |
| `Monica Rambeau` | ไม่พบ | `Not found` |
| `911` | ไม่พบ | `Not found` |

โปรแกรมตอบคำค้นหาทันทีภายใน loop จึงแสดงผลตามลำดับที่รับคำค้นหา
โดยไม่มีการเรียงลำดับใหม่

`strip()` ลบช่องว่างเฉพาะด้านหน้าและด้านหลัง แต่ไม่รวมช่องว่างหลายช่อง
ที่อยู่ตรงกลาง ชื่อในสมุดถูกสร้างด้วยช่องว่างตรงกลาง 1 ช่อง
ดังนั้นคำค้นหาชื่อต้องมีรูปแบบตรงกับ key ที่เก็บไว้

---

## รูปแบบการแสดงผล

ข้อความอธิบายข้อมูลส่งออกใน PDF ระบุค่าที่ต้องค้นหา แต่ตัวอย่างใน PDF
แสดงให้เห็นว่าต้องพิมพ์คำค้นหาเดิม ตามด้วย ` --> ` และคำตอบ
โค้ดจึงยึดรูปแบบจากตัวอย่างดังนี้

```text
087-222-2222 --> Henry Pym
Steven Rogers --> 089-444-4444
Monica Rambeau --> Not found
911 --> Not found
```

แต่ละบรรทัดมีช่องว่าง 1 ช่องก่อนและหลัง `-->`
ถ้าค้นพบ โปรแกรมนำค่าจาก Dictionary มาใส่ใน f-string เช่น

```python
print(f"{query} --> {name_to_telephone[query]}")
```

ถ้าค้นไม่พบทั้งชื่อและหมายเลข จะใช้รูปแบบเดียวกันแต่ลงท้ายด้วย `Not found`

```python
print(f"{query} --> Not found")
```

> [!NOTE]
>
> ชื่อ `Telephone Dictionary` ใน README, `Telephone Directory`
> ในส่วนหัวของไฟล์ Python และชื่อภาษาไทย `สมุดหน้าเหลือง` ใน PDF
> เป็นชื่อที่ต่างกันเล็กน้อย แต่ทั้งหมดกล่าวถึงโจทย์เดียวกัน

---

# Solution

```python
# --------------------------------------------------
# File Name : 08_Dict_23.py
# Problem   : Telephone Directory
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Initialize the telephone directory
name_to_telephone = {}
telephone_to_name = {}

# Input the entries in the directory
n = int(input())
for _ in range(n):
    first_name, last_name, telephone = input().strip().split()
    name = f"{first_name} {last_name}"
    name_to_telephone[name] = telephone
    telephone_to_name[telephone] = name

# Search queries in the directory
n = int(input())
for _ in range(n):
    query = input().strip()
    if query in name_to_telephone:
        print(f"{query} --> {name_to_telephone[query]}")

    elif query in telephone_to_name:
        print(f"{query} --> {telephone_to_name[query]}")

    else:
        print(f"{query} --> Not found")
```
