<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Group Stage ★★ (
      <a href="https://drive.google.com/file/d/1F26AfX7ZdT7tbOQrNPDPe9K53HqM6b1w/view?usp=sharing">
        <code>2565_1_Q3_01</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเก็บข้อมูลทีมด้วย Dictionary**](#การเก็บข้อมูลทีมด้วย-dictionary)
-   [**การตรวจประเทศซ้ำด้วย Set**](#การตรวจประเทศซ้ำด้วย-set)
-   [**การรับข้อมูลหลายกลุ่มจนพบ q**](#การรับข้อมูลหลายกลุ่มจนพบ-q)
-   [**ลำดับการทำงาน**](#ลำดับการทำงาน)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ข้อควรระวัง**](#ข้อควรระวัง)
-   [**Solution**](#solution)

---

## การเก็บข้อมูลทีมด้วย Dictionary

ก่อนตรวจแต่ละกลุ่ม เราต้องตอบให้ได้อย่างรวดเร็วว่าแต่ละทีมมาจากประเทศใด
จึงใช้ `dictionary` เก็บชื่อทีมเป็น key และชื่อประเทศเป็น value

```python
teams_country = {}
teams_country[team] = country
```

ตัวอย่างเช่น เมื่อเก็บ `"Liverpool"` คู่กับ `"England"`
เราสามารถอ่านชื่อประเทศกลับมาได้ด้วย `teams_country["Liverpool"]`

โปรแกรมรับจำนวนทีม `n` ก่อน แล้วทำซ้ำ `n` รอบ

```python
n = int(input())
for _ in range(n):
    team, country = input().split()
    teams_country[team] = country
```

แต่ละบรรทัดจึงต้องมีชื่อทีมและชื่อประเทศอย่างละหนึ่งคำ คั่นด้วยช่องว่าง

---

## การตรวจประเทศซ้ำด้วย Set

กฎของโจทย์กำหนดว่า ทีมทุกทีมในกลุ่มเดียวกันต้องมาจากคนละประเทศ
เราจึงใช้ `set` เก็บประเทศที่พบ เพราะสมาชิกที่มีค่าเหมือนกันจะถูกเก็บเพียงครั้งเดียว

ให้ `G` เป็นรายการทีมในกลุ่ม และให้ `D(t)` เป็นประเทศของทีม `t`
เซตประเทศของกลุ่มคือ

$$
C = \{D(t) \mid t \in G\}
$$

ใน Python การเพิ่มประเทศของแต่ละทีมลงในเซตเขียนได้ดังนี้

```python
countries = set()
countries.add(teams_country[team])
```

ถ้าทุกทีมมาจากคนละประเทศ จำนวนประเทศใน `countries` จะเท่ากับจำนวนทีมใน
`group`

$$
\text{กลุ่มถูกกฎ} \iff |C| = |G|
$$

ซึ่งตรงกับเงื่อนไขในโปรแกรม

```python
if len(countries) == len(group):
    print("OK")
else:
    print("Not OK")
```

ตัวอย่างเช่น `Barcelona` และ `Real` มาจาก `Spain` เหมือนกัน
แม้ `group` จะมี 2 ทีม แต่ `countries` จะมีสมาชิกเพียง 1 ประเทศ
จึงต้องแสดง `Not OK`

---

## การรับข้อมูลหลายกลุ่มจนพบ q

โจทย์ไม่ได้บอกจำนวนกลุ่มล่วงหน้า โปรแกรมจึงใช้ `while True`
รับข้อมูลทีละบรรทัดไปเรื่อย ๆ

```python
group = input().strip().split()
if group == ["q"]:
    break
```

`split()` แยกชื่อทีมตามช่องว่างและคืนค่าเป็น list เช่น
`"Liverpool Dortmund Milan Ajax"` จะกลายเป็น
`["Liverpool", "Dortmund", "Milan", "Ajax"]`

โปรแกรมจะหยุดก็ต่อเมื่อบรรทัดนั้นมีเพียง `q` ตัวเล็กหนึ่งตัวเท่านั้น
และจะไม่แสดงผลสำหรับบรรทัด `q`

ถ้าพบชื่อทีมที่ไม่มีอยู่ใน `teams_country` โปรแกรมจะ `break`
ออกจากลูปที่ตรวจทีมในกลุ่มทันที

```python
if team not in teams_country:
    break
```

เมื่อหยุดก่อนตรวจครบทุกทีม จำนวนประเทศที่เก็บได้จะน้อยกว่า
`len(group)` เสมอ เงื่อนไขตรวจจำนวนจึงให้ผลเป็น `Not OK`
ตามข้อกำหนดของโจทย์

---

## ลำดับการทำงาน

1. รับ `n` และสร้าง `teams_country` จากข้อมูลทีม `n` บรรทัด
2. รับรายชื่อทีมหนึ่งกลุ่มด้วย `input().strip().split()`
3. ถ้าได้ `['q']` ให้จบการทำงาน
4. สร้าง `countries` เป็นเซตว่าง
5. ตรวจทีมตามลำดับ ถ้าทีมไม่อยู่ใน dictionary ให้หยุดตรวจกลุ่มนั้น
6. เพิ่มประเทศของทีมที่รู้จักลงใน `countries`
7. เปรียบเทียบ `len(countries)` กับ `len(group)` แล้วแสดง `OK` หรือ
   `Not OK`
8. กลับไปรับกลุ่มถัดไป

---

## ตัวอย่างการทำงาน

สมมติว่ามีข้อมูลทีมดังนี้

```text
A Thailand
B Japan
C Thailand
```

-   กลุ่ม `A B` ได้เซตประเทศ `{Thailand, Japan}` ซึ่งมี 2 ประเทศสำหรับ 2 ทีม
    จึงแสดง `OK`
-   กลุ่ม `A C` ได้เซตประเทศ `{Thailand}` เพียง 1 ประเทศสำหรับ 2 ทีม
    จึงแสดง `Not OK`
-   กลุ่ม `A Unknown` พบทีมที่ไม่รู้จัก จึงแสดง `Not OK`

ผลลัพธ์เรียงตามลำดับกลุ่มที่รับเข้ามา

```text
OK
Not OK
Not OK
```

---

## ข้อควรระวัง

-   ข้อความผลลัพธ์ต้องตรงตัวพิมพ์ทุกตัว คือ `OK` และ `Not OK`
-   การใส่ทีมเดิมซ้ำในกลุ่มก็ทำให้ผิดกฎ เพราะทั้งสองตำแหน่งมาจากประเทศเดียวกัน
-   บรรทัดว่างไม่ได้เป็นข้อมูลตามเงื่อนไขโจทย์ แม้โค้ดจะอ่านเป็น list ว่างได้

---

# Solution

```python
# --------------------------------------------------
# File Name : 2565_1_Q3_01.py
# Problem   : Group Stage
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

# Input teams and their country and store them in a dictionary
teams_country = {}
n = int(input())
for _ in range(n):
    team, country = input().split()
    teams_country[team] = country

# Input groups of teams and check if all teams in a group are from different countries
while True:
    # Input a group of teams or 'q' to quit
    group = input().strip().split()
    if group == ["q"]:
        break

    # Create a set to store unique countries in the group
    countries = set()
    for team in group:
        # Stop if a team is does not exist in the teams_country dictionary
        if team not in teams_country:
            break
        countries.add(teams_country[team])

    # Check if all teams in the group are from different countries
    if len(countries) == len(group):
        print("OK")
    else:
        print("Not OK")
```
