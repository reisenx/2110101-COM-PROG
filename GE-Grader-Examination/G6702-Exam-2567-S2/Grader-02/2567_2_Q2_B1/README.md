<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    List Rearragement 2 ★★ (
      <a href="https://drive.google.com/file/d/1g1L5WnvX83lrKPCAEQFQQbIM8RMDpLfe/view?usp=sharing">
        <code>2567_2_Q2_B1</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิดของลำดับ D P และ X**](#แนวคิดของลำดับ-d-p-และ-x)
-   [**การสร้างลำดับ P ในโค้ด**](#การสร้างลำดับ-p-ในโค้ด)
-   [**การสร้างลำดับ X**](#การสร้างลำดับ-x)
-   [**ความคลาดเคลื่อนระหว่างโจทย์กับโค้ด**](#ความคลาดเคลื่อนระหว่างโจทย์กับโค้ด)
-   [**การรับคำสั่งจากเกรดเดอร์**](#การรับคำสั่งจากเกรดเดอร์)
-   [**Solution**](#solution)

---

## แนวคิดของลำดับ D P และ X

โจทย์เริ่มจากลิสต์จำนวนเต็ม `D` แล้วสร้างลำดับตำแหน่ง `P`
เพื่อนำไปหยิบสมาชิกออกจาก `D` ทีละตัว สมาชิกที่หยิบได้ตามลำดับจะกลายเป็น
ลิสต์คำตอบ `X`

ฟังก์ชันในโปรแกรมใช้ชื่อตัวแปรดังนี้

-   `numbers` คือ `D` ที่รับเข้ามา
-   `positions` คือ `P` ที่ได้จาก `find_P()`
-   `rearranged_numbers` คือ `X` ที่ `rearrange()` สร้างขึ้น

---

## การสร้างลำดับ P ในโค้ด

`find_P()` สร้างลิสต์กลับลำดับด้วย `numbers[::-1]` ก่อน
การ slice นี้สร้างลิสต์ใหม่ จึงยังไม่แก้ไข `numbers` ต้นฉบับ

จากนั้นพิจารณาสมาชิกจากขวาไปซ้าย โดยใช้ดัชนี `i` ของลิสต์ที่กลับแล้ว

-   ถ้า `i` เป็นจำนวนคู่ ใช้ `append()` เพิ่มสมาชิกต่อท้าย `positions`
-   ถ้า `i` เป็นจำนวนคี่ ใช้ `insert(0, ...)` เพิ่มสมาชิกไว้ด้านหน้า

ตัวอย่างการทำงานจริงของโค้ดเมื่อ `numbers` เป็น `[8, 3, 1, 6]`

```text
reversed_numbers = [6, 1, 3, 8]
i = 0: append(6)     -> [6]
i = 1: insert(0, 1)  -> [1, 6]
i = 2: append(3)     -> [1, 6, 3]
i = 3: insert(0, 8)  -> [8, 1, 6, 3]
```

ดังนั้น `find_P([8, 3, 1, 6])` ของโค้ดชุดนี้คืนค่า `[8, 1, 6, 3]`

---

## การสร้างลำดับ X

`rearrange()` เริ่มจาก `pos = 0` แล้วสะสมค่าจาก `positions` ทีละตัว

```python
pos += add_position
idx = pos % len(numbers)
```

ในข้อกำหนด ตำแหน่งที่ต้องหยิบคือ `1 +` ผลรวมสะสมของค่าใน `P`
แต่ `D*(k)` นับตำแหน่งจาก `1` ขณะที่ลิสต์ Python นับดัชนีจาก `0`
เมื่อลบ `1` เพื่อแปลงเป็นดัชนี จึงเหลือผลรวมสะสมพอดี

เครื่องหมาย `% len(numbers)` ทำให้เมื่อเดินเลยสมาชิกตัวสุดท้ายแล้ว
ดัชนีวนกลับมาที่ต้นลิสต์ ทุกครั้งที่เลือกสมาชิก โปรแกรมทำสองอย่าง

```python
rearranged_numbers.append(numbers[idx])
numbers.pop(idx)
```

ค่าที่เลือกถูกเพิ่มลงคำตอบ แล้วถูกลบออกจาก `numbers`
รอบถัดไปจึงคำนวณ modulo ด้วยจำนวนสมาชิกที่เหลือน้อยลง

> [!WARNING]
>
> `pop()` ทำให้ลิสต์ที่ส่งเข้า `rearrange()` ถูกแก้ไขโดยตรง
> เมื่อฟังก์ชันทำงานครบทุกสมาชิก ลิสต์ต้นฉบับที่ผู้เรียกส่งมาจะเหลือเป็นลิสต์ว่าง

---

## ความคลาดเคลื่อนระหว่างโจทย์กับโค้ด

PDF และโค้ดคำตอบมาตรฐานสลับกติกาการวางสมาชิกใน `find_P()` คนละทิศ
จึงให้ผลต่างกันในตัวอย่างที่มีสมาชิกหลายตัว

-   PDF ระบุว่า `find_P([8, 3, 1, 6])` ควรได้ `3 6 1 8`
-   โค้ดชุดนี้คืนค่า `8 1 6 3`
-   PDF ระบุว่า `rearrange([8, 3, 1, 6])` ควรได้ `6 8 3 1`
-   โค้ดชุดนี้คืนค่า `8 3 6 1`

README นี้อธิบายพฤติกรรมของโค้ดในส่วน Solution ตามที่มีอยู่จริง
และคงโค้ดไว้โดยไม่แก้ไข จึงไม่ควรใช้ผลตัวอย่างใน PDF เพื่อสรุปว่า
การสลับ `append()` กับ `insert(0, ...)` ในโค้ดนี้ให้ผลตรงกัน

---

## การรับคำสั่งจากเกรดเดอร์

บรรทัดสุดท้ายรับข้อความหนึ่งบรรทัดแล้วสั่งให้ Python ประมวลผลเป็นโค้ด

```python
exec(input().strip())
```

เกรดเดอร์จึงส่งคำสั่งอย่าง `print(*find_P([8,3,1,6]))`
หรือ `print(*rearrange([999]))` มาเรียกฟังก์ชันและแสดงผลได้โดยตรง

> [!WARNING]
>
> `exec()` สามารถสั่งทำงานโค้ด Python ใด ๆ ได้ บรรทัดนี้มีไว้เป็นส่วนเชื่อมต่อ
> กับข้อมูลที่เกรดเดอร์ควบคุมเท่านั้น ห้ามใช้ `exec(input())`
> กับข้อความจากผู้ใช้หรือแหล่งข้อมูลที่ไม่น่าเชื่อถือ

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_2_Q2_B1.py
# Problem   : List Rearrangement 2
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------


# Returns a new position list based on the input numbers
def find_P(numbers):
    # Initialize an empty list to store positions
    positions = []

    # Reverse the input numbers and rearrange them
    reversed_numbers = numbers[::-1]
    for i in range(len(reversed_numbers)):
        # If the index is even, append to the end
        if i % 2 == 0:
            positions.append(reversed_numbers[i])

        # If the index is odd, insert at the beginning
        else:
            positions.insert(0, reversed_numbers[i])

    # Return the rearranged positions
    return positions


# Rearranges the input list based on the positions calculated from find_P
def rearrange(numbers):
    # Initialize an empty list to hold the rearranged numbers
    rearranged_numbers = []
    # Get the positions from the find_P function
    positions = find_P(numbers)
    # Initialize the position counter
    pos = 0

    # Rearrange the numbers based on the positions
    for add_position in positions:
        # Calculate the new position and index in the original list
        pos += add_position
        idx = pos % len(numbers)

        # Append the number at the calculated index to the rearranged list
        rearranged_numbers.append(numbers[idx])
        # Remove the current number from the original list
        numbers.pop(idx)

    # Return the rearranged numbers
    return rearranged_numbers


# Execute the input string as code
exec(input().strip())
```
