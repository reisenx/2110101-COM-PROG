<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Downsampling ★★ (
      <a href="https://drive.google.com/file/d/1cXqiNjkYF3NR1C04DxC9gApQuYIOjy5I/view?usp=sharing">
        <code>2567_1_Q3_B1-S</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การแบ่งข้อมูลเป็นช่วง**](#การแบ่งข้อมูลเป็นช่วง)
-   [**เวลาของข้อมูลหลังลดตัวอย่าง**](#เวลาของข้อมูลหลังลดตัวอย่าง)
-   [**การเลือกค่าสูงสุดหรือค่าเฉลี่ย**](#การเลือกค่าสูงสุดหรือค่าเฉลี่ย)
-   [**ข้อแตกต่างระหว่างโจทย์กับโค้ด**](#ข้อแตกต่างระหว่างโจทย์กับโค้ด)
-   [**Solution**](#solution)

---

## การแบ่งข้อมูลเป็นช่วง

การทำ downsampling คือการย่อข้อมูลหลายตัวที่อยู่ติดกันให้เหลือหนึ่งตัว
โจทย์ให้ขนาดช่วงเป็น `k` โค้ดจึงเดินตำแหน่งเริ่มต้นทีละ `k`

```python
for idx in range(0, len(numbers), k):
    chunk = numbers[idx : idx + k]
```

ใน Solution จริงไม่ได้สร้างตัวแปร `chunk` แต่ใช้ slice
`numbers[idx : idx + k]` โดยตรง หลักการเหมือนกัน

ถ้าจำนวนข้อมูลหารด้วย `k` ไม่ลงตัว slice สุดท้ายจะสั้นกว่า `k` ได้โดยไม่เกิด
ข้อผิดพลาด เช่นข้อมูล `7` ตัวและ `k = 3` จะแบ่งเป็นขนาด `3`, `3`, `1`
และตัวสุดท้ายยังต้องนำมาคำนวณ

ตัวแปร `n` รับจำนวนข้อมูลตามโจทย์ แต่ลูปใช้ `len(numbers)` จริง
จึงอาศัยเงื่อนไขว่าอินพุตบรรทัดที่สองมีข้อมูลครบ `n` ตัว

---

## เวลาของข้อมูลหลังลดตัวอย่าง

แต่ละผลลัพธ์ใช้เวลาของข้อมูลตัวแรกในช่วงนั้น
เมื่อ `idx` คือระยะจากข้อมูลตัวแรก เวลาจึงเป็น

$$
\text{current time} = S + \text{idx}
$$

ซึ่งตรงกับ Python ว่า

```python
current_time = initial_time + idx
```

ตัวอย่าง `S = 10` และ `k = 3` จะได้เวลา `10`, `13`, `16`, ...
ตามตัวอย่างผลลัพธ์ใน PDF

---

## การเลือกค่าสูงสุดหรือค่าเฉลี่ย

โปรแกรมคำนวณทั้งสองค่าในทุกช่วงก่อนเลือกแสดงตาม `cmd`

$$
\text{mean} = \frac{\text{ผลรวมของข้อมูลในช่วง}}{\text{จำนวนข้อมูลในช่วง}}
$$

```python
max_value = max(numbers[idx : idx + k])
mean_value = sum(numbers[idx : idx + k]) / len(numbers[idx : idx + k])
```

-   ถ้า `cmd == "max"` แสดงค่าสูงสุด
-   ถ้า `cmd == "mean"` แสดงค่าเฉลี่ยที่ผ่าน `round(mean_value, 2)`

ผลลัพธ์แต่ละบรรทัดเรียงเป็นเวลา เว้นวรรค แล้วตามด้วยค่าที่สรุปได้

---

## ข้อแตกต่างระหว่างโจทย์กับโค้ด

> [!WARNING]
>
> PDF สั่งให้ใช้ `round(x, 2)` กับข้อมูลผลลัพธ์ แต่โค้ดต้นฉบับปัดเฉพาะกรณี
> `mean` ส่วนกรณี `max` แสดง `max_value` โดยตรง ถ้าค่าสูงสุดเป็น `1.234`
> โค้ดจะแสดง `1.234` ไม่ใช่ `1.23`

ข้อความอธิบายช่วงเวลาใน PDF มีส่วนที่ดูเหมือนเขียนปลายช่วงเป็น `S - N - 1`
แต่ตัวอย่างและโค้ดเพิ่มเวลาไปข้างหน้าด้วย `S + idx`
คำอธิบายนี้จึงยึดลำดับเวลาที่ตัวอย่างและโปรแกรมใช้จริง

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q3_B1-S.py
# Problem   : Downsampling
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Input amount of numbers and initial time
n, initial_time = [int(num) for num in input().split()]

# Input numbers list
numbers = [float(num) for num in input().split()]

# Input k and command
data = input().strip().split()
k = int(data[0])
cmd = data[1].strip()

# Separate the numbers into chunks of size k and process them
for idx in range(0, len(numbers), k):
    # Calculate the current time of the current chunk
    current_time = initial_time + idx

    # Calculate the max and mean values for the current chunk
    max_value = max(numbers[idx : idx + k])
    mean_value = sum(numbers[idx : idx + k]) / len(numbers[idx : idx + k])

    # Output the result based on the command
    if cmd == "max":
        print(f"{current_time} {max_value}")
    elif cmd == "mean":
        print(f"{current_time} {round(mean_value, 2)}")
```
