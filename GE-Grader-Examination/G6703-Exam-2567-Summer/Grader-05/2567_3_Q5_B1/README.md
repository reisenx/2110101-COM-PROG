<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Least Common Animals ★★ (
      <a href="https://drive.google.com/file/d/1Q02DPgZGhBLSBO2v77qX7kNRvZI2Sisn/view?usp=sharing">
        <code>2567_3_Q5_B1</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**จัดกลุ่มสัตว์ตามจำนวน**](#จัดกลุ่มสัตว์ตามจำนวน)
-   [**เรียงจากน้อยไปมาก**](#เรียงจากน้อยไปมาก)
-   [**การนับอันดับเมื่อมีค่าเท่ากัน**](#การนับอันดับเมื่อมีค่าเท่ากัน)
-   [**Solution**](#solution)

---

## จัดกลุ่มสัตว์ตามจำนวน

บรรทัดแรกรับจำนวนชนิดสัตว์ `M` และจำนวนอันดับที่ต้องการแสดง `N`

```python
animal_amount, ranking_display_limit = [int(num) for num in input().split()]
```

อีก `M` บรรทัด แต่ละบรรทัดประกอบด้วยชื่อสัตว์และจำนวน เช่น `cobra 2`
เนื่องจากสัตว์หลายชนิดอาจมีจำนวนเท่ากัน โค้ดใช้จำนวนสัตว์เป็น key ของ
dictionary และเก็บชื่อทั้งหมดที่มีจำนวนนั้นไว้ในลิสต์

```python
if animal_count not in animal_ranking:
    animal_ranking[animal_count] = []
animal_ranking[animal_count].append(animal_name)
```

ตัวอย่างเช่น `cobra 2` และ `elephant 2` จะอยู่ในกลุ่มเดียวกัน

---

## เรียงจากน้อยไปมาก

โจทย์ต้องการสัตว์ที่มีจำนวนน้อยที่สุดก่อน จึงเรียงคู่
`(animal_count, animal_names)` ด้วย

```python
for animal_count, animal_names in sorted(animal_ranking.items()):
```

`sorted()` จะเรียง key ที่เป็นจำนวนจากน้อยไปมาก ภายในกลุ่มเดียวกันเรียงชื่อ
ตามพจนานุกรมอีกครั้งด้วย `sorted(animal_names)` แล้วแสดงชื่อกับจำนวนทีละบรรทัด

ดังนั้นข้อมูล `deer 3`, `elephant 2`, `cobra 2` จะเรียงเป็น

```text
cobra 2
elephant 2
deer 3
```

> [!NOTE]
>
> คำอธิบายตัวอย่างบางจุดใน PDF พิมพ์จำนวนของ `deer` เป็น `2` แต่ข้อมูลนำเข้า
> ระบุ `deer 3` และโปรแกรมใช้ค่าจากข้อมูลนำเข้าจริง จึงแสดง `deer 3`

---

## การนับอันดับเมื่อมีค่าเท่ากัน

ตัวแปร `ranking_display_limit` เริ่มจาก `N` เมื่อกำลังจะแสดงกลุ่มหนึ่ง
โปรแกรมลดค่าด้วยจำนวนชื่อทั้งหมดในกลุ่ม

```python
ranking_display_limit -= len(animal_names)
```

จากนั้นแสดง **ทุกชื่อในกลุ่มนั้น** แม้ค่าคงเหลือจะติดลบ วิธีนี้ทำให้สัตว์ที่มี
จำนวนเท่ากับลำดับที่ `N` ถูกแสดงครบทุกชนิด

ตัวอย่าง หาก `N = 4` และก่อนถึงกลุ่มจำนวน `4` แสดงไปแล้วสามชื่อ
กลุ่ม `leopard 4` กับ `orangutan 4` จะถูกแสดงทั้งคู่ ทำให้ผลลัพธ์มีห้าบรรทัด
ได้ตามเงื่อนไขโจทย์ ลูปจะหยุดก่อนเริ่มกลุ่มถัดไปเมื่อค่าคงเหลือ `<= 0`

หากมีสัตว์น้อยกว่า `N` ชนิด โปรแกรมจะวนครบทุกกลุ่มและแสดงเท่าที่มี

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_3_Q5_B1.py
# Problem   : Least Common Animals
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Input animal amount and ranking display limit
animal_amount, ranking_display_limit = [int(num) for num in input().split()]

# Input animal name and its count, then store them in a dictionary based on count
animal_ranking = {}
for _ in range(animal_amount):
    # Extract animal name and count from input
    data = input().split()
    animal_name = data[0]
    animal_count = int(data[1])

    # Store the animal name in the dictionary based on its count
    if animal_count not in animal_ranking:
        animal_ranking[animal_count] = []
    animal_ranking[animal_count].append(animal_name)

# Output the animal names sorted by count and name in ascending order
for animal_count, animal_names in sorted(animal_ranking.items()):
    # Stop if the ranking display limit is reached
    if ranking_display_limit <= 0:
        break

    # Decrease the ranking display limit by the number of animal names on this count
    ranking_display_limit -= len(animal_names)

    # Sort animal names alphabetically and print them
    for animal_name in sorted(animal_names):
        print(animal_name, animal_count)
```
