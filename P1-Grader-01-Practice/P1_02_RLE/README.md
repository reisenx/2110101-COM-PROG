<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    RLE ★★ (
      <a href="https://drive.google.com/file/d/1xbPthJmwu74ThTo_pm99cJfS2WJHIkOE/view?usp=drive_link">
        <code>P1_02_RLE</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**รู้จัก Run-Length Encoding**](#รู้จัก-run-length-encoding)
-   [**แปลงสตริงเป็น RLE**](#แปลงสตริงเป็น-rle)
-   [**แปลง RLE กลับเป็นสตริง**](#แปลง-rle-กลับเป็นสตริง)
-   [**เลือกการทำงานจากคำสั่ง**](#เลือกการทำงานจากคำสั่ง)
-   [**Solution**](#solution)

---

## รู้จัก Run-Length Encoding

Run-Length Encoding หรือ RLE คือการแทนกลุ่มอักขระที่เหมือนกันและอยู่ติดกัน
ด้วยคู่ `อักขระ จำนวนครั้ง` ตัวอย่างเช่น

```
AAABBCCA -> A 3 B 2 C 2 A 1
```

ตัว `A` ชุดสุดท้ายต้องเป็นอีกคู่หนึ่ง เพราะไม่ได้อยู่ติดกับ `A` สามตัวแรก
RLE จึงนับความยาวของแต่ละ **ช่วงที่ต่อเนื่องกัน** ไม่ได้นับจำนวนรวมทั้งข้อความ

โจทย์กำหนดให้บรรทัดแรกเป็นคำสั่ง และใช้บรรทัดที่สองเป็นข้อมูลเฉพาะเมื่อคำสั่ง
เป็น `str2RLE` หรือ `RLE2str`

---

## แปลงสตริงเป็น RLE

เมื่อ `cmd == "str2RLE"` โปรแกรมอ่านข้อความที่จะเข้ารหัส แล้วเริ่มช่วงแรกด้วย
อักขระตัวแรกและจำนวน `1`

```python
char = text[0]
count = 1
```

ลูปเริ่มที่ index `1` เพราะ index `0` ถูกนำมาใช้ตั้งต้นแล้ว ในแต่ละรอบมี 2 กรณี

-   ถ้า `text[i] == char` แสดงว่ายังอยู่ในช่วงเดิม จึงเพิ่ม `count` อีก `1`
-   ถ้าอักขระเปลี่ยน โปรแกรมนำช่วงเดิมต่อท้าย `result` ในรูป
    `f"{char} {count} "` แล้วตั้ง `char` และ `count` เพื่อเริ่มช่วงใหม่

ตัวอย่างการอ่าน `AAABB` จะนับ `A` จนได้ `count == 3` เมื่อพบ `B` ตัวแรก
จึงบันทึก `A 3` แล้วเริ่มนับช่วงของ `B`

หลังลูปจบ จะไม่มีอักขระตัวใหม่มากระตุ้นกรณีที่อักขระเปลี่ยน โปรแกรมจึงต้อง
นำช่วงสุดท้ายมาต่อเพิ่มเอง

```python
result += f"{char} {count}"
```

ส่วนนี้ยังตั้งใจไม่เติมช่องว่างท้ายผลลัพธ์ ทำให้ทุกคู่คั่นด้วยช่องว่างพอดี

> [!WARNING]
>
> โค้ดชุดนี้ใช้ `text[0]` จึงสมมติว่าข้อความสำหรับ `str2RLE` ไม่เป็นสตริงว่าง
> ซึ่งเป็นรูปแบบข้อมูลที่โจทย์นำมาใช้ หากส่งบรรทัดว่างจะเกิด `IndexError`

---

## แปลง RLE กลับเป็นสตริง

เมื่อ `cmd == "RLE2str"` คำสั่ง `text.split()` จะแบ่งข้อมูล RLE เป็นลิสต์สลับกัน
ระหว่างอักขระกับจำนวนครั้ง เช่น

```python
parts = "A 3 B 2 C 1".split()
# parts == ["A", "3", "B", "2", "C", "1"]
```

ลูป `range(0, len(parts), 2)` จึงเลือก index `0, 2, 4, ...` ซึ่งเป็นตำแหน่ง
ของอักขระ ส่วนสมาชิกถัดไปที่ `i + 1` คือจำนวนครั้ง

```python
char = parts[i]
count = int(parts[i + 1])
result += char * count
```

ใน Python การคูณสตริง เช่น `"A" * 3` ให้ผลเป็น `"AAA"`
เมื่อนำผลของทุกคู่มาต่อกัน `A 3 B 2 C 1` จึงกลับเป็น `AAABBC`

ข้อมูล RLE ที่ถูกต้องสำหรับโค้ดนี้ต้องมีสมาชิกเป็นคู่ครบถ้วน และจำนวนครั้ง
ต้องเป็นข้อความที่ `int()` แปลงได้ หากขาดสมาชิกหรือจำนวนไม่ใช่จำนวนเต็ม
โปรแกรมจะเกิดข้อผิดพลาดแทนการสร้างผลลัพธ์

---

## เลือกการทำงานจากคำสั่ง

โปรแกรมตรวจคำสั่งแบบตรงตัวและแยกการทำงานดังนี้

-   `str2RLE` อ่านอีก 1 บรรทัด แล้วแสดง RLE
-   `RLE2str` อ่านอีก 1 บรรทัด แล้วแสดงสตริงที่ถอดรหัส
-   คำสั่งอื่น เช่น `str2str` ไม่อ่านข้อมูลเพิ่ม และกำหนด `result = "Error"`

ทุกกรณีใช้ `print(result)` เพียงครั้งเดียวตอนท้าย จึงได้ผลลัพธ์ 1 บรรทัด

---

# Solution

```python
# --------------------------------------------------
# File Name : P1_02_RLE.py
# Problem   : Part-I RLE
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input command
cmd = input().strip()

# Initialize result variable
result = ""

# Convert string to RLE
if cmd == "str2RLE":
    # Input text
    text = input().strip()

    # Initialize counter
    char = text[0]
    count = 1

    # Iterate through the text
    for i in range(1, len(text)):
        if text[i] == char:
            count += 1
        else:
            result += f"{char} {count} "
            char = text[i]
            count = 1
    # Append the last character and its count
    result += f"{char} {count}"

# Convert RLE to string
elif cmd == "RLE2str":
    # Input text
    text = input().strip()

    # Split the input text into parts
    parts = text.split()

    # Iterate through the parts in pairs
    for i in range(0, len(parts), 2):
        char = parts[i]
        count = int(parts[i + 1])
        result += char * count
else:
    result = "Error"

# Output the result
print(result)
```
