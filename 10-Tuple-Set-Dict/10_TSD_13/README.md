<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Winner ★ (
      <a href="https://drive.google.com/file/d/1WZFAdB_0dZ0niGUEbE1tPmyu4GFuwu3w/view?usp=drive_link">
        <code>10_TSD_13</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเก็บทีมด้วยเซต**](#การเก็บทีมด้วยเซต)
-   [**การหาทีมที่ไม่เคยแพ้**](#การหาทีมที่ไม่เคยแพ้)
-   [**ลำดับการทำงานและรูปแบบผลลัพธ์**](#ลำดับการทำงานและรูปแบบผลลัพธ์)
-   [**กรณีพิเศษ**](#กรณีพิเศษ)
-   [**Solution**](#solution)

---

## การเก็บทีมด้วยเซต

ผลการแข่งขันหนึ่งบรรทัดมีชื่อทีมที่ชนะและทีมที่แพ้ตามลำดับ เช่น

```text
Chelsea Liverpool
```

โปรแกรมแยกสองชื่อนี้ด้วย

```python
winner, loser = input().strip().split()
```

แล้วเก็บข้อมูลลงในเซตสองชุด

-   `winners` เก็บทุกทีมที่เคยชนะอย่างน้อยหนึ่งครั้ง
-   `losers` เก็บทุกทีมที่เคยแพ้อย่างน้อยหนึ่งครั้ง

```python
winners.add(winner)
losers.add(loser)
```

การใช้ `set` เหมาะกับโจทย์นี้เพราะเราสนใจเพียงว่า "เคย" ชนะหรือแพ้หรือไม่
ไม่ได้สนใจจำนวนครั้ง ทีมเดียวกันจึงถูกเก็บเพียงค่าเดียวแม้จะปรากฏหลายนัด

---

## การหาทีมที่ไม่เคยแพ้

กำหนดให้ \(W\) เป็นเซตทีมที่เคยชนะ และ \(L\) เป็นเซตทีมที่เคยแพ้
ทีมที่ต้องการคือทีมที่อยู่ใน \(W\) แต่ไม่อยู่ใน \(L\)

\[
\text{ทีมที่ไม่เคยแพ้} = W - L
\]

ใน Python เขียนตรงกับสูตรได้เป็น

```python
winners - losers
```

ทีมที่เคยชนะหลายครั้งแต่แพ้แม้เพียงครั้งเดียวจะอยู่ใน `losers`
จึงถูกตัดออกจากผลต่างของเซต ส่วนทีมที่ปรากฏเป็นผู้แพ้อย่างเดียวก็ไม่เคยอยู่ใน
`winners` ตั้งแต่แรก

---

## ลำดับการทำงานและรูปแบบผลลัพธ์

จากตัวอย่างที่มีการแข่งขันต่อไปนี้

```text
Chelsea Liverpool
ManU Liverpool
Liverpool ManU
Chelsea Arsenal
Everton ManCity
```

เมื่ออ่านครบทุกนัด จะสรุปได้ว่า

-   `winners` มี `Chelsea`, `ManU`, `Liverpool` และ `Everton`
-   `losers` มี `Liverpool`, `ManU`, `Arsenal` และ `ManCity`
-   `winners - losers` จึงเหลือ `Chelsea` และ `Everton`

เซตไม่มีลำดับที่แน่นอน แต่โจทย์กำหนดให้เรียงตามชื่อทีม
โปรแกรมจึงเรียก `sorted()` ก่อนแสดงผล

```python
print(sorted(winners - losers))
```

`sorted()` คืนค่าเป็นลิสต์ที่เรียงชื่อแบบข้อความจากน้อยไปมาก และ `print()`
แสดงรูปแบบลิสต์พร้อมวงเล็บเหลี่ยม เครื่องหมายคำพูด และจุลภาคให้โดยอัตโนมัติ

```text
['Chelsea', 'Everton']
```

---

## กรณีพิเศษ

-   ถ้าทีมเดิมชนะหรือแพ้หลายครั้ง เซตจะไม่เก็บชื่อซ้ำและคำตอบยังถูกต้อง
-   ถ้าทีมที่เคยชนะทุกทีมเคยแพ้ด้วย ผลต่างจะเป็นเซตว่างและโปรแกรมแสดง `[]`
-   ชื่อทีมหนึ่งชื่อเป็นข้อมูลหนึ่งคำตามรูปแบบโจทย์ เพราะ `split()` ใช้ช่องว่าง
    แยกชื่อผู้ชนะกับชื่อผู้แพ้

---

# Solution

```python
# --------------------------------------------------
# File Name : 10_TSD_13.py
# Problem   : Winner
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# Input number of matches
n = int(input())

# Initialize sets for winners and losers
winners = set()
losers = set()

# Process each match
for _ in range(n):
    # Read the match result
    winner, loser = input().strip().split()

    # Update winners and losers sets
    winners.add(winner)
    losers.add(loser)

# Output the winner who is not in the losers set
print(sorted(winners - losers))
```
