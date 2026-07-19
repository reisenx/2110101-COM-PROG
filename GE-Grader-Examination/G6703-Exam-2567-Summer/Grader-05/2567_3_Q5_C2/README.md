<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Maximum Sales ★★ (
      <a href="https://drive.google.com/file/d/1qWUIet-zn5YuB5f9ndRhYzUuGX5YOk8x/view?usp=sharing">
        <code>2567_3_Q5_C2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**อ่านรายการขายจนพบ END**](#อ่านรายการขายจนพบ-end)
-   [**รวมยอดขายตามชั่วโมง**](#รวมยอดขายตามชั่วโมง)
-   [**หาชั่วโมงที่มียอดสูงสุด**](#หาชั่วโมงที่มียอดสูงสุด)
-   [**การปัดเศษและรูปแบบผลลัพธ์**](#การปัดเศษและรูปแบบผลลัพธ์)
-   [**Solution**](#solution)

---

## อ่านรายการขายจนพบ END

ข้อมูลการขายหนึ่งบรรทัดมีสี่ส่วนตามลำดับ

```text
ชื่อสินค้า วันที่ เวลา ยอดขาย
```

ตัวอย่างเช่น `Apple 2025/07/04 09:15:20 100.50` โปรแกรมอ่านข้อมูลด้วย
`split()` และทำซ้ำจนพบบรรทัด `END`

```python
data = input().strip().split()
if data == ["END"]:
    break
```

ชื่อสินค้าและวันที่จำเป็นต่อรูปแบบข้อมูล แต่โจทย์ต้องการยอดรวมตาม **ชั่วโมง**
เท่านั้น โค้ดจึงใช้เฉพาะ `data[2]` ซึ่งเป็นเวลา และ `data[3]` ซึ่งเป็นยอดขาย

---

## รวมยอดขายตามชั่วโมง

เวลาอยู่ในรูป `hh:mm:ss` จึงแยกด้วย `:` แล้วเลือกส่วนแรก

```python
hour = data[2].split(":")[0]
```

ตัวแปร `hour` เป็นสตริง ทำให้เลขศูนย์ด้านหน้ายังคงอยู่ เช่น `09:15:20`
ให้ค่า `"09"` และเวลาเที่ยงคืน `00:30:00` ให้ค่า `"00"`

ยอดขายแปลงเป็น `float` แล้วสะสมใน dictionary `hourly_sales`

```python
if hour not in hourly_sales:
    hourly_sales[hour] = 0.0
hourly_sales[hour] += sale
```

รายการที่มีชั่วโมงเดียวกันจะถูกรวมเข้าด้วยกัน แม้ชื่อสินค้าหรือวันที่ต่างกัน
ในเชิงคณิตศาสตร์ ยอดของชั่วโมง $h$ คือ

$$
S_h = \sum_{i:\,\text{hour}_i=h} \text{sale}_i
$$

ตัวอย่าง รายการในชั่วโมง `09` ที่มียอด `100.50`, `50` และ `20.25`
รวมเป็น $100.50 + 50 + 20.25 = 170.75$

---

## หาชั่วโมงที่มียอดสูงสุด

โปรแกรมวนดูคู่ `hour, sale` ที่สะสมไว้ แล้วเปลี่ยนคำตอบเมื่อพบยอดที่มากกว่า
ค่าสูงสุดเดิม

```python
if sale > top_sale:
    top_sale = sale
    top_hour = hour
```

ใช้เครื่องหมาย `>` ไม่ใช่ `>=` แต่โจทย์รับประกันว่ามีชั่วโมงที่มียอดสูงสุด
เพียงชั่วโมงเดียว จึงไม่ต้องกำหนดกติกาแก้กรณีเสมอกัน

---

## การปัดเศษและรูปแบบผลลัพธ์

ผลลัพธ์ประกอบด้วยชั่วโมงแบบสองหลักและยอดรวมที่ผ่าน `round(top_sale, 2)`
คั่นด้วยช่องว่าง

```python
print(top_hour, round(top_sale, 2))
```

`round(value, 2)` ปัดค่าให้มีความละเอียดไม่เกินสองตำแหน่ง แต่ไม่ได้บังคับให้
แสดงเลขศูนย์ท้ายครบสองหลัก เช่นยอด `100.0` จะแสดงเป็น `100.0` ไม่ใช่
`100.00` ซึ่งตรงกับการใช้ `round()` ตามที่โจทย์ระบุ

> [!NOTE]
>
> ยอดขายถูกเก็บเป็น `float` จึงอาจมีความคลาดเคลื่อนเล็กน้อยจากการแทนจำนวน
> ทศนิยมในคอมพิวเตอร์ การปัดด้วย `round(..., 2)` ทำก่อนแสดงผลเพื่อลดผลของ
> ความคลาดเคลื่อนดังกล่าว

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_3_Q5_C2.py
# Problem   : Maximum Sales
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Initialize a dictionary to store sales by hour
hourly_sales = {}

while True:
    # Read input until "END" is encountered
    data = input().strip().split()
    if data == ["END"]:
        break

    # Extract hour and sale amount from the input
    sale = float(data[3])
    hour = data[2].split(":")[0]

    # Add the sale amount to the corresponding hour in the dictionary
    if hour not in hourly_sales:
        hourly_sales[hour] = 0.0
    hourly_sales[hour] += sale

# Initialize variables to find the hour with the highest sales
top_hour = ""
top_sale = 0.0

# Find the hour with the highest sales
for hour, sale in hourly_sales.items():
    if sale > top_sale:
        top_sale = sale
        top_hour = hour

# Output the hour with the highest sales
print(top_hour, round(top_sale, 2))
```
