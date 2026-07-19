<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Bad Words ★☆ (
      <a href="https://drive.google.com/file/d/1EbQl9iRAR5RYoMG8uj5-foiY2b5J6Ydo/view?usp=sharing">
        <code>2566_2_Q2_01</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**โจทย์ต้องการอะไร**](#โจทย์ต้องการอะไร)
-   [**แนวคิดในการแก้ปัญหา**](#แนวคิดในการแก้ปัญหา)
-   [**ลำดับการทำงาน**](#ลำดับการทำงาน)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ข้อควรระวัง**](#ข้อควรระวัง)
-   [**Solution**](#solution)

---

# โจทย์ต้องการอะไร

โปรแกรมรับข้อมูล 2 บรรทัดตามลำดับดังนี้

1. รายการคำไม่สุภาพ คั่นแต่ละคำด้วยช่องว่าง
2. ข้อความที่ต้องการตรวจสอบ

จากนั้นให้ค้นหาทุก **สตริงย่อย** ที่ตรงกับคำไม่สุภาพโดยไม่สนใจตัวพิมพ์เล็กหรือตัวพิมพ์ใหญ่ แล้วแทนสระ `a`, `e`, `i`, `o`, `u` ภายในสตริงย่อยนั้นด้วย `*` ส่วนพยัญชนะ เครื่องหมายต่าง ๆ และรูปแบบตัวพิมพ์เดิมต้องอยู่เหมือนเดิม

ตัวอย่างเช่น เมื่อคำไม่สุภาพคือ `damn` ข้อความ `Damnit` จะกลายเป็น `D*mnit` เพราะ `Damn` ที่อยู่ต้นคำเป็นสตริงย่อยที่ตรงกัน

# แนวคิดในการแก้ปัญหา

## 1. ซ่อนสระโดยยังรักษาตัวอักษรเดิม

ฟังก์ชัน `hide_vowels(word)` พิจารณาตัวอักษรทีละตัว แล้วใช้ `char.lower()` เพื่อตรวจว่าเป็นสระหรือไม่ การแปลงเป็นตัวพิมพ์เล็กเกิดขึ้นเพื่อใช้เปรียบเทียบเท่านั้น จึงยังรักษาตัวพิมพ์ของพยัญชนะในข้อความเดิมได้

```python
if char.lower() in "aeiou":
    char = "*"
```

เนื่องจากสตริงแก้ไขตัวอักษรภายในโดยตรงไม่ได้ ฟังก์ชันจึงค่อย ๆ ต่อผลลัพธ์ใหม่ลงใน `result` แล้วคืนสตริงที่ซ่อนสระเรียบร้อยแล้ว

## 2. ค้นหาแบบไม่สนใจตัวพิมพ์เล็ก-ใหญ่

ฟังก์ชัน `censor_text(text, target)` แปลงทั้งข้อความและคำเป้าหมายเป็นตัวพิมพ์เล็กเฉพาะตอนค้นหา

```python
start_idx = result.lower().find(target.lower(), search_idx)
```

เมธอด `.find()` คืนตำแหน่งเริ่มต้นของคำที่พบ หรือคืน `-1` เมื่อหาไม่พบแล้ว หากพบคำ ตำแหน่งท้ายคำนวณได้จาก

$$
\text{end\_idx} = \text{start\_idx} + \operatorname{len}(\text{target})
$$

ซึ่งตรงกับคำสั่ง Python `end_idx = start_idx + len(target)` และช่วงคำที่พบคือ `result[start_idx:end_idx]`

## 3. แบ่งข้อความแล้วประกอบกลับ

เมื่อรู้ขอบเขตของคำแล้ว โปรแกรมแบ่งข้อความเป็น 3 ส่วน

- `result[:start_idx]` คือข้อความก่อนคำเป้าหมาย
- `result[start_idx:end_idx]` คือคำเป้าหมายที่ต้องส่งให้ `hide_vowels()`
- `result[end_idx:]` คือข้อความหลังคำเป้าหมาย

เมื่อนำทั้งสามส่วนมาต่อกัน ความยาวข้อความจะเท่าเดิม จากนั้นกำหนด `search_idx = end_idx` เพื่อค้นหาครั้งต่อไปจากตำแหน่งหลังคำที่เพิ่งแก้ และไม่วนกลับไปพบคำเดิมซ้ำ

# ลำดับการทำงาน

1. อ่านรายการคำไม่สุภาพด้วย `.split()` ให้ได้ลิสต์ `offensive_words`
2. อ่านข้อความต้นฉบับเก็บไว้ใน `text`
3. นำคำแต่ละคำใน `offensive_words` ไปเรียก `censor_text()` ตามลำดับ
4. ภายใน `censor_text()` ค้นหาและซ่อนสระของทุกตำแหน่งที่พบจน `.find()` คืน `-1`
5. แสดงข้อความหลังจากประมวลผลครบทุกคำ

# ตัวอย่างการทำงาน

กำหนดคำไม่สุภาพเป็น `damn` และข้อความเป็น

```text
Damnit, I don't give a damn.
```

- การค้นหาครั้งแรกพบ `Damn` ที่ตำแหน่งต้นข้อความ แล้ว `hide_vowels("Damn")` คืน `D*mn`
- โปรแกรมค้นหาต่อจากท้ายคำแรก จึงพบ `damn` อีกครั้งและเปลี่ยนเป็น `d*mn`
- เครื่องหมายวรรคตอน ช่องว่าง และข้อความส่วนอื่นไม่เปลี่ยน

ผลลัพธ์คือ

```text
D*mnit, I don't give a d*mn.
```

# ข้อควรระวัง

> [!NOTE]
> โจทย์ให้ค้นหา **สตริงย่อย** ไม่ได้ตรวจขอบเขตของคำ ดังนั้น `damn` ต้องตรงกับส่วนต้นของ `Damnit` แต่ไม่ตรงกับ `darn` และการค้นหาไม่สนใจตัวพิมพ์เล็ก-ใหญ่

- โปรแกรมซ่อนเฉพาะสระภาษาอังกฤษใน `"aeiou"`; ตัวอักษร `y` ไม่ถูกนับเป็นสระ
- หากไม่พบคำเป้าหมาย ข้อความจะคงเดิม
- การกำหนด `search_idx = end_idx` ทำให้การพบคำแต่ละครั้งไม่ซ้อนทับกัน
- การใช้ `.strip()` ตอนรับข้อมูลทำให้ช่องว่างที่ต้นและท้ายบรรทัดถูกตัดออก ซึ่งเป็นพฤติกรรมของโค้ดชุดนี้

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_2_Q2_01.py
# Problem   : Bad Words
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------


# Replace vowels in offensive words with '*'
def hide_vowels(word):
    result = ""
    for char in word:
        if char.lower() in "aeiou":
            char = "*"
        result += char
    return result


# Censor the text by replacing offensive word with their vowel-hidden versions
def censor_text(text, target):
    # Initialize the result with the original text and search index
    result = text
    search_idx = 0
    # Loop to find and replace all occurrences of the target word
    while True:
        # Find the next occurrence of the target word
        start_idx = result.lower().find(target.lower(), search_idx)
        end_idx = start_idx + len(target)
        # If no more occurrences are found, break the loop
        if start_idx == -1:
            break
        # Replace the target word with its vowel-hidden version
        before_target = result[:start_idx]
        censored_target = hide_vowels(result[start_idx:end_idx])
        after_target = result[end_idx:]
        result = before_target + censored_target + after_target
        # Update the search index to continue searching after the replaced word
        search_idx = end_idx
    # Return the censored text
    return result


# Read the list of offensive words and the text to censor
offensive_words = input().strip().split()
text = input().strip()
# Censor the text for each offensive word
for word in offensive_words:
    text = censor_text(text, word)
# Output the final censored text
print(text)
```
