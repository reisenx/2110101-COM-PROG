<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Connect Four ★★★☆ (
      <a href="https://drive.google.com/file/d/1VZzXLBxJCZVnwWJkAfcxgIwhTQsdcmev/view?usp=sharing">
        <code>2567_2_Q3_C1</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แทนกระดานและหยอดหมาก**](#แทนกระดานและหยอดหมาก)
-   [**ตรวจการเรียงติดกันสี่ตัว**](#ตรวจการเรียงติดกันสี่ตัว)
-   [**จำลองตาเล่นและเงื่อนไขจบเกม**](#จำลองตาเล่นและเงื่อนไขจบเกม)
-   [**แสดงสถานะสุดท้ายของกระดาน**](#แสดงสถานะสุดท้ายของกระดาน)
-   [**Solution**](#solution)

---

## แทนกระดานและหยอดหมาก

ข้อมูลบรรทัดแรกให้ความกว้างและความสูงของกระดานตามลำดับ โค้ดจึงรับเป็น
`cols, rows` แล้วสร้างลิสต์สองมิติที่ทุกช่องเริ่มต้นเป็น `"."`

```python
board = [["."] * cols for _ in range(rows)]
pieces_on_column = [0] * cols
```

`board[row][col]` ใช้แถว `0` เป็นแถวบนสุด ส่วน `pieces_on_column[col]`
เก็บจำนวนหมากที่อยู่ในแต่ละคอลัมน์ ทำให้หาตำแหน่งว่างถัดไปจากด้านล่างได้โดย

$$
\text{row}=\text{rows}-(\text{จำนวนหมากในคอลัมน์}+1)
$$

ซึ่งตรงกับ Python

```python
return rows - (pieces_on_column[col] + 1)
```

หมายเลขคอลัมน์ในโจทย์เริ่มจาก `1` แต่ index ของลิสต์เริ่มจาก `0`
จึงลบหนึ่งตั้งแต่ตอนรับลำดับการหยอด

```python
drop_on_column_order = [int(num) - 1 for num in input().split()]
```

`drop_piece()` จะวางหมายเลขผู้เล่นลงในกระดานและเพิ่มตัวนับของคอลัมน์
เฉพาะเมื่อ `(row, col)` อยู่ในกระดาน หากคอลัมน์เต็ม สูตรหาแถวจะได้ `-1`
ซึ่งอยู่นอกกระดาน ฟังก์ชันจึงคืน `False` และไม่แก้ข้อมูลใด ๆ

---

## ตรวจการเรียงติดกันสี่ตัว

การชนะเกิดได้ 4 แนว ได้แก่ แนวนอน แนวตั้ง และแนวทแยงสองแบบ
แต่จากหมากตัวล่าสุดต้องตรวจได้ทั้งสองด้านของแต่ละแนว โค้ดจึงเก็บทิศทาง 8 ทิศ
โดยวางทิศตรงข้ามไว้ติดกัน

| คู่ทิศ | การเปลี่ยน `(row, col)` | แนวที่ตรวจ |
| :-: | :-: | :-- |
| ตะวันออก–ตะวันตก | `(0, 1)`, `(0, -1)` | แนวนอน |
| เหนือ–ใต้ | `(-1, 0)`, `(1, 0)` | แนวตั้ง |
| ตะวันออกเฉียงเหนือ–ตะวันตกเฉียงใต้ | `(-1, 1)`, `(1, -1)` | ทแยง `/` |
| ตะวันตกเฉียงเหนือ–ตะวันออกเฉียงใต้ | `(-1, -1)`, `(1, 1)` | ทแยง `\` |

สำหรับทิศ `(dr, dc)` ช่องที่ห่างจากหมากล่าสุด `n` ตำแหน่งคือ

$$
(\text{row}+dr\times n,\ \text{col}+dc\times n)
$$

ตรงกับคำสั่ง

```python
is_player_piece(row + (dr * n), col + (dc * n), player)
```

`is_player_piece()` ตรวจขอบกระดานก่อนเข้าถึง `board` จึงไม่เกิด index เกินขอบ
เมื่อเริ่มคู่ทิศใหม่ (`i % 2 == 0`) จะตั้ง `piece_count = 1`
เพื่อนับหมากล่าสุดหนึ่งตัว แล้วสะสมจำนวนหมากสีเดียวกันจากทั้งสองทิศของคู่เดิม
หากรวมได้อย่างน้อย `4` ตัวก็ชนะทันที

ตัวอย่างเช่น มีหมากสีเดียวกันทางซ้าย 2 ตัวและทางขวา 1 ตัว
เมื่อรวมหมากล่าสุดอีก 1 ตัวจะได้ `2 + 1 + 1 = 4` ตัวติดกัน

---

## จำลองตาเล่นและเงื่อนไขจบเกม

ลูปใน `play_game()` ประมวลผลหมายเลขคอลัมน์ตามลำดับที่รับมา
ผู้เล่นสลับกันด้วย

```python
player = PLAYER[turn % 2]
```

ดังนั้น `turn` เลขคู่เป็นผู้เล่น `1` และ `turn` เลขคี่เป็นผู้เล่น `2`
หลังพยายามหยอดแต่ละครั้ง โปรแกรมตรวจเหตุจบเกมตามลำดับนี้

1. ถ้าหมากล่าสุดทำให้ผู้เล่นเรียงครบ 4 ตัว แสดง `Player 1 wins` หรือ
   `Player 2 wins`
2. ถ้าหยอดในคอลัมน์ที่เต็ม แสดง `Column full`
3. ถ้าหมากเต็มทั้งกระดานพอดีและยังไม่มีผู้ชนะ แสดง `Board full`
4. ถ้าใช้ลำดับการหยอดหมดก่อนเกิดสามกรณีข้างต้น แสดง `No more moves`

ลำดับนี้สำคัญ เช่น หมากตัวสุดท้ายอาจทำให้ทั้งกระดานเต็มและทำให้ผู้เล่นชนะพร้อมกัน
โค้ดจะรายงานการชนะก่อน เมื่อพบเหตุจบเกมจะใช้ `break`
จึงไม่ประมวลผลข้อมูลการหยอดส่วนที่เหลือหลังเกมจบ

> [!NOTE]
>
> เงื่อนไข `turn >= 3` ก่อนตรวจชนะเป็นเพียงการข้ามตาแรก ๆ
> ที่ยังไม่มีโอกาสเรียงครบ 4 ตัว การชนะจริงของผู้เล่นคนหนึ่งย่อมต้องใช้หมาก
> ของผู้เล่นคนนั้นอย่างน้อย 4 ตัวอยู่แล้ว

---

## แสดงสถานะสุดท้ายของกระดาน

`display_board()` วนจากแถวบนลงแถวล่าง แล้วเชื่อมสมาชิกแต่ละแถวด้วย
`"".join(row)` จึงไม่มีช่องว่างคั่นระหว่างช่อง

-   `.` หมายถึงช่องว่าง
-   `1` หมายถึงหมากของผู้เล่น 1
-   `2` หมายถึงหมากของผู้เล่น 2

ไม่ว่าเกมจะจบด้วยเหตุใด โปรแกรมจะแสดงข้อความบอกเหตุก่อนหนึ่งบรรทัด
ตามด้วยกระดานจำนวน `rows` บรรทัดในสถานะขณะที่เกมจบ

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_2_Q3_C1.py
# Problem   : Connect Four
# Author    : Worralop Srichainont
# Date      : 2025-07-30
# --------------------------------------------------

# Constants for directions
# East      ( 0,  1) | West      (0, -1)
# North     (-1,  0) | South     (1,  0)
# Northeast (-1,  1) | Southwest (1, -1)
# Northwest (-1, -1) | Southeast (1,  1)
DIRECTIONS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1))

# Game Configuration
PLAYER = ["1", "2"]
WINNING_PIECE_COUNT = 4

# Input amount of rows and columns of the board
cols, rows = [int(num) for num in input().split()]

# Initialize the game board and pieces on each column
board = [["."] * cols for _ in range(rows)]
pieces_on_column = [0] * cols

# Input the order of dropping pieces to each columns
drop_on_column_order = [int(num) - 1 for num in input().split()]


# Check if the given row and column are inside the board
def is_inside_board(row, col):
    return (0 <= row < rows) and (0 <= col < cols)


# Calculate the row to drop a piece in the given column
def get_drop_piece_row(col):
    return rows - (pieces_on_column[col] + 1)


# Check if the piece at the given row and column is the player's piece
def is_player_piece(row, col, player):
    return is_inside_board(row, col) and board[row][col] == player


# Drop a piece in the given row and column for the player
# Return True if the piece is dropped successfully, otherwise return False
def drop_piece(row, col, player):
    if is_inside_board(row, col):
        board[row][col] = player
        pieces_on_column[col] += 1
        return True
    return False


# Check if the player has won by connecting 4 pieces in a row
def is_player_win(row, col, player):
    # Initialize the piece count
    piece_count = 1

    # Check all 8 directions for a win
    for i in range(len(DIRECTIONS)):
        # Get the current direction
        dr, dc = DIRECTIONS[i]
        # Reset piece count when resetting direction
        if i % 2 == 0:
            piece_count = 1

        # Count pieces in the current direction
        for n in range(1, WINNING_PIECE_COUNT):
            if not is_player_piece(row + (dr * n), col + (dc * n), player):
                break
            piece_count += 1

        # Check if the player has connected enough pieces
        if piece_count >= WINNING_PIECE_COUNT:
            return True
    # If no direction has enough pieces, return False
    return False


# Display the game board
def display_board():
    for row in board:
        print("".join(row))


# Main function to play the game
def play_game():
    # Initialize the game state
    is_game_end = False

    # Process each turn in the order of dropping pieces
    for turn in range(len(drop_on_column_order)):
        # Get the row and column to drop the piece
        col = drop_on_column_order[turn]
        row = get_drop_piece_row(col)
        player = PLAYER[turn % 2]

        # Player drops a piece in the specified column
        # If the column is full, the piece cannot be dropped
        is_column_full = not drop_piece(row, col, player)

        # If the player has won, display the board and end the game
        if turn >= 3 and is_player_win(row, col, player):
            print("Player", player, "wins")
            display_board()
            is_game_end = True
            break

        # If the column is full, display a message and end the game
        if turn >= rows - 1 and is_column_full:
            print("Column full")
            display_board()
            is_game_end = True
            break

        # If the board is full, display a message and end the game
        if turn == (rows * cols) - 1:
            print("Board full")
            display_board()
            is_game_end = True
            break

    # If the game has not ended after all turns, display a message
    if not is_game_end:
        print("No more moves")
        display_board()


# Run the function to play the game
play_game()
```
