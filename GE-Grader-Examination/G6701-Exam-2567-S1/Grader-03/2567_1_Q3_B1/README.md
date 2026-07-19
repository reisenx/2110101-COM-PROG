<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Generations ★★ (
      <a href="https://drive.google.com/file/d/1bOT4kKkTAf6p6lZ0D9E3ZAFUwL9Drklp/view?usp=sharing">
        <code>2567_1_Q3_B1</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การแบ่งกลุ่มตามปีเกิด**](#การแบ่งกลุ่มตามปีเกิด)
-   [**การเรียงจากอายุน้อยไปมาก**](#การเรียงจากอายุน้อยไปมาก)
-   [**การตอบคำถามและรูปแบบผลลัพธ์**](#การตอบคำถามและรูปแบบผลลัพธ์)
-   [**ข้อแตกต่างด้านเครื่องหมาย colon**](#ข้อแตกต่างด้านเครื่องหมาย-colon)
-   [**Solution**](#solution)

---

## การแบ่งกลุ่มตามปีเกิด

โปรแกรมกำหนดช่วงปีของแต่ละ generation ไว้ใน `GEN_INFO`

| ชื่อย่อ | ช่วงปีเกิด พ.ศ. |
|:---:|:---:|
| `S` | 2468–2488 |
| `B` | 2489–2507 |
| `X` | 2508–2523 |
| `Y` | 2524–2539 |
| `Z` | 2540–2555 |
| `A` | ตั้งแต่ 2556 เป็นต้นไป |

โปรแกรมอ่านข้อมูลทีละบรรทัดจนพบ `-1` แล้วแยกวันที่รูปแบบ
`dd/mm/yyyy` เป็นวัน เดือน และปี

```python
birth_day, birth_month, birth_year = [int(num) for num in birth_date.split("/")]
```

จากนั้นตรวจว่าปีเกิดอยู่ในช่วงใด และเก็บ tuple
`(birth_year, birth_month, birth_day, name)` ลงในรายการของกลุ่มนั้น
การเก็บปีไว้ก่อนช่วยให้ Python เปรียบเทียบวันเกิดตามลำดับ ปี → เดือน → วัน
ได้โดยตรง

---

## การเรียงจากอายุน้อยไปมาก

คนอายุน้อยกว่าเกิดวันที่ใหม่กว่า เช่นผู้ที่เกิดปี `2540` อายุน้อยกว่าผู้ที่เกิดปี
`2530` ดังนั้นการเรียงวันเกิดจากค่ามากไปน้อยจะเท่ากับเรียงอายุจากน้อยไปมาก

```python
people.sort(reverse=True)
```

tuple จะถูกเทียบจากสมาชิกซ้ายไปขวา จึงเรียงปี เดือน และวันครบถ้วน
โจทย์รับประกันว่าไม่มีสองคนที่อายุเท่ากัน จึงไม่ต้องกำหนดวิธีตัดสินกรณีวันเกิดซ้ำ

---

## การตอบคำถามและรูปแบบผลลัพธ์

หลังรับจำนวนคำถาม `n` โปรแกรมเก็บชื่อย่อทั้ง `n` บรรทัดไว้
แล้วตอบตามลำดับที่ได้รับ

-   ถ้ากลุ่มมีคนอยู่ นำเฉพาะชื่อมาเชื่อมด้วยช่องว่าง
-   ถ้ากลุ่มว่างหรือชื่อย่อไม่อยู่ใน dictionary แสดง `Not found`

ตัวอย่างรูปแบบที่โค้ดสร้างจริงคือ

```text
Y: Urassaya Nadech Ranee
X: Not found
```

---

## ข้อแตกต่างด้านเครื่องหมาย colon

> [!WARNING]
>
> PDF แสดงรูปแบบเป็น `S : Buffet` ซึ่งมีช่องว่างทั้งก่อนและหลัง `:`
> แต่โค้ดต้นฉบับใช้ `f"{gen_name}: ..."` จึงแสดง `S: Buffet`
> โดยไม่มีช่องว่างก่อน `:` Solution ด้านล่างคงพฤติกรรมของไฟล์ `.py` ไว้ตามเดิม

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_1_Q3_B1.py
# Problem   : Generations
# Author    : Worralop Srichainont
# Date      : 2025-07-28
# --------------------------------------------------

# Generations information about name, start year, and end year
GEN_INFO = (
    ("S", 2468, 2488),
    ("B", 2489, 2507),
    ("X", 2508, 2523),
    ("Y", 2524, 2539),
    ("Z", 2540, 2555),
    ("A", 2556, 9999),
)

# Dictionary to hold people by generation
GEN_PEOPLE = {"S": [], "B": [], "X": [], "Y": [], "Z": [], "A": []}

while True:
    # Input each line of data
    data = input().strip()
    # Stop, if the input is "-1"
    if data == "-1":
        break

    # Extract name, birth day, month, and year
    name, birth_date = data.split()
    birth_day, birth_month, birth_year = [int(num) for num in birth_date.split("/")]

    # Create a tuple with birth year, month, day, and name
    info = (birth_year, birth_month, birth_day, name)

    # Determine the generation based on the birth year and add to the corresponding list
    for gen_name, start_year, end_year in GEN_INFO:
        if start_year <= birth_year <= end_year:
            GEN_PEOPLE[gen_name].append(info)

# Sort each generation's people by age in ascending order
# which means sorting by birth date in descending order
for _, people in GEN_PEOPLE.items():
    people.sort(reverse=True)

# Input query of generation names
n = int(input())
query_gen = []
for _ in range(n):
    query_gen.append(input().strip())

# Iterate through each queried generation name
for gen_name in query_gen:
    # If the generation exists and has people
    if gen_name in GEN_PEOPLE and len(GEN_PEOPLE[gen_name]) > 0:
        # Get the names of people in that generation
        names = []
        for _, _, _, name in GEN_PEOPLE[gen_name]:
            names.append(name)
        # Output the generation name and names
        print(f"{gen_name}: {' '.join(names)}")

    # If the generation does not exist or has no people
    else:
        print(f"{gen_name}: Not found")
```
