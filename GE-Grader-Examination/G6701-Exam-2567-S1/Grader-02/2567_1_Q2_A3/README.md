<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Image Flip ★☆ (
      <a href="https://drive.google.com/file/d/1ubTd8JIen2MJeLl6EGGRO86ZEGh-YOYs/view?usp=sharing">
        <code>2567_1_Q2_A3</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเก็บภาพเป็นรายการข้อความ**](#การเก็บภาพเป็นรายการข้อความ)
-   [**การกลับภาพตามแนวนอน**](#การกลับภาพตามแนวนอน)
-   [**การกลับภาพตามแนวดิ่ง**](#การกลับภาพตามแนวดิ่ง)
-   [**ข้อสังเกตเกี่ยวกับโค้ด**](#ข้อสังเกตเกี่ยวกับโค้ด)
-   [**Solution**](#solution)

---

## การเก็บภาพเป็นรายการข้อความ

ภาพในโจทย์นี้ประกอบด้วยข้อความหลายบรรทัด โดยทุกบรรทัดมีจำนวนอักขระเท่ากัน
โปรแกรมจึงเก็บภาพเป็น `list` ที่สมาชิกแต่ละตัวแทนหนึ่งแถวของภาพ

```python
rows = int(input())
img = [input().strip() for _ in range(rows)]
```

ถ้า `img = ["abc", "def"]` จะมองได้ว่าเป็นภาพสูง `2` แถว กว้าง `3`
คอลัมน์ แม้โปรแกรมจะคำนวณความกว้างไว้ใน `cols` แต่การกลับภาพทั้งสองแบบด้านล่าง
ไม่จำเป็นต้องนำตัวแปรนี้มาใช้ต่อ

> [!NOTE]
>
> `strip()` ตัดช่องว่างที่อยู่ซ้ายและขวาสุดของแต่ละบรรทัด
> โค้ดนี้จึงอาศัยเงื่อนไขของชุดทดสอบว่า ช่องว่างส่วนนั้นไม่ใช่ส่วนสำคัญของภาพ

---

## การกลับภาพตามแนวนอน

คำสั่ง `hflip` กลับซ้ายเป็นขวา แต่ยังคงลำดับแถวเดิมไว้
การเขียน `row[::-1]` คือการอ่านอักขระในแถวนั้นจากท้ายมาหาต้น

```python
for row in img:
    modified_img.append(row[::-1])
```

ตัวอย่างเช่น แถว `"abc"` จะกลายเป็น `"cba"` ดังนั้น

```text
abc       cba
def  -->  fed
```

---

## การกลับภาพตามแนวดิ่ง

คำสั่ง `vflip` สลับแถวบนกับแถวล่าง แต่ไม่กลับอักขระภายในแถว
จึงใช้ `img[::-1]` เพื่ออ่านรายการแถวจากท้ายมาหาต้นได้โดยตรง

```python
modified_img = img[::-1]
```

จากภาพตัวอย่างเดิม ผลลัพธ์จึงเป็น

```text
abc       def
def  -->  abc
```

หลังเลือกวิธีแล้ว ลูปสุดท้ายแสดงสมาชิกของ `modified_img` ตามลำดับ
ทีละหนึ่งบรรทัด ทำให้จำนวนแถวและจำนวนคอลัมน์ยังเท่าเดิม

---

## ข้อสังเกตเกี่ยวกับโค้ด

> [!WARNING]
>
> คอมเมนต์ในโค้ดต้นฉบับเขียนว่าเป็นการหมุน `90` และ `180` องศา
> แต่คำสั่งที่ตรวจจริงคือ `hflip` และ `vflip` และตัวโค้ดทำงานเป็นการ
> **กลับภาพ** ตามแนวนอนและแนวดิ่งตามโจทย์ ไม่ใช่การหมุนภาพ

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q2_A3.py
# Problem   : Image Flip
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input number of rows and the image
rows = int(input())
img = [input().strip() for _ in range(rows)]

# Find the number of columns
cols = len(img[0])

# Initialize the modified image
modified_img = []

# Input command to modify the image
cmd = input().strip()

# Rotate the image by 90 degrees clockwise
if cmd == "hflip":
    for row in img:
        modified_img.append(row[::-1])

# Rotate the image by 180 degrees
elif cmd == "vflip":
    modified_img = img[::-1]

# Output the modified image
for line in modified_img:
    print(line)
```
