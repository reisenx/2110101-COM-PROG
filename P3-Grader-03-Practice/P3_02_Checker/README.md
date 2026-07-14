<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Giant Checker ★★★ (
      <a href="https://drive.google.com/file/d/1yxHWqPdlpDYGA5fi5GwBWQIgUZU1_xvg/view?usp=drive_link">
        <code>P3_02_Checker</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แปลงชื่อช่องเป็นเลขแถวและคอลัมน์**](#แปลงชื่อช่องเป็นเลขแถวและคอลัมน์)
-   [**แยกข้อมูลนำเข้าสองรูปแบบ**](#แยกข้อมูลนำเข้าสองรูปแบบ)
-   [**ตรวจสอบความถูกต้องของแถวและคอลัมน์**](#ตรวจสอบความถูกต้องของแถวและคอลัมน์)
-   [**หาสีของช่องด้วยเลขคู่และเลขคี่**](#หาสีของช่องด้วยเลขคู่และเลขคี่)
-   [**ลำดับการทำงานของโปรแกรม**](#ลำดับการทำงานของโปรแกรม)
-   [**Solution**](#solution)

---

## แปลงชื่อช่องเป็นเลขแถวและคอลัมน์

ตารางในโจทย์มีขนาด `52 x 52` แต่ละช่องระบุด้วย **แถว** และ **คอลัมน์**

-   แถวเรียงจาก `a` ถึง `z` แล้วต่อด้วย `A` ถึง `Z`
-   คอลัมน์เป็นจำนวนเต็มตั้งแต่ `1` ถึง `52`

โปรแกรมเก็บตัวอักษรของทุกแถวไว้ตามลำดับ

```python
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

ตำแหน่งในสตริงเริ่มนับจาก `0` แต่หมายเลขแถวในโจทย์เริ่มนับจาก `1`
จึงต้องบวก `1` หลังใช้ `index()`

```python
row = ALPHABET.index(row_str) + 1
```

ตัวอย่างเช่น `a` เป็นแถวที่ `1`, `z` เป็นแถวที่ `26`,
`A` เป็นแถวที่ `27` และ `Z` เป็นแถวที่ `52`
ส่วนเลขคอลัมน์ใช้ค่าที่อ่านได้โดยตรง

ข้อมูลนำเข้ามีเพียง `1` บรรทัด โปรแกรมใช้ `input().strip()`
เพื่อตัดช่องว่างที่ต้นและท้ายทั้งบรรทัดก่อนแยกแถวกับคอลัมน์
โจทย์รับรองว่าข้อมูลมีอย่างน้อย `1` ตัวอักษร
และตัวแรกหลังตัดช่องว่างไม่ใช่ช่องว่าง

---

## แยกข้อมูลนำเข้าสองรูปแบบ

โจทย์รับตำแหน่งช่องได้ `2` รูปแบบ
โปรแกรมตัดสินรูปแบบจากความยาวของสตริงหลัง `strip()`

### รูปแบบสั้น

ถ้าความยาวไม่เกิน `3` ตัวอักษร ตัวแรกคือแถว
และตัวที่เหลือทั้งหมดคือคอลัมน์

```python
row_str = string[0].strip()
col_str = string[1:].strip()
```

ตัวอย่าง `z03` จะได้ `row_str == "z"` และ `col_str == "03"`
ช่องว่างที่อยู่ก่อนเลขคอลัมน์ เช่น `"9 9"`
จะถูกตัดออกจาก `col_str` แต่ `"9"` ตัวแรกยังคงเป็นค่าแถวที่ไม่ถูกต้อง

### รูปแบบระบุชื่อ row และ col

ถ้าความยาวมากกว่า `3` ตัวอักษร
โปรแกรมคาดหวังส่วนประกอบ `row` และ `col`
โดยอนุญาตให้สลับลำดับและมีช่องว่างรอบส่วนต่าง ๆ ได้ เช่น

```text
row = A, col = 02
col=2,row=A
```

การแยกข้อมูลเริ่มจากแทนจุลภาคด้วยเครื่องหมายเท่ากับ
แล้วแยกสตริงทุกตำแหน่งที่มีเครื่องหมายเท่ากับ

```python
parts = [p.strip() for p in string.replace(",", "=").split("=")]
```

ตัวอย่าง `"col = 2, row = A"` จะกลายเป็น

```python
["col", "2", "row", "A"]
```

โปรแกรมยอมรับต่อเมื่อได้ครบ `4` ส่วน
และชื่อส่วนเป็น `row` กับ `col` อย่างละหนึ่งครั้งในลำดับใดลำดับหนึ่ง
จึงกำหนด `row_str` และ `col_str` ให้ตรงกับชื่อของข้อมูล

> [!NOTE]
>
> คำอธิบายใน PDF ระบุว่ารูปแบบที่สองมีความยาวตั้งแต่ `3` ตัวอักษรขึ้นไป
> ซึ่งทับซ้อนกับรูปแบบสั้นที่มีความยาวไม่เกิน `3` ตัวอักษร
> แต่โครงโปรแกรมใน PDF และโค้ด Solution ใช้เงื่อนไขเดียวกันคือ
> `len(string) <= 3` สำหรับรูปแบบสั้น และใช้รูปแบบที่สองเมื่อยาวกว่า `3`
> โดยข้อมูลรูปแบบที่สองที่เขียนครบยาวเกิน `3` อยู่แล้ว

---

## ตรวจสอบความถูกต้องของแถวและคอลัมน์

ฟังก์ชันทั้งสองเริ่มต้นค่าที่แปลงแล้วด้วย `-1`
เพื่อใช้เป็นเครื่องหมายว่าข้อมูลส่วนนั้นยังไม่ถูกต้อง

แถวจะถูกต้องเมื่อเป็นตัวอักษรเพียง `1` ตัวและอยู่ใน `ALPHABET`

```python
if row_str in ALPHABET and len(row_str) == 1:
    row = ALPHABET.index(row_str) + 1
```

คอลัมน์จะถูกต้องเมื่อประกอบด้วยตัวเลขทั้งหมด
และค่าหลังแปลงเป็นจำนวนเต็มอยู่ในช่วง `1` ถึง `52`

```python
if col_str.isdigit() and 1 <= int(col_str) <= 52:
    col = int(col_str)
```

`isdigit()` ป้องกันไม่ให้เรียก `int()` กับข้อความที่ไม่ใช่ตัวเลข
ส่วนการแปลงด้วย `int()` ทำให้เลขศูนย์ด้านหน้าไม่มีผล
เช่น `z03` ในรูปแบบสั้นและ `"col=0003,row=z"` ในรูปแบบที่สอง
ต่างก็หมายถึงคอลัมน์ `3`

หลังตรวจครบแล้ว โปรแกรมแสดงผลตามสถานะดังนี้

| ค่า `row` | ค่า `col` | ผลลัพธ์ |
| --- | --- | --- |
| `-1` | `-1` | `Invalid row and column` |
| `-1` | ค่าที่ถูกต้อง | `Invalid row` |
| ค่าที่ถูกต้อง | `-1` | `Invalid column` |
| ค่าที่ถูกต้อง | ค่าที่ถูกต้อง | ตรวจสีของช่องต่อ |

ชื่อ `row` และ `col` ในรูปแบบที่สองต้องเขียนด้วยตัวพิมพ์เล็กตามนี้
ถ้ามีส่วนเกิน เครื่องหมายเกิน หรือชื่อส่วนไม่ตรง
รายการ `parts` จะไม่เข้าเงื่อนไขและทั้งสองค่าจะยังเป็น `-1`

> [!WARNING]
>
> comment ใน Solution ยกตัวอย่างรูปแบบที่สองว่า `"row=1, col=2"`
> แต่ค่าแถว `1` ไม่ถูกต้องตามโจทย์และตามโค้ดจริง
> แถวต้องเป็นตัวอักษรเพียงหนึ่งตัวตั้งแต่ `a` ถึง `z` หรือ `A` ถึง `Z`
> ตัวอย่างรูปแบบที่ถูกต้องควรเป็น `"row=A, col=2"`

---

## หาสีของช่องด้วยเลขคู่และเลขคี่

สีของตารางสลับกันทุกครั้งที่เลื่อนไปหนึ่งแถวหรือหนึ่งคอลัมน์
เมื่อใช้หมายเลขแถวและคอลัมน์แบบเริ่มจาก `1`
ช่องจะเป็นสีขาวเมื่อทั้งคู่มีเศษจากการหารด้วย `2` เท่ากัน

\[
row\bmod 2 = col\bmod 2
\]

ใน Python เขียนเป็น

```python
row % 2 == col % 2
```

-   `b2` คือแถว `2` และคอลัมน์ `2` ทั้งคู่เป็นเลขคู่ จึงแสดง `White`
-   `z03` คือแถว `26` และคอลัมน์ `3` มีความเป็นคู่คี่ต่างกัน
    จึงแสดง `Black`

> [!NOTE]
>
> โปรแกรมตัวอย่างขนาด `3 x 3` ใน PDF ใช้ `find()`
> จึงได้หมายเลขแถวแบบเริ่มจาก `0` และแสดง `Black` เมื่อเศษเท่ากัน
> ส่วน Solution บวก `1` ให้เป็นหมายเลขแถวตามโจทย์
> จึงแสดง `White` เมื่อเศษเท่ากัน ทั้งสองวิธีให้สีของช่องเดียวกันตรงกัน
> เพราะการบวก `1` ทำให้ความเป็นคู่คี่ของหมายเลขแถวสลับไป

---

## ลำดับการทำงานของโปรแกรม

การทำงานทั้งหมดเรียงตามลำดับนี้

1.  อ่านข้อมูลหนึ่งบรรทัดและตัดช่องว่างที่ต้นกับท้าย
2.  เลือก `pattern01_parser()` เมื่อความยาวไม่เกิน `3`
    มิฉะนั้นเลือก `pattern02_parser()`
3.  แปลงแถวและคอลัมน์ โดยเก็บ `-1` ไว้สำหรับส่วนที่ไม่ถูกต้อง
4.  ตรวจกรณีผิดทั้งคู่ก่อน แล้วจึงตรวจแถวและคอลัมน์ทีละส่วน
5.  ถ้าทั้งคู่ถูกต้อง จึงเปรียบเทียบเศษจากการหารด้วย `2` และแสดงสี

การเรียงเงื่อนไขข้อผิดพลาดจากกรณีผิดทั้งคู่ก่อนมีความสำคัญ
เพราะหนึ่งข้อมูลนำเข้าต้องแสดงผลเพียง `1` บรรทัด
โปรแกรมไม่เติมช่องว่าง ไม่ปัดเศษ และไม่เปลี่ยนตัวพิมพ์เล็กหรือตัวพิมพ์ใหญ่
ข้อความผลลัพธ์จึงต้องตรงตามที่กำหนดทุกตัวอักษร

---

# Solution

```python
# --------------------------------------------------
# File Name : P3_02_Checker.py
# Problem   : Part-III Giant Checker
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# Constants for character to number mapping
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Parse the input string into row and column numbers
# This pattern supports formats: "A1", "B2", ..., "Z52"
def pattern01_parser(string):
    # Initialize row and column to -1 (invalid)
    row, col = -1, -1
    # Extract the first character as row and the rest as column
    row_str = string[0].strip()
    col_str = string[1:].strip()

    # Check if the row is a valid letter
    if row_str in ALPHABET and len(row_str) == 1:
        row = ALPHABET.index(row_str) + 1
    # Check if the column is a valid number between 1 and 52
    if col_str.isdigit() and 1 <= int(col_str) <= 52:
        col = int(col_str)
    # Return the row and column as a list
    return [row, col]


# Parse the input string into row and column numbers
# This pattern supports formats: "row=1, col=2", "col=3, row=A", etc.
def pattern02_parser(string):
    # Initialize row and column to -1 (invalid)
    row, col = -1, -1
    # Split the string by commas and equal signs
    parts = [p.strip() for p in string.replace(",", "=").split("=")]

    # Check if the input has exactly 4 parts
    if len(parts) == 4:
        # Extract the keys and values
        key1, val1, key2, val2 = parts
        # Check if the keys are "row" and "col" in any order
        if (key1 == "row" and key2 == "col") or (key1 == "col" and key2 == "row"):
            # Determine the row and column based on the keys
            if key1 == "row" and key2 == "col":
                row_str, col_str = val1, val2
            else:
                row_str, col_str = val2, val1

            # Check if the row is a valid letter
            if row_str in ALPHABET and len(row_str) == 1:
                row = ALPHABET.index(row_str) + 1
            # Check if the column is a valid number between 1 and 52
            if col_str.isdigit() and 1 <= int(col_str) <= 52:
                col = int(col_str)
    # Return the row and column as a list
    return [row, col]


# Input a string
string = input().strip()
# Determine the pattern and parse the input
if len(string) <= 3:
    row, col = pattern01_parser(string)
else:
    row, col = pattern02_parser(string)

# Output the results
if row == -1 and col == -1:
    print("Invalid row and column")
elif row == -1:
    print("Invalid row")
elif col == -1:
    print("Invalid column")
elif row % 2 == col % 2:
    print("White")
else:
    print("Black")
```
