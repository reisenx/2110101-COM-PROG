<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Most Common Alphabet ★★ (
      <a href="https://drive.google.com/file/d/166wIhXhfHUudlgLNZJymGaIKxNRExgRG/view?usp=sharing">
        <code>2567_3_Q4_B1</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การนับตัวอักษรด้วย Dictionary**](#การนับตัวอักษรด้วย-dictionary)
-   [**การเรียงตามความถี่**](#การเรียงตามความถี่)
-   [**การรักษาอันดับที่เสมอกัน**](#การรักษาอันดับที่เสมอกัน)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## การนับตัวอักษรด้วย Dictionary

โจทย์รับจำนวนเต็มบวก `N` แล้วรับข้อความภาษาอังกฤษตัวพิมพ์เล็กหนึ่งบรรทัด
จากนั้นต้องแสดงตัวอักษรที่พบบ่อยที่สุดก่อน โดยไม่นับช่องว่าง

เราสามารถเก็บจำนวนครั้งที่พบแต่ละตัวอักษรไว้ใน dictionary ได้ โดยใช้ตัวอักษร
เป็น key เช่น ถ้าข้อความคือ `coffee cake` จำนวนจริงที่นับได้จะเป็น

```text
e: 3, c: 2, f: 2, a: 1, k: 1, o: 1
```

อย่างไรก็ตาม โค้ดข้อนี้ตั้งใจเก็บ **ค่าติดลบของจำนวนครั้ง** เมื่อพบตัวอักษร
จึงลดค่าด้วย `-= 1`

```python
if char.isalpha() and char not in letter_count:
    letter_count[char] = 0

if char.isalpha():
    letter_count[char] -= 1
```

ถ้าให้ $f_c$ เป็นจำนวนครั้งที่พบตัวอักษร `c` ค่าที่เก็บจริงคือ

$$
\text{letter_count[c]} = -f_c
$$

ดังนั้นตัวอักษร `e` ที่พบ `3` ครั้งจะเก็บค่า `-3` ส่วน `c` ที่พบ `2` ครั้ง
จะเก็บค่า `-2` คำสั่ง `char.isalpha()` ทำให้ช่องว่างไม่ถูกเพิ่มเข้า dictionary
สำหรับข้อมูลตามข้อกำหนดจึงเหลือเฉพาะตัวอักษรภาษาอังกฤษตัวพิมพ์เล็ก

---

## การเรียงตามความถี่

หลังนับเสร็จ โปรแกรมสร้าง dictionary อีกตัวชื่อ `letter_rankings`
เพื่อรวมตัวอักษรที่มีจำนวนครั้งเท่ากันไว้ในลิสต์เดียวกัน

สำหรับข้อความ `coffee cake` จะมีโครงสร้างในลักษณะนี้

```python
{
    -3: ["e"],
    -2: ["c", "f"],
    -1: ["o", "a", "k"],
}
```

เมื่อใช้ `sorted(letter_rankings.items())` key จะเรียงจากน้อยไปมากเป็น
`-3`, `-2`, `-1` ซึ่งเท่ากับเรียงความถี่จริงจากมากไปน้อยเป็น `3`, `2`, `1`
พอดี วิธีเก็บค่าติดลบจึงช่วยให้ใช้ `sorted()` ตามปกติได้

ภายในกลุ่มความถี่เดียวกัน โปรแกรมใช้ `sorted(chars)` อีกครั้ง
เพื่อเรียงตัวอักษรตามพจนานุกรม แล้วคืนค่าความถี่ให้เป็นบวกตอนแสดงผลด้วย
`-count`

```python
for char in sorted(chars):
    print(char, -count)
```

ผลลัพธ์แต่ละบรรทัดจึงอยู่ในรูป `ตัวอักษร จำนวนครั้ง`

---

## การรักษาอันดับที่เสมอกัน

โจทย์กำหนดว่า ถ้าตัวอักษรตรงขอบอันดับที่ `N` มีความถี่เท่ากับตัวอื่น
ต้องแสดงตัวที่เสมอกันทั้งหมด ผลลัพธ์จึงอาจมีมากกว่า `N` บรรทัด

โค้ดทำตามกติกานี้ด้วยการลด `rank_display_limit` ทีละ **ขนาดของกลุ่ม**
แต่เมื่อเลือกกลุ่มหนึ่งแล้ว จะพิมพ์สมาชิกทุกตัวในกลุ่มนั้นก่อนตรวจว่าจะครบหรือเกิน
`N` หรือไม่

```python
rank_display_limit -= len(chars)
```

เช่น หากเหลือที่ว่างตามอันดับเพียง `1` ตำแหน่ง แต่กลุ่มถัดไปมีตัวอักษร
`a`, `k`, `o` ที่พบอย่างละ `1` ครั้ง โปรแกรมจะพิมพ์ทั้ง 3 ตัว
เมื่อจบกลุ่มแล้ว ถ้า `rank_display_limit <= 0` การวนรอบถัดไปจึงหยุดด้วย `break`

ถ้าจำนวนตัวอักษรที่แตกต่างกันทั้งหมดน้อยกว่า `N` ลูปจะจบเองและแสดงเท่าที่มี
ถ้าข้อความไม่มีตัวอักษรเลย `letter_rankings` จะว่างและไม่มีบรรทัดผลลัพธ์

---

## ตัวอย่างการทำงาน

เมื่อข้อความคือ `coffee cake` ลำดับกลุ่มความถี่คือ

| ความถี่ | ตัวอักษรตามลำดับพจนานุกรม |
|---:|:---|
| `3` | `e` |
| `2` | `c`, `f` |
| `1` | `a`, `k`, `o` |

ถ้า `N = 3` โปรแกรมใช้กลุ่มแรก `1` ตัวและกลุ่มที่สอง `2` ตัวพอดี จึงแสดง

```text
e 3
c 2
f 2
```

ถ้า `N = 4` โปรแกรมต้องเข้าถึงกลุ่มความถี่ `1` และแสดงตัวที่เสมอกันทั้งกลุ่ม
จึงได้ทั้งหมด 6 บรรทัด คือ `e`, `c`, `f`, `a`, `k` และ `o` ตามลำดับ

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_3_Q4_B1.py
# Problem   : Most Common Alphabet
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Initialize a dictionary to count occurrences of each letter
letter_count = {}

# Initialize a dictionary to store the alphabet based on their counts
letter_rankings = {}

# Input the number of letter occurrences ranks to display
rank_display_limit = int(input())

# Input text
text = input().strip()

# Count occurrences of each letter in the text
# and store them in the letter_count dictionary
for char in text:
    # Initialize the alphabet character in the dictionary if not already present
    if char.isalpha() and char not in letter_count:
        letter_count[char] = 0

    # Decrement the count for each alphabet character for sorting
    if char.isalpha():
        letter_count[char] -= 1

# Iterate through the letter_count dictionary
for char, count in letter_count.items():
    # Initialize the letter_rankings dictionary if the count is not already present
    if count not in letter_rankings:
        letter_rankings[count] = []

    # Append the character to the list for its count
    letter_rankings[count].append(char)

# Output the letters sorted by their counts in descending order
for count, chars in sorted(letter_rankings.items()):
    # Stop if the rank display limit is reached
    if rank_display_limit <= 0:
        break

    # Decrement the rank display limit by the number of characters printed
    rank_display_limit -= len(chars)

    # Sort the characters alphabetically and print them with their counts
    for char in sorted(chars):
        print(char, -count)
```
