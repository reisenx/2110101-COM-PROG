<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Small Lot First ★★ (
      <a href="https://drive.google.com/file/d/1amVihMObcBwSYfZxmxeAXNxFKbRssTFi/view?usp=sharing">
        <code>2565_2_Q2_01</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**หลักการ Small Lot First**](#หลักการ-small-lot-first)
-   [**การเก็บข้อมูลผู้จอง**](#การเก็บข้อมูลผู้จอง)
-   [**การจัดสรรแบบวนรอบ**](#การจัดสรรแบบวนรอบ)
-   [**Solution**](#solution)

---

## หลักการ Small Lot First

ข้อมูลจำนวนเงินทั้งหมดในโจทย์มีหน่วยเป็น **พันบาท** ดังนั้น การจัดสรรเพิ่ม
`1` หน่วยในโปรแกรมจึงหมายถึงการจัดสรรเงินเพิ่ม `1,000` บาท

การจัดสรรแบบ Small Lot First จะวนพิจารณาผู้จองตามลำดับที่รับข้อมูล
ในแต่ละรอบ ผู้จองที่ยังได้รับเงินไม่ครบตามยอดจองจะได้รับเพิ่มคนละ `1` หน่วย
ส่วนผู้จองที่ได้รับครบแล้วจะถูกข้าม การวนรอบสิ้นสุดทันทีเมื่อวงเงินรวมเหลือ `0`

ตัวอย่างเช่น เมื่อมีวงเงิน `7` หน่วย และยอดจองของ `A`, `B`, `C`, `D` คือ
`4`, `1`, `3`, `1` หน่วยตามลำดับ ผลระหว่างการจัดสรรเป็นดังนี้

| รอบที่เสร็จสิ้น | `A` | `B` | `C` | `D` | จัดสรรสะสม |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 4 |
| 2 | 2 | 1 | 2 | 1 | 6 |
| 3 (สิ้นสุดที่ `A`) | 3 | 1 | 2 | 1 | 7 |

ในรอบที่ 3 วงเงินหมดหลังจัดสรรให้ `A` จึงไม่ต้องเริ่มพิจารณาคนถัดไปอีก
ผลลัพธ์สุดท้ายจึงเป็น `A 3`, `B 1`, `C 2` และ `D 1`

---

## การเก็บข้อมูลผู้จอง

โปรแกรมรับวงเงินรวมจากบรรทัดแรกด้วย `int(input())` แล้วเก็บไว้ใน
`total_money` จากนั้นจึงรับข้อมูลผู้จองทีละบรรทัดจนพบข้อความ `Q`
ซึ่งเป็นเครื่องหมายบอกว่าข้อมูลหมดแล้ว และไม่นำ `Q` ไปเก็บในรายการ

ข้อมูลของผู้จองแต่ละคนถูกเก็บในลิสต์รูปแบบ
`[name, current_money, reserved]` โดยมีความหมายดังนี้

-   `name` คือรหัสผู้จอง
-   `current_money` คือจำนวนเงินที่ได้รับแล้ว เริ่มต้นที่ `0`
-   `reserved` คือจำนวนเงินที่จอง ซึ่งแปลงเป็นจำนวนเต็มด้วย `int(reserved)`

เช่น ข้อมูล `A 4` จะถูกเก็บเป็น `['A', 0, 4]` การ append ตามลำดับที่อ่าน
ทำให้ลิสต์ `customers` รักษาลำดับเวลาจองไว้สำหรับทั้งการจัดสรรและการแสดงผล

---

## การจัดสรรแบบวนรอบ

ตัวแปร `idx` ระบุตำแหน่งของผู้จองที่กำลังพิจารณา โดยเริ่มจากคนแรกที่
ตำแหน่ง `0` ในแต่ละรอบของลูป โปรแกรมอ่านยอดที่ได้รับแล้วและยอดที่จองไว้

```python
current_money, reserved = customers[idx][1:]
```

ถ้า `current_money < reserved` แสดงว่าผู้จองคนนี้ยังได้รับไม่ครบ
โปรแกรมจึงเพิ่มยอดที่ได้รับ `1` หน่วย และลดวงเงินคงเหลือ `1` หน่วยพร้อมกัน
แต่ถ้าได้รับครบแล้วจะไม่เปลี่ยนยอดใด ๆ

ไม่ว่าจะจัดสรรให้คนปัจจุบันหรือข้ามคนนั้น โปรแกรมจะเลื่อนไปยังคนถัดไปด้วย

$$
\text{ตำแหน่งถัดไป} = (\text{ตำแหน่งปัจจุบัน} + 1) \bmod
\text{จำนวนผู้จอง}
$$

ซึ่งเขียนใน Python ได้เป็น

```python
idx = (idx + 1) % len(customers)
```

เครื่องหมาย `%` ทำให้ตำแหน่งวนจากคนสุดท้ายกลับไปเป็นคนแรกได้ เมื่อ
`total_money` ลดลงถึง `0` เงื่อนไข `while total_money > 0` จะเป็นเท็จ
จึงหยุดตรงจุดนั้น แม้ว่าจะเป็นช่วงกลางรอบก็ตาม

ท้ายสุด โปรแกรมวนอ่าน `[name, current_money, _]` จาก `customers`
แล้วใช้ `print(name, current_money)` แสดงรหัสและยอดที่ได้รับคั่นด้วยช่องว่าง
ทีละคนตามลำดับเดียวกับข้อมูลนำเข้า ส่วน `_` หมายถึงค่าที่ไม่ได้นำมาใช้
ในที่นี้คือยอดจองเดิม

> [!NOTE]
>
> โจทย์รับประกันว่าวงเงินรวมน้อยกว่ายอดจองรวม โปรแกรมจึงสามารถแจกวงเงิน
> จนหมดได้เสมอ หากไม่มีกติกานี้และทุกคนได้รับครบก่อนวงเงินหมด ลูปจะข้าม
> ทุกคนไปเรื่อย ๆ โดย `total_money` ไม่ลดลง

---

# Solution

```python
# --------------------------------------------------
# File Name : 2565_2_Q2_01.py
# Problem   : Small Lot First
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

# Input the total money available
total_money = int(input())

# Input the customers and their reserved money
customers = []
while True:
    data = input().strip()
    # Break if the input is "Q"
    if data == "Q":
        break
    # Append customer data to the list
    name, reserved = data.split()
    customers.append([name, 0, int(reserved)])

# Initialize the index of the current customer
idx = 0

# Distribute the money to customers in a round-robin fashion
while total_money > 0:
    # Extract the current customer's data
    current_money, reserved = customers[idx][1:]
    # If the current customer has less money than reserved, give them 1 unit of money
    if current_money < reserved:
        customers[idx][1] += 1
        total_money -= 1
    # Move to the next customer
    idx = (idx + 1) % len(customers)

# Output the final money for each customer
for name, current_money, _ in customers:
    print(name, current_money)
```
