<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Delivery ★★★ (
      <a href="https://drive.google.com/file/d/1ihF9HlO3j0o5VpNef82U5qOwOZMpUZh7/view?usp=drive_link">
        <code>P2_04_Delivery</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิดของโจทย์**](#แนวคิดของโจทย์)
-   [**เตรียมข้อมูลปฏิทินและประเภทการจัดส่ง**](#เตรียมข้อมูลปฏิทินและประเภทการจัดส่ง)
-   [**ตรวจสอบข้อมูลตามลำดับที่กำหนด**](#ตรวจสอบข้อมูลตามลำดับที่กำหนด)
-   [**คำนวณวันที่จัดส่ง**](#คำนวณวันที่จัดส่ง)
-   [**เรียงลำดับและแสดงผล**](#เรียงลำดับและแสดงผล)
-   [**ลำดับการทำงานของโปรแกรม**](#ลำดับการทำงานของโปรแกรม)
-   [**ข้อควรระวัง**](#ข้อควรระวัง)
-   [**Solution**](#solution)

---

## แนวคิดของโจทย์

โจทย์นี้มีงานหลัก 3 ส่วนที่ต้องทำตามลำดับ

1. อ่านคำสั่งซื้อทีละบรรทัดจนพบคำว่า `END`
2. ตรวจสอบคำสั่งซื้อ หากข้อมูลผิดต้องแสดงสาเหตุเพียงอย่างเดียวตามลำดับที่โจทย์กำหนด
3. คำนวณวันส่งถึงของคำสั่งซื้อที่ถูกต้อง แล้วเรียงตามวันส่งถึงก่อนแสดงผล

ข้อมูลหนึ่งบรรทัดมีรูปแบบ

```text
เลขที่คำสั่งซื้อ ประเภทการจัดส่ง วัน เดือน ปีพุทธศักราช
```

เช่น `10005 Q 10 4 2559` หมายถึงคำสั่งซื้อหมายเลข `10005` เลือกส่งแบบ Quick และสั่งซื้อวันที่ 10 เมษายน พ.ศ. 2559

ข้อผิดพลาดถูกพิมพ์ทันทีระหว่างรับข้อมูล ส่วนคำสั่งซื้อที่ถูกต้องจะถูกเก็บไว้ก่อน รอจนรับข้อมูลครบแล้วจึงเรียงและพิมพ์ในภายหลัง จึงได้ผลลัพธ์เป็นสองส่วนตามที่โจทย์ต้องการ

## เตรียมข้อมูลปฏิทินและประเภทการจัดส่ง

จำนวนวันของแต่ละเดือนต่างกันระหว่างปีปกติกับปีอธิกสุรทิน โปรแกรมจึงเตรียมลิสต์ไว้สองชุด

```python
COMMON = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
```

เดือนในข้อมูลเริ่มนับจาก 1 แต่ตำแหน่งในลิสต์เริ่มนับจาก 0 ดังนั้นจำนวนวันของเดือนที่ `month` จึงอยู่ที่ตำแหน่ง `month - 1`

ระยะเวลาจัดส่งเก็บใน dictionary เพื่อให้ใช้ตัวอักษรประเภทการส่งค้นหาจำนวนวันได้โดยตรง

| ประเภท | รูปแบบการจัดส่ง | จำนวนวัน | Python |
|:---:|---|---:|---|
| `E` | Express | 1 | `DELIVERY["E"]` |
| `Q` | Quick | 3 | `DELIVERY["Q"]` |
| `N` | Normal | 7 | `DELIVERY["N"]` |
| `F` | Free | 14 | `DELIVERY["F"]` |

### การตรวจปีอธิกสุรทิน

ปีที่รับเข้ามาเป็น พ.ศ. แต่กฎปีอธิกสุรทินใช้กับปี ค.ศ. จึงต้องแปลงปีก่อน

$$
\text{ปี ค.ศ.} = \text{ปี พ.ศ.} - 543
$$

ให้ $y$ เป็นปี ค.ศ. ปีนั้นเป็นปีอธิกสุรทินเมื่อ

$$
(y \bmod 400 = 0)
\quad\text{หรือ}\quad
(y \bmod 4 = 0 \text{ และ } y \bmod 100 \ne 0)
$$

ตรงกับ Python ในฟังก์ชัน `is_leap_year()` ดังนี้

```python
((year - 543) % 400 == 0) or (
    (year - 543) % 100 != 0 and (year - 543) % 4 == 0
)
```

ตัวอย่างเช่น พ.ศ. 2563 คือ ค.ศ. 2020 ซึ่งหารด้วย 4 ลงตัวและหารด้วย 100 ไม่ลงตัว เดือนกุมภาพันธ์จึงมี 29 วัน

## ตรวจสอบข้อมูลตามลำดับที่กำหนด

ฟังก์ชัน `is_order_valid()` ตรวจข้อผิดพลาดตามลำดับนี้

| ลำดับ | เงื่อนไข | ข้อความ |
|:---:|---|---|
| 1 | `year < 2558` | `Invalid year` |
| 2 | `month < 1 or month > 12` | `Invalid month` |
| 3 | วันน้อยกว่า 1 หรือเกินจำนวนวันของเดือนนั้น | `Invalid date` |
| 4 | `o_type not in DELIVERY` | `Invalid delivery type` |

เมื่อพบข้อผิดพลาด ฟังก์ชันจะพิมพ์ข้อความแล้ว `return False` ทันที จึงรายงานเพียงข้อแรกตามลำดับข้างบน แม้บรรทัดเดียวกันจะผิดหลายจุดก็ตาม

ตัวอย่าง `10003 X 30 -200 2559` มีทั้งเดือนและประเภทการส่งที่ไม่ถูกต้อง แต่โปรแกรมแสดง `Invalid month` เพราะตรวจเดือนก่อนประเภทการส่ง

การตรวจเดือนก่อนวันยังทำให้การใช้ `COMMON[month - 1]` หรือ `LEAP[month - 1]` ปลอดภัย เพราะเมื่อมาถึงขั้นตรวจวัน ค่า `month` ต้องอยู่ในช่วง 1 ถึง 12 แล้ว

ข้อความผิดพลาดมีรูปแบบตายตัว

```text
Error: <id> <type> <day> <month> <year> --> <สาเหตุ>
```

## คำนวณวันที่จัดส่ง

ฟังก์ชัน `add_date()` ไม่ได้บวกวันที่ด้วยการไล่ทีละวัน แต่แปลงวันเดือนปีให้เป็น “ลำดับวันที่ของปี” ก่อน

### แปลงวันเดือนเป็นลำดับวันที่ของปี

$$
\text{ลำดับวันที่}
= \text{ผลรวมจำนวนวันของเดือนก่อนหน้า} + \text{วันที่}
$$

Python ใช้ slice เลือกเดือนก่อนหน้าแล้วหาผลรวม

```python
total_days = sum(COMMON[: month - 1]) + day
```

ถ้าเป็นปีอธิกสุรทินก็ใช้ `LEAP` แทน จากนั้นบวกจำนวนวันจัดส่ง

```python
total_days += DELIVERY[o_type]
```

### จัดการกรณีข้ามปี

ถ้าผลรวมเกิน 365 วันในปีปกติ หรือเกิน 366 วันในปีอธิกสุรทิน แสดงว่าวันส่งถึงอยู่ในปีถัดไป โปรแกรมจึงเพิ่มปีหนึ่งปีและหักจำนวนวันของปีเดิมออก

```python
new_year = year + 1
total_days -= 365  # หรือ 366 สำหรับปีอธิกสุรทิน
```

ตัวอย่างคำสั่งซื้อวันที่ 28 ธันวาคม พ.ศ. 2560 แบบ `F`

- วันที่ 28 ธันวาคมเป็นวันที่ 362 ของปีปกติ
- ส่งแบบ `F` ใช้ 14 วัน จึงได้ `362 + 14 = 376`
- `376 > 365` จึงข้ามปี และเหลือ `376 - 365 = 11`
- วันที่ส่งถึงคือ 11 มกราคม พ.ศ. 2561

### แปลงลำดับวันที่กลับเป็นวันและเดือน

โปรแกรมไล่ค่า `m` แล้วหาจุดแรกที่ `total_days` ไม่เกินผลรวมจำนวนวันตั้งแต่เดือนมกราคมถึงเดือน `m`

```python
if total_days <= sum(COMMON[:m]):
    new_month = m
    new_day = total_days - sum(COMMON[: m - 1])
```

เมื่อพบเดือนแล้ว วันที่ภายในเดือนคือ `total_days` ลบด้วยจำนวนวันทั้งหมดก่อนเดือนนั้น ฟังก์ชันจึงคืน `[new_day, new_month, new_year]`

> [!NOTE]
> ภายในลูปนี้โค้ดตรวจปีอธิกสุรทินจาก `year` ซึ่งเป็นปีที่สั่งซื้อ ส่วนปีผลลัพธ์เก็บใน `new_year` หากมีการข้ามปี อย่างไรก็ตาม ระยะเวลาจัดส่งยาวที่สุดเพียง 14 วัน ดังนั้นเมื่อข้ามปี วันส่งถึงต้องอยู่ในเดือนมกราคมเสมอ และเดือนมกราคมมี 31 วันเหมือนกันทุกปี ผลลัพธ์ของโจทย์นี้จึงยังถูกต้อง

## เรียงลำดับและแสดงผล

คำสั่งซื้อที่ถูกต้องถูกเก็บในรูป

```python
[year, month, day, o_id]
```

เมื่อเรียก `successful_orders.sort()` Python จะเปรียบเทียบสมาชิกของลิสต์จากซ้ายไปขวา จึงเรียงตามปี เดือน และวันก่อน หากวันส่งถึงเท่ากันจึงใช้ `o_id` ตัดสิน

ข้อความของคำสั่งซื้อที่ถูกต้องมีรูปแบบ

```text
<id>: delivered on <day>/<month>/<year>
```

> [!NOTE]
> โปรแกรมเก็บ `o_id` เป็น `str` ไม่ได้แปลงเป็น `int` การตัดสินกรณีวันเดียวกันจึงเป็นการเรียงข้อความ เช่น `"10"` มาก่อน `"2"` ถ้าเลขที่คำสั่งซื้อทุกตัวมีจำนวนหลักเท่ากัน ลำดับนี้จะตรงกับการเรียงค่าตัวเลข

## ลำดับการทำงานของโปรแกรม

1. สร้าง `successful_orders` เป็นลิสต์ว่าง
2. อ่านหนึ่งบรรทัดแล้วใช้ `.strip().split()` แยกข้อมูล
3. ถ้าส่วนแรกเป็น `END` ให้ออกจากลูป
4. แปลงวัน เดือน และปีเป็น `int`
5. เรียก `is_order_valid()`
   - ถ้าผิด ฟังก์ชันพิมพ์ข้อผิดพลาดทันที
   - ถ้าถูก เรียก `add_date()` แล้วเก็บ `[year, month, day, o_id]`
6. หลังพบ `END` ให้เรียง `successful_orders`
7. พิมพ์วันส่งถึงตามลำดับที่เรียงแล้ว

ด้วยโครงสร้างนี้ บรรทัดข้อผิดพลาดจึงเรียงตามลำดับที่รับเข้ามา และบรรทัดคำสั่งซื้อที่ถูกต้องจึงเรียงตามวันส่งถึง

## ข้อควรระวัง

- ต้องลบ 543 ก่อนตรวจปีอธิกสุรทิน เพราะข้อมูลใช้ปี พ.ศ.
- ต้องตรวจปี เดือน วัน และประเภทการส่งตามลำดับที่โจทย์กำหนด ห้ามสลับลำดับ
- เดือนกุมภาพันธ์ต้องเลือกจำนวนวันจาก `COMMON` หรือ `LEAP` ให้ถูกชุด
- การจัดส่งปลายเดือนหรือปลายปีอาจเปลี่ยนทั้งเดือนและปี
- ต้องรักษาช่องว่าง เครื่องหมาย `-->` เครื่องหมาย `/` และข้อความภาษาอังกฤษในผลลัพธ์ให้ตรงรูปแบบ

---

# Solution

```python
# --------------------------------------------------
# File Name : P2_04_Delivery.py
# Problem   : Part-II Delivery
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# List of days in each month for common and leap years
COMMON = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Delivery types and their corresponding days
DELIVERY = {"E": 1, "Q": 3, "N": 7, "F": 14}


# Check if the year is a leap year
def is_leap_year(year):
    return ((year - 543) % 400 == 0) or (
        (year - 543) % 100 != 0 and (year - 543) % 4 == 0
    )


# This function checks if the order is valid
def is_order_valid(o_id, o_type, day, month, year):
    # Case 1: Invalid order year
    if year < 2558:
        print(f"Error: {o_id} {o_type} {day} {month} {year} --> Invalid year")
        return False

    # Case 2: Invalid order month
    if month < 1 or month > 12:
        print(f"Error: {o_id} {o_type} {day} {month} {year} --> Invalid month")
        return False

    # Case 3: Invalid order date
    if (
        day < 1
        or (not is_leap_year(year) and day > COMMON[month - 1])
        or (is_leap_year(year) and day > LEAP[month - 1])
    ):
        print(f"Error: {o_id} {o_type} {day} {month} {year} --> Invalid date")
        return False

    # Case 4: Invalid delivery type
    if o_type not in DELIVERY:
        print(f"Error: {o_id} {o_type} {day} {month} {year} --> Invalid delivery type")
        return False

    # The order is valid
    return True


# This function adds the delivery days to the order date
def add_date(day, month, year, o_type):
    # Initialize total days in the year and the new date variables
    total_days = 0
    new_day, new_month, new_year = day, month, year
    # Add the delivery days to the order date and adjust the year
    if is_leap_year(year):
        total_days = sum(LEAP[: month - 1]) + day
        total_days += DELIVERY[o_type]
        if total_days > 366:
            new_year = year + 1
            total_days -= 366
    else:
        total_days = sum(COMMON[: month - 1]) + day
        total_days += DELIVERY[o_type]
        if total_days > 365:
            new_year = year + 1
            total_days -= 365

    # Determine the new month and day after adding delivery days
    for m in range(13):
        if is_leap_year(year):
            if total_days <= sum(LEAP[:m]):
                new_month = m
                new_day = total_days - sum(LEAP[: m - 1])
                break
        else:
            if total_days <= sum(COMMON[:m]):
                new_month = m
                new_day = total_days - sum(COMMON[: m - 1])
                break
    # Return the new date as a list [day, month, year]
    return [new_day, new_month, new_year]


# Input orders until "END" is entered
successful_orders = []
while True:
    # Read the order input
    order = input().strip().split()
    # Stop if "END" is entered
    if order[0] == "END":
        break

    # Extract order details
    o_id, o_type = order[:2]
    day, month, year = int(order[2]), int(order[3]), int(order[4])
    # Check if the order is valid
    if is_order_valid(o_id, o_type, day, month, year):
        # Add the delivery days to the order date
        day, month, year = add_date(day, month, year, o_type)
        # Append the successful order to the list
        successful_orders.append([year, month, day, o_id])

# Sort the successful orders by year, month, day, and ID
successful_orders.sort()

# Output the successful orders
for year, month, day, o_id in successful_orders:
    print(f"{o_id}: delivered on {day}/{month}/{year}")
```
