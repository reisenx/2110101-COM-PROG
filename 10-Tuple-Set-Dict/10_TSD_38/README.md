<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Sky Train ★★★ (
      <a href="https://drive.google.com/file/d/12Ak3Xe47gusCPmwAtTIi9WSXiHrxCNHp/view?usp=drive_link">
        <code>10_TSD_38</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การแทนเส้นทางด้วยกราฟ**](#การแทนเส้นทางด้วยกราฟ)
-   [**การสร้างรายการสถานีที่ติดกัน**](#การสร้างรายการสถานีที่ติดกัน)
-   [**การหาสถานีในระยะไม่เกินสองช่วง**](#การหาสถานีในระยะไม่เกินสองช่วง)
-   [**การเรียงผลลัพธ์และกรณีพิเศษ**](#การเรียงผลลัพธ์และกรณีพิเศษ)
-   [**Solution**](#solution)

---

## การแทนเส้นทางด้วยกราฟ

มองแต่ละสถานีเป็น **จุด** และการที่สองสถานีอยู่ติดกันเป็น **เส้นเชื่อม**
จะได้โครงสร้างที่เรียกว่า graph การเชื่อมต่อของโจทย์นี้ไม่มีทิศทาง เช่น
ถ้า `Siam` ติดกับ `ChitLom` ก็เดินจาก `Siam` ไป `ChitLom` หรือย้อนกลับได้

โปรแกรมใช้ dictionary `adjacent_stations` เก็บข้อมูล โดย key คือชื่อสถานี
และ value คือเซตของสถานีที่อยู่ติดกัน เช่น

```python
{"Siam": {"ChitLom", "NationalStadium"}}
```

การใช้ `set` ช่วยตัดชื่อที่ซ้ำกันอัตโนมัติ จึงรองรับกรณีที่คู่สถานีเดิมปรากฏซ้ำ
หรือปรากฏกลับลำดับ เช่น `ThongLo Ekkamai` และ `Ekkamai ThongLo`

---

## การสร้างรายการสถานีที่ติดกัน

โปรแกรมอ่านแต่ละบรรทัดด้วย `split()` ถ้าได้ชื่อ `2` สถานี จะเพิ่มเส้นเชื่อม
ทั้งสองทิศทาง

```python
adjacent_stations[station].add(adjacent)
adjacent_stations[adjacent].add(station)
```

ก่อนเพิ่มจะสร้างเซตว่างให้สถานีที่ยังไม่เคยเป็น key เมื่ออ่านเจอบรรทัดที่มี
ชื่อสถานีเพียง `1` ชื่อ โปรแกรมถือว่ารับข้อมูลเส้นทางครบแล้ว บันทึกชื่อนั้นใน
`start_station` และออกจากลูป

สถานีทั้งหมดไม่จำเป็นต้องเชื่อมถึงกัน ส่วนที่อยู่คนละกลุ่มกับสถานีเริ่มต้น
จะไม่ส่งผลต่อคำตอบ

---

## การหาสถานีในระยะไม่เกินสองช่วง

ให้ \(N(s)\) หมายถึงเซตสถานีที่ติดกับสถานี \(s\) คำตอบสำหรับสถานีเริ่มต้น
\(s\) คือ

\[
R = \{s\} \cup N(s) \cup \bigcup_{v \in N(s)} N(v)
\]

สามส่วนนี้คือสถานีที่อยู่ห่าง `0`, `1` และ `2` ช่วงตามลำดับ โปรแกรมเริ่มด้วย

```python
reachable_stations = {start_station}
```

จึงนับสถานีเริ่มต้นรวมในคำตอบตามตัวอย่าง จากนั้นถ้าสถานีเริ่มต้นมีอยู่ใน
`adjacent_stations` จะรวมเพื่อนบ้านระยะ `1` ด้วย `|=` แล้วเดินดูเพื่อนบ้าน
แต่ละสถานีเพื่อรวมเพื่อนบ้านของมัน ซึ่งเป็นระยะไม่เกิน `2`

```python
reachable_stations |= adjacent_stations[start_station]
for station in adjacent_stations[start_station]:
    reachable_stations |= adjacent_stations[station]
```

เซตจะกำจัดชื่อซ้ำที่เกิดจากหลายเส้นทางหรือวงจร เช่น การเดินกลับมาถึง
`start_station` อีกครั้ง จึงไม่ต้องเขียนเงื่อนไขกันสถานีซ้ำเอง

---

## การเรียงผลลัพธ์และกรณีพิเศษ

ท้ายโปรแกรมใช้ `sorted(reachable_stations)` เพื่อเรียงชื่อสถานีตามพจนานุกรม
แล้วพิมพ์สถานีละหนึ่งบรรทัด

-   ถ้าสถานีเดียวกันไปถึงได้หลายเส้นทาง เซตทำให้แสดงเพียงครั้งเดียว
-   สถานีที่ห่างเกิน `2` ช่วงและสถานีในกลุ่มที่ไม่เชื่อมกับจุดเริ่มต้นจะไม่ถูกเพิ่ม
-   ถ้าสถานีเริ่มต้นไม่ติดกับสถานีใดเลย ชื่อนั้นจะไม่มี key ใน
    `adjacent_stations` เงื่อนไข `if` จึงไม่ทำงาน และแสดงเพียงสถานีเริ่มต้น

---

# Solution

```python
# --------------------------------------------------
# File Name : 10_TSD_38.py
# Problem   : Sky Train
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Initialize a dictionary for adjacent stations
adjacent_stations = {}
start_station = ""

while True:
    # Read the input line
    data = input().strip().split()
    # Stop input if has only one station
    if len(data) == 1:
        start_station = data[0]
        break

    # Update the adjacent stations dictionary
    station, adjacent = data
    if station not in adjacent_stations:
        adjacent_stations[station] = set()
    adjacent_stations[station].add(adjacent)

    if adjacent not in adjacent_stations:
        adjacent_stations[adjacent] = set()
    adjacent_stations[adjacent].add(station)

# Find reachable stations from the start station in range of 2 stations
reachable_stations = {start_station}
if start_station in adjacent_stations:
    reachable_stations |= adjacent_stations[start_station]
    for station in adjacent_stations[start_station]:
        reachable_stations |= adjacent_stations[station]

# Output all reachable stations in sorted order
for station in sorted(reachable_stations):
    print(station)
```
