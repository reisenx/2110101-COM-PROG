<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Potpourri Functions ★★☆ (
      <a href="https://drive.google.com/file/d/1ZjELR1M5hd5JoqEdfDRaEHw24N2DReOd/view?usp=drive_link">
        <code>P2_03_Func2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ภาพรวม**](#ภาพรวม)
-   [**การหาพื้นที่รูปหลายเหลี่ยมนูน**](#การหาพื้นที่รูปหลายเหลี่ยมนูน)
-   [**การตรวจ Heterogram**](#การตรวจ-heterogram)
-   [**การแทนที่โดยไม่สนตัวพิมพ์**](#การแทนที่โดยไม่สนตัวพิมพ์)
-   [**การหา 3 อันดับแรก**](#การหา-3-อันดับแรก)
-   [**การทำงานร่วมกับ Grader**](#การทำงานร่วมกับ-grader)
-   [**Solution**](#solution)

---

## ภาพรวม

โจทย์นี้รวมฟังก์ชันสี่แบบไว้ด้วยกัน จึงต้องเลือกโครงสร้างข้อมูลและขั้นตอนให้เหมาะกับงานแต่ละชนิด

| ฟังก์ชัน | แนวคิดหลัก | ค่าที่คืน |
|:---|:---|:---|
| `convex_polygon_area` | สูตรเชือกรองเท้าและการวนกลับไปจุดแรก | พื้นที่รูปหลายเหลี่ยม |
| `is_heterogram` | ตรวจตัวอักษรซ้ำโดยไม่สนตัวพิมพ์ | `True` หรือ `False` |
| `replace_ignorecase` | เลื่อนหน้าต่างค้นหาจากซ้ายไปขวา | สตริงหลังแทนที่ |
| `top3` | เรียงด้วยคะแนนและชื่อ | ลิสต์ชื่อไม่เกิน 3 คน |

ทุกฟังก์ชันต้องไม่เปลี่ยนค่าพารามิเตอร์ที่รับมา โค้ดจึงอ่านข้อมูลเดิมและสร้างตัวแปรหรือลิสต์ผลลัพธ์ขึ้นใหม่

---

## การหาพื้นที่รูปหลายเหลี่ยมนูน

### สูตรเชือกรองเท้า

ให้จุดยอดที่เรียงตามขอบรูปเป็น $(x_0,y_0),(x_1,y_1),\ldots,(x_{n-1},y_{n-1})$ พื้นที่คำนวณด้วยสูตร

$$
A = \frac{1}{2}\left|
\sum_{i=0}^{n-1}
(x_i y_{i+1} - y_i x_{i+1})
\right|
$$

เมื่อถึงจุดสุดท้าย จุดถัดไปต้องวนกลับไปเป็นจุดแรก โค้ดเขียนดัชนีนี้เป็น

```python
points[(i + 1) % len(points)]
```

เครื่องหมาย `%` ทำให้ดัชนีหลังจุดสุดท้ายกลับเป็น `0` พอดี

### การจับคู่กับโค้ด

โค้ดแยกผลรวมในสูตรเป็นสองส่วน

```python
terms01 += x1 * y2
terms02 += y1 * x2
```

เมื่อครบทุกด้านจึงคำนวณ `abs(terms01 - terms02) / 2` การใช้ `abs` ทำให้ได้พื้นที่เป็นบวกไม่ว่าจุดยอดจะเรียงตามเข็มหรือทวนเข็มนาฬิกา ตราบใดที่จุดเรียงต่อกันตามขอบรูป ส่วน `/ 2` ทำให้ผลจากพิกัดจำนวนเต็มแสดงเป็น `float` ได้ เช่น `6.0` โดยโจทย์ไม่ได้กำหนดให้ปัดเศษเพิ่มเติม

> [!NOTE]
> comment ในโค้ดระบุว่าจุดเรียงทวนเข็มนาฬิกา แต่ตัวอย่างใน PDF มีทั้งสองทิศทาง และโค้ดรองรับทั้งคู่ด้วย `abs` comment เดิมยังคงอยู่ในส่วน Solution เพื่อให้ตรงกับไฟล์คำตอบ

---

## การตรวจ Heterogram

Heterogram คือคำหรือวลีที่ตัวอักษรภาษาอังกฤษแต่ละตัวปรากฏไม่เกินหนึ่งครั้ง โดยถือว่าตัวพิมพ์ใหญ่และเล็กเป็นตัวเดียวกัน เช่น `Python` เป็น heterogram แต่ `Java` ไม่เป็น เพราะมี `a` สองตัว

ฟังก์ชันทำงานดังนี้

1.  แปลงข้อความเป็นตัวพิมพ์ใหญ่ด้วย `text.upper()` เพื่อให้ `A` และ `a` เปรียบเทียบเป็นค่าเดียวกัน
2.  วนดูอักขระทีละตัว และพิจารณาเฉพาะตัวที่ `char.isalpha()` เป็นจริง จึงข้ามช่องว่าง ตัวเลข และเครื่องหมายวรรคตอน
3.  เก็บตัวอักษรที่เคยพบใน `char_count`
4.  ถ้าพบตัวอักษรเดิมอีกครั้ง ให้ `return False` ทันที หากตรวจครบโดยไม่ซ้ำจึง `return True`

ตัวอย่าง `"The big dwarf only jumps."` มีช่องว่างและจุดท้ายประโยค แต่สิ่งเหล่านั้นไม่ถูกนำมาตรวจ จึงได้ `True`

> [!NOTE]
> ขอบเขตของโจทย์กล่าวถึงตัวอักษรภาษาอังกฤษ ส่วน `str.isalpha()` ของ Python รู้จักตัวอักษรภาษาอื่นด้วย ดังนั้นโค้ดจริงจะตรวจการซ้ำของอักขระที่ Python จัดว่าเป็นตัวอักษรด้วยเช่นกัน

---

## การแทนที่โดยไม่สนตัวพิมพ์

`replace_ignorecase(text, target, replacement)` ต้องแทนข้อความย่อยที่ตรงกับ `target` โดยไม่สนตัวพิมพ์ และค้นหาจากซ้ายไปขวาแบบไม่ซ้อนทับกัน

ตัวแปร `start` ชี้ตำแหน่งเริ่มตรวจ ส่วน `end` อยู่ห่างออกไป `len(target)` ตัว จึงเปรียบเทียบหน้าต่างปัจจุบันได้ด้วย

```python
text[start:end].lower() == target.lower()
```

-   ถ้าตรงกัน ให้ต่อ `replacement` ลงใน `result` แล้วเลื่อนทั้ง `start` และ `end` ไป `len(target)` ตำแหน่ง เพื่อไม่ตรวจส่วนที่แทนไปแล้วซ้ำ
-   ถ้าไม่ตรงกัน ให้คัดลอก `text[start]` ตามตัวพิมพ์เดิม แล้วเลื่อนหน้าต่างไปหนึ่งตำแหน่ง

ตัวอย่าง `replace_ignorecase("AAabaAA", "Aa", "Aaa")` ทำงานดังนี้

| `start` | ส่วนที่ตรวจ | การทำงาน | `result` หลังทำงาน |
|---:|:---:|:---|:---|
| `0` | `"AA"` | ตรงกัน เติม `"Aaa"` | `"Aaa"` |
| `2` | `"ab"` | ไม่ตรง เติม `"a"` | `"Aaaa"` |
| `3` | `"ba"` | ไม่ตรง เติม `"b"` | `"Aaaab"` |
| `4` | `"aA"` | ตรงกัน เติม `"Aaa"` | `"AaaabAaa"` |
| `6` | `"A"` | สั้นกว่าเป้าหมาย เติม `"A"` | `"AaaabAaaA"` |

ผลลัพธ์จึงเป็น `"AaaabAaaA"` และสตริงต้นฉบับไม่ถูกแก้ไข

> [!WARNING]
> ขั้นตอนนี้สมมติว่า `target` ไม่ใช่สตริงว่าง เพราะเมื่อ `len(target) == 0` ตัวแปร `start` จะไม่ขยับเมื่อพบข้อความว่าง ทำให้ลูปไม่จบ ดังนั้นการเรียกใช้โค้ดนี้ต้องส่งข้อความเป้าหมายที่มีอย่างน้อยหนึ่งตัวอักษร

---

## การหา 3 อันดับแรก

`top3(votes)` ต้องเรียงผู้สมัครด้วยเงื่อนไขสองระดับ

1.  คะแนนมากอยู่ก่อน
2.  เมื่อคะแนนเท่ากัน ชื่อที่น้อยกว่าตามลำดับพจนานุกรมอยู่ก่อน

Python เรียงลิสต์จากน้อยไปมากตามสมาชิกช่องแรกก่อน แล้วจึงใช้ช่องถัดไปตัดสินเมื่อค่าเท่ากัน โค้ดจึงสร้างข้อมูลเป็น

```python
[-score, candidate]
```

คะแนนถูกใส่เครื่องหมายลบ ทำให้คะแนนจริงที่มากกว่ากลายเป็นค่าลบที่น้อยกว่าและถูกเรียงไว้ด้านหน้า ส่วนชื่อในช่องที่สองทำหน้าที่ตัดสินกรณีคะแนนเท่ากันโดยอัตโนมัติ

ตัวอย่าง

```python
votes = {"A": 8888, "B": 6666, "C": 7777, "X": 6666}
```

จะเรียงเป็น `A`, `C`, `B`, `X` เพราะ `B` กับ `X` มีคะแนนเท่ากันแต่ `B` มาก่อนตามลำดับชื่อ จากนั้น `ranked_votes[:3]` เลือกเพียงสามรายการแรก จึงคืน `['A', 'C', 'B']` หากข้อมูลมีไม่ถึงสามคน slice จะคืนเท่าที่มีโดยไม่เกิดข้อผิดพลาด

---

## การทำงานร่วมกับ Grader

ส่วนท้ายโปรแกรมอ่านคำสั่ง Python **สองบรรทัด** และประมวลผลตามลำดับด้วย

```python
for _ in range(2):
    exec(input().strip())
```

รูปแบบนี้ทำให้บรรทัดแรกสร้างตัวแปร และบรรทัดที่สองนำตัวแปรนั้นไปทดสอบได้ เช่นตัวอย่าง `top3` ใช้บรรทัดแรกกำหนด `v = {...}` ซึ่งยังไม่แสดงผล แล้วบรรทัดที่สองจึงสั่ง `print(top3(v))`

> [!WARNING]
> `exec` สามารถรันคำสั่ง Python ใด ๆ ได้ จึงควรใช้เฉพาะกับคำสั่งจาก Grader ที่เชื่อถือได้เท่านั้น ไม่ควรใช้ประมวลผลข้อความจากผู้ใช้ทั่วไป

---

# Solution

```python
# --------------------------------------------------
# File Name : P2_03_Func2.py
# Problem   : Part-II Potpourri Functions
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------


# Function to calculate the area of a convex polygon given its vertices
# The vertices are provided in a counterclockwise order.
def convex_polygon_area(points):
    # Initialize terms for the area calculation
    terms01 = 0
    terms02 = 0
    # Iterate through each vertex and calculate the terms
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        terms01 += x1 * y2
        terms02 += y1 * x2
    # Calculate the area
    return abs(terms01 - terms02) / 2


# Function to check if a given text is a heterogram
# where a heterogram is a word or phrase without a repeating letter.
def is_heterogram(text):
    # Initialize a dictionary to count occurrences of each character
    char_count = {}
    # Iterate through each character in the text
    for char in text.upper():
        # First occurrence of the character
        if char.isalpha() and char not in char_count:
            char_count[char] = 1
        # Repeated occurrence of the character
        elif char.isalpha() and char in char_count:
            return False
    # If no character is repeated, return True
    return True


# Function to replace all occurrences of a target substring with a replacement substring
def replace_ignorecase(text, target, replacement):
    # Initialize variables for the result
    result = ""
    # Initialize start and end indices for substring comparison
    start = 0
    end = len(target)
    # Iterate through the text to find and replace occurrences of the target substring
    while start < len(text):
        # Replace the target substring with the replacement substring
        if text[start:end].lower() == target.lower():
            result += replacement
            start += len(target)
            end += len(target)
        # Add the current character to the result if no match is found
        else:
            result += text[start]
            start += 1
            end += 1
    # Return the modified text
    return result


# Function to find the top 3 candidates based on votes
def top3(votes):
    # Sort the candidates based on their scores in descending order
    ranked_votes = []
    for candidate, score in votes.items():
        ranked_votes.append([-score, candidate])
    ranked_votes.sort()

    # Extract the top 3 candidates from the sorted list
    top_candidates = []
    for _, candidate in ranked_votes[:3]:
        top_candidates.append(candidate)
    return top_candidates


# Execute the input string as code
for _ in range(2):
    exec(input().strip())
```
