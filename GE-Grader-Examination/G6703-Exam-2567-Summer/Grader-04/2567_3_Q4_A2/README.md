<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Computer Price ★★ (
      <a href="https://drive.google.com/file/d/121_T1Fzngp5EhFhW_bUQCUaqqSB2bIyb/view?usp=sharing">
        <code>2567_3_Q4_A2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเก็บราคาส่วนประกอบ**](#การเก็บราคาส่วนประกอบ)
-   [**การคำนวณมูลค่าของแต่ละห้อง**](#การคำนวณมูลค่าของแต่ละห้อง)
-   [**การหาห้องที่มีมูลค่าสูงสุด**](#การหาห้องที่มีมูลค่าสูงสุด)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## การเก็บราคาส่วนประกอบ

คอมพิวเตอร์แต่ละเครื่องอาจมีส่วนประกอบชนิด `A`, `B`, `C`, `D` และ `E`
โจทย์ให้ราคาของส่วนประกอบทั้ง 5 ชนิดในบรรทัดแรกตามลำดับนี้พอดี
โค้ดจึงเก็บชนิดและราคาไว้ในลิสต์ที่ใช้ดัชนีตรงกัน

```python
COMPONENT_TYPES = ["A", "B", "C", "D", "E"]
component_prices = [int(price) for price in input().split()]
```

ความสัมพันธ์ของข้อมูลเป็นดังนี้

| ดัชนี `i` | `COMPONENT_TYPES[i]` | `component_prices[i]` |
|---:|:---:|---:|
| `0` | `A` | ราคาของ `A` |
| `1` | `B` | ราคาของ `B` |
| `2` | `C` | ราคาของ `C` |
| `3` | `D` | ราคาของ `D` |
| `4` | `E` | ราคาของ `E` |

เมื่อวน `for i in range(COMPONENT_AMOUNT)` โปรแกรมจึงหยิบชนิดกับราคาที่เป็นคู่กัน
ได้ครบทุกชนิด

---

## การคำนวณมูลค่าของแต่ละห้อง

ข้อมูลห้องหนึ่งบรรทัดประกอบด้วยชื่อห้องและข้อความแทนคอมพิวเตอร์ เช่น

```text
218 ABCD,ACDE,ADE
```

หลัง `input().split()` จะได้ชื่อห้องเป็น `data[0]` และข้อความคอมพิวเตอร์ทั้งหมด
เป็น `data[1]` เครื่องหมายจุลภาคยังอยู่ในข้อความ แต่ไม่กระทบการนับตัวอักษร

เมื่อต้องการทราบจำนวนส่วนประกอบชนิดหนึ่ง สามารถใช้ `str.count()` ได้ เช่น

```python
component_count = computers.count(COMPONENT_TYPES[i])
```

ให้ $n_A, n_B, n_C, n_D, n_E$ เป็นจำนวนส่วนประกอบแต่ละชนิด และให้
$p_A, p_B, p_C, p_D, p_E$ เป็นราคาต่อชิ้น มูลค่ารวมของห้องคือ

$$
\text{total price}
= n_Ap_A+n_Bp_B+n_Cp_C+n_Dp_D+n_Ep_E
$$

ในโค้ด ผลรวมนี้เกิดจากการทำคำสั่ง
`total_price += component_count * component_prices[i]` ซ้ำครบ 5 รอบ
ถ้าห้องหนึ่งไม่มีส่วนประกอบบางชนิด `count()` จะได้ `0` ชนิดนั้นจึงเพิ่มมูลค่า
`0 * price` หรือเท่ากับศูนย์

โปรแกรมอ่านห้องทีละบรรทัดภายใน `while True` และหยุดเมื่ออ่านได้ `END`
เพียงคำเดียว

```python
data = input().split()
if data == ["END"]:
    break
```

---

## การหาห้องที่มีมูลค่าสูงสุด

ตัวแปร `max_price_room` เก็บข้อมูล 2 ค่า คือ
`[มูลค่าสูงสุดที่พบ, ชื่อห้องที่มีมูลค่านั้น]` เริ่มต้นเป็น `[0, "room"]`

หลังคำนวณ `total_price` ของห้องปัจจุบัน โปรแกรมเปรียบเทียบกับค่าสูงสุดเดิม

```python
if total_price > max_price_room[0]:
    max_price_room = [total_price, room]
```

จึงอัปเดตข้อมูลเฉพาะเมื่อพบค่าที่มากกว่าเดิมจริง ๆ เมื่ออ่านถึง `END`
ชื่อห้องคำตอบจะอยู่ที่ `max_price_room[1]` และถูกแสดงออกมาเพียงค่าเดียว

> [!NOTE]
>
> โจทย์รับประกันว่ามีห้องที่มีมูลค่าสูงสุดเพียงห้องเดียว
> จึงไม่ต้องกำหนดวิธีตัดสินกรณีที่หลายห้องมีมูลค่าเท่ากัน

---

## ตัวอย่างการทำงาน

กำหนดราคาของ `A` ถึง `E` เป็น `5 10 15 20 25` และพิจารณาห้อง `218`

```text
218 ABCD,ACDE,ADE
```

เมื่อนับตัวอักษรจากคอมพิวเตอร์ทั้ง 3 เครื่อง จะได้

| ชนิด | จำนวน | มูลค่า |
|:---:|---:|---:|
| `A` | `3` | `3 * 5 = 15` |
| `B` | `1` | `1 * 10 = 10` |
| `C` | `2` | `2 * 15 = 30` |
| `D` | `3` | `3 * 20 = 60` |
| `E` | `2` | `2 * 25 = 50` |

ดังนั้นห้อง `218` มีมูลค่ารวม `15 + 10 + 30 + 60 + 50 = 165`
โปรแกรมจะคำนวณแบบเดียวกันให้ทุกห้อง แล้วแสดงชื่อห้องที่มีผลรวมมากที่สุด

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_3_Q4_A2.py
# Problem   : Computer Price
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Constants for computer components amount and types
COMPONENT_AMOUNT = 5
COMPONENT_TYPES = ["A", "B", "C", "D", "E"]

# Input each component's price
component_prices = [int(price) for price in input().split()]

# Initialize the maximum price and corresponding room
max_price_room = [0, "room"]

while True:
    # Input room and its computer components until "END" is entered
    data = input().split()
    if data == ["END"]:
        break

    # Extract room name and computer components from input
    room = data[0]
    computers = data[1]

    # Initialize total price for the current room
    total_price = 0

    # Calculate the total price of components in the room
    for i in range(COMPONENT_AMOUNT):
        component_count = computers.count(COMPONENT_TYPES[i])
        total_price += component_count * component_prices[i]

    # Update the maximum price and room if the current total price is higher
    if total_price > max_price_room[0]:
        max_price_room = [total_price, room]

# Output the room with the maximum total price
print(max_price_room[1])
```
