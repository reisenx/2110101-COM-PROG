<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Credit Points ★★ (
      <a href="https://drive.google.com/file/d/1i2hhun44grSnF-DZH80CKTKjj4O4ch3m/view?usp=sharing">
        <code>2566_2_Q2_02</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**โจทย์ต้องการอะไร**](#โจทย์ต้องการอะไร)
-   [**แนวคิดในการแก้ปัญหา**](#แนวคิดในการแก้ปัญหา)
-   [**ลำดับการทำงาน**](#ลำดับการทำงาน)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ข้อควรระวัง**](#ข้อควรระวัง)
-   [**Solution**](#solution)

---

# โจทย์ต้องการอะไร

โปรแกรมรับจำนวนคูปอง `n` ตามด้วยชื่อและคะแนนที่ใช้แลกของคูปองแต่ละชนิด แล้วจึงรับคะแนนสะสมทั้งหมดที่มีอยู่ การแลกต้องทำตามกติกา 2 ข้อ

1. พิจารณาคูปองที่ใช้คะแนนมากที่สุดก่อน
2. คูปองแต่ละชื่อแลกได้ไม่เกิน 3 ใบ

บรรทัดแรกของผลลัพธ์ต้องอยู่ในรูป

```text
> คะแนนทั้งหมด คะแนนที่ใช้ไป คะแนนคงเหลือ
```

หากแลกได้ ให้แสดงชื่อคูปองและจำนวนที่แลกโดยเรียง **ตามชื่อ** แบบพจนานุกรม แต่หากแลกไม่ได้เลยให้แสดง `No coupon`

จุดสำคัญคือ ลำดับที่ใช้ **แลก** กับลำดับที่ใช้ **แสดงผล** เป็นคนละลำดับกัน: แลกจากคะแนนมากไปน้อย แต่แสดงชื่อจากน้อยไปมาก

# แนวคิดในการแก้ปัญหา

## 1. เก็บคะแนนเป็นกุญแจของพจนานุกรม

โค้ดเก็บข้อมูลใน `coupons_details` โดยให้คะแนนเป็นกุญแจและชื่อคูปองเป็นค่า

```python
coupons_details[int(price)] = name
```

โจทย์รับประกันว่าคูปองต่างชนิดจะไม่มีคะแนนที่ใช้แลกเท่ากัน จึงใช้คะแนนเป็นกุญแจได้โดยข้อมูลไม่ทับกัน จากนั้น

```python
sorted_coupons_details = sorted(coupons_details.items())[::-1]
```

จะสร้างลำดับคู่ `(price, name)` จากคะแนนมากไปน้อยตามกติกาการแลก

## 2. แลกแบบละโมบตามลำดับที่โจทย์กำหนด

สมมติว่าขณะหนึ่งมีคะแนนคงเหลือ $R$ และคูปองใช้คะแนน $P$ จำนวนที่แลกได้คือ

$$
\text{usage} = \min\left(\left\lfloor\frac{R}{P}\right\rfloor, 3\right)
$$

Python เขียนตรงกับสูตรนี้ว่า

```python
usage = min(remain_points // price, 3)
```

- `remain_points // price` คือจำนวนเต็มสูงสุดที่คะแนนปัจจุบันพอแลกได้
- `min(..., 3)` จำกัดจำนวนไว้ไม่เกิน 3 ใบ

เมื่อแลกแล้ว อัปเดตคะแนนคงเหลือและคะแนนที่ใช้ไปด้วย

$$
R \leftarrow R - \text{usage}\times P
$$

$$
U \leftarrow U + \text{usage}\times P
$$

ซึ่งตรงกับ `remain_points -= usage * price` และ `used_points += usage * price` ทำให้ทุกขณะยังคงมีความสัมพันธ์

$$
\text{total\_points} = \text{used\_points} + \text{remain\_points}
$$

## 3. แยกการเรียงสำหรับแสดงผล

จำนวนคูปองที่แลกจริงถูกเก็บใน `coupons_usage` โดยใช้ชื่อเป็นกุญแจ ตอนแสดงผลจึงใช้

```python
for name, usage in sorted(coupons_usage.items()):
```

เพื่อเรียงตามชื่อแบบพจนานุกรมตามที่โจทย์กำหนด ไม่ใช่เรียงตามคะแนนที่ใช้แลก

# ลำดับการทำงาน

1. อ่านคูปอง `n` ชนิดและเก็บคู่ `price -> name`
2. อ่าน `total_points` แล้วกำหนดให้ `remain_points` เท่ากับคะแนนทั้งหมด และ `used_points` เริ่มที่ `0`
3. เรียงคูปองจากคะแนนมากไปน้อย
4. สำหรับคูปองแต่ละชนิด หากคะแนนคงเหลือพอ ให้คำนวณ `usage` ซึ่งไม่เกิน 3 แล้วอัปเดตคะแนนทั้งสองส่วน
5. แสดง `> total used remaining`
6. หาก `used_points == 0` ให้แสดง `No coupon`; มิฉะนั้นแสดงคูปองที่แลกโดยเรียงตามชื่อ

# ตัวอย่างการทำงาน

เมื่อมีคะแนน `15000` และใช้ข้อมูลราคาในตัวอย่างโจทย์ โปรแกรมพิจารณาคูปองจากแพงไปถูกดังนี้

| คูปอง | คะแนนต่อใบ | จำนวนที่แลก | คะแนนคงเหลือ |
|---|---:|---:|---:|
| `gas_2000` | 20000 | 0 | 15000 |
| `gas_1000` | 11000 | 1 | 4000 |
| `coffee_200` | 2100 | 1 | 1900 |
| `food_200` | 2000 | 0 | 1900 |
| `coffee_100` | 1200 | 1 | 700 |
| `food_100` | 1100 | 0 | 700 |

จึงใช้คะแนนไป $11000 + 2100 + 1200 = 14300$ คะแนน และเหลือ `700` คะแนน แม้จะแลกตามคะแนนจากมากไปน้อย แต่ผลลัพธ์คูปองต้องเรียงตามชื่อ

```text
> 15000 14300 700
coffee_100 1
coffee_200 1
gas_1000 1
```

# ข้อควรระวัง

> [!NOTE]
> ตารางแนะนำตอนต้นของ PDF ระบุ `food_100` ว่าใช้ 1000 คะแนน แต่ข้อมูลตัวอย่างที่นำไปรันจริงระบุ 1100 คะแนน โค้ดไม่ได้กำหนดราคาตายตัวและจะใช้ค่าที่รับมาในแต่ละบรรทัดเสมอ ดังนั้นให้ยึดข้อมูลนำเข้าของรอบนั้นเป็นหลัก

- หากคะแนนคงเหลือเท่ากับราคาพอดี `//` จะให้จำนวนอย่างน้อย 1 ใบ และคะแนนคงเหลืออาจเป็น `0`
- ต่อให้คะแนนพอแลกได้มากกว่า 3 ใบ `min(..., 3)` จะจำกัดไว้ที่ 3 ใบ
- ถ้าไม่มีคูปองใดแลกได้ ต้องพิมพ์ `No coupon` หลังบรรทัดสรุป
- เครื่องหมาย `>` และช่องว่างในบรรทัดสรุปเป็นส่วนหนึ่งของรูปแบบผลลัพธ์
- การคำนวณทั้งหมดใช้จำนวนเต็ม จึงไม่มีการปัดเศษ

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_2_Q2_02.py
# Problem   : Credit Points
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------

# Initialize dictionaries to store coupon details and usage
coupons_details = {}
coupons_usage = {}

# Read the number of coupons and their prices
n = int(input())
for _ in range(n):
    name, price = input().strip().split()
    coupons_details[int(price)] = name

# Input the total point available and initialize remaining points and used points
total_points = int(input())
remain_points = total_points
used_points = 0

# Sort the coupons by price in descending order and calculate usage
sorted_coupons_details = sorted(coupons_details.items())[::-1]
# Loop through the sorted coupons and calculate how many can be used
for price, name in sorted_coupons_details:
    # Spent points only if there are enough remaining points
    if remain_points >= price:
        # Calculate amount of coupon that can be used
        usage = min(remain_points // price, 3)
        # Update the usage and remaining points
        coupons_usage[name] = usage
        remain_points -= usage * price
        used_points += usage * price

# Output the total points, used points, and remaining points
print(f"> {total_points} {used_points} {remain_points}")
# Output the coupons and their usage sorted by name alphabetically
if used_points == 0:
    print("No coupon")
for name, usage in sorted(coupons_usage.items()):
    print(name, usage)
```
