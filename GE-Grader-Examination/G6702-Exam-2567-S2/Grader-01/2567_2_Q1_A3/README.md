<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Snake and Ladders ★★☆ (
      <a href="https://drive.google.com/file/d/1v0FWx0yP8K58KgW9GwB-JNcxdg_KzSO7/view?usp=sharing">
        <code>2567_2_Q1_A3</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเรียงหมายเลขบนกระดาน**](#การเรียงหมายเลขบนกระดาน)
-   [**การแปลงกระดานเป็นรายการ**](#การแปลงกระดานเป็นรายการ)
-   [**การจำลองการทอยลูกเต๋า**](#การจำลองการทอยลูกเต๋า)
-   [**งู บันได และการชนะ**](#งู-บันได-และการชนะ)
-   [**Solution**](#solution)

---

## การเรียงหมายเลขบนกระดาน

กระดานเริ่มที่มุมล่างซ้าย ช่องแรกมีหมายเลข `1` แล้วหมายเลขจะเดินสลับทิศ
แบบงูเลื้อยทีละแถว แถวล่างสุดเดินจากซ้ายไปขวา แถวถัดไปเดินจากขวาไปซ้าย
และสลับเช่นนี้ขึ้นไปจนถึงช่อง `win`

ตัวอย่างกระดานขนาด `4 × 4` จะเรียงหมายเลขดังนี้

```text
win 15 14 13
  9 10 11 12
  8  7  6  5
  1  2  3  4
```

แต่ข้อมูลกระดานถูกป้อนจากแถวบนลงแถวล่าง ถ้าเก็บแต่ละแถวต่อกันตามที่รับมา
ทันที ตำแหน่งในรายการจะไม่ตรงกับหมายเลขช่อง จึงต้องจัดทิศทางก่อนจำลองเกม

---

## การแปลงกระดานเป็นรายการ

โปรแกรมอ่านกระดานทีละแถวและใช้ `(rows - i - 1)` หาว่าแถวนั้นเป็นแถวที่เท่าไร
เมื่อนับจากด้านล่าง แถวที่ต้องสลับทิศจะถูกเพิ่มด้วย `line[::-1]` ส่วนอีกชุด
เพิ่มด้วย `line` ตามปกติ

หลังอ่านครบ โปรแกรมกลับรายการทั้งหมดอีกครั้งด้วย
`game_board = game_board[::-1]` ผลลัพธ์คือรายการหนึ่งมิติที่
`game_board[0]` แทนช่อง `1`, `game_board[1]` แทนช่อง `2` และเรียงต่อไปจน
สมาชิกสุดท้ายแทนช่อง `win`

การทำให้หมายเลขช่องตรงกับดัชนีช่วยให้เข้าถึงข้อมูลของช่องปัจจุบันได้โดยตรง
แต่ต้องระวังว่า Python เริ่มดัชนีที่ `0` ขณะที่หมายเลขบนกระดานเริ่มที่ `1`
ความสัมพันธ์จึงเป็น

```text
ดัชนี = หมายเลขช่อง - 1
หมายเลขช่อง = ดัชนี + 1
```

---

## การจำลองการทอยลูกเต๋า

ก่อนทอยครั้งแรก ผู้เล่นยังอยู่นอกกระดานตรงจุด `start` โปรแกรมจึงกำหนด
`idx = -1` เมื่อทอยได้ `roll` ให้ขยับด้วย `idx += roll` ตัวอย่างเช่น
ทอยครั้งแรกได้ `2` จะได้ดัชนี `-1 + 2 = 1` ซึ่งตรงกับช่องหมายเลข `2`

โปรแกรมวนตามแต้มใน `dice_rolls` ตามลำดับ หลังประมวลผลแต่ละครั้งจะเก็บ
หมายเลขช่องหรือคำว่า `win` ลงใน `game_process` แล้วพิมพ์ทั้งหมดคั่นด้วยช่องว่าง
ด้วย `" ".join(game_process)` ดังนั้นลำดับผลลัพธ์จึงตรงกับลำดับการทอย

---

## งู บันได และการชนะ

ช่องปกติใช้ข้อความ `.` ส่วนจุดเริ่มบันไดและหัวงูใช้ข้อความอย่าง `L13` และ
`S2` ตามลำดับ ตัวอักษรตัวแรกบอกชนิดของช่อง ส่วนตัวเลขที่เหลือบอกหมายเลข
ปลายทาง

เมื่อผู้เล่นตกบนช่องพิเศษ โปรแกรมตัดตัวอักษรแรกออกด้วย `[1:]` แปลงเลขปลายทาง
เป็น `int` แล้วลบ `1` เพื่อกลับมาเป็นดัชนีของ Python

```python
idx = int(game_board[idx][1:]) - 1
```

คำสั่งเดียวกันใช้ได้ทั้งบันไดและงู เพราะสิ่งที่ต้องทำเหมือนกันคือย้ายไปยัง
หมายเลขที่เขียนไว้หลังตัวอักษร เช่น `L13` ย้ายไปช่อง `13` และ `S2` ย้ายไป
ช่อง `2`

ช่องสุดท้ายมีดัชนี `len(game_board) - 1` ถ้า `idx` มีค่าตั้งแต่ดัชนีนี้ขึ้นไป
โปรแกรมจะบันทึก `win` แล้วใช้ `break` จบลูปทันที จึงถือว่าชนะทั้งกรณีเดินถึง
ช่องสุดท้ายพอดีและกรณีแต้มลูกเต๋าพาเลยช่องสุดท้าย การทอยที่เหลือหลังชนะจะไม่ถูก
นำมาประมวลผล

> [!NOTE]
>
> การตรวจ `idx < len(game_board) - 1` ก่อนอ่าน `game_board[idx]` ทำให้กรณี
> เดินเลยกระดานไม่เกิดข้อผิดพลาดจากการเข้าถึงดัชนีที่ไม่มีอยู่ และถ้าบันได
> พาไปถึงช่องสุดท้ายก็จะได้ผลลัพธ์เป็น `win` เช่นกัน

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_2_Q1_A3.py
# Problem   : Snakes and Ladders
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

    # Add the reversed line on even rows counting from the bottom
    if (rows - i - 1) % 2 == 0:
        game_board += line[::-1]

    # Add the line on odd rows counting from the bottom
    else:
        game_board += line

# Reverse the entire game board to correct the order
game_board = game_board[::-1]

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
