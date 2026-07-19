<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Temperature Change ★★ (
      <a href="https://drive.google.com/file/d/1j7D-tr5qBp5H0i1LItXGmxd--MQF71QW/view?usp=sharing">
        <code>2567_2_Q1_A2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**กฎการเย็นตัวของนิวตัน**](#กฎการเย็นตัวของนิวตัน)
-   [**การเลือกค่าคงที่**](#การเลือกค่าคงที่)
-   [**การจำลองอุณหภูมิทีละช่วงเวลา**](#การจำลองอุณหภูมิทีละช่วงเวลา)
-   [**เงื่อนไขหยุดและการแสดงผล**](#เงื่อนไขหยุดและการแสดงผล)
-   [**Solution**](#solution)

---

## กฎการเย็นตัวของนิวตัน

โจทย์ให้ประมาณอุณหภูมิของวัตถุทุก ๆ ช่วงเวลา $\Delta t$ นาที ด้วยกฎการเย็นตัว
ของนิวตัน ถ้าอุณหภูมิก่อนหน้าเป็น $T_{\text{old}}$ อุณหภูมิห้องเป็น
$T_{\text{room}}$ และค่าคงที่เป็น $k$ จะได้

$$
T_{\text{new}}
= T_{\text{old}} - k(T_{\text{old}} - T_{\text{room}})\Delta t
$$

ใน Python สูตรนี้ตรงกับ

```python
temp_new = temp_old - k * (temp_old - temp_room) * time_interval
```

-   ถ้า `temp_old > temp_room` ผลต่างในวงเล็บเป็นบวก โปรแกรมจึงลดอุณหภูมิ
    ของวัตถุลง
-   ถ้า `temp_old < temp_room` ผลต่างเป็นลบ การลบจำนวนลบทำให้อุณหภูมิของ
    วัตถุสูงขึ้น
-   ถ้าอุณหภูมิทั้งสองเท่ากัน อุณหภูมิใหม่จะเท่ากับค่าเดิม

ดังนั้นสูตรเดียวกันใช้ได้ทั้งกรณีวัตถุเย็นลงและอุ่นขึ้น โดยอุณหภูมิจะค่อย ๆ
เข้าใกล้อุณหภูมิห้องตามข้อมูลทดสอบของโจทย์

---

## การเลือกค่าคงที่

โจทย์กำหนด $k = k_1k_2$ หรือใน Python คือ
`k = K1[material_type - 1] * K2[wind_type - 1]` ค่า $k_1$ ขึ้นกับวัสดุ
และ $k_2$ ขึ้นกับความเร็วลม

| ตัวเลือกวัสดุ | วัสดุ | $k_1$ |
| ---: | --- | ---: |
| `1` | เหล็ก | `0.05` |
| `2` | น้ำ | `0.02` |
| `3` | พลาสติก | `0.01` |
| `4` | อื่น ๆ | `0.015` |

| ตัวเลือกแรงลม | ความเร็วลม | $k_2$ |
| ---: | --- | ---: |
| `1` | มากกว่า `5 m/s` | `1.5` |
| `2` | ตั้งแต่ `1–5 m/s` | `1.0` |
| `3` | น้อยกว่า `1 m/s` | `0.8` |

รายการใน Python เริ่มนับตำแหน่งจาก `0` แต่ค่าตัวเลือกของโจทย์เริ่มจาก `1`
จึงต้องลบ `1` ก่อนนำไปเป็นดัชนี เช่น `material_type = 1` จะเลือก
`K1[0]` ซึ่งมีค่า `0.05`

---

## การจำลองอุณหภูมิทีละช่วงเวลา

โปรแกรมรับข้อมูลทั้งหมด `5` บรรทัดตามลำดับ ได้แก่ อุณหภูมิเริ่มต้น
อุณหภูมิห้อง ช่วงเวลา ชนิดวัสดุ และประเภทความเร็วลม จากนั้นคำนวณอุณหภูมิ
หลังผ่านช่วงเวลาแรกไว้ทันที

```python
total_time = time_interval
temp_new = temp_old - k * (temp_old - temp_room) * time_interval
```

ถ้าอุณหภูมิยังเปลี่ยนตั้งแต่ `0.001` องศาขึ้นไป ลูปจะเพิ่มเวลาทีละ
`time_interval` เลื่อน `temp_new` ของรอบก่อนให้เป็น `temp_old` แล้วคำนวณ
อุณหภูมิของรอบถัดไป การอัปเดตลำดับนี้สำคัญ เพราะแต่ละรอบต้องเริ่มจาก
อุณหภูมิล่าสุด ไม่ใช่อุณหภูมิเริ่มต้นเดิม

ตัวอย่างแรกในโจทย์มี `temp_old = 25.042`, `temp_room = 25`,
`time_interval = 0.5` และ $k = 0.05$ หลังช่วงแรกได้

$$
T_{\text{new}} = 25.042 - 0.05(25.042 - 25)(0.5) = 25.04095
$$

อุณหภูมิเปลี่ยนไป `0.00105` องศา ซึ่งยังไม่น้อยกว่า `0.001` โปรแกรมจึง
จำลองช่วงเวลาถัดไป จนรอบที่สามมีการเปลี่ยนแปลงน้อยกว่าเกณฑ์และได้เวลารวม
`1.5` นาที

---

## เงื่อนไขหยุดและการแสดงผล

เงื่อนไขของลูปคือ

```python
abs(temp_old - temp_new) >= 10**-3
```

`abs()` ทำให้ตรวจขนาดของการเปลี่ยนแปลงโดยไม่สนใจเครื่องหมาย จึงใช้ได้ทั้ง
ตอนอุณหภูมิลดลงและเพิ่มขึ้น ส่วน `10**-3` มีค่าเท่ากับ $10^{-3} = 0.001$
ลูปจะหยุดเมื่ออุณหภูมิเปลี่ยนไป **น้อยกว่า** `0.001` องศา

> [!NOTE]
>
> โปรแกรมคำนวณรอบแรกก่อนตรวจเงื่อนไขเสมอ ถ้าอุณหภูมิเริ่มต้นเท่ากับ
> อุณหภูมิห้อง จะรายงานเวลาหลังผ่านไปหนึ่งช่วง เช่น `0.5` นาที ไม่ใช่ `0`

ผลลัพธ์พิมพ์เวลารวมก่อน แล้วตามด้วยอุณหภูมิสุดท้าย โดยใช้
`round(total_time, 2)` และ `round(temp_new, 3)` ตามลำดับ การใช้ `round()`
กับตัวเลขไม่ได้บังคับให้แสดงเลขศูนย์ท้ายครบทุกตำแหน่ง จึงอาจเห็น `25.0`
แทน `25.000` ได้

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_2_Q1_A2.py
# Problem   : Temperature Change
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Initialization of constants
K1 = [0.05, 0.02, 0.01, 0.015]
K2 = [1.5, 1.0, 0.8]

# Input temperatures information
temp_old = float(input())
temp_room = float(input())

# Input time interval
time_interval = float(input())

# Input material and wind type
material_type = int(input())
wind_type = int(input())

# Calculate k constant by material and wind type
k = K1[material_type - 1] * K2[wind_type - 1]

# Initialize total time and new temperature
total_time = time_interval
temp_new = temp_old - k * (temp_old - temp_room) * time_interval

# Calculate the time until the temperature difference is less than 0.001
while abs(temp_old - temp_new) >= 10**-3:
    # Update total time
    total_time += time_interval

    # Update temperatures
    temp_old = temp_new
    temp_new = temp_old - k * (temp_old - temp_room) * time_interval

# Output the total time and the final temperature
print(round(total_time, 2), round(temp_new, 3))
```
