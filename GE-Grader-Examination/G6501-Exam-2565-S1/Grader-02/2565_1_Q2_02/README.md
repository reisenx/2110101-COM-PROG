<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Match ★★☆ (
      <a href="https://drive.google.com/file/d/14nVgkqWfDCmAo63yftuhC75UoOSFs9Xi/view?usp=sharing">
        <code>2565_1_Q2_02</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**เงื่อนไขของคำที่ตรงรูปแบบ**](#เงื่อนไขของคำที่ตรงรูปแบบ)
-   [**การตรวจตัวอักษรบังคับ**](#การตรวจตัวอักษรบังคับ)
-   [**ลำดับการทำงาน**](#ลำดับการทำงาน)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**การทำงานร่วมกับ Grader**](#การทำงานร่วมกับ-grader)
-   [**Solution**](#solution)

---

## เงื่อนไขของคำที่ตรงรูปแบบ

ฟังก์ชัน `match()` รับ `word`, `pattern`, `included_chars` และ
`excluded_chars` แล้วคืนค่า `True` เมื่อคำผ่านทุกเงื่อนไข หรือคืนค่า `False`
ทันทีเมื่อพบว่าไม่ผ่านเงื่อนไขใดเงื่อนไขหนึ่ง

ในเอกสารโจทย์ใช้ชื่อ `include_chars` และ `exclude_chars` ส่วนโค้ดนี้ใช้ชื่อ
`included_chars` และ `excluded_chars` ตามลำดับ ชื่อแตกต่างกันเล็กน้อยแต่มี
ความหมายเดียวกัน

อันดับแรก `is_pattern_match(word, pattern)` ตรวจเงื่อนไขพื้นฐาน 2 ข้อ

1. `word` และ `pattern` ต้องยาวเท่ากัน ถ้ายาวไม่เท่ากันจะคืน `False`
   ก่อน เพื่อไม่ให้เข้าถึงตำแหน่งที่ไม่มีอยู่
2. ทุกตำแหน่งใน `pattern` ที่ไม่ใช่ `?` ต้องเป็นตัวอักษรเดียวกับตำแหน่งนั้นใน
   `word` ส่วน `?` เป็นช่องว่างที่แทนตัวอักษรใดก็ได้ในขั้นตอนนี้

เงื่อนไขตำแหน่งคงที่เขียนในภาษา Python ได้ดังนี้

```python
if pattern[i] != "?" and pattern[i] != word[i]:
    return False
```

หลังจากรูปแบบพื้นฐานตรงกันแล้ว `has_excluded_char()` จะตรวจเฉพาะตัวอักษรใน
`word` ที่อยู่ตรงกับตำแหน่ง `?` หากตัวอักษรเหล่านั้นมีอย่างน้อยหนึ่งตัวอยู่ใน
`excluded_chars` คำนั้นต้องไม่ผ่าน

```python
if pattern[i] == "?" and word[i] in excluded_chars:
    return True
```

ฟังก์ชันย่อยนี้คืน `True` เมื่อ **พบตัวอักษรต้องห้าม** แล้ว `match()` จึงใช้
`if has_excluded_char(...): return False` เพื่อปฏิเสธคำนั้น ตัวอักษรที่อยู่ใน
ตำแหน่งคงที่ของ `pattern` ไม่ถูกตรวจด้วยเงื่อนไขนี้

> [!NOTE]
>
> คอมเมนต์เหนือ `has_excluded_char()` ในโค้ดเขียนว่าเป็นการตรวจตัวอักษร
> “ทั้งหมด” แต่พฤติกรรมจริงคือ หากพบตัวอักษรต้องห้าม **แม้เพียงหนึ่งตัว**
> ในตำแหน่ง `?` ฟังก์ชันจะคืน `True` ทันที

## การตรวจตัวอักษรบังคับ

`included_chars` ระบุตัวอักษรที่ต้องปรากฏในตำแหน่ง `?` เท่านั้น โปรแกรมจึง
สร้าง `filled_letters` โดยเก็บตัวอักษรจาก `word` เฉพาะตำแหน่งที่ `pattern[i]`
เป็น `?`

ถ้ากำหนด

$$
F=[\,word[i]\mid pattern[i]=\texttt{"?"}\,]
$$

เงื่อนไขที่ต้องเป็นจริงสำหรับตัวอักษรทุกตัว $c$ คือ

$$
\operatorname{count}_{F}(c)
\ge
\operatorname{count}_{\texttt{included\_chars}}(c)
$$

กล่าวคือ ในช่อง `?` ต้องมีตัวอักษรแต่ละชนิดอย่างน้อยเท่ากับจำนวนครั้งที่
ตัวอักษรนั้นปรากฏใน `included_chars`

โค้ดไม่ได้ใช้ `count()` โดยตรง แต่ตรวจทีละตัวแล้วลบตัวที่ใช้แล้วออกจาก
`filled_letters`

```python
for char in included_chars:
    if char not in filled_letters:
        return False
    filled_letters.remove(char)
```

การใช้ `remove()` สำคัญต่อกรณีที่มีตัวอักษรซ้ำ เพราะตัวอักษรหนึ่งตัวใน
`filled_letters` จะใช้ตอบเงื่อนไขได้เพียงครั้งเดียว ลำดับตัวอักษรใน
`included_chars` ไม่สำคัญ แต่จำนวนครั้งที่แต่ละตัวปรากฏมีความสำคัญ

ตัวอย่าง `word = "MACMA"` และ `pattern = "M?C??"` จะได้

```
ตำแหน่งใน pattern        M  ?  C  ?  ?
ตัวอักษรใน word          M  A  C  M  A
ตัวอักษรใน filled_letters   A     M  A
```

ดังนั้น `included_chars = "MAA"` ผ่านเงื่อนไข เพราะมี `M` หนึ่งตัวและ `A`
สองตัวในช่อง `?` แต่ `included_chars = "AAA"` ไม่ผ่าน เพราะมี `A`
ในช่องเหล่านั้นเพียงสองตัว นอกจากนี้ `included_chars = "C"` ก็ไม่ผ่าน
เนื่องจาก `C` อยู่ในตำแหน่งคงที่ ไม่ใช่ตำแหน่ง `?`

## ลำดับการทำงาน

ฟังก์ชัน `match()` ตรวจเงื่อนไขตามลำดับต่อไปนี้

1. เรียก `is_pattern_match()` เพื่อตรวจความยาวและตัวอักษรตำแหน่งคงที่
2. เรียก `has_excluded_char()` หากพบตัวอักษรต้องห้ามในช่อง `?` ให้คืน `False`
3. เรียก `has_all_included_chars()` เพื่อตรวจตัวอักษรบังคับพร้อมจำนวนซ้ำ
4. คืนผลลัพธ์จากขั้นตอนที่ 3 เป็นคำตอบสุดท้าย

ถ้า `included_chars` หรือ `excluded_chars` เป็นสตริงว่าง การวนตรวจเงื่อนไขนั้น
จะไม่มีสมาชิกให้ตรวจ จึงไม่เพิ่มข้อจำกัดใด ๆ หาก `pattern` ไม่มี `?` เลย
`included_chars` ที่ไม่ว่างจะไม่ผ่าน แต่ `excluded_chars` จะไม่มีผล

โจทย์ข้อนี้ไม่มีการคำนวณตัวเลข การปัดเศษ หรือรูปแบบข้อความส่งออกจาก
`match()` โดยตรง ผลลัพธ์ของฟังก์ชันเป็นค่าบูลีน `True` หรือ `False`

## ตัวอย่างการทำงาน

จาก `word = "MACMA"` และ `pattern = "M?C??"` ช่อง `?` มีตัวอักษร
`A`, `M`, `A` ตัวอย่างต่อไปนี้จึงได้ผลลัพธ์ต่างกัน

| การเรียกฟังก์ชัน | ผลลัพธ์ | เหตุผล |
|:---|:---:|:---|
| `match("MACMA", "M?C??", "MAA", "")` | `True` | ตัวอักษรบังคับอยู่ในช่อง `?` ครบตามจำนวน |
| `match("MACMA", "M?C??", "AAA", "")` | `False` | ต้องการ `A` สามตัว แต่มีเพียงสองตัว |
| `match("MACMA", "M?C??", "C", "")` | `False` | `C` อยู่ในตำแหน่งคงที่ จึงไม่นับ |
| `match("MACMA", "M?C??", "", "MX")` | `False` | มี `M` ซึ่งเป็นตัวอักษรต้องห้ามอยู่ในช่อง `?` |
| `match("MACMA", "MACMA", "", "MACMA")` | `True` | ไม่มีช่อง `?` จึงไม่ใช้เงื่อนไขตัวอักษรต้องห้าม |

ถ้าความยาวไม่ตรงกัน เช่น `pattern = "M?C???"` หรือ `pattern = "M?C?"`
ฟังก์ชันจะคืน `False` ตั้งแต่การตรวจขั้นแรก

## การทำงานร่วมกับ Grader

บรรทัดสุดท้าย `exec(input().strip())` มีไว้ให้ระบบ Grader ส่งคำสั่งทดสอบ
เข้ามาหนึ่งบรรทัด เช่น

```python
print(match("MACMA", "M?C??", "MAA", ""))
```

`input()` รับข้อความคำสั่ง ส่วน `exec()` นำข้อความนั้นไปรันเป็นโค้ด Python
จึงทำให้ Grader เรียกฟังก์ชันและตรวจผลลัพธ์ได้ บรรทัดนี้เป็นส่วนหนึ่งของรูปแบบ
การตรวจคำตอบและต้องคงไว้ตามโจทย์

> [!WARNING]
>
> `exec()` สามารถรันโค้ดใด ๆ ที่อยู่ในข้อความได้ จึงควรใช้ที่นี่เฉพาะกับข้อมูล
> จากระบบ Grader ที่เชื่อถือได้เท่านั้น ห้ามใช้รูปแบบนี้กับข้อมูลจากผู้ใช้หรือ
> แหล่งที่ไม่เชื่อถือ

---

# Solution

```python
# --------------------------------------------------
# File Name : 2565_1_Q2_02.py
# Problem   : Match
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------


# Check if a word matches a given pattern
def is_pattern_match(word, pattern):
    # Check if the lengths of the word and pattern are the same
    if len(word) != len(pattern):
        return False

    # Check each character in the word against the pattern
    # Skip characters in the pattern that are '?'
    for i in range(len(word)):
        if pattern[i] != "?" and pattern[i] != word[i]:
            return False
    return True


# Check if all letters in ? position are in the excluded characters
def has_excluded_char(word, pattern, excluded_chars):
    for i in range(len(word)):
        if pattern[i] == "?" and word[i] in excluded_chars:
            return True
    return False


# Check if all letters in ? position are in the included characters
def has_all_included_chars(word, pattern, included_chars):
    # Collect letters from the word that are in ? positions
    filled_letters = []
    for i in range(len(word)):
        if pattern[i] == "?":
            filled_letters.append(word[i])

    # Check if all included characters are in the filled letters
    for char in included_chars:
        if char not in filled_letters:
            return False
        # Remove the checked character
        filled_letters.remove(char)
    return True


def match(word, pattern, included_chars, excluded_chars):
    # Check if the word matches the pattern
    if not is_pattern_match(word, pattern):
        return False

    # Check if the word contains any excluded characters
    if has_excluded_char(word, pattern, excluded_chars):
        return False

    return has_all_included_chars(word, pattern, included_chars)


# Execute a input string as code
exec(input().strip())
```
