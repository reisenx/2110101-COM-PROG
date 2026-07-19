<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Snake and Ladders 2 ★★☆ (
      <a href="https://drive.google.com/file/d/1HxprZGmq1r8nJj6YRfVJyiFnFduKlb-T/view?usp=sharing">
        <code>2567_2_Q2_A3</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**เปลี่ยนกระดานเป็นลิสต์หนึ่งมิติ**](#เปลี่ยนกระดานเป็นลิสต์หนึ่งมิติ)
-   [**ตำแหน่งในเกมและดัชนีของลิสต์**](#ตำแหน่งในเกมและดัชนีของลิสต์)
-   [**จำลองการทอยลูกเต๋า**](#จำลองการทอยลูกเต๋า)
-   [**เครื่องหมาย T และ L ในโจทย์**](#เครื่องหมาย-t-และ-l-ในโจทย์)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## เปลี่ยนกระดานเป็นลิสต์หนึ่งมิติ

กระดานข้อนี้เป็นแบบกลับด้าน จุดเริ่มต้นอยู่มุมซ้ายบนข้างช่องที่ `1`
เส้นทางเดินสลับทิศในแต่ละแถว ดังนี้

-   แถวที่ `0`, `2`, `4`, ... ซึ่งนับจากด้านบน เก็บจากซ้ายไปขวา
-   แถวที่ `1`, `3`, `5`, ... เก็บจากขวาไปซ้าย

โปรแกรมอ่านแถวตามลำดับจากบนลงล่าง แล้วต่อข้อมูลเข้ากับ `game_board`

```python
if i % 2 == 0:
    game_board += line
else:
    game_board += line[::-1]
```

การกลับ `line[::-1]` เฉพาะแถวคี่ทำให้ตำแหน่งในลิสต์เรียงตามเส้นทางจริง
ต่างจากบันไดงูแบบปกติที่เริ่มจากมุมซ้ายล่าง

---

## ตำแหน่งในเกมและดัชนีของลิสต์

หมายเลขช่องบนกระดานเริ่มที่ `1` แต่ดัชนีของลิสต์ Python เริ่มที่ `0`
จึงมีความสัมพันธ์ว่า

$$
\text{ตำแหน่งบนกระดาน} = \text{idx} + 1
$$

ก่อนทอยครั้งแรก ผู้เล่นยังอยู่ข้างช่อง `1` โปรแกรมจึงตั้ง `idx = -1`
ถ้าทอยได้ `2` จะคำนวณ `idx += 2` เป็น `1` ซึ่งตรงกับช่องที่ `2`

ข้อความพิเศษ เช่น `T13` หรือ `S4` เก็บหมายเลขปลายทางไว้หลังอักขระตัวแรก
โปรแกรมจึงใช้

```python
idx = int(game_board[idx][1:]) - 1
```

เพื่อตัดอักขระนำหน้า แปลงเลขปลายทางเป็นจำนวนเต็ม และลบ `1`
ให้กลับมาเป็นดัชนีของลิสต์

---

## จำลองการทอยลูกเต๋า

สำหรับแต้มลูกเต๋าแต่ละครั้ง โปรแกรมทำตามลำดับต่อไปนี้

1. เพิ่ม `idx` ด้วยแต้มที่ทอยได้
2. ถ้ายังไม่ถึงช่องสุดท้ายและช่องนั้นไม่ใช่ `.` ให้ย้ายไปหมายเลขที่ระบุ
3. ถ้ายังอยู่ก่อนช่องสุดท้าย ให้บันทึกหมายเลขช่องปัจจุบัน
4. ถ้าถึงหรือเลยช่องสุดท้าย ให้บันทึก `win` แล้ว `break`

ดังนั้นการทอยที่เดินเกินกระดานก็นับเป็นชัยชนะ และแต้มลูกเต๋าที่เหลือหลังจาก
`win` จะไม่ถูกประมวลผลอีก โปรแกรมตรวจท่อหรือหัวงูหนึ่งครั้งหลังเดินด้วยลูกเต๋า
และไม่ได้วนตรวจว่าช่องปลายทางเป็นช่องพิเศษอีกหรือไม่

---

## เครื่องหมาย T และ L ในโจทย์

ข้อกำหนดหลักของ PDF ใช้ `T` แทน Tunnel และ `S` แทน Snake
แต่หน้าคำใบ้แสดงตัวอย่างเป็น `L12` และ `L13` ซึ่งเป็นถ้อยคำที่หลงเหลือจาก
โจทย์บันไดงูรูปแบบเดิม สำหรับข้อมูลที่ถูกต้องควรยึด `T` และ `S`
ตามข้อกำหนดหลัก

> [!NOTE]
>
> โค้ดชุดนี้ตรวจเพียงว่าข้อความไม่ใช่ `.` แล้วอ่านตัวเลขด้วย `[1:]`
> จึงไม่ได้ตรวจอักขระตัวแรกจริง ๆ ทั้ง `T12`, `S12` และ `L12`
> จะพาไปช่อง `12` เหมือนกัน นี่คือพฤติกรรมของโค้ด ไม่ใช่การเพิ่มชนิดช่องใหม่
> ให้กับข้อกำหนดของโจทย์

---

## ตัวอย่างการทำงาน

จากกระดานตัวอย่างขนาด `4` ช่อง `T13` ที่อยู่ซ้ายสุดของแถวที่สองจากด้านบน
จะกลายเป็นตำแหน่งที่ `8` หลังกลับแถวนั้น

เมื่อทอย `2 6 4 3`

1. ทอย `2` ไปช่อง `2` จึงบันทึก `2`
2. ทอย `6` ไปช่อง `8` ซึ่งเป็น `T13` จึงย้ายและบันทึก `13`
3. ทอย `4` จากช่อง `13` แล้วเลยช่องสุดท้าย จึงบันทึก `win` และหยุด

ผลลัพธ์คือ `2 13 win`

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_2_Q2_A3.py
# Problem   : Snakes and Ladder 2
# Author    : Worralop Srichainont
# Date      : 2025-07-29
# --------------------------------------------------

# Input number of rows of the table
rows = int(input())

# Initialize the game board
game_board = []

# Input the game board
for i in range(rows):
    # Input each line of the game board
    line = input().strip().split()

    # Add the line on even rows counting from the above
    if i % 2 == 0:
        game_board += line

    # Add the reversed line on odd rows counting from the above
    else:
        game_board += line[::-1]

# Input the dice rolls
dice_rolls = [int(roll) for roll in input().split()]

# Initialize the list to keep track of the game process
# and the index of the current position
game_process = []
idx = -1

# Process the game based on the dice rolls
for roll in dice_rolls:
    # Update the index based on the dice roll
    idx += roll

    # Check if the index is on snake or ladder grid
    if (idx < len(game_board) - 1) and (game_board[idx] != "."):
        # Move to the position indicated by the snake or ladder
        idx = int(game_board[idx][1:]) - 1

    # Append the current position to the game process
    if idx < len(game_board) - 1:
        game_process.append(str(idx + 1))

    # Check if the player has reached the end of the game board
    else:
        game_process.append("win")
        break

# Output the game process
print(" ".join(game_process))
```
