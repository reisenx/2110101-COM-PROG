<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Complex Replace ★★★ (
      <a href="https://drive.google.com/file/d/1Zd8MrUHO1P-jSGC2izMmDDlxk3BqJw1O/view?usp=sharing">
        <code>2565_2_Q2_03</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเลือกข้อความที่อยู่ซ้ายสุด**](#การเลือกข้อความที่อยู่ซ้ายสุด)
-   [**การแทนที่ข้อความ**](#การแทนที่ข้อความ)
-   [**Solution**](#solution)

---

## การเลือกข้อความที่อยู่ซ้ายสุด

ฟังก์ชัน `complex_replace(text, patterns, replacements)` รับข้อความหลัก
พร้อมลิสต์ข้อความที่ต้องการค้นหาและลิสต์ข้อความสำหรับแทนที่ โดย
`patterns[i]` จับคู่กับ `replacements[i]` ที่ตำแหน่งเดียวกัน

โจทย์ต้องการแทนเพียงหนึ่งข้อความ คือข้อความที่มี **ตำแหน่งเริ่มต้นซ้ายสุด**
ฟังก์ชันช่วย `find_leftmost_replace()` จึงวนดู `patterns` ทุกตัว แล้วใช้
`text.find(pattern)` หาตำแหน่งแรกที่ pattern นั้นปรากฏใน `text`

-   หากพบ `str.find()` จะคืน index ของอักขระตัวแรกของ pattern
-   หากไม่พบจะคืน `-1` และโปรแกรมจะไม่นำ pattern นั้นไปเป็นตัวเลือก

ทุก pattern ที่พบจะถูกเก็บพร้อมข้อมูลสำหรับแทนที่ในรูปแบบ
`[idx, pattern, replacement]` จากนั้น `all_replaceable.sort()` จะเรียงลิสต์
โดยดู `idx` ซึ่งเป็นสมาชิกตัวแรกก่อน แล้วคืนตัวเลือกแรกที่อยู่ซ้ายสุด

เช่น เมื่อค้นหา `['war', 'wor', 'java']` ใน `"java world"` จะไม่พบ `war`
แต่พบ `wor` ที่ index `5` และ `java` ที่ index `0` ดังนั้นตัวเลือกที่คืนคือ
`[0, 'java', 'C']` เมื่อ replacement ที่ตรงกันคือ `C`

> [!NOTE]
>
> โจทย์รับประกันว่า pattern ที่พบจะไม่มีสองตัวเริ่มที่ index เดียวกัน
> จึงตัดสินตัวเลือกได้จากตำแหน่งเริ่มต้นเพียงอย่างเดียว และถ้า pattern เดิม
> ปรากฏหลายครั้ง `find()` จะเลือกเฉพาะครั้งแรกของ pattern นั้น

---

## การแทนที่ข้อความ

หากไม่พบ pattern ใดเลย `find_leftmost_replace()` จะคืน `[-1, "", ""]`
เมื่อ `complex_replace()` เห็นว่า `idx == -1` จึงคืน `text` เดิมโดยไม่แก้ไข

เมื่อพบ pattern โปรแกรมประกอบผลลัพธ์จากสามส่วน ได้แก่

1. ข้อความก่อน pattern จาก `text[:idx]`
2. replacement ที่ครอบด้วย `<` และ `>`
3. ข้อความหลัง pattern จาก `text[idx + len(pattern):]`

การทำงานตรงกับ f-string ในโปรแกรม

```python
f"{text[:idx]}<{replacement}>{text[idx + len(pattern):]}"
```

ตัวอย่าง `complex_replace("java world", ["a", "o"], ["A", "O"])`
พบ `a` ครั้งแรกที่ index `1` และพบ `o` ที่ index `6` จึงเลือก `a`
แล้วประกอบ `"j" + "<A>" + "va world"` เป็น `"j<A>va world"`

โปรแกรมแทนที่เฉพาะ pattern ที่เลือกหนึ่งครั้งเท่านั้น แม้ pattern เดียวกัน
จะปรากฏซ้ำหรือมี pattern อื่นอยู่ทางขวา และการค้นหาของ `str.find()`
แยกตัวพิมพ์เล็กกับตัวพิมพ์ใหญ่ หากไม่พบตัวใด ผลลัพธ์จะเป็นข้อความเดิม

บรรทัด `exec(input().strip())` เปิดให้ grader ป้อนคำสั่งเรียกฟังก์ชัน
เช่น `print(complex_replace(...))` เข้ามาเป็นข้อความ `strip()` ตัดช่องว่าง
หัวและท้าย ก่อนที่ `exec()` จะประมวลผลข้อความนั้นเป็นโค้ด Python

> [!WARNING]
>
> ควรใช้ `exec()` เฉพาะกับคำสั่งทดสอบที่เชื่อถือได้จาก grader เท่านั้น
> เพราะข้อความที่ส่งให้ `exec()` สามารถสั่งให้ Python ทำงานใด ๆ ก็ได้
> จึงไม่ปลอดภัยสำหรับข้อมูลจากผู้ใช้หรือแหล่งที่ไม่เชื่อถือ

---

# Solution

```python
# --------------------------------------------------
# File Name : 2565_2_Q2_03.py
# Problem   : Complex Replace
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------


# Find the leftmost replaceable pattern in the text
def find_leftmost_replace(text, patterns, replacements):
    # Find all patterns that are replaceable in the text
    all_replaceable = []
    for i in range(len(patterns)):
        # Extract the pattern and replacement
        pattern = patterns[i]
        replacement = replacements[i]
        # Find the index of the first occurrence of the pattern
        idx = text.find(pattern)
        # If the pattern is found, add it to the list of replaceable patterns
        if idx != -1:
            all_replaceable.append([idx, pattern, replacement])

    # If no patterns are found, return [-1, "", ""]
    if len(all_replaceable) == 0:
        return [-1, "", ""]
    # Sort the replaceable patterns by their index and return the leftmost one
    all_replaceable.sort()
    return all_replaceable[0]


# Replace the leftmost pattern in the text with its replacement
def complex_replace(text, patterns, replacements):
    # Find the leftmost replaceable pattern
    idx, pattern, replacement = find_leftmost_replace(text, patterns, replacements)
    # If no pattern is found, return the original text
    if idx == -1:
        return text
    # Replace the pattern with its replacement and return the modified text
    return f"{text[:idx]}<{replacement}>{text[idx + len(pattern):]}"


# Execute a input string as code
exec(input().strip())
```
