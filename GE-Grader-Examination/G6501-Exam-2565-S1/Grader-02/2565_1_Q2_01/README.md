<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Scrabble ★★ (
      <a href="https://drive.google.com/file/d/1X6OZDtOLyN39IAgno2ZU1lD7gL25xOpo/view?usp=sharing">
        <code>2565_1_Q2_01</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การคิดคะแนน**](#การคิดคะแนน)
-   [**การเรียงลำดับคำ**](#การเรียงลำดับคำ)
-   [**ลำดับการทำงาน**](#ลำดับการทำงาน)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## การคิดคะแนน

โจทย์กำหนดคะแนนให้ตัวอักษรภาษาอังกฤษแต่ละตัว ดังนี้

| คะแนน | ตัวอักษร |
|:---:|:---|
| `1` | `A`, `E`, `I`, `L`, `N`, `O`, `R`, `S`, `T`, `U` |
| `2` | `D`, `G` |
| `3` | `B`, `C`, `M`, `P` |
| `4` | `F`, `H`, `V`, `W`, `Y` |
| `5` | `K` |
| `8` | `J`, `X` |
| `10` | `Q`, `Z` |

ในโปรแกรม ตารางนี้ถูกเก็บไว้ใน `LETTER_POINT` โดยแต่ละสมาชิกประกอบด้วย
กลุ่มตัวอักษรและคะแนนของกลุ่มนั้น เช่น `["DG", 2]` หมายความว่า `D` และ `G`
มีคะแนนตัวละ `2` คะแนน

ฟังก์ชัน `get_letter_point(letter)` วนดูทีละกลุ่ม แล้วใช้
`letter in group` ตรวจว่าตัวอักษรอยู่ในกลุ่มนั้นหรือไม่ เมื่อพบแล้วจะคืนคะแนนทันที
โจทย์รับเฉพาะตัวอักษรภาษาอังกฤษตัวพิมพ์ใหญ่ จึงพบทุกตัวอักษรในตารางเสมอ ส่วน
`return 0` ตอนท้ายเป็นค่ารองรับกรณีที่ไม่พบตัวอักษร

คะแนนของคำหนึ่งคำคือผลรวมของคะแนนตัวอักษรทุกตัวในคำนั้น

$$
\operatorname{score}(w)=\sum_{c\in w}\operatorname{point}(c)
$$

ในภาษา Python ผลรวมนี้ตรงกับการสะสมค่าลงใน `total_point`

```python
total_point = 0
for letter in word:
    total_point += get_letter_point(letter)
```

ตัวอย่างเช่น คำว่า `ZEBRA` มีคะแนน

$$
10+1+3+1+1=16
$$

ซึ่งใน Python คำนวณได้จาก
`10 + 1 + 3 + 1 + 1` และได้ผลลัพธ์เป็นจำนวนเต็ม จึงไม่มีการปัดเศษ

> [!NOTE]
>
> บรรทัดแจกแจงคะแนน `ZEBRA` ในเอกสารโจทย์เขียนตัวอักษรตัวสุดท้ายเป็น `R`
> ซ้ำอีกครั้ง แต่ตัวอักษรตัวสุดท้ายที่ถูกต้องคือ `A` ซึ่งมีค่า `1` คะแนนเท่ากัน
> ดังนั้นคะแนนรวม `16` ในเอกสารยังคงถูกต้อง

## การเรียงลำดับคำ

ข้อมูลนำเข้าอยู่ในบรรทัดเดียวและคั่นแต่ละคำด้วยช่องว่าง คำสั่ง
`input().split()` จะแยกข้อมูลออกมาเป็นรายการของคำโดยไม่ต้องทราบจำนวนคำล่วงหน้า
จากนั้นโปรแกรมคำนวณคะแนนและเก็บข้อมูลแต่ละคำในรูป

```python
[-points, word]
```

เหตุผลที่เก็บคะแนนเป็นค่าติดลบ เพราะ `list.sort()` เรียงค่าน้อยไปมากตามปกติ
คะแนนที่มากกว่าจะกลายเป็นค่าติดลบที่น้อยกว่า เช่น คะแนน `16` กลายเป็น `-16`
และคะแนน `14` กลายเป็น `-14` ดังนั้น `-16` จึงถูกเรียงไว้ก่อน `-14`

เมื่อ Python เปรียบเทียบลิสต์ จะเปรียบเทียบสมาชิกจากซ้ายไปขวา ลิสต์
`[-points, word]` จึงทำให้เกิดลำดับ 2 ชั้นโดยอัตโนมัติ

1. เปรียบเทียบ `-points` ก่อน จึงเทียบเท่ากับเรียงคะแนนจากมากไปน้อย
2. ถ้าคะแนนเท่ากัน จึงเปรียบเทียบ `word` และเรียงคำตามลำดับพจนานุกรม

ตัวอย่างข้อมูลที่เตรียมไว้ก่อนเรียงคือ

```python
[-16, "ZEBRA"]
[-14, "QUEEN"]
[-14, "QUIET"]
[-14, "QUITE"]
```

`ZEBRA` จะอยู่ก่อนเพราะมีคะแนนมากที่สุด ส่วนสามคำที่ได้ `14` คะแนนจะเรียงเป็น
`QUEEN`, `QUIET`, `QUITE` ตามลำดับตัวอักษร เมื่อแสดงผลจึงใช้ `-points`
เปลี่ยนคะแนนกลับเป็นค่าบวก

## ลำดับการทำงาน

1. รับคำทั้งหมดด้วย `input().split()`
2. เรียก `word_point(word)` เพื่อรวมคะแนนตัวอักษรของแต่ละคำ
3. เก็บ `[-points, word]` ลงใน `word_points`
4. เรียก `word_points.sort()` เพื่อเรียงตามคะแนนและชื่อคำ
5. วนแสดง `word` และ `-points` ทีละบรรทัดตามลำดับที่เรียงแล้ว

หากข้อมูลมีคำซ้ำ แต่ละคำจะถูกเก็บเป็นคนละสมาชิกและแสดงผลครบทุกครั้งที่ปรากฏ

## ตัวอย่างการทำงาน

**Input**

```
COMPUTE ZEBRA QUEEN QUIET QUITE
```

**Output**

```
ZEBRA 16
QUEEN 14
QUIET 14
QUITE 14
COMPUTE 13
```

`ZEBRA` มีคะแนนสูงสุดจึงอยู่บรรทัดแรก ส่วน `QUEEN`, `QUIET` และ `QUITE`
มีคะแนนเท่ากันจึงตัดสินลำดับด้วยชื่อคำ `print(word, -points)` จะแสดงชื่อคำ
เว้นหนึ่งช่อง แล้วตามด้วยคะแนนจำนวนเต็ม

---

# Solution

```python
# --------------------------------------------------
# File Name : 2565_1_Q2_01.py
# Problem   : Scrabble
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

LETTER_POINT = [
    ["AEIOULNRST", 1],
    ["DG", 2],
    ["BCMP", 3],
    ["FHVWY", 4],
    ["K", 5],
    ["JX", 8],
    ["QZ", 10],
]


# Calculate the score of each letter in Scrabble
def get_letter_point(letter):
    for group, points in LETTER_POINT:
        if letter in group:
            return points
    return 0


# Calculate the total score of a word based on its letters
def word_point(word):
    total_point = 0
    for letter in word:
        total_point += get_letter_point(letter)
    return total_point


# Read input words and calculate their scores
word_points = []
for word in input().split():
    points = word_point(word)
    word_points.append([-points, word])

# Sort the words by their scores in descending order
# if scores are equal, sort alphabetically
word_points.sort()
# Output the words with their scores
for points, word in word_points:
    print(word, -points)
```
