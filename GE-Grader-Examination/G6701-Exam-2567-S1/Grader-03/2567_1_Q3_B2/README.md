<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Text Replace ★★☆ (
      <a href="https://drive.google.com/file/d/1j19e7_1eHrJkVVQhZYDJN_IPz6V9dBTP/view?usp=sharing">
        <code>2567_1_Q3_B2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเตรียมข้อความสำหรับค้นหา**](#การเตรียมข้อความสำหรับค้นหา)
-   [**การค้นหาแบบไม่ซ้อนทับ**](#การค้นหาแบบไม่ซ้อนทับ)
-   [**การชดเชยตำแหน่งหลังแทนข้อความ**](#การชดเชยตำแหน่งหลังแทนข้อความ)
-   [**การแทนข้อความข้ามบรรทัด**](#การแทนข้อความข้ามบรรทัด)
-   [**Solution**](#solution)

---

## การเตรียมข้อความสำหรับค้นหา

อินพุตบรรทัดแรกอยู่ในรูป `ข้อความที่ค้นหา/ข้อความใหม่`
อักขระ `/` ไม่อยู่ในข้อความทั้งสองฝั่งตามเงื่อนไข จึงแยกได้ด้วย

```python
target, replacement_str = input().strip().split("/")
```

`target` ถูกเปลี่ยนเป็นตัวพิมพ์เล็กเพื่อค้นหาแบบ case insensitive
ส่วน `replacement_str` คงรูปแบบตัวพิมพ์ตามที่รับมา

เช่นเดียวกับโจทย์ Text Search โปรแกรมสร้างข้อความสองชุด

-   `query_passage` เป็นตัวพิมพ์เล็ก และใช้ช่องว่างหนึ่งตัวแทนจุดขึ้นบรรทัดใหม่
-   `output` เก็บตัวอักษรเดิม และใช้ `\n` ที่จุดขึ้นบรรทัดใหม่

เพราะช่องว่างกับ `\n` ยาวหนึ่งอักขระ ตำแหน่งก่อนการแทนครั้งแรกจึงตรงกัน

---

## การค้นหาแบบไม่ซ้อนทับ

โปรแกรมค้นหาด้วย

```python
start_idx = query_passage.find(target, find_start_idx)
```

เมื่อพบแล้วจะกำหนดจุดเริ่มค้นหาครั้งต่อไปเป็น `end_idx`
จึงไม่เลือกคำที่ทับกับช่วงเดิม ตัวอย่างค้นหา `aa` ใน `aaaaa`
จะเลือกตำแหน่ง `0:2` และ `2:4` เท่านั้น

การค้นหาทุกครั้งทำใน `query_passage` ซึ่งไม่ถูกแก้ไข
ดังนั้นข้อความใหม่ที่เพิ่งแทนลงไปจะไม่ถูกนำมาค้นหาซ้ำ

---

## การชดเชยตำแหน่งหลังแทนข้อความ

ข้อความใหม่อาจยาวกว่า สั้นกว่า หรือยาวเท่าข้อความเดิม โปรแกรมคำนวณส่วนต่างว่า

```python
REPLACEMENT_OFFSET = len(replacement_str) - len(target)
```

หลังแทนไปแล้ว `replacement_count` ครั้ง ตำแหน่งใน `output` จะเลื่อนไปจาก
ตำแหน่งใน `query_passage` เป็นระยะ

$$
\text{offset} =
  \bigl(\text{ความยาวข้อความใหม่} - \text{ความยาวข้อความเดิม}\bigr)
  \times \text{จำนวนครั้งที่แทนแล้ว}
$$

จึงปรับทั้ง `start_idx` และ `end_idx` ด้วยค่านี้ก่อนใช้ slicing

```python
output = output[:start_idx] + replacement_str + output[end_idx:]
```

ถ้าข้อความใหม่สั้นกว่า ค่า offset จะติดลบและเลื่อนตำแหน่งกลับทางซ้ายได้ถูกต้อง

---

## การแทนข้อความข้ามบรรทัด

ถ้าช่องว่างใน `target` ตรงกับจุดขึ้นบรรทัดใหม่ โปรแกรมยังค้นพบได้
เพราะ `query_passage` ใช้ช่องว่างแทน `\n` เมื่อ slice ช่วงเดียวกันออกจาก
`output` ช่วงนั้นจะรวมอักขระขึ้นบรรทัดใหม่ด้วย และถูกแทนทั้งช่วงด้วย
`replacement_str` ทำให้ข้อความก่อนและหลังคำใหม่มาต่อกันตามตัวอย่างโจทย์

แต่ถ้าขึ้นบรรทัดใหม่กลางคำ `query_passage` จะมีช่องว่างเพิ่มกลางคำนั้น
จึงไม่ตรงกับ target ที่ไม่มีช่องว่าง

> [!NOTE]
>
> `output.strip()` ตัดช่องว่างรอบนอกก่อนแสดงผล โจทย์รับประกันว่าไม่มีช่องว่าง
> ท้ายบรรทัด จึงไม่เสียข้อมูลตามรูปแบบอินพุตที่กำหนด

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q3_B2.py
# Problem   : Text Replace
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input target and its replacement string
target, replacement_str = input().strip().split("/")
target = target.strip().lower()

# Calculate replacement offset
REPLACEMENT_OFFSET = len(replacement_str) - len(target)

# Initialize query passage and output strings
query_passage = ""
output = ""

# Input number of lines and read each line of the passage
n = int(input())
for _ in range(n):
    # Input each line of the passage
    line = input().strip()

    # Add lowercase line and replace newline characters with spaces
    # to query passage for case-insensitive search
    query_passage += line.lower() + " "

    # Add the exact passage line to the output string
    output += line + "\n"

# Remove trailing spaces from the query passage
query_passage = query_passage.strip()

# Initialize variables for searching and replacing
replacement_count = 0
find_start_idx = 0

while True:
    # Find the next occurrence of the target in the query passage
    start_idx = query_passage.find(target, find_start_idx)
    end_idx = start_idx + len(target)

    # Update the start index for the next search
    find_start_idx = end_idx

    # If no more occurrences are found, break the loop
    if start_idx == -1:
        break

    # Add the offset to the start and end indices for replacement on the output string
    start_idx += REPLACEMENT_OFFSET * replacement_count
    end_idx += REPLACEMENT_OFFSET * replacement_count

    # Replace the target in the output string with the replacement string
    output = output[:start_idx] + replacement_str + output[end_idx:]

    # Increment the replacement count
    replacement_count += 1

# Output the final result
print(output.strip())
```
