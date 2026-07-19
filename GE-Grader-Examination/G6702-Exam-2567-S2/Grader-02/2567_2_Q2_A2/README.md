<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Lyla ★★ (
      <a href="https://drive.google.com/file/d/1GhTOX-xn20MxpVoo8Q9_AnJzXfbU0CWA/view?usp=sharing">
        <code>2567_2_Q2_A2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แบบจำลองการเคลื่อนที่**](#แบบจำลองการเคลื่อนที่)
-   [**เก็บข้อมูลของผู้ล่าและผู้ถูกล่า**](#เก็บข้อมูลของผู้ล่าและผู้ถูกล่า)
-   [**ตรวจว่าไล่ทันหรือไม่**](#ตรวจว่าไล่ทันหรือไม่)
-   [**จำลองทีละหน่วยเวลา**](#จำลองทีละหน่วยเวลา)
-   [**การแสดงผล**](#การแสดงผล)
-   [**Solution**](#solution)

---

## แบบจำลองการเคลื่อนที่

ตอนเริ่มต้นผู้ล่าอยู่ที่ตำแหน่ง `0` ผู้ถูกล่าอยู่ข้างหน้าที่ตำแหน่ง `s`
และทั้งคู่มีความเร็วเริ่มต้นเป็น `0` โจทย์กำหนดให้คำนวณทีละหนึ่งหน่วยเวลา
ด้วยสมการ

$$
v_{\mathrm{new}} = v_{\mathrm{old}} + a
$$

และ

$$
p_{\mathrm{new}}
= p_{\mathrm{old}} + v_{\mathrm{old}}
+ \frac{1}{2}\left(v_{\mathrm{new}}-v_{\mathrm{old}}\right)
= p_{\mathrm{old}} + v_{\mathrm{old}} + \frac{1}{2}a
$$

เพราะ `v_new - v_old` เท่ากับความเร่ง `a` ตำแหน่งจึงอัปเดตใน Python ได้เป็น

```python
position += velocity + (0.5 * acceleration)
velocity += acceleration
```

ต้องอัปเดตตำแหน่งก่อนความเร็ว เพื่อให้พจน์แรกใช้ `v_old` ตามสมการของโจทย์

---

## เก็บข้อมูลของผู้ล่าและผู้ถูกล่า

โปรแกรมใช้ลิสต์สองช่อง โดยกำหนดความหมายของดัชนีให้เหมือนกันทุกตัวแปร

-   ดัชนี `0` เก็บข้อมูลของผู้ล่า
-   ดัชนี `1` เก็บข้อมูลของผู้ถูกล่า

ข้อมูลนำเข้าคือ `a1 a2 s` ซึ่งล้วนเป็นจำนวนจริงบวก

```python
acceleration = [data[0], data[1]]
displacement[1] = data[2]
```

ดังนั้น `acceleration[0]` คือ `a1`, `acceleration[1]` คือ `a2`
และตำแหน่งเริ่มต้นของผู้ถูกล่าคือ `s`

---

## ตรวจว่าไล่ทันหรือไม่

ทั้งคู่เริ่มจากหยุดนิ่งและเร่งคงที่ ถ้า `a1 <= a2`
ระยะห่างจะไม่ลดลงจนผู้ล่าตามทัน โปรแกรมจึงแสดง

```text
Not possible
```

เฉพาะเมื่อ `a1 > a2` เท่านั้นที่โปรแกรมเริ่มจำลองการไล่ล่า
กรณีความเร่งเท่ากันก็อยู่ในกิ่ง `Not possible` ด้วย

---

## จำลองทีละหน่วยเวลา

ลูปทำงานขณะที่ตำแหน่งผู้ถูกล่ายังมากกว่าตำแหน่งผู้ล่า

1. เพิ่ม `time` ขึ้น `1`
2. อัปเดตตำแหน่งของทั้งคู่ด้วยความเร็วเดิมและความเร่งของตนเอง
3. อัปเดตความเร็วของทั้งคู่
4. กลับไปตรวจตำแหน่งอีกครั้ง

ถ้าผู้ล่าไปอยู่ตำแหน่งเดียวกันหรือเลยผู้ถูกล่าแล้ว
เงื่อนไข `displacement[1] > displacement[0]` จะเป็นเท็จและลูปจบ
ระยะทางที่รายงานจึงเป็นระยะของปลายหน่วยเวลาที่ตามทันหรือแซงแล้ว

ตัวอย่าง `2 1 5` จะได้ตำแหน่งผู้ล่าเป็น `1`, `4`, `9`, `16`
หลังเวลา `1`, `2`, `3`, `4` ตามลำดับ ส่วนผู้ถูกล่าอยู่ที่ `5.5`, `7`,
`9.5`, `13` ผู้ล่าจึงตามทันเมื่อเวลา `4`

---

## การแสดงผล

เมื่อไล่ทัน โปรแกรมแสดงเวลาและตำแหน่งของผู้ล่า โดยคั่นด้วยช่องว่าง

```python
print(time, round(displacement[0], 2))
```

`round(..., 2)` ปัดค่าเป็นทศนิยมไม่เกิน 2 ตำแหน่ง แต่ไม่ได้บังคับให้มีเลข
หลังจุดครบ 2 หลัก เพราะค่าที่ยังส่งให้ `print()` เป็นตัวเลข เช่น `16.0`
จะแสดงเป็น `16.0` ไม่ใช่ `16.00`

> [!NOTE]
>
> การจำลองใช้เฉพาะเวลาจำนวนเต็ม หากตำแหน่งของทั้งคู่ตัดกันระหว่างสองช่วงเวลา
> โปรแกรมจะรายงานปลายหน่วยเวลาถัดไปตามวิธีคำนวณที่โจทย์กำหนด

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_2_Q2_A2.py
# Problem   : Lyla
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Initializing time, displacement, and velocity variables
time = 0
displacement = [0.0, 0.0]
velocity = [0.0, 0.0]

# Input acceleration and displacement
data = [float(e) for e in input().split()]
acceleration = [data[0], data[1]]
displacement[1] = data[2]

# Check if the acceleration of the hunter is more than the acceleration of the prey
if acceleration[0] > acceleration[1]:
    # Loop until the hunter catches the prey
    while displacement[1] > displacement[0]:
        # Increment time
        time += 1

        # Update displacement
        displacement[0] += velocity[0] + (0.5 * acceleration[0])
        displacement[1] += velocity[1] + (0.5 * acceleration[1])

        # Update velocity
        velocity[0] += acceleration[0]
        velocity[1] += acceleration[1]

    # Output the time and displacement of the hunter when he catches the prey
    print(time, round(displacement[0], 2))

# If the acceleration of the hunter is not greater than the prey's,
# it's not possible to catch the prey
else:
    print("Not possible")
```
