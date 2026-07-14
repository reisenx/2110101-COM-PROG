<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Location Analysis ★★ (
      <a href="https://drive.google.com/file/d/1q6ZCJdDag9yIrOAhdH0dGYcXHTZxTHKG/view?usp=drive_link">
        <code>10_TSD_26</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**มองข้อมูลเป็นสองทิศทาง**](#มองข้อมูลเป็นสองทิศทาง)
-   [**การสร้างพจนานุกรม**](#การสร้างพจนานุกรม)
-   [**การค้นหา ID ที่เกี่ยวข้อง**](#การค้นหา-id-ที่เกี่ยวข้อง)
-   [**ลำดับการแสดงผล**](#ลำดับการแสดงผล)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ชื่อตัวแปรในโค้ด**](#ชื่อตัวแปรในโค้ด)
-   [**กรณีพิเศษ**](#กรณีพิเศษ)
-   [**Solution**](#solution)

---

## มองข้อมูลเป็นสองทิศทาง

ข้อมูลแต่ละบรรทัดอยู่ในรูป `ID: เมืองที่ 1, เมืองที่ 2, ...` เช่น

```text
38216542: Z, B, D, J
```

หมายความว่า ID `38216542` เคยไปเมือง `Z`, `B`, `D` และ `J` โจทย์ให้รับ
`keyID` แล้วหา ID อื่นทุก ID ที่มีเมืองร่วมกับ `keyID` อย่างน้อยหนึ่งเมือง

การค้นหานี้ต้องมองข้อมูลได้สองทิศทาง

1. จาก ID ไปหาเซตของเมืองที่ ID นั้นเคยไป
2. จากเมืองไปหาเซตของ ID ที่เคยไปเมืองนั้น

ถ้ามีเพียงทิศทางแรก เราจะต้องไล่ตรวจทุก ID ทีละคน แต่เมื่อสร้างทิศทางที่สองไว้
เราสามารถเปิดดูแต่ละเมืองของ `keyID` แล้วรวม ID ที่เกี่ยวข้องได้ทันที

## การสร้างพจนานุกรม

โปรแกรมแยกบรรทัดด้วย `split(": ")` เพื่อแยก ID ออกจากรายชื่อเมือง
แล้วใช้ `split(", ")` แยกเมืองแต่ละเมือง

ในความหมายของโจทย์ โครงสร้างข้อมูลที่สร้างขึ้นคือ

```text
ID -> set ของเมือง
เมือง -> set ของ ID
```

การใช้ `set` มีประโยชน์สองอย่าง คือค้นหาสมาชิกได้โดยตรง และป้องกันข้อมูลซ้ำ
เช่น ถ้า ID สองคนมีเมืองร่วมกันมากกว่าหนึ่งเมือง ผลลัพธ์สุดท้ายก็ยังเก็บ ID
แต่ละคนเพียงครั้งเดียว

โค้ดสร้างพจนานุกรมทิศทางแรกจากข้อมูลแต่ละบรรทัด แล้วเติมพจนานุกรมกลับทิศทาง
ทีละเมืองด้วยแนวคิดต่อไปนี้

```python
for user in users_list:
    if user not in users_to_locations:
        users_to_locations[user] = set()
    users_to_locations[user].add(location)
```

ชื่อในโค้ดอาจทำให้สับสน จึงควรอ่าน `user` ในช่วงนี้ว่า “เมืองหนึ่งเมือง” และ
`location` ว่า “ID หนึ่ง ID” รายละเอียดของชื่อทั้งหมดอธิบายไว้ในหัวข้อ
[ชื่อตัวแปรในโค้ด](#ชื่อตัวแปรในโค้ด)

## การค้นหา ID ที่เกี่ยวข้อง

ให้ $C(k)$ เป็นเซตเมืองของ `keyID` ชื่อ $k$ และให้ $I(c)$ เป็นเซต ID
ที่เคยไปเมือง $c$ เซตคำตอบคือ

$$
\left(\bigcup_{c \in C(k)} I(c)\right) - \{k\}
$$

ความหมายคือ รวม ID ของทุกเมืองที่ `keyID` เคยไป แล้วนำ `keyID` ออกจากคำตอบ
เพราะโจทย์ต้องการ ID อื่น โค้ดใช้ union แบบปรับค่าเดิมด้วยตัวดำเนินการ `|=`

```python
visited_locations = set()
for user in locations_to_users[analysis_location]:
    visited_locations |= users_to_locations[user]

visited_locations -= {analysis_location}
```

ในที่นี้ `locations_to_users[analysis_location]` คือเซตเมืองของ `keyID`
ส่วน `users_to_locations[user]` คือเซต ID ที่เคยไปเมืองนั้น การลบด้วย
`-= {analysis_location}` ตรงกับการลบเซต \(\{k\}\) ในสูตร

## ลำดับการแสดงผล

โจทย์ไม่ได้ให้เรียง ID ตามตัวเลขหรือข้อความ แต่ให้คงลำดับเดียวกับที่รับข้อมูล
โปรแกรมจึงเก็บ ID ทุกตัวไว้ใน list `location_order` ตั้งแต่ตอนอ่านข้อมูล

เมื่อได้เซตคำตอบแล้ว โปรแกรมวน `location_order` และพิมพ์เฉพาะสมาชิกที่อยู่ใน
`visited_locations`

```python
for location in location_order:
    if location in visited_locations:
        print(location)
```

วิธีนี้ใช้ `set` เพื่อค้นหาอย่างสะดวก แต่ใช้ `list` เพื่อรักษาลำดับการแสดงผล
จึงไม่ควรพิมพ์สมาชิกของเซตโดยตรง เพราะลำดับของเซตไม่ใช่ลำดับข้อมูลนำเข้า

## ตัวอย่างการทำงาน

จากข้อมูลตัวอย่าง ID `4126548` เคยไปเมือง `J` และ `Z3`

-   เมือง `J` มี ID `38216542` และ `4126548`
-   เมือง `Z3` มีเพียง ID `4126548`

เมื่อ union ทั้งสองเซตแล้วลบ `4126548` ออก จึงเหลือ `38216542` และแสดง

```text
38216542
```

สำหรับ `keyID` เป็น `423212822` เมือง `D` เชื่อมกับ ID สามตัวแรกในข้อมูล
โปรแกรมจึงพิมพ์ `51234621`, `427613829` และ `38216542` ตามลำดับที่รับเข้ามา
แม้จะพบ ID เหล่านี้ผ่านเซตซึ่งไม่มีลำดับก็ตาม

## ชื่อตัวแปรในโค้ด

> [!WARNING]
>
> ชื่อตัวแปรและ comment ในไฟล์คำตอบสลับความหมายของ “ID” กับ “เมือง”
> คำอธิบายใน README นี้ยึดรูปแบบข้อมูลจากโจทย์ แต่บล็อก Solution ต้องคงโค้ด
> ต้นฉบับไว้ตามเดิม

ตารางต่อไปนี้ช่วยแปลชื่อในโค้ดให้ตรงกับความหมายจริง

| ชื่อในโค้ด | ความหมายตามข้อมูลโจทย์ |
|---|---|
| `location` | ID ที่อยู่หน้าสัญลักษณ์ `:` |
| `users_list` และตัวแปร `user` | รายชื่อเมือง และเมืองหนึ่งเมือง |
| `locations_to_users` | พจนานุกรม `ID -> set ของเมือง` |
| `users_to_locations` | พจนานุกรม `เมือง -> set ของ ID` |
| `location_order` | ลำดับ ID ที่รับเข้ามา |
| `analysis_location` | `keyID` ที่ต้องการค้นหา |
| `visited_locations` | เซต ID ที่มีเมืองร่วมกับ `keyID` |

แม้ชื่อจะสลับกัน แต่ทิศทางของข้อมูลและผลลัพธ์ที่โค้ดคำนวณยังตรงกับโจทย์

## กรณีพิเศษ

-   ถ้า ID เดียวกันพบร่วมกับ `keyID` หลายเมือง `set` จะทำให้พิมพ์เพียงครั้งเดียว
-   `keyID` ถูกลบออกจากคำตอบเสมอ แม้จะอยู่ในทุกเซตที่นำมา union
-   ถ้าไม่มี ID อื่นเหลืออยู่ โปรแกรมพิมพ์ `Not Found`
-   โค้ดเก็บ ID เป็น string จึงไม่ทำเลขศูนย์ด้านหน้าหาย และไม่เรียง ID
    แบบตัวเลข
-   ข้อมูลที่ถูกต้องต้องมี `keyID` อยู่ในพจนานุกรม เพราะโปรแกรมเข้าถึง
    `locations_to_users[analysis_location]` โดยตรง

---

# Solution

```python
# --------------------------------------------------
# File Name : 10_TSD_26.py
# Problem   : Location Analysis
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Initialize a dictionary to store locations and their users.
locations_to_users = {}
users_to_locations = {}
location_order = []

# Input number of locations
n = int(input())

# Read each location and its users
for _ in range(n):
    line = input().strip().split(": ")
    location = line[0]
    users_list = line[1].split(", ")

    # Update locations set
    location_order.append(location)

    # Store the location and its users in the dictionary
    locations_to_users[location] = set(users_list)

    # Update the users dictionary
    for user in users_list:
        if user not in users_to_locations:
            users_to_locations[user] = set()
        users_to_locations[user].add(location)

# Input analysis location
analysis_location = input().strip()

# Find all locations visited by users of the analysis location
visited_locations = set()
for user in locations_to_users[analysis_location]:
    visited_locations |= users_to_locations[user]

# Exclude the analysis location itself
visited_locations -= {analysis_location}

# Output the result
if len(visited_locations) > 0:
    for location in location_order:
        if location in visited_locations:
            print(location)
else:
    print("Not Found")
```
