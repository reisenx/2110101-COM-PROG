<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    APEC Headache ★★★★ (
      <a href="https://drive.google.com/file/d/1SPMt7LOB8ThKCUKVqYJX3_a5lpx71_bv/view?usp=sharing">
        <code>2565_1_Q3_03</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเก็บความสัมพันธ์ด้วย Dictionary ของ Set**](#การเก็บความสัมพันธ์ด้วย-dictionary-ของ-set)
-   [**การเพิ่มพันธมิตรและคู่สงคราม**](#การเพิ่มพันธมิตรและคู่สงคราม)
-   [**การขยายความเป็นศัตรูตามกฎ**](#การขยายความเป็นศัตรูตามกฎ)
-   [**การตรวจที่นั่งรอบโต๊ะกลม**](#การตรวจที่นั่งรอบโต๊ะกลม)
-   [**การประมวลผลคำสั่ง**](#การประมวลผลคำสั่ง)
-   [**ลำดับการทำงาน**](#ลำดับการทำงาน)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ข้อควรระวัง**](#ข้อควรระวัง)
-   [**Solution**](#solution)

---

## การเก็บความสัมพันธ์ด้วย Dictionary ของ Set

ประเทศหนึ่งประเทศอาจมีพันธมิตรและคู่สงครามได้หลายประเทศ
โปรแกรมจึงใช้ dictionary 2 ตัว โดยให้ชื่อประเทศเป็น key และใช้ `set`
เก็บประเทศที่มีความสัมพันธ์ด้วย

```python
allies = {}
enemies = {}
```

ตัวอย่างเช่น ถ้า `allies["A"]` มีค่า `{"B", "C"}` หมายความว่า
`B` และ `C` เป็นพันธมิตรของ `A`

ประเทศอาจปรากฏครั้งแรกในคำสั่ง `Ally`, `Enemy` หรือ `Table` ก็ได้
ฟังก์ชัน `init_countries()` จึงเตรียมเซตว่างเฉพาะประเทศที่ยังไม่เคยพบ

```python
if country not in allies:
    allies[country] = set()
if country not in enemies:
    enemies[country] = set()
```

การตรวจด้วย `if` ทำให้ข้อมูลความสัมพันธ์เดิมไม่ถูกลบเมื่อชื่อประเทศนั้น
ปรากฏในคำสั่งบรรทัดใหม่

---

## การเพิ่มพันธมิตรและคู่สงคราม

ให้ `L` เป็นเซตของประเทศทั้งหมดที่ตามหลังคำสั่ง และให้ `c` เป็นประเทศหนึ่งใน
`L` ประเทศอื่นในบรรทัดเดียวกันคือ

$$
L - \{c\}
$$

### คำสั่ง Ally

ทุกประเทศในบรรทัด `Ally` เป็นพันธมิตรซึ่งกันและกัน
สำหรับแต่ละประเทศ `c` โปรแกรมจึงปรับเซตพันธมิตรเป็น

$$
A(c) \leftarrow A(c) \cup (L - \{c\})
$$

Python ใช้ `set(countries) - {country}` ตัดประเทศตัวเองออก และใช้ `|=`
รวมสมาชิกใหม่เข้ากับเซตเดิม

```python
allies[country] |= set(countries) - {country}
```

ตัวอย่างเช่น `Ally A B C` จะทำให้ `A` มีพันธมิตร `B`, `C`
และสร้างความสัมพันธ์ในทิศทางกลับกันให้ครบทุกคู่ด้วย

### คำสั่ง Enemy

Solution ใช้หลักเดียวกันกับรายชื่อหลังคำสั่ง `Enemy`

$$
E(c) \leftarrow E(c) \cup (L - \{c\})
$$

```python
enemies[country] |= set(countries) - {country}
```

ดังนั้น ถ้ามีชื่อมากกว่า 2 ประเทศในบรรทัด `Enemy`
โค้ดจะถือว่าทุกประเทศในบรรทัดเป็นคู่สงครามกันทุกคู่
ส่วนตัวอย่างในโจทย์ใช้ประเทศครั้งละ 2 ประเทศ

---

## การขยายความเป็นศัตรูตามกฎ

ก่อนตรวจโต๊ะ โปรแกรมเรียก `add_more_enemies()` เพื่อเพิ่มความเป็นศัตรูที่อนุมาน
ได้จากพันธมิตร ตามกฎ 2 ข้อของโจทย์

### พันธมิตรของศัตรูคือศัตรู

ถ้า `e` เป็นศัตรูของ `c` พันธมิตรทุกประเทศของ `e` ต้องเป็นศัตรูของ `c` ด้วย

$$
E(c) \leftarrow E(c) \cup \bigcup_{e \in E(c)} A(e)
$$

โค้ดรวมพันธมิตรของศัตรูทุกคนไว้ใน `allies_of_enemies`
แล้วเพิ่มลงใน `enemies[country]`

```python
allies_of_enemies = set()
for enemy in enemy_countries:
    allies_of_enemies |= allies[enemy]
enemies[country] |= allies_of_enemies
```

### ศัตรูของพันธมิตรคือศัตรู

ถ้า `a` เป็นพันธมิตรของ `c` ศัตรูทุกประเทศของ `a` ต้องเป็นศัตรูของ `c` ด้วย

$$
E(c) \leftarrow E(c) \cup \bigcup_{a \in A(c)} E(a)
$$

Python เขียนได้ดังนี้

```python
enemies_of_allies = set()
for ally in ally_countries:
    enemies_of_allies |= enemies[ally]
enemies[country] |= enemies_of_allies
```

ทั้งสองขั้นใช้ `|=` จึงเพิ่มข้อมูลลงในเซตเดิม และไม่ลบคู่สงครามที่เคยมีอยู่
โปรแกรมไม่สรุปว่าศัตรูของศัตรูต้องเป็นพันธมิตร เพราะโจทย์ระบุว่าไม่จำเป็น

---

## การตรวจที่นั่งรอบโต๊ะกลม

รายชื่อหลังคำสั่ง `Table` เรียงตามตำแหน่งที่นั่งรอบโต๊ะ
ประเทศที่อยู่ติดกันห้ามเป็นคู่สงคราม

โต๊ะเป็นวงกลม คู่สุดท้ายที่ต้องตรวจจึงเป็น **ประเทศสุดท้ายกับประเทศแรก**
โปรแกรมทำให้ตรวจคู่นี้ด้วยลูปเดียวกันได้โดยนำประเทศแรกไปต่อท้าย list

```python
circular_countries = countries + [countries[0]]
```

ถ้าที่นั่งเดิมคือ `[A, B, C]` list ที่ใช้ตรวจจะเป็น `[A, B, C, A]`
จึงได้คู่ `A-B`, `B-C` และ `C-A` ครบถ้วน

ฟังก์ชัน `is_enemy_pair()` ตรวจความสัมพันธ์ทั้งสองทิศทาง

```python
return country02 in enemies[country01] or country01 in enemies[country02]
```

ให้ประเทศรอบโต๊ะเป็น `c_0, c_1, ..., c_{n-1}` และกำหนด
`c_n = c_0` โต๊ะจะจัดได้ก็ต่อเมื่อทุกคู่ติดกันไม่เป็นศัตรูกัน

$$
\text{valid} \iff
\forall i \in \{0, 1, \ldots, n-1\},
\neg\operatorname{enemy}(c_i, c_{i+1})
$$

เมื่อพบคู่ที่เป็นศัตรูกัน ฟังก์ชันคืน `False` ทันที
ถ้าตรวจครบทุกคู่จึงคืน `True`

---

## การประมวลผลคำสั่ง

โปรแกรมอ่านข้อมูลทีละบรรทัดด้วย `while True` และแยกคำแรกเป็น `cmd`

```python
data = input().strip().split()
if data == ["End"]:
    break

cmd = data[0]
countries = data[1:]
```

คำสั่งมีผลดังนี้

-   `Ally` เพิ่มความสัมพันธ์พันธมิตร และยังไม่แสดงผล
-   `Enemy` เพิ่มความสัมพันธ์คู่สงคราม และยังไม่แสดงผล
-   `Table` ขยายความเป็นศัตรู ตรวจที่นั่ง แล้วแสดง `Okay` หรือ `No`
-   `End` จบโปรแกรม และไม่แสดงผล

ข้อมูลความสัมพันธ์อยู่ใน dictionary ที่ประกาศไว้นอกฟังก์ชัน จึงคงอยู่ต่อเนื่อง
ระหว่างทุกบรรทัด และข้อมูลศัตรูที่อนุมานก่อนตรวจโต๊ะก็ถูกเก็บไว้ใช้กับโต๊ะถัดไป

โจทย์รับรองว่าแต่ละบรรทัดเริ่มด้วยหนึ่งในสี่คำสั่งนี้ จำนวนบรรทัดทดสอบไม่เกิน
100 บรรทัด ไม่มีประเทศอยู่ในสองกลุ่มพันธมิตร และไม่มีคู่ประเทศที่เป็นทั้ง
พันธมิตรและคู่สงครามพร้อมกัน

---

## ลำดับการทำงาน

1. รับข้อมูลหนึ่งบรรทัดและแยกเป็นคำด้วย `split()`
2. ถ้าเป็น `End` ให้จบโปรแกรม
3. เตรียมเซตพันธมิตรและศัตรูให้ประเทศที่เพิ่งพบด้วย `init_countries()`
4. ถ้าเป็น `Ally` ให้เพิ่มประเทศอื่นในบรรทัดเป็นพันธมิตรของแต่ละประเทศ
5. ถ้าเป็น `Enemy` ให้เพิ่มประเทศอื่นในบรรทัดเป็นศัตรูของแต่ละประเทศ
6. ถ้าเป็น `Table` ให้เพิ่มพันธมิตรของศัตรูและศัตรูของพันธมิตรลงในข้อมูลศัตรู
7. ตรวจประเทศที่นั่งติดกันทุกคู่ รวมทั้งคู่ประเทศสุดท้ายกับประเทศแรก
8. แสดง `No` ทันทีเมื่อพบคู่ศัตรู มิฉะนั้นแสดง `Okay`
9. กลับไปรับคำสั่งบรรทัดถัดไป

---

## ตัวอย่างการทำงาน

จากข้อมูลบางส่วนในโจทย์

```text
Ally America England Ukraine France
Ally Russia China
Enemy China America
Enemy France Iran
```

`America` เป็นศัตรูกับ `China` ดังนั้นพันธมิตรของ `America`
และพันธมิตรของ `China` จะถูกขยายให้เป็นศัตรูระหว่างสองกลุ่มด้วย

-   `Table America England Russia` แสดง `No` เพราะโต๊ะกลมทำให้
    `Russia` ซึ่งอยู่ท้าย list นั่งติดกับ `America` ซึ่งอยู่ต้น list
-   ประเทศอย่าง `Iceland`, `Thailand` หรือ `Japan` ที่เพิ่งปรากฏในคำสั่ง
    `Table` จะถูกสร้างด้วยเซตความสัมพันธ์ว่าง และไม่เป็นศัตรูกับใครจนกว่าจะมี
    ข้อมูลระบุไว้

ผลลัพธ์ของโต๊ะทั้งสามในตัวอย่างโจทย์คือ

```text
No
No
Okay
```

---

## ข้อควรระวัง

-   ต้องตรวจคู่สุดท้ายกับคู่แรกเสมอ เพราะโต๊ะเป็นวงกลม
-   ข้อความผลลัพธ์ต้องเป็น `Okay` และ `No` ตามตัวพิมพ์ที่กำหนด
-   `add_more_enemies()` แก้ไขข้อมูลใน `enemies` จริง ความสัมพันธ์ที่อนุมานแล้ว
    จึงยังอยู่เมื่อรับคำสั่ง `Table` ถัดไป
-   โค้ดตรวจประเทศตามลำดับที่ได้รับและไม่ได้ตรวจว่าชื่อประเทศในโต๊ะซ้ำกันหรือไม่
    ตัวอย่างใน PDF เองมี `China` ปรากฏสองตำแหน่งในโต๊ะสุดท้าย
-   คำสั่ง `Table` ที่ไม่มีชื่อประเทศไม่อยู่ในเงื่อนไขข้อมูล เพราะโค้ดต้องใช้
    `countries[0]` เพื่อปิดวงกลม

---

# Solution

```python
# --------------------------------------------------
# File Name : 2565_1_Q3_03.py
# Problem   : APEC Headache
# Author    : Worralop Srichainont
# Date      : 2025-07-11
# --------------------------------------------------

# Initialize dictionaries to store allies and enemies of countries
allies = {}
enemies = {}


# Initialize the allies and enemies dictionaries for each country
def init_countries(countries):
    for country in countries:
        if country not in allies:
            allies[country] = set()
        if country not in enemies:
            enemies[country] = set()


# Add allies of each country based on the list of countries
def add_allies(countries):
    for country in countries:
        allies[country] |= set(countries) - {country}


# Add enemies of each country based on the list of countries
def add_enemies(countries):
    for country in countries:
        enemies[country] |= set(countries) - {country}


# Add more enemies based on the allies and enemies relationships
def add_more_enemies():
    # Add allies of enemies to the enemies of each country
    for country, enemy_countries in enemies.items():
        # Collect all allies of enemies
        allies_of_enemies = set()
        for enemy in enemy_countries:
            allies_of_enemies |= allies[enemy]
        # Add these allies to the enemies of the country
        enemies[country] |= allies_of_enemies

    # Add enemies of allies to the enemies of each country
    for country, ally_countries in allies.items():
        # Collect all enemies of allies
        enemies_of_allies = set()
        for ally in ally_countries:
            enemies_of_allies |= enemies[ally]
        # Add these enemies to the enemies of the country
        enemies[country] |= enemies_of_allies


# Check if two countries are enemies
def is_enemy_pair(country01, country02):
    return country02 in enemies[country01] or country01 in enemies[country02]


# Check if the circular table of countries can be a valid arrangement
def is_table_valid(countries):
    # Ensure the list is circular by appending the first country to the end
    circular_countries = countries + [countries[0]]
    # Check each pair of adjacent countries if they are enemies
    for i in range(len(circular_countries) - 1):
        # If any adjacent pair is an enemy pair, return False
        if is_enemy_pair(circular_countries[i], circular_countries[i + 1]):
            return False
    # If no adjacent pairs are enemies, return True
    return True


# Main function
def main():
    while True:
        # Read input data
        data = input().strip().split()
        # If the input is "End", break the loop
        if data == ["End"]:
            break

        # Extract the command and the list of countries
        cmd = data[0]
        countries = data[1:]

        # Initialize the allies and enemies dictionary for the given countries
        init_countries(countries)
        # Add allies for each country in the list
        if cmd == "Ally":
            add_allies(countries)
        # Add enemies for each country in the list
        elif cmd == "Enemy":
            add_enemies(countries)
        # Check if the arrangement of countries can be a valid table arrangement
        elif cmd == "Table":
            # Add more enemies based on the current allies and enemies relationships
            add_more_enemies()
            # Check if the arrangement of countries is valid
            if is_table_valid(countries):
                print("Okay")
            else:
                print("No")


# Run the main function to start the program
main()
```
