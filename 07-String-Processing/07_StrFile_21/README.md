<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    ROT13 ★★ (
      <a href="https://drive.google.com/file/d/1TO8vz37m9d83js4X4iks1d9j4NRwG50a/view?usp=drive_link">
        <code>07_StrFile_21</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**หลักการทำงานของ ROT13**](#หลักการทำงานของ-rot13)
-   [**การเลื่อนตำแหน่งด้วย Modulo**](#การเลื่อนตำแหน่งด้วย-modulo)
-   [**ฟังก์ชัน rot13**](#ฟังก์ชัน-rot13)
-   [**การรับข้อความหลายบรรทัด**](#การรับข้อความหลายบรรทัด)
-   [**Solution**](#solution)

---

## หลักการทำงานของ ROT13

ROT13 เป็นวิธีแทนตัวอักษรภาษาอังกฤษแต่ละตัวด้วยตัวที่อยู่ถัดไป 13 ตำแหน่ง
ในวงจรตัวอักษร 26 ตัว เช่น `a` เปลี่ยนเป็น `n`, `n` เปลี่ยนเป็น `a`
และ `Z` เปลี่ยนเป็น `M`

โปรแกรมแยกชุดตัวพิมพ์เล็กกับตัวพิมพ์ใหญ่ เพื่อให้ผลลัพธ์คงรูปแบบตัวพิมพ์เดิม

```python
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

อักขระที่ไม่ใช่ตัวอักษรภาษาอังกฤษ เช่น ตัวเลข ช่องว่าง และเครื่องหมายวรรคตอน
จะไม่ถูกเปลี่ยน ดังนั้น `"Hello, World!"` จะได้ `"Uryyb, Jbeyq!"`

---

## การเลื่อนตำแหน่งด้วย Modulo

เมื่อกำหนดให้ดัชนีของ `a` หรือ `A` เป็น 0 ตำแหน่งใหม่คำนวณได้จาก

$$
\text{new index} = (\text{index} + 13) \bmod 26
$$

เขียนเป็น Python ได้ว่า

```python
(idx + 13) % 26
```

เครื่องหมาย `% 26` ทำให้ตำแหน่งวนกลับไปต้นชุดเมื่อเลื่อนเกินดัชนี `25`
ตัวอย่างเช่น `z` อยู่ที่ดัชนี `25` จึงได้ตำแหน่งใหม่เป็น
`(25 + 13) % 26` หรือ `12` ซึ่งตรงกับ `m`

เนื่องจากการเลื่อน 13 ตำแหน่งสองครั้งเท่ากับเลื่อนครบ 26 ตำแหน่ง
การใช้ ROT13 กับผลลัพธ์ซ้ำอีกครั้งจึงได้ข้อความเดิมกลับมา

---

## ฟังก์ชัน rot13

ฟังก์ชัน `rot13(text)` สร้าง `result` เป็นข้อความว่าง แล้ววนพิจารณา `char`
ทีละตัวตามลำดับ

-   ถ้า `char in LOWERCASE` ให้หา `idx` ด้วย `LOWERCASE.index(char)`
    แล้วเลือกตัวพิมพ์เล็กตำแหน่งใหม่
-   ถ้า `char in UPPERCASE` ให้คำนวณแบบเดียวกันใน `UPPERCASE`
-   ถ้าไม่อยู่ในทั้งสองชุด ให้ต่อ `char` เดิมเข้า `result`

การต่ออักขระเข้า `result` ตามลำดับทำให้ช่องว่างและเครื่องหมายที่อยู่ภายในข้อความ
ยังอยู่ในตำแหน่งเดิม เมื่อวนครบทุกตัว ฟังก์ชันจึง `return result`

ตัวอย่างการจับคู่บางตำแหน่งมีดังนี้

| อักขระเดิม | อักขระหลัง ROT13 |
|:--:|:--:|
| `a` | `n` |
| `m` | `z` |
| `n` | `a` |
| `A` | `N` |
| `Z` | `M` |
| `!` | `!` |

---

## การรับข้อความหลายบรรทัด

ส่วนหลักของโปรแกรมใช้ `while True` รับข้อมูลทีละบรรทัด เมื่อบรรทัดนั้นเท่ากับ
`"end"` ทุกตัวและเป็นตัวพิมพ์เล็ก โปรแกรมจะ `break` โดยไม่เข้ารหัสหรือแสดงบรรทัดนี้
มิฉะนั้นจะเรียก `rot13(text)` และแสดงผลทันที ทำให้ลำดับผลลัพธ์ตรงกับลำดับข้อมูลเข้า

```python
while True:
    text = input().strip()
    if text == "end":
        break
    print(rot13(text))
```

> [!NOTE]
>
> โปรแกรมเรียก `strip()` กับทุกบรรทัด จึงตัดช่องว่างที่หัวและท้ายก่อนตรวจ `end`
> และก่อนเข้ารหัส แต่ช่องว่างภายในข้อความยังคงอยู่ตามเดิม นอกจากนี้ `END`
> ไม่ใช่คำสั่งหยุด เพราะการเปรียบเทียบข้อความแยกตัวพิมพ์เล็ก–ใหญ่

---

# Solution

```python
# --------------------------------------------------
# File Name : 07_StrFile_21.py
# Problem   : ROT13
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# List of lowercase and uppercase letters
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Function to encrypt text using ROT13 cipher
def rot13(text):
    result = ""
    for char in text:
        # Encrypt lowercase letters
        if char in LOWERCASE:
            idx = LOWERCASE.index(char)
            result += LOWERCASE[(idx + 13) % 26]

        # Encrypt uppercase letters
        elif char in UPPERCASE:
            idx = UPPERCASE.index(char)
            result += UPPERCASE[(idx + 13) % 26]

        # Keep non-alphabetic characters unchanged
        else:
            result += char
    # Return the encrypted text
    return result


# ROT13 encryption
while True:
    # Input a text
    text = input().strip()
    # Stop if the input is "end"
    if text == "end":
        break
    # Output the encrypted text
    print(rot13(text))
```
