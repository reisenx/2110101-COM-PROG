<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Jumping Bug ★★ (
      <a href="https://drive.google.com/file/d/1MP-Vht8zederPQOsSz3z0IIsUNj98Gcf/view?usp=sharing">
        <code>2567_1_Q3_A2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ตัวแปรหลักและสูตรการกระโดด**](#ตัวแปรหลักและสูตรการกระโดด)
-   [**การจัดการหลุมโคลน**](#การจัดการหลุมโคลน)
-   [**เงื่อนไขหยุดกระโดด**](#เงื่อนไขหยุดกระโดด)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ข้อควรระวังเรื่องจำนวนจริง**](#ข้อควรระวังเรื่องจำนวนจริง)
-   [**Solution**](#solution)

---

## ตัวแปรหลักและสูตรการกระโดด

แมลงเริ่มที่ตำแหน่ง `0` และต้องเข้าไปอยู่ในบริเวณสิ้นสุด ซึ่งหมายถึง
เหลือระยะถึงปลายทางไม่เกิน `end_gap` โปรแกรมเก็บสถานะสำคัญสองค่า

-   `current_distance` คือตำแหน่งปัจจุบันที่วัดจากจุดเริ่มต้น
-   `remaining_distance` คือระยะที่ยังเหลือถึงปลายทาง

ตอนเริ่มต้นจึงมีค่าเป็น `0` และ `total_distance` ตามลำดับ

ถ้าก่อนกระโดดเหลือระยะ $R$ และ `jump_factor` มีค่า $f$
ระยะกระโดดครั้งถัดไปคือ

$$
J = fR
$$

ตรงกับคำสั่ง `jump_distance = jump_factor * remaining_distance` หลังจากกระโดด
โปรแกรมปรับตำแหน่งและระยะที่เหลือด้วย

```python
current_distance += jump_distance
remaining_distance -= jump_distance
```

ดังนั้นหากไม่มีการเดินผ่านหลุม ระยะที่เหลือใหม่เท่ากับ
$(1-f)R$ ทุกครั้งที่กระโดด และตัวแปร `jumps` จะเพิ่มขึ้นครั้งละ `1`

---

## การจัดการหลุมโคลน

ที่ต้นรอบของลูป โปรแกรมตรวจว่าตำแหน่งปัจจุบันอยู่ในช่วงปิด
`pit_start <= current_distance <= pit_end` หรือไม่ คำว่า *ช่วงปิด* หมายความว่า
การตกตรงขอบ `pit_start` หรือ `pit_end` ก็นับว่าอยู่ในหลุมด้วย

ถ้าอยู่ในหลุม แมลงจะเดินไปที่ `pit_end` และคำนวณระยะที่เหลือใหม่

```python
current_distance = pit_end
remaining_distance = total_distance - pit_end
```

การเดินนี้ไม่ใช่การกระโดด จึงไม่เพิ่ม `jumps` เนื่องจากตรวจหลุมที่ต้นรอบ
ผลของการกระโดดลงหลุมจะถูกจัดการก่อนการกระโดดครั้งถัดไป

หากไม่มีหลุม โจทย์กำหนดให้ `pit_start` และ `pit_end` เป็น `-1` ทั้งคู่
ตำแหน่งของแมลงเริ่มที่ `0` และเพิ่มขึ้น จึงไม่เข้าเงื่อนไขช่วง `[-1, -1]`

---

## เงื่อนไขหยุดกระโดด

ลูปทำงานขณะที่ `remaining_distance > end_gap` เมื่อระยะที่เหลือ
**น้อยกว่าหรือเท่ากับ** `end_gap` แมลงอยู่ในบริเวณสิ้นสุดแล้ว จึงหยุด

โปรแกรมตรวจเงื่อนไขนี้สองตำแหน่ง

1. ที่เงื่อนไขของ `while` สำหรับกรณีทั่วไปหลังการกระโดด
2. หลังเดินถึง `pit_end` เพื่อหยุดทันทีหากปลายหลุมอยู่ในบริเวณสิ้นสุด

การตรวจครั้งที่สองทำให้ไม่มีการกระโดดเพิ่มโดยไม่จำเป็น ส่วน `break`
จะออกจากลูปและไปแสดงจำนวนครั้งที่กระโดด

กรณีที่ `total_distance <= end_gap` ตั้งแต่ต้น ลูปจะไม่ทำงานและผลลัพธ์เป็น `0`

---

## ตัวอย่างการทำงาน

เมื่อ `total_distance = 15`, `jump_factor = 0.5`, `end_gap = 1.5`
และหลุมอยู่จาก `4.8` ถึง `9.8` เมตร

| ครั้ง | จุดเริ่ม | ระยะกระโดด | จุดที่ถึง | เหตุการณ์ |
|---:|---:|---:|---:|:---|
| 1 | `0` | `0.5 * 15 = 7.5` | `7.5` | ตกในหลุม แล้วเดินถึง `9.8` |
| 2 | `9.8` | `0.5 * 5.2 = 2.6` | `12.4` | เหลือ `2.6` เมตร |
| 3 | `12.4` | `0.5 * 2.6 = 1.3` | `13.7` | เหลือ `1.3` เมตร จึงหยุด |

โปรแกรมจึงแสดง `3` การเดินจาก `7.5` ถึง `9.8` ไม่ถูกนับเป็นการกระโดด

---

## ข้อควรระวังเรื่องจำนวนจริง

> [!WARNING]
>
> ตัวแปรทั้งหมดรับด้วย `float()` และโปรแกรมเปรียบเทียบค่าด้วย `<=` และ `>`
> โดยตรง จำนวนจริงบางค่าอาจเก็บในคอมพิวเตอร์ได้ไม่ตรงทั้งหมด
> จึงควรไล่ค่าตามผลการคำนวณของ Python โดยเฉพาะกรณีที่ตำแหน่งอยู่ใกล้
> `pit_start`, `pit_end` หรือขอบ `end_gap` มาก ๆ

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q3_A2.py
# Problem   : Jumping Bug
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input information of the ground and the bug
total_distance = float(input())
jump_factor = float(input())
end_gap = float(input())

# Input information of the pit on the ground
pit_start = float(input())
pit_end = float(input())

# Initialize variables
current_distance = 0
remaining_distance = total_distance
jumps = 0

# Loop until the bug reaches the end gap of the ground
while remaining_distance > end_gap:
    # Check if the bug is in the pit
    if pit_start <= current_distance <= pit_end:
        # Set the current position to the end of the pit
        current_distance = pit_end
        remaining_distance = total_distance - pit_end

    # Stop if the bug is at or beyond the end gap
    if remaining_distance <= end_gap:
        break
    # Calculate the jump distance of the bug
    jump_distance = jump_factor * remaining_distance

    # Update the current distance and remaining distance
    current_distance += jump_distance
    remaining_distance -= jump_distance

    # Increment the jump count
    jumps += 1

# Output the number of jumps made by the bug
print(jumps)
```
