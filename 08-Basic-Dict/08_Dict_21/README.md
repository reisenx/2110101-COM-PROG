<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Character Count ★★ (
      <a href="https://drive.google.com/file/d/1eojT5SxU4rf77ntGiALT98hMyYlzkops/view?usp=drive_link">
        <code>08_Dict_21</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเตรียมข้อความ**](#การเตรียมข้อความ)
-   [**การนับความถี่ด้วยพจนานุกรม**](#การนับความถี่ด้วยพจนานุกรม)
-   [**การเรียงลำดับหลายเงื่อนไข**](#การเรียงลำดับหลายเงื่อนไข)
-   [**การแสดงผล**](#การแสดงผล)
-   [**Solution**](#solution)

---

## การเตรียมข้อความ

โจทย์กำหนดให้ตัวพิมพ์เล็กและตัวพิมพ์ใหญ่เป็นตัวอักษรเดียวกัน เราจึงแปลง
ข้อความทั้งหมดเป็นตัวพิมพ์เล็กก่อนเริ่มนับ

```python
text = input().strip().lower()
```

-   `.strip()` ตัดช่องว่างที่อยู่หน้าสุดและท้ายสุดของข้อความ
-   `.lower()` แปลงตัวอักษรภาษาอังกฤษเป็นตัวพิมพ์เล็ก

ตัวอย่างเช่น ข้อความ `"AaB"` จะกลายเป็น `"aab"` ทำให้ `A` และ `a`
ถูกนับรวมกันภายใต้คีย์ `"a"`

## การนับความถี่ด้วยพจนานุกรม

เราสร้าง `char_count` เพื่อเก็บ **ตัวอักษร → จำนวนครั้งที่พบ** แล้ววนดูอักขระ
ในข้อความทีละตัว

```python
char_count = {}

for char in text:
    if char.isalpha():
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
```

คำสั่ง `char.isalpha()` เป็นจริงเมื่อ `char` เป็นตัวอักษร จึงไม่นับตัวเลข
ช่องว่าง หรือเครื่องหมายต่าง ๆ เมื่อพบตัวอักษรเป็นครั้งแรก โค้ดจะสร้างคีย์นั้น
ด้วยค่าเริ่มต้น `0` ก่อน แล้วจึงเพิ่มจำนวนด้วย `char_count[char] += 1`

ตัวอย่างเช่น เมื่ออ่าน `"aab"` ตามลำดับ พจนานุกรมจะเปลี่ยนเป็น
`{"a": 1}`, `{"a": 2}` และ `{"a": 2, "b": 1}`

> [!NOTE]
>
> โจทย์ให้เรานับเฉพาะตัวอักษรภาษาอังกฤษ แต่เมธอด `isalpha()` ของ Python
> ยอมรับตัวอักษรในภาษาอื่นด้วย หากรับข้อมูลตามเงื่อนไขของโจทย์
> พจนานุกรมนี้จึงมีเฉพาะคีย์ `a` ถึง `z` ตามที่ต้องการ

## การเรียงลำดับหลายเงื่อนไข

ผลลัพธ์ต้องเรียงตามจำนวนครั้งจากมากไปน้อย และถ้าจำนวนเท่ากันให้เรียงตาม
ตัวอักษรจากน้อยไปมาก โค้ดจึงสร้างลิสต์ย่อยในรูป
`[-จำนวนครั้ง, ตัวอักษร]` สำหรับทุกคู่ใน `char_count`

```python
for char, count in char_count.items():
    sorted_char_count.append([-count, char])
```

จากข้อมูลตัวอย่าง จะได้ค่าที่ใช้เรียงดังนี้

| ตัวอักษร | จำนวนครั้ง | ลิสต์ที่ใช้เรียง |
| :---: | :---: | :---: |
| `b` | `7` | `[-7, "b"]` |
| `d` | `4` | `[-4, "d"]` |
| `a` | `2` | `[-2, "a"]` |
| `c` | `2` | `[-2, "c"]` |

เมื่อใช้ `.sort()` Python จะเรียงลิสต์จากน้อยไปมากโดยเปรียบเทียบสมาชิกตัวแรก
ก่อน เนื่องจาก `-7 < -4 < -2` ตัวอักษรที่พบ `7` ครั้งจึงอยู่ก่อนตัวที่พบ
`4` และ `2` ครั้ง เท่ากับว่าเรียงจำนวนจริงจากมากไปน้อย

ถ้าสมาชิกตัวแรกเท่ากัน Python จะเปรียบเทียบสมาชิกตัวถัดไปแทน เช่น
`[-2, "a"]` จะอยู่ก่อน `[-2, "c"]` จึงได้การเรียงตัวอักษรตามลำดับ
พจนานุกรมเมื่อจำนวนครั้งเท่ากัน

## การแสดงผล

หลังเรียงเสร็จ สมาชิกตัวแรกของแต่ละลิสต์ยังเป็นจำนวนติดลบ ลูปสุดท้ายจึงใช้
`-count` เพื่อแปลงกลับเป็นจำนวนครั้งจริง แล้วสร้างข้อความด้วย f-string

```python
for count, char in sorted_char_count:
    print(f"{char} -> {-count}")
```

รูปแบบผลลัพธ์มีช่องว่างอยู่ทั้งสองข้างของ `->` เช่น `b -> 7`
โปรแกรมแสดงตัวอักษรละ 1 บรรทัดตามลำดับที่เรียงไว้ หากข้อความไม่มีตัวอักษร
เลย `sorted_char_count` จะว่างและโปรแกรมจะไม่แสดงผล

---

# Solution

```python
# --------------------------------------------------
# File Name : 08_Dict_21.py
# Problem   : Character Count
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input text and lowercase it
text = input().strip().lower()

# Initialize a dictionary to count characters
char_count = {}

# Count each character in the text
for char in text:
    if char.isalpha():
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

# Sort the characters by count (descending) and then alphabetically
sorted_char_count = []
for char, count in char_count.items():
    sorted_char_count.append([-count, char])

sorted_char_count.sort()

# Output the sorted characters and their counts
for count, char in sorted_char_count:
    print(f"{char} -> {-count}")
```
