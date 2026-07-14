<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Anagram ★★ (
      <a href="https://drive.google.com/file/d/1AXiZNOMmZwkKV2cUSMS500qbqEBiFDwQ/view?usp=drive_link">
        <code>07_StrFile_22</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิดของ Anagram**](#แนวคิดของ-anagram)
-   [**การเตรียมข้อความ**](#การเตรียมข้อความ)
-   [**การนับความถี่ของอักขระ**](#การนับความถี่ของอักขระ)
-   [**การตัดสินคำตอบ**](#การตัดสินคำตอบ)
-   [**Solution**](#solution)

---

## แนวคิดของ Anagram

ข้อความสองข้อความเป็น **Anagram** ของกันและกัน เมื่อประกอบด้วยอักขระชุดเดียวกัน
และอักขระแต่ละตัวปรากฏเป็นจำนวนเท่ากัน โดยไม่สนใจลำดับของอักขระ เช่น
`Elvis` กับ `lives` เป็น Anagram เพราะเมื่อนับแบบไม่แยกตัวพิมพ์เล็ก-ใหญ่แล้ว
ทั้งสองข้อความมี `e`, `i`, `l`, `s` และ `v` อย่างละหนึ่งตัวเท่ากัน

สำหรับโจทย์นี้ โปรแกรมนับเฉพาะตัวอักษรภาษาอังกฤษ `a` ถึง `z` และตัวเลข `0`
ถึง `9` ส่วนช่องว่างและเครื่องหมายวรรคตอนจะไม่ถูกนำมานับ ดังนั้นเงื่อนไขของ
Anagram คือ สำหรับอักขระที่สนใจทุกตัว $c$

$$
\operatorname{count}_{\text{text01}}(c)
=
\operatorname{count}_{\text{text02}}(c)
$$

จำนวนครั้งที่ปรากฏมีความสำคัญด้วย เช่น `aab` กับ `aba` เป็น Anagram
แต่ `aab` กับ `abb` ไม่เป็น Anagram แม้ทั้งสองข้อความจะมีชนิดของตัวอักษรเป็น
`a` และ `b` เหมือนกัน

## การเตรียมข้อความ

โปรแกรมสร้างข้อความ `CHARACTERS` ซึ่งรวมอักขระที่ต้องนับทั้งหมด 36 ตัวไว้ก่อน

```python
CHARACTERS = "abcdefghijklmnopqrstuvwxyz0123456789"
```

จากนั้นรับข้อความสองบรรทัด แล้วใช้ `strip()` ตัดช่องว่างที่หัวและท้ายข้อความ
และใช้ `lower()` เปลี่ยนตัวอักษรภาษาอังกฤษให้เป็นตัวพิมพ์เล็ก

```python
text01 = input().strip().lower()
text02 = input().strip().lower()
```

การใช้ `lower()` ทำให้ `E` กับ `e` ถูกนับเป็นอักขระเดียวกัน ส่วนอักขระที่ไม่อยู่ใน
`CHARACTERS` เช่น ช่องว่างหรือเครื่องหมายวรรคตอน จะถูกข้ามในขั้นตอนนับ

## การนับความถี่ของอักขระ

โปรแกรมสร้างลิสต์สำหรับนับความถี่สองลิสต์ แต่ละลิสต์มีค่าเริ่มต้นเป็น `0` จำนวน
36 ช่อง โดยแต่ละตำแหน่งตรงกับอักขระตำแหน่งเดียวกันใน `CHARACTERS`

```python
char_count_01 = [0] * len(CHARACTERS)
char_count_02 = [0] * len(CHARACTERS)
```

ตัวอย่างตำแหน่งสำคัญมีดังนี้

| อักขระ | ตำแหน่งในลิสต์ |
|---|---:|
| `a` | `0` |
| `z` | `25` |
| `0` | `26` |
| `9` | `35` |

เมื่อตรวจอักขระแต่ละตัว หากอักขระนั้นอยู่ใน `CHARACTERS` โปรแกรมจะหา
ตำแหน่งด้วย `CHARACTERS.index(char)` แล้วเพิ่มค่าของช่องเดียวกันขึ้น `1`

```python
if char in CHARACTERS:
    index = CHARACTERS.index(char)
    char_count_01[index] += 1
```

กระบวนการเดียวกันนี้ถูกทำกับข้อความที่สองโดยเก็บผลไว้ใน `char_count_02`
ตัวเลขจึงมีผลต่อคำตอบเช่นเดียวกับตัวอักษร เช่น `abc11` กับ `1abc1` เป็น
Anagram แต่ `abc11` กับ `abc12` ไม่เป็น Anagram

## การตัดสินคำตอบ

ลิสต์สองลิสต์จะเท่ากันด้วยตัวดำเนินการ `==` ก็ต่อเมื่อสมาชิกในทุกตำแหน่งเท่ากัน
จึงเขียนเงื่อนไขจากสูตรข้างต้นในภาษา Python ได้โดยตรงว่า

```python
char_count_01 == char_count_02
```

ถ้าความถี่ทั้ง 36 ตำแหน่งเท่ากัน โปรแกรมแสดง `YES` มิฉะนั้นจะแสดง `NO`
โดยคำตอบใช้ตัวพิมพ์ใหญ่ทั้งหมดตามรูปแบบที่โจทย์กำหนด

---

# Solution

```python
# --------------------------------------------------
# File Name : 07_StrFile_22.py
# Problem   : Anagram
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Initialize the character set
CHARACTERS = "abcdefghijklmnopqrstuvwxyz0123456789"

# Initialize character count arrays for two strings
# Index 0-25 for 'a'-'z', index 26-35 for '0'-'9'
char_count_01 = [0] * len(CHARACTERS)
char_count_02 = [0] * len(CHARACTERS)

# Input two strings and lowercase them
text01 = input().strip().lower()
text02 = input().strip().lower()

# Count characters in the first string
for char in text01:
    if char in CHARACTERS:
        index = CHARACTERS.index(char)
        char_count_01[index] += 1

# Count characters in the second string
for char in text02:
    if char in CHARACTERS:
        index = CHARACTERS.index(char)
        char_count_02[index] += 1

# Check if the two strings are anagrams
if char_count_01 == char_count_02:
    print("YES")
else:
    print("NO")
```
