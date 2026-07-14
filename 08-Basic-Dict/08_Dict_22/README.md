<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Ice Cream Sales ★★ (
      <a href="https://drive.google.com/file/d/1hxgTFuNQ-XUr5p4xlReWOb0wvgzQSXRF/view?usp=drive_link">
        <code>08_Dict_22</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเก็บราคาและยอดขายด้วย Dictionary**](#การเก็บราคาและยอดขายด้วย-dictionary)
-   [**การสะสมยอดขาย**](#การสะสมยอดขาย)
-   [**การหายอดขายรวมและเมนูขายดีที่สุด**](#การหายอดขายรวมและเมนูขายดีที่สุด)
-   [**การแสดงผล**](#การแสดงผล)
-   [**Solution**](#solution)

---

## การเก็บราคาและยอดขายด้วย Dictionary

โจทย์ให้ข้อมูล 2 ส่วน ได้แก่ ราคาไอศกรีมแต่ละชนิด และรายการสินค้าที่ขายได้
เราจึงใช้ Dictionary 2 ตัวเพื่อแยกหน้าที่กันอย่างชัดเจน

| Dictionary | Key | Value |
|---|---|---|
| `menu` | ชื่อไอศกรีม | ราคาต่อชิ้น |
| `sales` | ชื่อไอศกรีม | ยอดขายสะสมของไอศกรีมชนิดนั้น |

เมื่ออ่านข้อมูลเมนูแต่ละบรรทัด โปรแกรมจะแปลงราคาเป็น `float`
แล้วกำหนดยอดขายเริ่มต้นของไอศกรีมชนิดนั้นให้เป็น `0.0`

```python
menu[item] = float(price)
sales[item] = 0.0
```

ตัวอย่างเช่น ข้อมูล `Magnum 50` ทำให้ `menu["Magnum"]` มีค่าเป็น `50.0`
และ `sales["Magnum"]` มีค่าเริ่มต้นเป็น `0.0`

> [!NOTE]
>
> ค่าใน `sales` คือ **ยอดเงินที่ขายได้** ไม่ใช่จำนวนชิ้นที่ขายได้

ชื่อสินค้าในข้อมูลเมนูและรายการขายต้องเป็นข้อความ 1 คำ เพราะโปรแกรมแยกข้อมูล
แต่ละบรรทัดออกเป็น 2 ส่วนด้วย `.split()` ส่วนจำนวนที่ขายจะแปลงเป็น `int`
ถ้าชื่อเมนูซ้ำกัน การกำหนดค่ารอบหลังจะเขียนทับราคาและตั้งยอดขายกลับเป็น `0.0`
โจทย์ไม่ได้กำหนดกรณีนี้ โค้ดจึงอาศัยข้อมูลเมนูที่แต่ละชื่อไม่ซ้ำกัน

---

## การสะสมยอดขาย

รายการขายอาจมีทั้งไอศกรีมที่อยู่ในเมนูและสินค้าอื่น โปรแกรมจึงตรวจสอบชื่อสินค้า
ด้วย `if item in menu:` ก่อน ถ้าชื่อไม่อยู่ใน `menu` รายการนั้นจะถูกข้ามไป

สำหรับสินค้าที่อยู่ในเมนู ยอดขายของรายการหนึ่งคำนวณจาก

$$
\text{revenue ใหม่}
= \text{revenue เดิม} + \text{price} \times \text{quantity}
$$

ซึ่งตรงกับคำสั่ง Python

```python
sales[item] += menu[item] * int(quantity)
```

เครื่องหมาย `+=` ทำให้ยอดขายใหม่ถูกบวกต่อจากยอดเดิม
ดังนั้นรายการขายชื่อเดิมที่ปรากฏหลายครั้งจะถูกรวมเข้าด้วยกัน ตัวอย่างเช่น
`Magnum` ราคา `50.0` บาทและขายครั้งละ `5` ชิ้น 2 ครั้ง จะมียอดขายสะสมเป็น

$$
50.0 \times 5 + 50.0 \times 5 = 500.0
$$

ใน Python การคำนวณเดียวกันเขียนได้เป็น
`50.0 * 5 + 50.0 * 5` ส่วนสินค้าอย่าง `Cookie` ซึ่งไม่มีชื่อใน `menu`
จะไม่ถูกนำมาคำนวณ

---

## การหายอดขายรวมและเมนูขายดีที่สุด

โปรแกรมพิจารณาเฉพาะไอศกรีมที่มี `revenue > 0` แล้วบวกยอดขายนั้นเข้า
`total_revenue`

$$
\mathrm{total\_revenue}
= \sum_{\mathrm{revenue} > 0} \mathrm{revenue}
$$

การบวกยอดขายทีละรายการใน Python คือ

```python
total_revenue += revenue
```

ขณะเดียวกัน โปรแกรมเก็บข้อมูลสำหรับเรียงลำดับในรูป `[-revenue, item]`

```python
sorted_sales.append([-revenue, item])
sorted_sales.sort()
```

Python เรียง list จากน้อยไปมากและเปรียบเทียบสมาชิกจากซ้ายไปขวา

-   การใส่เครื่องหมายลบหน้ารายได้ทำให้ยอดขายจริงที่มากกว่าอยู่ก่อน เช่น
    ยอดขาย `500.0` กลายเป็น `-500.0` ซึ่งอยู่ก่อน `-20.0`
-   ถ้ายอดขายเท่ากัน Python จะเปรียบเทียบ `item` ตัวที่ 2 ต่อ
    จึงได้ชื่อเรียงตามลำดับพจนานุกรม

จากตัวอย่างที่ 2 ในโจทย์ ยอดขายที่นำมาคิดมีดังนี้

| ไอศกรีม | การคำนวณ | คำสั่ง Python ที่เทียบเท่า | ยอดขาย |
|---|---:|---:|---:|
| `Magnum` | $50 \times 5 + 50 \times 5$ | `50 * 5 + 50 * 5` | `500.0` |
| `Cornetto` | $25 \times 20$ | `25 * 20` | `500.0` |
| `AsianDelight` | $20 \times 1$ | `20 * 1` | `20.0` |

ดังนั้นยอดขายรวมคือ $500 + 500 + 20 = 1020.0$ หรือใน Python คือ
`500.0 + 500.0 + 20.0` ส่วน `Cornetto` และ `Magnum` มียอดขายสูงสุดเท่ากัน
เมื่อเรียงชื่อตามพจนานุกรมจึงได้ `Cornetto` ก่อน `Magnum`

> [!NOTE]
>
> ตัวแปร `highest_revenue` ในโค้ดเก็บสมาชิกตัวแรกของ `sorted_sales`
> ซึ่งเป็น **ค่ารายได้ติดลบที่ใช้เป็นกุญแจเรียงลำดับ** ไม่ใช่รายได้จริง
> การเปรียบเทียบยังถูกต้องเพราะค่ารายได้ใน `sorted_sales` ทุกตัวถูกติดลบเหมือนกัน
> โค้ดเปรียบเทียบค่าที่เสมอกันด้วย `revenue == highest_revenue` โดยไม่ปัดเศษก่อน
> ค่าทศนิยมที่ใกล้กันแต่ไม่เท่ากันจริงในชนิด `float` จึงไม่ถือว่าเสมอกัน

---

## การแสดงผล

ถ้า `sorted_sales` มีข้อมูล โปรแกรมจะแสดงยอดขายรวมก่อน
แล้วแสดงชื่อไอศกรีมที่มียอดขายสูงสุดในบรรทัดถัดไป
ชื่อที่เสมอกันจะถูกเชื่อมด้วย `", ".join(top_items)` จึงมีเครื่องหมายจุลภาค
และช่องว่างคั่นระหว่างชื่อ

```text
Total ice cream sales: 1020.0
Top sales: Cornetto, Magnum
```

ราคาและยอดขายเป็น `float` และคำสั่ง
`print(f"Total ice cream sales: {total_revenue}")` ใช้รูปแบบปกติของ Python
โค้ดไม่ได้เรียก `round()` และไม่ได้กำหนดจำนวนตำแหน่งทศนิยม เช่น `:.2f`
ดังนั้นจึงไม่มีการปัดเศษหรือบังคับให้แสดงทศนิยมจำนวนคงที่

ถ้าไม่มีรายการที่มียอดขายมากกว่า `0` เช่น ไม่มีรายการขายเลย
หรือสินค้าที่ขายทั้งหมดไม่อยู่ในเมนู โปรแกรมจะแสดงเพียง

```text
No ice cream sales
```

เงื่อนไขในโค้ดคือ `revenue > 0` โดยตรง ดังนั้นยอดขายสะสมที่เป็น `0`
หรือติดลบก็จะไม่ถูกนับว่าเป็นการขายเช่นกัน

---

# Solution

```python
# --------------------------------------------------
# File Name : 08_Dict_22.py
# Problem   : Ice Cream Sales
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Initialize dictionaries for menu and sales
menu = {}
sales = {}
total_revenue = 0.0

# Input the menu items and their prices
n = int(input())
for _ in range(n):
    item, price = input().strip().split()
    menu[item] = float(price)
    sales[item] = 0.0

# Input the sales data
n = int(input())
for _ in range(n):
    item, quantity = input().strip().split()
    if item in menu:
        sales[item] += menu[item] * int(quantity)

# Sort the sales items by total sales amount (descending) and then alphabetically
sorted_sales = []
for item, revenue in sales.items():
    if revenue > 0:
        total_revenue += revenue
        sorted_sales.append([-revenue, item])
sorted_sales.sort()

# Output
if len(sorted_sales) > 0:
    # Find the top sales items and their total sales
    highest_revenue = sorted_sales[0][0]
    top_items = []
    for revenue, item in sorted_sales:
        if revenue == highest_revenue:
            top_items.append(item)

    # Output the top sales items
    print(f"Total ice cream sales: {total_revenue}")
    print("Top sales:", ", ".join(top_items))
else:
    print("No ice cream sales")
```
