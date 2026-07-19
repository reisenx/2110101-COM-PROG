<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    List Rearrangement ★★ (
      <a href="https://drive.google.com/file/d/1Rx2OWmHmJHDPIgUdRF2nwEdlr3RrBEnL/view?usp=sharing">
        <code>2567_1_Q2_B1</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ลำดับที่ใช้ในโจทย์**](#ลำดับที่ใช้ในโจทย์)
-   [**การแปลงตำแหน่งเป็น index**](#การแปลงตำแหน่งเป็น-index)
-   [**ลำดับการจัดเรียงใหม่**](#ลำดับการจัดเรียงใหม่)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## ลำดับที่ใช้ในโจทย์

อินพุตคือจำนวนเต็มไม่ติดลบในลำดับ $D$ เก็บในลิสต์ `numbers`
โปรแกรมสร้างอีกลำดับหนึ่งชื่อ `sorted_numbers` โดยเรียงสมาชิกของ $D$
จากน้อยไปมาก ลำดับนี้ตรงกับ $P=(p_1,p_2,\ldots,p_n)$ ในโจทย์

`sorted()` สร้างลิสต์ใหม่ ดังนั้นแม้ภายหลังจะลบสมาชิกออกจาก `numbers`
ค่าและลำดับของ `sorted_numbers` ก็ยังคงเดิม สมาชิกที่มีค่าเท่ากันยังถือเป็น
คนละตัวและถูกใช้คนละรอบ

การทำให้สมาชิกตัวหนึ่งเป็น “ตัวต้องห้าม” ทำได้โดย `pop()` สมาชิกนั้นออกจาก
`numbers` ลิสต์ที่เหลือจึงมีเฉพาะสมาชิกที่ยังเลือกได้และยังรักษาลำดับเดิมไว้

---

## การแปลงตำแหน่งเป็น index

ในรอบที่ $i$ โจทย์ต้องการสมาชิกตำแหน่ง

$$
D^*\left(1+\sum_{j=1}^{i}p_j\right)
$$

แต่ $D^*(k)$ นับตำแหน่งจาก `1` ขณะที่ index ของลิสต์ Python เริ่มจาก `0`
ถ้าขณะนั้นเหลือสมาชิก $m$ ตัว index ที่ต้องใช้จึงเป็น

$$
\left(1+\sum p_j-1\right) \bmod m
= \left(\sum p_j\right) \bmod m
$$

โปรแกรมเก็บผลรวม $\sum p_j$ ใน `position` ด้วย `position += add_position`
แล้วคำนวณ

```python
idx = position % len(numbers)
```

การหารเอาเศษทำหน้าที่วนกลับไปต้นลิสต์เมื่อเดินเลยสมาชิกขวาสุด
และ `len(numbers)` จะลดลงทุกครั้งหลังเลือกสมาชิก

---

## ลำดับการจัดเรียงใหม่

สำหรับ `add_position` แต่ละค่าใน `sorted_numbers` โปรแกรมทำตามขั้นตอนนี้

1. เพิ่มค่านั้นเข้า `position` เพื่อให้ได้ผลรวมสะสมของ $P$
2. หา `idx` ในลิสต์สมาชิกที่ยังไม่ถูกห้าม
3. เก็บ `numbers[idx]` เป็นสมาชิกถัดไปของคำตอบ
4. ลบสมาชิกที่เลือกด้วย `numbers.pop(idx)` เพื่อไม่ให้เลือกซ้ำ

ค่าที่เลือกถูกแปลงเป็นข้อความก่อนเก็บใน `rearranged_numbers`
เมื่อทำครบทุกตัวจึงต่อด้วยช่องว่างผ่าน `" ".join(...)`

---

## ตัวอย่างการทำงาน

เมื่อ $D$ คือ `8 3 1 6` จะได้ $P$ คือ `1 3 6 8`

| รอบ | ค่าใน $P$ | `position` | สมาชิกที่ยังเหลือ | `idx` | ค่าที่เลือก |
|---:|---:|---:|:---|---:|---:|
| 1 | 1 | 1 | `[8, 3, 1, 6]` | `1 % 4 = 1` | 3 |
| 2 | 3 | 4 | `[8, 1, 6]` | `4 % 3 = 1` | 1 |
| 3 | 6 | 10 | `[8, 6]` | `10 % 2 = 0` | 8 |
| 4 | 8 | 18 | `[6]` | `18 % 1 = 0` | 6 |

จึงแสดงผล `3 1 8 6` ในบรรทัดเดียว รอบสุดท้ายมีสมาชิกเพียงตัวเดียว
การหารเอาเศษด้วย `1` จึงได้ index `0` เสมอ และลบสมาชิกได้อย่างปลอดภัย

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q2_B1.py
# Problem   : List Rearrangement
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Input a list of numbers
numbers = [int(num) for num in input().split()]

# Create another sequence of sorted numbers
sorted_numbers = sorted(numbers)

# Initialize an empty list to hold the rearranged numbers
rearranged_numbers = []
# Initialize the position counter
position = 0

# Rearrange the numbers based on the sorted sequence
for add_position in sorted_numbers:
    # Calculate the new position in the original list
    position += add_position
    # Get the index in the original list
    idx = position % len(numbers)

    # Append the number at the calculated index to the rearranged list
    rearranged_numbers.append(str(numbers[idx]))
    # Remove the number from the original list
    numbers.pop(idx)

# Output the rearranged numbers
print(" ".join(rearranged_numbers))
```
