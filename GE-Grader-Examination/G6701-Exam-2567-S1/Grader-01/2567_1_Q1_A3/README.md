<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Image Rotation ★★ (
      <a href="https://drive.google.com/file/d/1w2NXIPMJdgbLTamYX4en2fHmGKXnAClv/view?usp=sharing">
        <code>2567_1_Q1_A3</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเก็บภาพเป็นข้อความ**](#การเก็บภาพเป็นข้อความ)
-   [**การหมุน 90 องศาตามเข็มนาฬิกา**](#การหมุน-90-องศาตามเข็มนาฬิกา)
-   [**การหมุน 180 องศา**](#การหมุน-180-องศา)
-   [**ขนาดและลำดับผลลัพธ์**](#ขนาดและลำดับผลลัพธ์)
-   [**Solution**](#solution)

---

## การเก็บภาพเป็นข้อความ

ภาพในโจทย์ประกอบด้วยอักขระหลายบรรทัด โปรแกรมอ่านจำนวนแถวเป็น `rows` แล้วเก็บ
แต่ละบรรทัดไว้ในลิสต์ `img` ดังนั้น `img[r][c]` หมายถึงอักขระที่แถว `r`
คอลัมน์ `c` โดยดัชนีเริ่มนับจาก `0`

```python
rows = int(input())
img = [input().strip() for _ in range(rows)]
cols = len(img[0])
```

โจทย์รับประกันว่าทุกบรรทัดยาวเท่ากัน จึงใช้ความยาวของ `img[0]` เป็นจำนวน
คอลัมน์ `cols` ได้ จากนั้นอ่านคำสั่ง `rot90` หรือ `rot180` อีกหนึ่งบรรทัด

> [!NOTE]
>
> โค้ดใช้ `input().strip()` จึงตัดช่องว่างที่อยู่ซ้ายและขวาสุดของแต่ละแถว
> การทำงานนี้อาศัยชุดทดสอบที่ไม่มีช่องว่างรอบนอกซึ่งเป็นส่วนสำคัญของภาพ

## การหมุน 90 องศาตามเข็มนาฬิกา

เมื่อหมุนตามเข็มนาฬิกา 90 องศา คอลัมน์เดิมแต่ละคอลัมน์จะกลายเป็นแถวใหม่
โดยต้องอ่านจากแถวล่างขึ้นแถวบน โค้ดจึงให้วงวนนอกเลือกคอลัมน์ `c` จากซ้ายไปขวา
และวงวนในเลือกแถว `r` ย้อนจาก `rows - 1` ลงถึง `0`

```python
for c in range(cols):
    line = ""
    for r in range(rows - 1, -1, -1):
        line += img[r][c]
    modified_img.append(line)
```

ตัวอย่างภาพขนาด 2 แถว 3 คอลัมน์

```text
abc
def
```

คอลัมน์แรกอ่านจากล่างขึ้นบนได้ `da` คอลัมน์ถัดไปได้ `eb` และ `fc` ผลหลัง
หมุนจึงเป็น

```text
da
eb
fc
```

## การหมุน 180 องศา

การหมุน 180 องศาต้องกลับทั้งลำดับแถวและลำดับอักขระในแต่ละแถว โปรแกรมจึง
ไล่ `r` จากแถวสุดท้ายกลับมาแถวแรก และใช้ `img[r][::-1]` กลับข้อความในแถวนั้น

```python
for r in range(rows - 1, -1, -1):
    modified_img.append(img[r][::-1])
```

สำหรับภาพตัวอย่างเดิม แถว `def` ถูกนำมาก่อนและกลับเป็น `fed` แล้วแถว `abc`
กลับเป็น `cba` ผลลัพธ์จึงเป็น

```text
fed
cba
```

> [!NOTE]
>
> `[::-1]` กลับเฉพาะอักขระภายในหนึ่งแถว การหมุน 180 องศาจึงยังต้องวนแถว
> จากท้ายมาหน้าด้วย หากทำเพียงอย่างใดอย่างหนึ่งจะเป็นการพลิกภาพ ไม่ใช่การหมุน

## ขนาดและลำดับผลลัพธ์

-   `rot90` เปลี่ยนภาพขนาด `rows × cols` เป็น `cols × rows` จึงแสดงทั้งหมด
    `cols` บรรทัด และแต่ละบรรทัดยาว `rows` อักขระ
-   `rot180` ยังคงมี `rows` บรรทัด บรรทัดละ `cols` อักขระ
-   โปรแกรมสะสมบรรทัดที่หมุนแล้วใน `modified_img` ตามลำดับบนลงล่าง จากนั้น
    ใช้ `print(line)` แสดงทีละบรรทัดโดยไม่มีช่องว่างหรือเครื่องหมายอื่นเพิ่ม

แนวทางนี้ทำงานได้กับภาพสี่เหลี่ยมผืนผ้า ไม่จำเป็นต้องมีจำนวนแถวเท่ากับจำนวน
คอลัมน์ โดยเฉพาะกรณี `rot90` ต้องระวังว่าจำนวนแถวและคอลัมน์ของผลลัพธ์จะสลับกัน

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q1_A3.py
# Problem   : Image Rotation
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
if cmd == "rot90":
    for c in range(cols):
        line = ""
        for r in range(rows - 1, -1, -1):
            line += img[r][c]
        modified_img.append(line)

# Rotate the image by 180 degrees
elif cmd == "rot180":
    for r in range(rows - 1, -1, -1):
        modified_img.append(img[r][::-1])

# Output the modified image
for line in modified_img:
    print(line)
```
