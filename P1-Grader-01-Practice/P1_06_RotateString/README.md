<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Rotate String ★★★ (
      <a href="https://drive.google.com/file/d/1Ms1AhMxEaiGeOR3I9wMfwIeC27iwGTCP/view?usp=drive_link">
        <code>P1_06_RotateString</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**เก็บภาพเป็นรายการของสตริง**](#เก็บภาพเป็นรายการของสตริง)
-   [**ตรวจสอบขนาดของภาพ**](#ตรวจสอบขนาดของภาพ)
-   [**หมุนตามเข็มนาฬิกา 90 องศา**](#หมุนตามเข็มนาฬิกา-90-องศา)
-   [**หมุน 180 องศาและกลับซ้ายขวา**](#หมุน-180-องศาและกลับซ้ายขวา)
-   [**แสดงผลและจัดการข้อมูลที่ไม่ถูกต้อง**](#แสดงผลและจัดการข้อมูลที่ไม่ถูกต้อง)
-   [**Solution**](#solution)

---

## เก็บภาพเป็นรายการของสตริง

โจทย์มองชุดข้อความเป็นภาพสี่เหลี่ยม โดยตัวอักษรหนึ่งตัวแทนหนึ่งช่องของภาพ
โปรแกรมอ่านคำสั่งไว้ใน `cmd` อ่านจำนวนแถวไว้ใน `row`
แล้วเก็บข้อความแต่ละแถวไว้ในลิสต์ `img`

```python
cmd = input().strip()
row = int(input())
img = [input().strip() for _ in range(row)]
```

ตัวอย่างเช่น ภาพสามแถวสี่คอลัมน์จะถูกเก็บดังนี้

```text
img[0] = "ABCD"
img[1] = "1234"
img[2] = "WXYZ"
```

การเข้าถึงตัวอักษรใช้ `img[r][c]` โดย `r` คือดัชนีแถวและ `c` คือดัชนีคอลัมน์
ทั้งสองดัชนีเริ่มจาก `0` ส่วน `.strip()` ทำตามข้อกำหนดของโจทย์โดยตัดช่องว่าง
และอักขระขึ้นบรรทัดใหม่ที่หัวหรือท้ายข้อมูลก่อนประมวลผล

## ตรวจสอบขนาดของภาพ

ภาพที่จะหมุนได้ต้องมีจำนวนตัวอักษรเท่ากันทุกแถว โปรแกรมใช้ความยาวของ
แถวแรกเป็นจำนวนคอลัมน์อ้างอิง

```python
col = len(img[0])
```

จากนั้นวนตรวจทุก `line` ถ้าพบ `len(line) != col` จะเปลี่ยน `is_valid`
เป็น `False` แสดง `Invalid size` แล้วใช้ `break` หยุดตรวจทันที
จึงแสดงข้อความผิดพลาดเพียงครั้งเดียว แม้จะมีหลายแถวที่ยาวไม่เท่ากัน

> [!NOTE]
>
> การเข้าถึง `img[0]` หมายความว่าโค้ดนี้อาศัยเงื่อนไขข้อมูลเข้าของโจทย์ว่า
> มีข้อความอย่างน้อยหนึ่งแถว

## หมุนตามเข็มนาฬิกา 90 องศา

ถ้าภาพเดิมมี `row` แถวและ `col` คอลัมน์ ภาพหลังหมุน 90 องศาจะมี
`col` แถวและ `row` คอลัมน์ โปรแกรมจึงวนคอลัมน์เดิมจากซ้ายไปขวา
ด้วย `for c in range(col)` เพื่อสร้างแต่ละแถวใหม่

ภายในแต่ละคอลัมน์ โปรแกรมอ่านแถวเดิมจากล่างขึ้นบน

```python
for r in range(row - 1, -1, -1):
    line += img[r][c]
```

ดังนั้นแถวใหม่หมายเลข `c` คือ
`img[row - 1][c] + img[row - 2][c] + ... + img[0][c]`
หรือมองเป็นตำแหน่งได้ว่าอักขระเดิม `img[r][c]`
จะไปอยู่ที่แถว `c` คอลัมน์ `row - 1 - r` ของภาพใหม่

จากภาพตัวอย่าง

```text
ABCD
1234
WXYZ
```

เมื่อ `c` เป็น `0` โปรแกรมอ่าน `W`, `1`, `A` จากล่างขึ้นบน จึงได้แถวแรก
เป็น `W1A` ทำเช่นเดียวกันจนครบทุกคอลัมน์แล้วได้

```text
W1A
X2B
Y3C
Z4D
```

## หมุน 180 องศาและกลับซ้ายขวา

คำสั่ง `180` ต้องกลับภาพทั้งแนวบน-ล่างและแนวซ้าย-ขวา โปรแกรมจึง

1.  วนแถวจาก `row - 1` ลงมาถึง `0` เพื่ออ่านแถวล่างก่อน
2.  ใช้ `img[r][::-1]` กลับลำดับตัวอักษรในแต่ละแถว

เช่น

```text
ABCD       4321
1234  ->   DCBA
```

ส่วนคำสั่ง `flip` กลับเฉพาะแนวซ้าย-ขวา จึงอ่านแถวตามลำดับเดิม
`0, 1, ..., row - 1` แต่ยังใช้ `[::-1]` กับทุกแถว

| คำสั่ง | ลำดับแถว | ลำดับตัวอักษรในแถว |
|:---:|:---|:---|
| `180` | ล่างขึ้นบน | ขวาไปซ้าย |
| `flip` | บนลงล่างเหมือนเดิม | ขวาไปซ้าย |

## แสดงผลและจัดการข้อมูลที่ไม่ถูกต้อง

ถ้าทุกแถวยาวเท่ากัน โปรแกรมจะสร้าง `modified_img` ตามคำสั่ง
แล้วใช้ลูปแสดงผลทีละแถว

```python
for line in modified_img:
    print(line)
```

แต่ถ้าขนาดไม่ถูกต้อง `is_valid` จะเป็น `False` ทำให้ข้ามส่วนหมุนภาพทั้งหมด
ผลลัพธ์จึงมีเพียง `Invalid size` เท่านั้น ส่วนข้อมูลเข้าตามข้อกำหนดจะใช้คำสั่ง
หนึ่งใน `90`, `180` หรือ `flip`; หากเป็นข้อความอื่น โค้ดนี้จะไม่เพิ่มแถวใดลงใน
`modified_img` และไม่แสดงผล

---

# Solution

```python
# --------------------------------------------------
# File Name : P1_06_RotateString.py
# Problem   : Part-I Rotate String
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input command to modify the image
cmd = input().strip()

# Input original image
row = int(input())
img = [input().strip() for _ in range(row)]

# Validate the image size
is_valid = True
col = len(img[0])
for line in img:
    if len(line) != col:
        is_valid = False
        print("Invalid size")
        break

# Modify the image based on the command
if is_valid:
    # Initialize the modified image
    modified_img = []
    # Rotate the image by 90 degrees clockwise
    if cmd == "90":
        for c in range(col):
            line = ""
            for r in range(row - 1, -1, -1):
                line += img[r][c]
            modified_img.append(line)

    # Rotate the image by 180 degrees
    elif cmd == "180":
        for r in range(row - 1, -1, -1):
            modified_img.append(img[r][::-1])

    # Flip the image horizontally
    elif cmd == "flip":
        for r in range(row):
            modified_img.append(img[r][::-1])

    # Output the modified image
    for line in modified_img:
        print(line)
```
