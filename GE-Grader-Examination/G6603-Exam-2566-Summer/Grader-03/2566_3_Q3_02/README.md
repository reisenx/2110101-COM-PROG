<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    RSP Team ★★☆ (
      <a href="https://drive.google.com/file/d/1e3KDAFFtn3tNY_MHorr3GtRUzFQd2ddP/view?usp=sharing">
        <code>2566_3_Q3_02</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**รูปแบบข้อมูลของเกม**](#รูปแบบข้อมูลของเกม)
-   [**การแบ่งลำดับการเล่นออกเป็นแต่ละตา**](#การแบ่งลำดับการเล่นออกเป็นแต่ละตา)
-   [**การตัดสินผลและติดตามคะแนน**](#การตัดสินผลและติดตามคะแนน)
-   [**การเปลี่ยนผู้เล่น**](#การเปลี่ยนผู้เล่น)
-   [**การบันทึกท่าของผู้เล่นแต่ละคน**](#การบันทึกท่าของผู้เล่นแต่ละคน)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ข้อกำหนดของข้อมูลนำเข้า**](#ข้อกำหนดของข้อมูลนำเข้า)
-   [**การรับคำสั่งจากระบบตรวจ**](#การรับคำสั่งจากระบบตรวจ)
-   [**Solution**](#solution)

---

## รูปแบบข้อมูลของเกม

ฟังก์ชัน `player_moves()` มีหน้าที่จำลองเกมเป่ายิงฉุบแบบทีม
แล้วสรุปว่าผู้เล่นแต่ละคนออกท่าอะไรไปบ้าง โดยรับข้อมูลทั้งหมด 3 ค่า

| ตัวแปร | ความหมาย |
|---|---|
| `playing_order` | ข้อความที่เก็บท่าของทีม A และทีม B สลับกันในแต่ละตา |
| `team_a` | `list` ชื่อผู้เล่นทีม A เรียงตามลำดับที่จะลงแข่ง |
| `team_b` | `list` ชื่อผู้เล่นทีม B เรียงตามลำดับที่จะลงแข่ง |

ท่าเป่ายิงฉุบใช้ตัวอักษรแทนดังนี้

-   `R` คือค้อน (Rock)
-   `S` คือกรรไกร (Scissors)
-   `P` คือกระดาษ (Paper)

ผลลัพธ์ที่คืนจากฟังก์ชันเป็น `team_a_moves, team_b_moves`
หรือ `tuple` ที่มีข้อมูลของทีม A อยู่ก่อนทีม B แต่ละทีมเป็น `list`
ของข้อมูลผู้เล่นในรูปแบบ

```python
[ชื่อผู้เล่น, [ท่าที่ออกตามลำดับ]]
```

ตัวอย่างเช่น `['A1', ['R', 'S']]` หมายถึงผู้เล่น `A1`
ออกค้อนแล้วจึงออกกรรไกร

---

## การแบ่งลำดับการเล่นออกเป็นแต่ละตา

ใน `playing_order` การเล่นหนึ่งตาใช้ตัวอักษร 2 ตัวติดกัน
โดยตัวแรกเป็นท่าของทีม A และตัวที่สองเป็นท่าของทีม B ดังนั้นเราต้องอ่าน
ข้อความครั้งละ 2 ตำแหน่ง

คำสั่ง `range(0, len(playing_order), 2)` สร้างตำแหน่ง
`0, 2, 4, ...` ส่วน slice `playing_order[i : i + 2]`
เลือกข้อความตั้งแต่ตำแหน่ง `i` จำนวน 2 ตัว จึงนำมาแบ่งตาได้ดังนี้

```python
for i in range(0, len(playing_order), 2):
    move = playing_order[i : i + 2]
    moves.append(move)
```

ตัวอย่าง `playing_order = "RSSPRR"`

-   `playing_order[0:2]` ได้ `"RS"`
-   `playing_order[2:4]` ได้ `"SP"`
-   `playing_order[4:6]` ได้ `"RR"`

ดังนั้น `get_moves("RSSPRR")` จะคืนค่า
`["RS", "SP", "RR"]` โดย `"RS"` หมายถึงทีม A ออก `R`
และทีม B ออก `S`

---

## การตัดสินผลและติดตามคะแนน

ค่าคงที่ `WINNING` และ `LOSING` มองผลการแข่งขันจากฝั่งทีม A

| คู่ท่า `move` | ผลของตานั้น | คำสั่งที่เปลี่ยนคะแนน |
|---|---|---|
| `RS`, `SP`, `PR` | ทีม A ชนะ | `score[0] += 1` |
| `SR`, `PS`, `RP` | ทีม B ชนะ | `score[1] += 1` |
| `RR`, `SS`, `PP` | เสมอ | คะแนนไม่เปลี่ยน |

โปรแกรมตรวจผลด้วยตัวดำเนินการ `in` เช่น `move in WINNING`
ถ้าเป็นจริงก็เพิ่มคะแนนของทีม A ส่วนตาที่เสมอจะไม่อยู่ในทั้งสอง `list`
จึงไม่มีทีมใดได้คะแนน

ผู้เล่นคู่เดิมจะแข่งกันจนฝ่ายหนึ่งชนะครบ 2 ครั้ง โดยไม่จำเป็นต้องชนะติดกัน
เมื่อประมวลผลแต่ละตา `get_match_status()` จะบันทึกสถานะหนึ่งค่า

-   `"NO CHANGE"` หมายถึงยังใช้ผู้เล่นคู่เดิม
-   `"CHANGE TEAM B"` หมายถึงทีม A ชนะครบ 2 ครั้ง
    ผู้เล่นทีม B จึงต้องออกจากเกม
-   `"CHANGE TEAM A"` หมายถึงทีม B ชนะครบ 2 ครั้ง
    ผู้เล่นทีม A จึงต้องออกจากเกม

ชื่อสถานะบอกว่า **ทีมใดต้องเปลี่ยนผู้เล่น** ไม่ใช่ทีมที่ชนะ
เมื่อมีการเปลี่ยนผู้เล่น คะแนนจะถูกกำหนดกลับเป็น `score = [0, 0]`
เพื่อให้คู่ใหม่เริ่มนับคะแนนตั้งแต่ศูนย์

---

## การเปลี่ยนผู้เล่น

ฟังก์ชัน `get_next_player()` หาตำแหน่งของผู้เล่นปัจจุบันด้วย
`team.index(current_player)` แล้วเลื่อนไปหนึ่งตำแหน่ง

ถ้าให้ `idx` เป็นตำแหน่งปัจจุบัน และให้ $n$ เป็นจำนวนผู้เล่นในทีม
ตำแหน่งถัดไปคือ

$$
(idx + 1) \bmod n
$$

ซึ่งเขียนในภาษา Python เป็น

```python
(idx + 1) % len(team)
```

เครื่องหมาย `%` ทำให้ตำแหน่งวนกลับเป็น `0` หลังตำแหน่งสุดท้าย
จึงไม่เกิดดัชนีเกินขอบเขตของ `list`

> [!NOTE]
>
> ตามกติกา เกมจะจบเมื่อทีมใดทีมหนึ่งไม่มีผู้เล่นเหลือ และข้อมูลจากระบบตรวจ
> จะหยุด ณ จุดนั้น โค้ดนี้ไม่ได้ตรวจว่าทีมหมดผู้เล่น แต่ใช้ `% len(team)`
> ซึ่งจะวนกลับไปผู้เล่นคนแรกหากยังมีข้อมูลการเล่นต่อหลังผู้เล่นคนสุดท้ายแพ้

---

## การบันทึกท่าของผู้เล่นแต่ละคน

ตอนเริ่มเกม ผู้เล่นคนแรกของแต่ละทีมเป็นผู้เล่นปัจจุบัน
และยังไม่มีประวัติการออกท่า

```python
player_a = [team_a[0], []]
player_b = [team_b[0], []]
```

ในแต่ละรอบของ loop โปรแกรมทำงานตามลำดับดังนี้

1. เพิ่มตัวอักษรตัวแรกของ `moves[i]` ลงในประวัติของผู้เล่นทีม A
2. เพิ่มตัวอักษรตัวที่สองของ `moves[i]` ลงในประวัติของผู้เล่นทีม B
3. ตรวจ `match_status[i]` ว่าต้องเปลี่ยนผู้เล่นหรือไม่
4. ถ้ามีผู้แพ้ ให้นำข้อมูลของผู้แพ้เพิ่มลงในผลลัพธ์ของทีมนั้น
   แล้วสร้างข้อมูลว่างสำหรับผู้เล่นคนถัดไป

เนื่องจากโปรแกรมบันทึกท่าก่อนตรวจสถานะ ท่าที่ทำให้ฝ่ายหนึ่งชนะครบ 2 ครั้ง
จึงถูกรวมอยู่ในประวัติของผู้เล่นคู่เดิมอย่างถูกต้อง ส่วนผู้ชนะยังใช้ข้อมูลเดิมต่อ
และสะสมท่าที่ออกกับคู่แข่งคนถัดไป

หลังประมวลผลทุกตา ผู้เล่นปัจจุบันอาจยังไม่ได้ถูกเพิ่มลงในผลลัพธ์
โปรแกรมจึงเพิ่มข้อมูลของผู้เล่นทั้งสองทีมเมื่อ `list` ท่าของคนนั้นไม่ว่าง

```python
if player_a[1] != []:
    team_a_moves.append(player_a)
if player_b[1] != []:
    team_b_moves.append(player_b)
```

เงื่อนไขนี้ยังป้องกันไม่ให้เพิ่มผู้เล่นคนถัดไปที่เพิ่งถูกเปลี่ยนเข้ามา
แต่ยังไม่ได้ออกท่าเลย

---

## ตัวอย่างการทำงาน

พิจารณาคำสั่งจากตัวอย่างในโจทย์

```python
player_moves("RSSPRR", ["A1", "A2", "A3"], ["B1", "B2", "B3"])
```

`get_moves()` แบ่งลำดับการเล่นได้เป็น `['RS', 'SP', 'RR']`

| ตา | ผู้เล่นทีม A | ผู้เล่นทีม B | คู่ท่า | ผลและสถานะหลังจบตา |
|---:|---|---|---|---|
| 1 | `A1` | `B1` | `RS` | A ชนะ คะแนน `1:0`, `NO CHANGE` |
| 2 | `A1` | `B1` | `SP` | A ชนะ คะแนนถึง `2:0`, `CHANGE TEAM B` |
| 3 | `A1` | `B2` | `RR` | เสมอ คะแนนคู่ใหม่ยังเป็น `0:0`, `NO CHANGE` |

หลังตาที่ 2 โปรแกรมบันทึก `B1` พร้อมท่า `['S', 'P']`
แล้วเปลี่ยนเป็น `B2` และรีเซ็ตคะแนน ส่วน `A1` เป็นผู้ชนะจึงเล่นต่อ
เมื่อลำดับการเล่นจบ โปรแกรมเพิ่มข้อมูลของ `A1` และ `B2` ที่ยังเป็นผู้เล่นปัจจุบัน
จึงได้ผลลัพธ์

```python
([['A1', ['R', 'S', 'R']]], [['B1', ['S', 'P']], ['B2', ['R']]])
```

---

## ข้อกำหนดของข้อมูลนำเข้า

โค้ดนี้ออกแบบมาสำหรับข้อมูลที่ถูกต้องตามโจทย์และไม่ได้ตรวจสอบความถูกต้องซ้ำ
ข้อมูลจากระบบตรวจจึงมีลักษณะสำคัญดังนี้

-   `playing_order` มีจำนวนตัวอักษรเป็นเลขคู่ เพราะหนึ่งตาต้องมีท่าครบสองทีม
-   ทุกตัวอักษรใน `playing_order` เป็น `R`, `S` หรือ `P`
-   `team_a` และ `team_b` ไม่ว่าง และมีจำนวนผู้เล่นเท่ากันตามกติกา
-   ลำดับการเล่นสิ้นสุดเมื่อเกมจบ จึงไม่มีการขอผู้เล่นถัดไปหลังทีมหมดผู้เล่น

โจทย์ข้อนี้ไม่มีการคำนวณทศนิยม การปัดเศษ หรือการจัดรูปแบบตัวเลข
สิ่งสำคัญคือโครงสร้างและลำดับของ `list` ที่คืนออกมาให้ตรงตามที่กำหนด

---

## การรับคำสั่งจากระบบตรวจ

บรรทัดสุดท้ายรับข้อความหนึ่งบรรทัด ลบช่องว่างหัวท้ายด้วย `.strip()`
แล้วใช้ `exec()` รันข้อความนั้นเป็นคำสั่ง Python

```python
exec(input().strip())
```

ระบบตรวจจึงส่งคำสั่งอย่าง `print(player_moves(...))` เข้ามาได้
โดย `player_moves()` ทำหน้าที่คืนค่า และ `print()` ในคำสั่ง input
ทำหน้าที่แสดงผล

> [!WARNING]
>
> `exec()` สามารถรันข้อความเป็นโปรแกรม Python ได้ทั้งหมด จึงเหมาะกับ input
> ที่ระบบตรวจเตรียมไว้เท่านั้น ไม่ควรใช้ `exec()` กับข้อความจากแหล่งที่ไม่น่าเชื่อถือ
> เพราะข้อความนั้นอาจสั่งให้โปรแกรมทำสิ่งที่เป็นอันตรายได้

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_3_Q3_02.py
# Problem   : RSP Team
# Author    : Worralop Srichainont
# Date      : 2025-07-15
# --------------------------------------------------

# Initialize constants for winning and losing combinations.
WINNING = ["RS", "SP", "PR"]
LOSING = ["SR", "PS", "RP"]


# Get moves of each turn from the playing order string.
def get_moves(playing_order):
    moves = []
    for i in range(0, len(playing_order), 2):
        move = playing_order[i : i + 2]
        moves.append(move)
    return moves


# Get the match status of each turn based on the moves.
def get_match_status(playing_order):
    # Initialize match status score for both teams.
    match_status = []
    score = [0, 0]
    # Get the moves from the playing order string.
    moves = get_moves(playing_order)

    # Iterate through each move to determine the match status.
    for move in moves:
        # Initialize status as "NO CHANGE".
        status = "NO CHANGE"
        # Update the score based on the move.
        if move in WINNING:
            score[0] += 1
        elif move in LOSING:
            score[1] += 1
        # Check if either team has reached the winning score of 2.
        if score[0] == 2:
            # Reset score and change team B.
            score = [0, 0]
            status = "CHANGE TEAM B"
        elif score[1] == 2:
            # Reset score and change team A.
            score = [0, 0]
            status = "CHANGE TEAM A"
        # Append the status to the match status list.
        match_status.append(status)
    # Return the final match status list.
    return match_status


# Get the next player in the team based on the current player.
def get_next_player(current_player, team):
    idx = team.index(current_player)
    return team[(idx + 1) % len(team)]


# Get the moves made by each player in the teams based on the playing order.
def player_moves(playing_order, team_a, team_b):
    # Initialize lists to store moves for each team.
    team_a_moves = []
    team_b_moves = []

    # Get the moves and match status from the playing order.
    moves = get_moves(playing_order)
    match_status = get_match_status(playing_order)

    # Initialize players for each team.
    player_a = [team_a[0], []]
    player_b = [team_b[0], []]

    # Iterate through the moves and match status to track player moves.
    for i in range(len(moves)):
        # Append the current move to the respective player's moves.
        player_a[1].append(moves[i][0])
        player_b[1].append(moves[i][1])

        # Check the match status to determine if a team change is needed.
        if match_status[i] == "CHANGE TEAM A":
            # Append the current player's moves to team A's moves.
            team_a_moves.append(player_a)
            # Switch to the next player in team A.
            player_a = [get_next_player(player_a[0], team_a), []]

        elif match_status[i] == "CHANGE TEAM B":
            # Append the current player's moves to team B's moves.
            team_b_moves.append(player_b)
            # Switch to the next player in team B.
            player_b = [get_next_player(player_b[0], team_b), []]

    # Append the final players' moves if they have made any moves.
    if player_a[1] != []:
        team_a_moves.append(player_a)
    if player_b[1] != []:
        team_b_moves.append(player_b)
    # Return the moves made by each team.
    return team_a_moves, team_b_moves


# Execute the input string as code
exec(input().strip())
```
