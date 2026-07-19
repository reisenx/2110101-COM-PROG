<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Matching Rule ★★★ (
      <a href="https://drive.google.com/file/d/16Gvn09eigAaaOKhbSdg5DJ9Bx_W5tTHV/view?usp=sharing">
        <code>2565_2_Q2_02</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**รูปแบบของ Matching Rule**](#รูปแบบของ-matching-rule)
-   [**การแปลงเงื่อนไขเป็นรายการ**](#การแปลงเงื่อนไขเป็นรายการ)
-   [**การตรวจสอบข้อความ**](#การตรวจสอบข้อความ)
-   [**Solution**](#solution)

---

## รูปแบบของ Matching Rule

ฟังก์ชัน `match(text, pattern_str)` ตรวจว่าข้อความ `text` ตรงกับเงื่อนไข
`pattern_str` หรือไม่ โดยเงื่อนไขหนึ่งตำแหน่งต้องตรงกับอักขระของข้อความ
**หนึ่งตัวพอดี** รูปแบบที่โปรแกรมรองรับมีดังนี้

| รูปแบบ | กฎของอักขระตำแหน่งนั้น | ตัวอย่างที่ตรงกัน |
|:---:|---|---|
| `a` | ต้องเป็นอักขระ `a` เท่านั้น (`exact`) | `a` |
| `?` | เป็นตัวอักษรหรือตัวเลขใดก็ได้หนึ่งตัว (`any`) | `b`, `7` |
| `[abc]` | ต้องเป็นหนึ่งในอักขระภายใน `[]` (`include`) | `a`, `b`, `c` |
| `(abc)` | ต้องไม่เป็นอักขระภายใน `()` (`exclude`) | `d`, `5` |

วงเล็บหนึ่งชุดนับเป็นเงื่อนไขเพียงหนึ่งตำแหน่ง ไม่ว่าข้างในจะมีอักขระกี่ตัว
เช่น `[bcd]` ใช้ตรวจอักขระหนึ่งตัว ไม่ได้ใช้ตรวจข้อความยาวสามตัว และ `?`
ต้องแทนอักขระหนึ่งตัวเสมอ จึงไม่สามารถแทนข้อความว่างหรือหลายตัวได้

---

## การแปลงเงื่อนไขเป็นรายการ

เพื่อให้ตรวจทีละตำแหน่งได้ง่าย ฟังก์ชัน `pattern_to_list()` จะแปลงข้อความ
เงื่อนไขเป็นลิสต์ที่แต่ละสมาชิกเก็บ `[chars, rule]`

ขั้นแรก โปรแกรมเติมช่องว่างรอบ `[]` และ `()` แล้วใช้ `split()` แบ่งเงื่อนไข
ออกเป็นส่วน ๆ เช่น

```text
a[bcd](123)bc  →  a  [bcd]  (123)  bc
```

จากนั้นจึงพิจารณาแต่ละส่วนตามลำดับ

-   ส่วนที่ขึ้นต้นและลงท้ายด้วย `()` จะตัดวงเล็บออกด้วย `part[1:-1]`
    แล้วเก็บกฎ `"exclude"`
-   ส่วนที่ขึ้นต้นและลงท้ายด้วย `[]` จะตัดวงเล็บออกเช่นกัน แล้วเก็บกฎ
    `"include"`
-   ส่วนที่อยู่นอกวงเล็บจะวนดูทีละอักขระ ถ้าเป็น `?` จะเก็บกฎ `"any"`
    มิฉะนั้นจะเก็บกฎ `"exact"`

ดังนั้น `a[bcd](123)bc` จะกลายเป็นลิสต์ที่มี 5 ตำแหน่ง

```python
[
    ["a", "exact"],
    ["bcd", "include"],
    ["123", "exclude"],
    ["b", "exact"],
    ["c", "exact"],
]
```

---

## การตรวจสอบข้อความ

ฟังก์ชัน `match()` เริ่มจากเรียก `pattern_to_list()` ก่อน หากจำนวนอักขระ
ใน `text` ไม่เท่ากับจำนวนเงื่อนไข โปรแกรมคืนค่า `False` ทันที เช่น `a?b`
มี 3 ตำแหน่ง จึงไม่ตรงกับ `ab` ที่มีเพียง 2 ตัว

เมื่อความยาวเท่ากัน โปรแกรมจะตรวจ `text[i]` กับ `[chars, rule]` ตำแหน่ง
เดียวกัน และคืนค่า `False` ทันทีเมื่อพบกรณีใดกรณีหนึ่งต่อไปนี้

-   กฎ `exact` แต่อักขระไม่เท่ากับ `chars`
-   กฎ `include` แต่อักขระไม่อยู่ใน `chars`
-   กฎ `exclude` แต่อักขระกลับอยู่ใน `chars`

กฎ `any` ไม่มีเงื่อนไขที่ทำให้ไม่ผ่าน จึงยอมรับอักขระตำแหน่งนั้นเสมอ
หากตรวจครบทุกตำแหน่งโดยไม่พบข้อผิดเงื่อนไข ฟังก์ชันจึงคืนค่า `True`

ตัวอย่าง `match("ab4bc", "a[bcd](123)bc")` คืนค่า `True` เพราะ `b`
อยู่ใน `bcd`, ตัว `4` ไม่อยู่ใน `123` และตำแหน่งอื่นตรงแบบ `exact` ทั้งหมด
ค่าที่ฟังก์ชันส่งกลับเป็น Boolean `True` หรือ `False`; หากต้องการเห็นผลบนจอ
คำสั่งทดสอบของโจทย์จึงเรียกผ่าน `print(match(...))`

บรรทัดสุดท้าย `exec(input().strip())` มีไว้ให้ grader ส่งคำสั่งทดสอบ
เช่น `print(match('aa', 'a?'))` เข้ามาหนึ่งบรรทัด `strip()` จะตัดช่องว่าง
หัวและท้าย แล้ว `exec()` จึงประมวลผลข้อความนั้นเป็นคำสั่ง Python

> [!WARNING]
>
> `exec()` สามารถรันคำสั่ง Python ใด ๆ ที่อยู่ในข้อความได้ จึงใช้ในข้อนี้
> เพื่อรองรับคำสั่งจาก grader ที่เชื่อถือได้เท่านั้น ไม่ควรใช้กับข้อความจาก
> ผู้ใช้หรือแหล่งข้อมูลที่ไม่เชื่อถือในโปรแกรมทั่วไป

---

# Solution

```python
# --------------------------------------------------
# File Name : 2565_2_Q2_02.py
# Problem   : Matching Rule
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------


# Convert a pattern string to a pattern list which contains
# each character and its matching rule.
def pattern_to_list(pattern_str):
    # Add spaces around brackets and parentheses for splitting
    temp = (
        pattern_str.replace("[", " [")
        .replace("]", "] ")
        .replace("(", " (")
        .replace(")", ") ")
    )

    # Split the string into parts and create a pattern list
    pattern = []
    for part in temp.split():
        # Check if the part has parentheses which indicate a exclude rule
        if part[0] + part[-1] == "()":
            pattern.append([part[1:-1], "exclude"])
        # Check if the part has brackets which indicate a include rule
        elif part[0] + part[-1] == "[]":
            pattern.append([part[1:-1], "include"])
        # Otherwise, it is a single character with exact or any rule
        else:
            # Add each character in the part to the pattern list
            for char in part:
                if char == "?":
                    pattern.append(["?", "any"])
                else:
                    pattern.append([char, "exact"])
    # Return the pattern list
    return pattern


# Match a text against a pattern list
def match(text, pattern_str):
    # Convert the pattern string to a pattern list
    pattern = pattern_to_list(pattern_str)
    # Check if the length of text matches the length of pattern
    if len(text) != len(pattern):
        return False

    # Check each character in the text against the pattern
    for i in range(len(text)):
        # Extract the characters and rule from the pattern list
        chars, rule = pattern[i]
        # Check if the character in text matches the rule
        if (
            (rule == "exact" and text[i] != chars)
            or (rule == "include" and text[i] not in chars)
            or (rule == "exclude" and text[i] in chars)
        ):
            return False
    return True


# Execute a input string as code
exec(input().strip())
```
