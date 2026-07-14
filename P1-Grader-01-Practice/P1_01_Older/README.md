<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Older ★☆ (
      <a href="https://drive.google.com/file/d/1YN9OMxSfGfOwWz8Qk8Hn3UuJl-xrfQ6D/view?usp=drive_link">
        <code>P1_01_Older</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**รูปแบบข้อมูลนำเข้า**](#รูปแบบข้อมูลนำเข้า)
-   [**แปลงวันเกิดให้อยู่ในรูปที่เปรียบเทียบได้**](#แปลงวันเกิดให้อยู่ในรูปที่เปรียบเทียบได้)
-   [**เปรียบเทียบวันเกิดและแสดงผล**](#เปรียบเทียบวันเกิดและแสดงผล)
-   [**Solution**](#solution)

---

## รูปแบบข้อมูลนำเข้า

โจทย์ให้วันเกิดของคน 2 คน คนละ 1 บรรทัด โดยแต่ละบรรทัดมีข้อมูล 4 ส่วน
เรียงเป็น ชื่อเล่น ชื่อเดือน วัน และปี พ.ศ. เช่น

```
Jane March 23, 2543
```

คำสั่ง `input().strip().split()` แบ่งบรรทัดนี้ตามช่องว่าง แล้วนำค่า 4 ส่วน
ไปเก็บในตัวแปรด้วยการ unpack

```python
name01, m1, d1, y1 = input().strip().split()
```

จึงได้ `name01 == "Jane"`, `m1 == "March"`, `d1 == "23,"` และ
`y1 == "2543"` สังเกตว่าวันยังมีเครื่องหมายจุลภาคติดอยู่

---

## แปลงวันเกิดให้อยู่ในรูปที่เปรียบเทียบได้

ข้อความชื่อเดือนยังนำมาเรียงตามเวลาโดยตรงไม่ได้ โปรแกรมจึงเก็บชื่อเดือนทั้ง 12
ไว้ในลิสต์ `MONTH` แล้วใช้ `MONTH.index(m1) + 1` แปลงชื่อเดือนเป็นเลขเดือน
เช่น `March` อยู่ที่ index `2` เมื่อบวก `1` จึงได้เดือน `3`

ส่วน `d1.strip(",")` นำจุลภาคออกจาก `"23,"` ให้เหลือ `"23"`
ก่อนใช้ `int()` แปลงวันและปีจากข้อความเป็นจำนวนเต็ม จากนั้นรวมข้อมูลเป็นลิสต์
ตามลำดับ `[ปี, เดือน, วัน]`

```python
birthday01 = [int(y1), MONTH.index(m1) + 1, int(d1.strip(","))]
```

ตัวอย่างเช่น วันเกิดของ Jane จะกลายเป็น `[2543, 3, 23]`

> [!NOTE]
>
> Python เปรียบเทียบลิสต์จากซ้ายไปขวา เมื่อเขียนเป็น `[ปี, เดือน, วัน]`
> โปรแกรมจึงเทียบปีก่อน ถ้าปีเท่ากันจึงเทียบเดือน และถ้าเดือนเท่ากันจึงเทียบวัน

ชื่อเดือนที่รับเข้ามาต้องสะกดและใช้ตัวพิมพ์ใหญ่-เล็กตรงกับชื่อใน `MONTH`
เช่น `March` เพราะ `list.index()` จะค้นหาข้อความแบบตรงตัว

---

## เปรียบเทียบวันเกิดและแสดงผล

วันเกิดที่มีค่าน้อยกว่าคือวันที่เกิดก่อน ดังนั้นคนนั้นจึงอายุมากกว่า เช่น

```
Jane -> [2543, 3, 23]
Kate -> [2544, 6, 9]
```

เนื่องจาก `[2543, 3, 23] < [2544, 6, 9]` โปรแกรมจึงแสดง `Jane`

เงื่อนไขการแสดงผลครบทั้ง 3 กรณีคือ

-   ถ้า `birthday01 < birthday02` ให้แสดงชื่อคนแรก
-   ถ้า `birthday01 > birthday02` ให้แสดงชื่อคนที่สอง
-   ถ้าวันเกิดเท่ากัน ให้ `print(name01, name02)` แสดงทั้งสองชื่อในบรรทัดเดียว
    คั่นด้วยช่องว่าง และรักษาลำดับเดียวกับข้อมูลนำเข้า

---

# Solution

```python
# --------------------------------------------------
# File Name : P1_01_Older.py
# Problem   : Part-I Older
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# List of month names
MONTH = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# Input first person's name and birthday
name01, m1, d1, y1 = input().strip().split()
birthday01 = [int(y1), MONTH.index(m1) + 1, int(d1.strip(","))]

# Input second person's name and birthday
name02, m2, d2, y2 = input().strip().split()
birthday02 = [int(y2), MONTH.index(m2) + 1, int(d2.strip(","))]

# Compare the two birthdays and output the older person
if birthday01 < birthday02:
    print(name01)
elif birthday01 > birthday02:
    print(name02)
else:
    print(name01, name02)
```
