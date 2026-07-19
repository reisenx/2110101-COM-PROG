<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Earthquake ★★ (
      <a href="https://drive.google.com/file/d/13OMN41ZzzXgnYZwzrfwgXP-PRR_fNqel/view?usp=sharing">
        <code>2567_2_Q3_A2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ภาพรวมของการเคลื่อนที่**](#ภาพรวมของการเคลื่อนที่)
-   [**คำนวณเวลาที่มองเห็นกัน**](#คำนวณเวลาที่มองเห็นกัน)
-   [**เลือกนาทีและระยะห่างที่แสดงผล**](#เลือกนาทีและระยะห่างที่แสดงผล)
-   [**ตัวอย่างการคำนวณ**](#ตัวอย่างการคำนวณ)
-   [**ข้อสังเกตเกี่ยวกับตัวอย่างในโจทย์**](#ข้อสังเกตเกี่ยวกับตัวอย่างในโจทย์)
-   [**Solution**](#solution)

---

## ภาพรวมของการเคลื่อนที่

ลูกเดินด้วยความเร็ว `2` เมตรต่อวินาที ส่วนพ่อเดินเร็วเป็นสองเท่าของลูก
จึงมีความเร็ว `4` เมตรต่อวินาที ทั้งสองคนเดินเข้าหากัน ระยะห่างจึงลดลงด้วย
ความเร็วรวม

$$v = 2 + 4 = 6 \text{ เมตรต่อวินาที}$$

ในโปรแกรมเก็บค่านี้เป็น `VELOCITY_PER_SEC = 6` และระยะที่ลดลงในหนึ่งนาทีคือ

$$6 \times 60 = 360 \text{ เมตร}$$

ตรงกับ `VELOCITY_PER_MIN = VELOCITY_PER_SEC * 60`

ทั้งสองคนมองเห็นกันเมื่ออยู่ห่างกันไม่เกิน `50` เมตร ถ้าระยะเริ่มต้น
`initial_distance <= 50` โปรแกรมจึงไม่ต้องจำลองการเดิน และแสดง
`0` กับค่า `initial_distance` คั่นด้วยช่องว่างทันที

---

## คำนวณเวลาที่มองเห็นกัน

สมมติให้ระยะเริ่มต้นเป็น $s$ เมตร ระยะที่ต้องลดลงก่อนมองเห็นกันคือ

$$D = \max(0, s - 50)$$

ซึ่งเขียนใน Python เป็น

```python
distance_to_run = max(0, initial_distance - VISIBLE_DISTANCE)
```

โปรแกรมพิจารณาเวลาเป็นจำนวนวินาทีเต็ม จึงใช้ `math.ceil()` ปัดขึ้นเพื่อหา
วินาทีแรกที่ระยะห่างเหลือไม่เกิน `50` เมตร

$$t = \left\lceil\frac{D}{6}\right\rceil$$

ตรงกับ `total_seconds = math.ceil(distance_to_run / VELOCITY_PER_SEC)`
จากนั้นหาว่าเหตุการณ์อยู่ในนาทีที่เท่าใดด้วย

$$m = \left\lceil\frac{t}{60}\right\rceil$$

หรือ `total_minutes = math.ceil(total_seconds / 60)` การปัดขึ้นมีความสำคัญ เช่น
ถ้าใช้เวลา `61` วินาที เหตุการณ์นั้นเกิดในนาทีที่ `2`

---

## เลือกนาทีและระยะห่างที่แสดงผล

โจทย์ให้แสดงระยะห่างเฉพาะห้านาทีแรก และต้องมีบรรทัดสุดท้ายบอกนาทีที่
มองเห็นกันเสมอ โปรแกรมจึงสร้าง `timestamps` ตามกติกานี้

-   ถ้ามองเห็นกันภายในนาทีที่ `1` ถึง `5` แสดงทุกนาทีตั้งแต่นาทีที่ `1`
    จนถึงนาทีสุดท้าย
-   ถ้าใช้เวลามากกว่า `5` นาที แสดงนาทีที่ `1` ถึง `5` แล้วข้ามไปแสดง
    นาทีสุดท้ายอีกหนึ่งบรรทัด

สำหรับนาทีก่อนนาทีสุดท้าย โปรแกรมคำนวณหลังผ่านไปครบ `time` นาที

$$\text{ระยะห่าง} = s - 360(\text{time})$$

ตรงกับ `initial_distance - (time * VELOCITY_PER_MIN)` แต่ในนาทีสุดท้าย
ต้องใช้เวลาจริง $t$ วินาที ไม่ใช่ปลายของนาทีนั้น จึงคำนวณด้วย
`initial_distance - (total_seconds * VELOCITY_PER_SEC)`

เพราะ $t$ ถูกปัดขึ้น ระยะห่างสุดท้ายอาจต่ำกว่า `50` เล็กน้อย แต่จะเป็น
วินาทีเต็มแรกที่มองเห็นกัน

---

## ตัวอย่างการคำนวณ

ถ้าระยะเริ่มต้นเป็น `2020` เมตร จะได้

```text
distance_to_run = 2020 - 50 = 1970
total_seconds = ceil(1970 / 6) = 329
total_minutes = ceil(329 / 60) = 6
```

เนื่องจากใช้เวลามากกว่าห้านาที โปรแกรมแสดงระยะหลังครบหนึ่งถึงห้านาทีก่อน
แล้วแสดงนาทีที่ `6` โดยใช้เวลาเดินจริง `329` วินาที

```text
1 1660
2 1300
3 940
4 580
5 220
6 46
```

อีกกรณีหนึ่ง ถ้าระยะเริ่มต้นเป็น `70` เมตร ต้องลดระยะลง `20` เมตร ใช้เวลา
`ceil(20 / 6) = 4` วินาที จึงมองเห็นกันในนาทีที่ `1` และเหลือระยะห่าง
`70 - 4 * 6 = 46` เมตร ผลลัพธ์คือ `1 46`

---

## ข้อสังเกตเกี่ยวกับตัวอย่างในโจทย์

> [!NOTE]
>
> คำอธิบายประกอบใน PDF มีตัวเลขพิมพ์ผิดอยู่สองตำแหน่ง แต่ตารางผลลัพธ์และ
> โปรแกรมเฉลยใช้ค่าที่คำนวณได้ถูกต้อง
>
> -   เมื่อเริ่มที่ `2020` เมตร หลัง `120` วินาทีต้องเหลือ
>     `2020 - 120 * 6 = 1300` เมตร ไม่ใช่ `1330` เมตร
> -   เมื่อเริ่มที่ `10000` เมตร หลัง `1659` วินาทีต้องเหลือ
>     `10000 - 1659 * 6 = 46` เมตร ไม่ใช่ `26` เมตร

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_2_Q3_A2.py
# Problem   : Earthquake
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------

import math

# Initialize constants
VELOCITY_PER_SEC = 6
VELOCITY_PER_MIN = VELOCITY_PER_SEC * 60

VISIBLE_DISTANCE = 50
DISPLAY_LIMIT = 5

# Input the initial distance between the two persons
initial_distance = int(input())

# Calculate the sum of distance for both to run to see each other
distance_to_run = max(0, initial_distance - VISIBLE_DISTANCE)

# Calculate the distance between them in each minute until they can see each other
if distance_to_run > 0:
    # Calculate the total time in seconds and minutes required to run
    total_seconds = math.ceil(distance_to_run / VELOCITY_PER_SEC)
    total_minutes = math.ceil(total_seconds / 60)

    # Initialize a list to store the timestamps to display
    timestamps = []
    # Add the minute 1 until the total minutes or DISPLAY_LIMIT
    for time in range(1, min(total_minutes, DISPLAY_LIMIT) + 1):
        timestamps.append(time)
    # Add the total minutes if it exceeds DISPLAY_LIMIT
    if total_minutes > DISPLAY_LIMIT:
        timestamps.append(total_minutes)

    # Calculate the distance between them at each timestamp
    for time in timestamps:
        # Before reaching the final minute, calculate the distance based on minutes
        if time < total_minutes:
            current_distance = initial_distance - (time * VELOCITY_PER_MIN)
        # At the final minute, calculate the distance based on seconds
        else:
            current_distance = initial_distance - (total_seconds * VELOCITY_PER_SEC)
        # Output the current timestamp and distance
        print(time, current_distance)

# No need to run if they can already see each other
else:
    print(0, initial_distance)
```
