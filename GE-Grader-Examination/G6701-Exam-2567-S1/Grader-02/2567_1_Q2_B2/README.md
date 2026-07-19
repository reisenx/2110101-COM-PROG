<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Text Search ★★☆ (
      <a href="https://drive.google.com/file/d/1xu1O_qGHxO20ac01xD5N8_NyYTaAmBD6/view?usp=sharing">
        <code>2567_1_Q2_B2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเตรียมข้อความสองชุด**](#การเตรียมข้อความสองชุด)
-   [**การค้นหาแบบไม่สนใจตัวพิมพ์**](#การค้นหาแบบไม่สนใจตัวพิมพ์)
-   [**การแทรกแท็กลงในผลลัพธ์**](#การแทรกแท็กลงในผลลัพธ์)
-   [**กรณีข้ามบรรทัดและกรณีขอบ**](#กรณีข้ามบรรทัดและกรณีขอบ)
-   [**Solution**](#solution)

---

## การเตรียมข้อความสองชุด

โจทย์ต้องค้นหาโดยไม่สนใจตัวพิมพ์เล็กหรือตัวพิมพ์ใหญ่
แต่ผลลัพธ์ต้องคงข้อความเดิมไว้ โปรแกรมจึงสร้างข้อความคู่ขนานสองชุด

-   `query_passage` เก็บข้อความตัวพิมพ์เล็กสำหรับค้นหา
-   `output` เก็บตัวอักษรเดิมสำหรับนำไปแสดงผล

เมื่อรับแต่ละบรรทัด โปรแกรมเติมช่องว่างหนึ่งตัวลงใน `query_passage`
และเติม `\n` หนึ่งตัวลงใน `output`

```python
query_passage += line.lower() + " "
output += line + "\n"
```

ช่องว่างกับ `\n` ต่างก็มีความยาวหนึ่งอักขระ ตำแหน่งของอักขระอื่น ๆ
ในข้อความทั้งสองชุดจึงตรงกันก่อนเริ่มแทรกแท็ก

---

## การค้นหาแบบไม่สนใจตัวพิมพ์

ข้อความเป้าหมายถูกแปลงเป็นตัวพิมพ์เล็กตั้งแต่รับข้อมูล

```python
target = input().strip().lower()
```

จากนั้น `find(target, find_start_idx)` คืนตำแหน่งเริ่มต้นของคำที่พบครั้งถัดไป
หรือคืน `-1` เมื่อหาไม่พบ โปรแกรมเลื่อนจุดค้นหาครั้งต่อไปไปที่
`end_idx` ของคำปัจจุบัน จึงเลือกเฉพาะคำที่ **ไม่ซ้อนทับกัน**

ตัวอย่างเช่น เมื่อค้นหา `aa` ใน `aaaaa` จะพบช่วงตำแหน่ง `0:2` และ `2:4`
แต่จะไม่ย้อนกลับไปเลือกช่วง `1:3`

---

## การแทรกแท็กลงในผลลัพธ์

เมื่อพบคำ โปรแกรมประกอบ `output` ใหม่จากสามส่วน คือข้อความก่อนคำ
คำเดิมที่ครอบด้วยแท็ก และข้อความหลังคำ

```python
output = (
    output[:start_idx]
    + "<found>"
    + output[start_idx:end_idx]
    + "</found>"
    + output[end_idx:]
)
```

แท็ก `<found>` และ `</found>` เพิ่มความยาวรวม

```python
REPLACEMENT_OFFSET = len("<found>") + len("</found>")
```

ดังนั้น หลังแทรกไปแล้ว `replacement_count` ครั้ง ตำแหน่งจากข้อความค้นหาเดิม
ต้องขยับไปทางขวาอีก `REPLACEMENT_OFFSET * replacement_count` ตัว
การเก็บตัวอักษรจริงจาก `output` ทำให้รูปแบบตัวพิมพ์เดิมยังอยู่ครบ

---

## กรณีข้ามบรรทัดและกรณีขอบ

ถ้าจุดขึ้นบรรทัดใหม่ตรงกับช่องว่างในคำเป้าหมาย การแทน `\n` ด้วยช่องว่างใน
`query_passage` ทำให้ยังค้นพบได้ เช่น เป้าหมาย `boiling or baking` สามารถครอบ
ข้อความที่อยู่เป็นสามบรรทัดได้ โดยแท็กใน `output` จะคร่อมบรรทัดเหล่านั้น

แต่ถ้าขึ้นบรรทัดใหม่กลางคำ เช่น `e` อยู่ท้ายบรรทัดและ `at` อยู่ต้นบรรทัดถัดไป
ข้อความค้นหาจะเป็น `e at` ไม่ใช่ `eat` จึงไม่พบตามเงื่อนไขของโจทย์

> [!NOTE]
>
> `strip()` ตอนรับและก่อนแสดงผลจะตัดช่องว่างรอบนอกของข้อความ
> โจทย์รับประกันว่าไม่มีช่องว่างท้ายบรรทัด จึงไม่กระทบข้อมูลที่กำหนดให้

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q2_B2.py
# Problem   : Text Search
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Replacement offset for "<found>" and "</found>" tags
REPLACEMENT_OFFSET = len("<found>") + len("</found>")

# Input replacement target
target = input().strip().lower()

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

    # Add "<found>" and "</found>" tags around the found target in the output string
    output = (
        output[:start_idx]
        + "<found>"
        + output[start_idx:end_idx]
        + "</found>"
        + output[end_idx:]
    )

    # Increment the replacement count
    replacement_count += 1

# Output the final result
print(output.strip())
```
