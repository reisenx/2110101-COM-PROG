<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Reality Show ★★ (
      <a href="https://drive.google.com/file/d/1Kmkh6j223BnjUQg9vZjQBdBVK_uOZTnC/view?usp=sharing">
        <code>2567_3_Q3_B1</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การรวมเวลาของผู้เล่น**](#การรวมเวลาของผู้เล่น)
-   [**การเรียงอันดับ**](#การเรียงอันดับ)
-   [**การเลือกสามอันดับแรก**](#การเลือกสามอันดับแรก)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## การรวมเวลาของผู้เล่น

อินพุตหนึ่งบรรทัดสลับกันระหว่างชื่อผู้เล่นกับเวลาที่อยู่รอดในแต่ละ Episode
เช่น `Alice 10 Bob 5 Alice 7` หมายถึง Alice มีเวลา `10` และ `7` นาที
ส่วน Bob มีเวลา `5` นาที

โปรแกรมใช้ `split()` แยกข้อมูลทุกส่วน แล้วอ่านครั้งละ 2 ตำแหน่ง

```python
for i in range(0, len(data), 2):
    player = data[i]
    time = int(data[i + 1])
```

ชื่อคนเดิมอาจปรากฏหลายครั้ง จึงใช้ dictionary ชื่อ `survival_time`
เก็บผลรวมในรูปแบบ `ชื่อ: เวลารวม`

```python
if player not in survival_time:
    survival_time[player] = 0
survival_time[player] += time
```

การกำหนดค่าเริ่มต้นเป็น `0` เฉพาะตอนพบชื่อครั้งแรก ทำให้ครั้งต่อ ๆ ไป
สามารถบวกเวลาเพิ่มลงในยอดเดิมได้ทันที

---

## การเรียงอันดับ

โจทย์ต้องการเรียงตามกติกา 2 ข้อ

1. เวลารวมมากกว่าอยู่ก่อน
2. ถ้าเวลารวมเท่ากัน ให้ชื่อที่มาก่อนตามลำดับพจนานุกรม `A` ถึง `Z` อยู่ก่อน

Python เรียง list จากค่าน้อยไปมาก และเมื่อสมาชิกเป็น list ย่อย
จะเปรียบเทียบช่องแรกก่อน หากเท่ากันจึงเปรียบเทียบช่องถัดไป
โปรแกรมจึงสร้างข้อมูลเป็น `[-time, player]`

```python
sorted_survival_time.append([-time, player])
sorted_survival_time.sort()
```

การติดเครื่องหมายลบทำให้เวลามากกลายเป็นตัวเลขที่น้อยกว่า เช่น
เวลา `20` กลายเป็น `-20` และเวลา `15` กลายเป็น `-15`
เมื่อนำไปเรียงจากน้อยไปมาก ผู้ที่มีเวลา `20` จึงอยู่ก่อนผู้ที่มีเวลา `15`

ถ้าเวลารวมเท่ากัน ค่าในช่องแรกก็เท่ากัน Python จึงเปรียบเทียบชื่อในช่องที่สอง
และได้ลำดับตัวอักษรตามที่โจทย์กำหนด

---

## การเลือกสามอันดับแรก

ค่าคงที่ `DISPLAY_LIMIT = 3` ระบุจำนวนผู้เล่นสูงสุดที่ต้องแสดง
หลังเรียงแล้ว โปรแกรมเลือกเพียง 3 รายการแรกด้วย `[:DISPLAY_LIMIT]`

```python
for _, player in sorted_survival_time[:DISPLAY_LIMIT]:
    top_player_names.append(player)
```

ตัวแปร `_` รับค่าเวลาติดลบที่ไม่ต้องนำไปใช้ต่อ ส่วน `player` คือชื่อที่ต้องแสดง
ถ้ามีผู้เล่นน้อยกว่า 3 คน การ slice จะคืนเท่าที่มีโดยไม่เกิดข้อผิดพลาด

สุดท้าย `" ".join(top_player_names)` เชื่อมชื่อด้วยช่องว่างหนึ่งช่อง
โจทย์ต้องการเฉพาะชื่อ จึงไม่แสดงเวลารวมออกมา

---

## ตัวอย่างการทำงาน

สำหรับข้อมูล

```text
Alice 10 Bob 0 Charlie 10 Bob 5 Alice 5
```

จะรวมเวลาได้ดังนี้

| ผู้เล่น | เวลารวม |
|---|---:|
| Alice | `10 + 5 = 15` |
| Bob | `0 + 5 = 5` |
| Charlie | `10` |

เมื่อเรียงเวลาจากมากไปน้อย จึงได้ Alice, Charlie และ Bob ตามลำดับ

```text
Alice Charlie Bob
```

ถ้าทุกคนมีเวลารวมเท่ากัน เช่น Dan, Eva และ Fred คนละ `10` นาที
ผลลัพธ์จะเรียงชื่อเป็น `Dan Eva Fred`

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_3_Q3_B1.py
# Problem   : Reality Show
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------

# Constants for the number of top players to display
DISPLAY_LIMIT = 3

# Initialize a dictionary to store survival times of each player
survival_time = {}

# Input raw data
data = input().strip().split()

# Process the input data to calculate total survival time for each player
for i in range(0, len(data), 2):
    # Extract player name and time from the input data
    player = data[i]
    time = int(data[i + 1])

    # Update the survival time for the player
    if player not in survival_time:
        survival_time[player] = 0
    survival_time[player] += time

# Sort players by survival time in descending order and then by name in ascending order
sorted_survival_time = []
for player, time in survival_time.items():
    sorted_survival_time.append([-time, player])
sorted_survival_time.sort()

# Extract the top players based on survival time
top_player_names = []
for _, player in sorted_survival_time[:DISPLAY_LIMIT]:
    top_player_names.append(player)

# Output the names of the top players
print(" ".join(top_player_names))
```
