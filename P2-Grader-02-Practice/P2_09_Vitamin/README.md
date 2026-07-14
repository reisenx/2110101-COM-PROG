<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Vitamin ★★★ (
      <a href="https://drive.google.com/file/d/1Ii96AFOhIT41F2HvPDy6QUoS0mqEmHNs/view?usp=drive_link">
        <code>P2_09_Vitamin</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**รูปแบบข้อมูลและโครงสร้างที่ใช้**](#รูปแบบข้อมูลและโครงสร้างที่ใช้)
-   [**เลือกวิตามินด้วยดัชนี**](#เลือกวิตามินด้วยดัชนี)
-   [**คำสั่ง show และ get**](#คำสั่ง-show-และ-get)
-   [**คำสั่ง avg**](#คำสั่ง-avg)
-   [**คำสั่ง max**](#คำสั่ง-max)
-   [**คำสั่ง sort**](#คำสั่ง-sort)
-   [**รูปแบบการแสดงผลและกรณีสำคัญ**](#รูปแบบการแสดงผลและกรณีสำคัญ)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## รูปแบบข้อมูลและโครงสร้างที่ใช้

บรรทัดแรกของข้อมูลเป็นจำนวนเต็มบวก `n` ซึ่งบอกจำนวนชนิดของผลไม้
จากนั้นมีข้อมูลผลไม้ `n` บรรทัด แต่ละบรรทัดประกอบด้วยชื่อผลไม้
ตามด้วยปริมาณวิตามินชนิดที่ 1, 2, 3, ... ซึ่งเป็นจำนวนจริง

ผลไม้ทุกชนิดมีจำนวนค่าวิตามินเท่ากัน ตัวอย่างเช่น

```text
apple 0.005 0.06 0.01
```

หมายถึง `apple` มีปริมาณวิตามินชนิดที่ 1, 2 และ 3 เท่ากับ `0.005`,
`0.06` และ `0.01` ตามลำดับ

โปรแกรมจัดเก็บข้อมูลในดิกชันนารี `all_fruits` โดยใช้ชื่อผลไม้เป็น key
และใช้ลิสต์ของจำนวนจริงเป็น value

```python
data = input().strip().split()
fruit = data[0]
vitamins = [float(percent) for percent in data[1:]]
all_fruits[fruit] = vitamins
```

`split()` แยกข้อมูลด้วยช่องว่าง `data[0]` จึงเป็นชื่อผลไม้
ส่วน `data[1:]` เป็นค่าปริมาณทั้งหมด list comprehension จะแปลงแต่ละค่า
จากสตริงเป็น `float` ก่อนเก็บลงในลิสต์

โครงสร้างที่ได้มีลักษณะดังนี้

```python
{
    "apricots": [0.2, 0.06],
    "apple": [0.005, 0.06],
    "banana": [0.008, 0.04],
}
```

ดิกชันนารีของ Python เก็บลำดับการเพิ่ม key ทำให้การวน `all_fruits.items()`
สามารถแสดงผลไม้ตามลำดับที่อ่านเข้ามาได้ตามที่คำสั่ง `show` ต้องการ

หลังจากอ่านผลไม้ครบ `n` บรรทัด โปรแกรมอ่านคำสั่งบรรทัดสุดท้าย
แล้วแยกชื่อคำสั่งกับอาร์กิวเมนต์ด้วย `split()` อีกครั้ง

---

## เลือกวิตามินด้วยดัชนี

โจทย์เรียกชนิดวิตามินด้วยหมายเลขเริ่มจาก 1 แต่ตำแหน่งของลิสต์ใน Python
เริ่มจาก 0 ดังนั้นคำสั่งที่มีหมายเลขวิตามิน `m` ต้องแปลงตำแหน่งด้วย

\[
\text{index} = m - 1
\]

ซึ่งเขียนใน Python เป็น

```python
idx = int(cmd[1]) - 1
```

ตัวอย่างเช่น คำสั่ง `avg 2` มี `cmd[1] == "2"` จึงได้ `idx == 1`
และเข้าถึงวิตามินชนิดที่ 2 ของผลไม้หนึ่งชนิดด้วย `vitamins[idx]`

โจทย์รับประกันว่า `m` อยู่ในช่วงที่ถูกต้อง จึงไม่ต้องตรวจว่า `idx`
เกินขอบเขตของลิสต์หรือไม่

---

## คำสั่ง show และ get

### คำสั่ง `show`

คำสั่ง `show` ต้องแสดงข้อมูลผลไม้ทุกชนิดตามลำดับที่อ่านเข้ามา
โปรแกรมจึงวนผ่านคู่ `fruit, vitamins` ในดิกชันนารี

```python
for fruit, vitamins in all_fruits.items():
    print(f"{fruit} {' '.join([str(percent) for percent in vitamins])}")
```

ค่าปริมาณเป็น `float` จึงต้องแปลงกลับเป็นสตริงด้วย `str()`
แล้วใช้ `' '.join(...)` เชื่อมทุกค่าด้วยช่องว่างหนึ่งช่อง
`print()` หนึ่งครั้งต่อผลไม้หนึ่งชนิดทำให้ผลไม้แต่ละชนิดอยู่คนละบรรทัด

### คำสั่ง `get ชื่อผลไม้`

คำสั่ง `get` แสดงข้อมูลเพียงผลไม้ที่ระบุ โปรแกรมใช้
`if fruit in all_fruits` ตรวจว่าชื่อนั้นเป็น key ในดิกชันนารีหรือไม่

-   ถ้าพบ แสดงชื่อและปริมาณวิตามินทั้งหมดในรูปแบบเดียวกับ `show`
-   ถ้าไม่พบ แสดง `<ชื่อผลไม้> not found`

การเปรียบเทียบสตริงใน Python แยกตัวอักษรใหญ่และเล็ก
ดังนั้น `Durian`, `durian` และ `DURIAN` ถือเป็นคนละชื่อกัน

---

## คำสั่ง avg

คำสั่ง `avg m` ต้องหาค่าเฉลี่ยของวิตามินชนิดที่ `m` จากผลไม้ทุกชนิด
โปรแกรมรวบรวม `vitamins[idx]` ของแต่ละผลไม้ลงใน `percentages`

ถ้ามีผลไม้ทั้งหมด \(n\) ชนิด และปริมาณวิตามินชนิดที่ \(m\)
ของแต่ละชนิดคือ \(x_{1,m}, x_{2,m}, \ldots, x_{n,m}\) ค่าเฉลี่ยคือ

\[
\bar{x}_m = \frac{x_{1,m} + x_{2,m} + \cdots + x_{n,m}}{n}
\]

สูตรเดียวกันเขียนใน Python ได้เป็น

```python
sum(percentages) / len(percentages)
```

ก่อนแสดงผล โปรแกรมปัดเศษทศนิยมด้วย

```python
round(sum(percentages) / len(percentages), 4)
```

เช่น วิตามินชนิดที่ 1 มีค่า `0.2`, `0.005` และ `0.008`

\[
\frac{0.2 + 0.005 + 0.008}{3} = 0.071
\]

จึงแสดง `0.071`

---

## คำสั่ง max

คำสั่ง `max m` ต้องแสดงชื่อผลไม้ที่มีวิตามินชนิดที่ `m` มากที่สุด
และแสดงปริมาณสูงสุดนั้นด้วย ถ้ามีค่าสูงสุดเท่ากันหลายชนิด
ต้องเลือกชื่อที่มาก่อนตามลำดับพจนานุกรม

โปรแกรมสร้างลิสต์ย่อยในรูปแบบ

```python
[-vitamins[idx], fruit]
```

จากนั้นใช้ `sort()` ซึ่งเปรียบเทียบสมาชิกตำแหน่งแรกก่อน
และเปรียบเทียบชื่อตำแหน่งที่สองเมื่อค่าตำแหน่งแรกเท่ากัน

การใส่เครื่องหมายลบทำให้ปริมาณที่มากกว่ากลายเป็นจำนวนที่น้อยกว่า
จึงขึ้นมาอยู่หน้าสุดเมื่อเรียงจากน้อยไปมาก เช่น

| ผลไม้ | ปริมาณเดิม | ข้อมูลที่ใช้เรียง |
|---|---:|---|
| `apricots` | `0.06` | `[-0.06, "apricots"]` |
| `apple` | `0.06` | `[-0.06, "apple"]` |
| `banana` | `0.04` | `[-0.04, "banana"]` |

`apple` และ `apricots` มีค่าเท่ากัน แต่ `apple` มาก่อนตามลำดับชื่อ
จึงเป็นสมาชิกแรกหลังเรียง และได้ผลลัพธ์ `apple 0.06`

เมื่อเลือกสมาชิกแรกแล้ว โปรแกรมนำเครื่องหมายลบออกอีกครั้งด้วย
`-vitamin_ranks[0][0]` เพื่อให้ปริมาณที่แสดงกลับเป็นค่าเดิม

---

## คำสั่ง sort

คำสั่ง `sort m` ต้องแสดงเฉพาะชื่อผลไม้ เรียงตามปริมาณวิตามินชนิดที่ `m`
จากน้อยไปมาก ถ้าปริมาณเท่ากันจึงเรียงชื่อตามลำดับพจนานุกรม

กรณีนี้สร้างข้อมูลสำหรับเรียงโดยไม่ต้องเปลี่ยนเครื่องหมาย

```python
vitamin_ranks.append([vitamins[idx], fruit])
vitamin_ranks.sort()
```

`sort()` จะเรียงตามปริมาณในตำแหน่งแรกจากน้อยไปมากโดยตรง
และใช้ชื่อในตำแหน่งที่สองตัดสินกรณีที่ปริมาณเท่ากัน

หลังเรียงแล้ว โปรแกรมดึงชื่อผลไม้ตามลำดับมาใส่ใน `result`
และเชื่อมชื่อทั้งหมดด้วยช่องว่างหนึ่งช่อง

```python
print(" ".join(result))
```

ตัวอย่างเช่น ปริมาณวิตามินชนิดที่ 4 ของ `banana`, `apple` และ `apricots`
คือ `0.01`, `0.05` และ `0.05` ตามลำดับ ผลลัพธ์จึงเป็น
`banana apple apricots`

---

## รูปแบบการแสดงผลและกรณีสำคัญ

แต่ละคำสั่งมีรูปแบบผลลัพธ์ต่างกัน

-   `show` แสดงผลไม้ทุกชนิด บรรทัดละหนึ่งชนิด ตามลำดับอินพุต
-   `get` แสดงข้อมูลผลไม้หนึ่งบรรทัด หรือแสดง `<ชื่อ> not found`
-   `avg` แสดงค่าเฉลี่ยที่ผ่าน `round(..., 4)` หนึ่งค่า
-   `max` แสดงชื่อผลไม้ ตามด้วยปริมาณสูงสุด
-   `sort` แสดงชื่อผลไม้ทั้งหมดในบรรทัดเดียว คั่นด้วยช่องว่าง

เนื่องจากโปรแกรมแปลงปริมาณเป็น `float` แล้วแสดงด้วย `str()`
รูปแบบอาจไม่เหมือนข้อความอินพุตทุกตัว เช่น `0.200` จะแสดงเป็น `0.2`
แต่ค่าทางตัวเลขยังเท่ากัน

> [!NOTE]
>
> `round(value, 4)` หมายถึงปัดให้เหลือ **ไม่เกิน** 4 ตำแหน่งหลังจุดทศนิยม
> ไม่ได้บังคับให้แสดงครบ 4 ตำแหน่ง จึงอาจได้ `0.071` แทน `0.0710`

กรณีที่ควรตรวจเป็นพิเศษคือชื่อผลไม้ที่ตัวพิมพ์ไม่ตรงกัน
ค่าสูงสุดที่เสมอกัน และค่าที่ใช้ `sort` เท่ากัน เพราะแต่ละกรณีมีเกณฑ์
เลือกหรือลำดับผลลัพธ์ที่ชัดเจน

---

## ตัวอย่างการทำงาน

สมมติว่าอ่านข้อมูลต่อไปนี้

```text
3
apricots 0.2 0.06 0.05 0.05
apple 0.005 0.06 0.01 0.05
banana 0.008 0.04 0.03 0.01
```

ถ้าบรรทัดสุดท้ายเป็น `show` จะได้

```text
apricots 0.2 0.06 0.05 0.05
apple 0.005 0.06 0.01 0.05
banana 0.008 0.04 0.03 0.01
```

ตัวอย่างคำสั่งอื่นกับข้อมูลชุดนี้คือ

| คำสั่ง | ผลลัพธ์ | เหตุผลสำคัญ |
|---|---|---|
| `get banana` | `banana 0.008 0.04 0.03 0.01` | พบ key ที่ชื่อตรงกัน |
| `avg 1` | `0.071` | ค่าเฉลี่ยของวิตามินชนิดที่ 1 |
| `max 2` | `apple 0.06` | ค่าสูงสุดเสมอกัน จึงเลือกชื่อที่มาก่อน |
| `sort 4` | `banana apple apricots` | เรียงค่า แล้วใช้ชื่อตัดสินค่าที่เสมอกัน |

แต่ถ้าสั่ง `get Durian` จะได้ `Durian not found`
เพราะไม่มี key ที่มีตัวพิมพ์ตรงกับ `Durian`

---

# Solution

```python
# --------------------------------------------------
# File Name : P2_09_Vitamin.py
# Problem   : Part-II Vitamin
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# Initialize the fruit dictionary
all_fruits = {}

# Input fruit information
n = int(input())
for _ in range(n):
    data = input().strip().split()
    fruit = data[0]
    vitamins = [float(percent) for percent in data[1:]]
    all_fruits[fruit] = vitamins

# Input the command
cmd = input().strip().split()

# Command: show
# Output all fruits with their vitamin percentages in the order of input
if cmd[0] == "show":
    for fruit, vitamins in all_fruits.items():
        print(f"{fruit} {' '.join([str(percent) for percent in vitamins])}")

# Command: get
# Output the vitamin percentages of a specific fruit
elif cmd[0] == "get":
    fruit = cmd[1]
    # Check if the fruit exists in the dictionary
    if fruit in all_fruits:
        vitamins = all_fruits[fruit]
        print(f"{fruit} {' '.join([str(percent) for percent in vitamins])}")
    # If the fruit does not exist, output "not found"
    else:
        print(f"{fruit} not found")

# Command: avg
# Output the average percentage of a specific vitamin across all fruits
elif cmd[0] == "avg":
    idx = int(cmd[1]) - 1
    # Get all vitamin percentages for the specified index
    percentages = []
    for _, vitamins in all_fruits.items():
        percentages.append(vitamins[idx])
    # Calculate and print the average percentage
    print(round(sum(percentages) / len(percentages), 4))

# Command: max
# Output the fruit with the maximum percentage of a specific vitamin
elif cmd[0] == "max":
    idx = int(cmd[1]) - 1
    # Create a list of fruits with their vitamin percentages for sorting
    vitamin_ranks = []
    for fruit, vitamins in all_fruits.items():
        vitamin_ranks.append([-vitamins[idx], fruit])
    # Sort the list by vitamin percentage (descending) and fruit name (ascending)
    vitamin_ranks.sort()

    # Output the fruit with the maximum percentage
    max_fruit = vitamin_ranks[0][1]
    max_percentage = -vitamin_ranks[0][0]
    print(f"{max_fruit} {max_percentage}")

# Command: sort
# Output all fruits sorted by a specific vitamin percentage
elif cmd[0] == "sort":
    idx = int(cmd[1]) - 1
    # Create a list of fruits with their vitamin percentages for sorting
    vitamin_ranks = []
    for fruit, vitamins in all_fruits.items():
        vitamin_ranks.append([vitamins[idx], fruit])
    # Sort the list by vitamin percentage (ascending) and fruit name (ascending)
    vitamin_ranks.sort()

    # Output the sorted fruits
    result = []
    for _, fruit in vitamin_ranks:
        result.append(fruit)
    print(" ".join(result))
```
