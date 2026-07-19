<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Computer Price 2 ★★ (
      <a href="https://drive.google.com/file/d/1pOeszxNdypPvpQTMQmdbzZTr3cbNWI9d/view?usp=sharing">
        <code>2567_3_Q5_A2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**รูปแบบข้อมูลคอมพิวเตอร์**](#รูปแบบข้อมูลคอมพิวเตอร์)
-   [**รวมจำนวนอุปกรณ์ทุกห้อง**](#รวมจำนวนอุปกรณ์ทุกห้อง)
-   [**หาชนิดที่มีมูลค่ารวมสูงสุด**](#หาชนิดที่มีมูลค่ารวมสูงสุด)
-   [**Solution**](#solution)

---

## รูปแบบข้อมูลคอมพิวเตอร์

บรรทัดแรกรับราคาต่อชิ้นของอุปกรณ์ `A`, `B`, `C`, `D` และ `E` ตามลำดับ
แล้วเก็บไว้ในลิสต์ `component_prices`

```python
component_prices = [int(price) for price in input().split()]
```

บรรทัดถัด ๆ ไปมีชื่อห้องและข้อความแทนคอมพิวเตอร์ในห้องนั้น เช่น
`218 ABCD,ACDE,ADE` เครื่องหมาย `,` ใช้แบ่งเครื่องคอมพิวเตอร์ แต่ในการหา
มูลค่ารวม เราสนใจเพียงว่าตัวอักษรแต่ละชนิดปรากฏกี่ครั้งเท่านั้น

โปรแกรมอ่านข้อมูลจนพบ `END`

```python
data = input().split()
if data == ["END"]:
    break
```

---

## รวมจำนวนอุปกรณ์ทุกห้อง

โจทย์ถามว่า **อุปกรณ์ชนิดใด** มีมูลค่ารวมมากที่สุด จึงไม่ต้องแยกยอดตามห้อง
โค้ดนำข้อความอุปกรณ์ของทุกห้องมาต่อกันใน `all_computers`

```python
all_computers += computers
```

จากนั้นใช้ `str.count()` นับตัวอักษร `A` ถึง `E` เครื่องหมายจุลภาคที่ติดอยู่ใน
ข้อความไม่ตรงกับตัวอักษรเหล่านี้ จึงไม่กระทบต่อการนับ

สำหรับอุปกรณ์ชนิดลำดับที่ $i$ มูลค่ารวมคำนวณได้จาก

$$
\text{total}_i = \text{count}_i \times \text{price}_i
$$

ซึ่งตรงกับ Python ว่า

```python
component_count = all_computers.count(COMPONENT_TYPES[i])
component_total_price[i] = component_count * component_prices[i]
```

ตัวอย่างแรกของโจทย์นับได้ `A=6`, `B=2`, `C=3`, `D=4`, `E=3`
เมื่อราคาต่อชิ้นเป็น `5 10 15 20 25` จะได้มูลค่ารวมตามลำดับเป็น
`30 20 45 80 75`

---

## หาชนิดที่มีมูลค่ารวมสูงสุด

คำสั่ง `max(component_total_price)` หามูลค่าที่มากที่สุด และ `index()` หา
ตำแหน่งของค่านั้นในลิสต์

```python
idx = component_total_price.index(max(component_total_price))
```

ตำแหน่งเดียวกันใน `COMPONENT_TYPES` คือชื่ออุปกรณ์ที่ต้องแสดง ดังนั้นตัวอย่าง
ข้างต้นตอบ `D 80`

> [!NOTE]
>
> โจทย์รับประกันว่ามีอุปกรณ์ที่มูลค่ารวมสูงสุดเพียงชนิดเดียว หากมีค่าสูงสุด
> เท่ากันจริง `index()` จะเลือกตำแหน่งแรกตามลำดับ `A`, `B`, `C`, `D`, `E`

ผลลัพธ์หนึ่งบรรทัดประกอบด้วยชนิดอุปกรณ์และมูลค่ารวม คั่นด้วยช่องว่าง

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_3_Q5_A2.py
# Problem   : Computer Price 2
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Constants for computer components amount and types
COMPONENT_AMOUNT = 5
COMPONENT_TYPES = ["A", "B", "C", "D", "E"]

# Input each component's price
component_prices = [int(price) for price in input().split()]

component_total_price = [0] * COMPONENT_AMOUNT

all_computers = ""
while True:
    # Input room and its computer components until "END" is entered
    data = input().split()
    if data == ["END"]:
        break

    # Extract room name and computer components from input
    room = data[0]
    computers = data[1]

    # Add the current room's computers to the total string
    all_computers += computers

# Calculate the total price for each component type
for i in range(COMPONENT_AMOUNT):
    component_count = all_computers.count(COMPONENT_TYPES[i])
    component_total_price[i] = component_count * component_prices[i]

# Find and output the component with the maximum total price
idx = component_total_price.index(max(component_total_price))
print(COMPONENT_TYPES[idx], component_total_price[idx])
```
