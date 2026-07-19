<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    One Piece ★★★ (
      <a href="https://drive.google.com/file/d/1x2IVrmVc27GaYGnEhnUbKJCNJO1p6gpi/view?usp=sharing">
        <code>2566_1_Q3_01</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**โครงสร้างแผนที่เกาะ**](#โครงสร้างแผนที่เกาะ)
-   [**การเดินตามเส้นทาง**](#การเดินตามเส้นทาง)
-   [**การตรวจทางตันและวงจร**](#การตรวจทางตันและวงจร)
-   [**การตอบคำถาม**](#การตอบคำถาม)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**กรณีพิเศษ**](#กรณีพิเศษ)
-   [**Solution**](#solution)

---

## โครงสร้างแผนที่เกาะ

เส้นทางในโจทย์นี้มี **ทิศทาง** เช่น เส้นทางจาก `A` ไป `B`
ไม่ได้หมายความว่าจะเดินทางย้อนจาก `B` ไป `A` ได้ และโจทย์กำหนดให้แต่ละเกาะ
มีเส้นทางออกได้เพียงเส้นทางเดียว เราจึงเก็บแผนที่ด้วย dictionary ได้พอดี

```python
goto_next_island[current_island] = (next_island, int(duration))
```

-   key คือชื่อเกาะต้นทาง `current_island`
-   value เป็น tuple `(next_island, duration)` ซึ่งเก็บเกาะถัดไปและเวลาเดินทาง

ตัวอย่างเช่น ข้อมูล `NewMarineford PunkHazard 5` จะถูกเก็บเป็น

```python
goto_next_island["NewMarineford"] = ("PunkHazard", 5)
```

เมื่ออ่าน value ออกจาก dictionary เราสามารถแยกสมาชิกของ tuple ใส่ตัวแปร 2 ตัวได้

```python
next_island, duration = goto_next_island[current_island]
```

ข้อมูลนำเข้ามี 2 ส่วน ส่วนแรกเริ่มด้วยจำนวนเส้นทาง ตามด้วยข้อมูลเส้นทางทีละบรรทัด
ส่วนที่สองเริ่มด้วยจำนวนคำถาม ตามด้วยชื่อเกาะต้นทางและปลายทางของแต่ละคำถาม

---

## การเดินตามเส้นทาง

ฟังก์ชัน `find_route(start_island, end_island)` เดินตามเส้นทางจากเกาะหนึ่ง
ไปยังเกาะถัดไปเรื่อย ๆ โดยใช้ตัวแปรสำคัญ 3 ตัว

-   `current_island` คือเกาะที่กำลังอยู่ เริ่มต้นที่ `start_island`
-   `total_duration` คือเวลาสะสม เริ่มต้นที่ `0`
-   `visited_island` คือเซตของเกาะที่เคยผ่าน ใช้ตรวจวงจร

ตราบใดที่ `current_island != end_island` โปรแกรมจะหาเส้นทางออกจากเกาะปัจจุบัน
แล้วบวกเวลาเดินทางเข้ากับเวลาสะสม

$$
T_{\text{new}} = T_{\text{old}} + d
$$

เขียนเป็นภาษา Python ได้ว่า

```python
total_duration += duration
```

จากนั้นจึงย้ายไปยังเกาะถัดไป

```python
current_island = next_island
```

เมื่อ `current_island` เท่ากับปลายทาง เงื่อนไขของ `while` จะเป็นเท็จ
และฟังก์ชันคืน `total_duration` ทันที

---

## การตรวจทางตันและวงจร

การเดินทางอาจล้มเหลวได้ 2 แบบหลัก

**1. พบทางตัน**

ถ้าเกาะปัจจุบันไม่เป็น key ใน `goto_next_island` แสดงว่าไม่มีเส้นทางออก
และยังไปไม่ถึงปลายทาง ฟังก์ชันจึงคืน `-1`

```python
if current_island not in goto_next_island:
    return -1
```

**2. เดินวนเป็นวงจร**

ก่อนออกจากเกาะ โปรแกรมเพิ่มชื่อเกาะนั้นลงใน `visited_island`
เมื่อเดินไปเกาะถัดไปแล้วพบว่าเกาะนั้นอยู่ในเซตนี้ แสดงว่าเรากลับมายังเกาะเดิม
ถ้าเดินต่อก็จะวนซ้ำและไม่มีทางถึงปลายทาง จึงคืน `-1` เช่นกัน

```python
visited_island.add(current_island)

if current_island in visited_island:
    return -1
```

การค้นหาใน `set` ด้วย `in` เหมาะกับการถามว่าเคยพบเกาะนี้แล้วหรือไม่
และฟังก์ชันสร้าง `visited_island` ชุดใหม่ทุกครั้ง จึงไม่ปะปนกันระหว่างคำถาม

> [!NOTE]
>
> ค่า `-1` เป็นสัญญาณที่ใช้ภายในโปรแกรมเท่านั้น ไม่ใช่ข้อความที่ต้องแสดงผล

---

## การตอบคำถาม

โปรแกรมอ่านคำถามตามลำดับที่ได้รับ แล้วเรียก `find_route()` หนึ่งครั้งต่อคำถาม
ผลลัพธ์แต่ละคำถามจึงถูกแสดงคนละบรรทัดและอยู่ในลำดับเดิม

| ค่าที่ `find_route()` คืน | ผลลัพธ์ที่แสดง |
| :----------------------- | :------------- |
| `-1`                     | `Route not found` |
| จำนวนตั้งแต่ `0` ขึ้นไป   | เวลาสะสมเป็นจำนวนเต็ม |

```python
if total_duration == -1:
    print("Route not found")
else:
    print(total_duration)
```

เวลาเดินทางทุกช่วงถูกแปลงด้วย `int(duration)` และนำมาบวกกันตรง ๆ
จึงไม่มีการหาร การปัดเศษ หรือการกำหนดจำนวนตำแหน่งทศนิยม

---

## ตัวอย่างการทำงาน

พิจารณาคำถามจาก `NewMarineford` ไป `ApplenineIsland`

| เกาะปัจจุบัน | เกาะถัดไป | เวลาช่วงนี้ | เวลาสะสม |
| :----------- | :-------- | ----------: | --------: |
| `NewMarineford` | `PunkHazard` | `5` | `5` |
| `PunkHazard` | `ApplenineIsland` | `7` | `12` |

เมื่อถึง `ApplenineIsland` ฟังก์ชันจึงคืน `12`

สำหรับคำถามจาก `WanoKuni` ไป `Zou` โปรแกรมเดินจาก `WanoKuni` ไป `Sphinx`
แล้วพบว่า `Sphinx` ไม่มีทางออก จึงแสดง `Route not found`

ส่วนคำถามจาก `PunkHazard` ไป `WholecakeIsland` จะเดินเป็นวงจร

```text
PunkHazard -> ApplenineIsland -> NewMarineford -> PunkHazard
```

เมื่อพบ `PunkHazard` ซ้ำ โปรแกรมตรวจพบวงจรและแสดง `Route not found`

---

## กรณีพิเศษ

-   ถ้าเกาะต้นทางเท่ากับเกาะปลายทางตั้งแต่แรก เงื่อนไข `while` จะไม่ทำงาน
    และฟังก์ชันคืน `0` แม้ชื่อเกาะนั้นจะไม่มีอยู่ในแผนที่
-   ถ้าไม่มีชื่อเกาะต้นทางใน dictionary และต้นทางไม่ใช่ปลายทาง
    โปรแกรมจะพบทางตันและแสดง `Route not found`
-   ชื่อเกาะถูกเปรียบเทียบเป็นข้อความแบบตรงตัว จึงต้องสะกดและใช้ตัวพิมพ์ให้ตรงกัน
-   เส้นทางมีทิศทางเดียว โปรแกรมจะไม่สร้างเส้นทางย้อนกลับให้อัตโนมัติ
-   โจทย์รับประกันว่าแต่ละเกาะมีเส้นทางออกเพียงเส้นทางเดียว
    โปรแกรมจึงไม่ต้องเลือกระหว่างหลายเส้นทาง

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_1_Q3_03.py
# Problem   : One Piece
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------

# Initialize a dictionary to store the routes between islands
goto_next_island = {}


# Function to input the island routes
def input_island_route():
    n = int(input())
    for _ in range(n):
        # Extract the current island, next island, and duration from input
        current_island, next_island, duration = input().strip().split()
        # Store the route in the dictionary
        goto_next_island[current_island] = (next_island, int(duration))


# Function to calculate the total duration of the route from start to end island
# If the route is not found, return -1
def find_route(start_island, end_island):
    # Initialize total duration, current island and a set to track visited islands
    total_duration = 0
    current_island = start_island
    visited_island = set()

    # Traverse the islands until reaching the end island
    while current_island != end_island:
        # Add the current island to the visited set
        visited_island.add(current_island)
        # If the current island has no outgoing route, the route is not exist
        if current_island not in goto_next_island:
            return -1

        # Get the next island and duration from the current island
        next_island, duration = goto_next_island[current_island]
        # Calculate the total duration
        total_duration += duration

        # Set the current island to the next island
        current_island = next_island
        # Check if the current island has been visited before
        if current_island in visited_island:
            return -1
    # Return the total duration if the route is found
    return total_duration


# Main function
def main():
    # Input the island routes
    input_island_route()

    # Input queries
    n = int(input())
    for _ in range(n):
        start_island, end_island = input().strip().split()
        # Calculate the total duration of the route from start to end island
        total_duration = find_route(start_island, end_island)
        # Output the total duration
        if total_duration == -1:
            print("Route not found")
        else:
            print(total_duration)


# Run the main function
main()
```
