<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Cut and Shuffle ★★ (
      <a href="https://drive.google.com/file/d/1al5XKCb9Usd64yo8XfzuD__YfFuVWrxa/view?usp=drive_link">
        <code>05_List_31</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การแบ่งสำรับเป็นสองกอง**](#การแบ่งสำรับเป็นสองกอง)
-   [**คำสั่ง C: ตัดไพ่**](#คำสั่ง-c-ตัดไพ่)
-   [**คำสั่ง S: กรีดไพ่**](#คำสั่ง-s-กรีดไพ่)
-   [**การทำคำสั่งตามลำดับ**](#การทำคำสั่งตามลำดับ)
-   [**การแสดงผล**](#การแสดงผล)
-   [**Solution**](#solution)

---

## การแบ่งสำรับเป็นสองกอง

บรรทัดแรกเป็นชื่อไพ่จากบนลงล่าง คั่นกันด้วยช่องว่าง
`input().split()` จึงเปลี่ยนข้อมูลเป็นลิสต์ `deck` ที่สมาชิกแต่ละตัวคือ
ชื่อไพ่หนึ่งใบ

โจทย์รับรองว่าจำนวนไพ่เป็นจำนวนคู่ โปรแกรมจึงหาตำแหน่งกึ่งกลางด้วย

```python
half_idx = len(deck) // 2
```

ก่อนทำแต่ละคำสั่ง สำรับปัจจุบันถูกแบ่งด้วย slice เป็นสองกองที่มีขนาดเท่ากัน

```python
first_half = deck[:half_idx]
second_half = deck[half_idx:]
```

`first_half` คือครึ่งบนของสำรับ และ `second_half` คือครึ่งล่าง
จำนวนไพ่ไม่เปลี่ยนระหว่างการตัดหรือกรีด จึงคำนวณ `half_idx` เพียงครั้งเดียว
ก่อนเริ่มทำคำสั่งได้

## คำสั่ง C: ตัดไพ่

การตัดไพ่ย้ายครึ่งล่างขึ้นมาไว้หน้าครึ่งบน จึงเชื่อมสองลิสต์ในลำดับ
`second_half + first_half`

```python
deck = second_half + first_half
```

ตัวอย่างเช่น สำรับ `A J Q 10` แบ่งเป็น `A J` กับ `Q 10`
เมื่อทำคำสั่ง `C` จะได้ `Q 10 A J`

## คำสั่ง S: กรีดไพ่

การกรีดไพ่สลับหยิบไพ่ตำแหน่งเดียวกันจากครึ่งบนและครึ่งล่าง
โปรแกรมจึงสร้าง `deck` ใหม่ แล้ววน index ตั้งแต่ `0` ถึง
`half_idx - 1`

```python
deck = []
for i in range(half_idx):
    deck.append(first_half[i])
    deck.append(second_half[i])
```

ในแต่ละรอบจะใส่ `first_half[i]` ก่อน แล้วตามด้วย `second_half[i]`
เช่น สำรับ `A J Q 10` จะกลายเป็น `A Q J 10`

## การทำคำสั่งตามลำดับ

บรรทัดที่สองเป็นสตริงคำสั่ง โปรแกรมใช้ `for cmd in commands`
อ่านทีละตัวอักษร และนำผลของคำสั่งก่อนหน้าไปเป็นสำรับตั้งต้นของคำสั่งถัดไป
ดังนั้นลำดับคำสั่งมีผลต่อคำตอบ

ตัวอย่าง `CS` กับสำรับ `A J Q 10` ทำงานดังนี้

```text
เริ่มต้น: A J Q 10
C:       Q 10 A J
S:       Q A 10 J
```

โค้ดเปลี่ยนสำรับเฉพาะเมื่อ `cmd == "C"` หรือ `cmd == "S"`
ตัวอักษรอื่นจึงถูกละเลยตามข้อกำหนด รวมถึงช่องว่างภายในบรรทัดคำสั่งด้วย
เพราะช่องว่างก็เป็นอักขระที่ไม่ตรงกับสองเงื่อนไขนี้

หากบรรทัดคำสั่งว่าง `commands` จะเป็นสตริงว่าง ลูปไม่ทำงาน
และสำรับจะคงลำดับเดิม

## การแสดงผล

สุดท้าย `" ".join(deck)` เชื่อมชื่อไพ่ทั้งหมดด้วยช่องว่างหนึ่งช่อง
แล้ว `print()` แสดงไพ่จากบนลงล่างในบรรทัดเดียว

```python
print(" ".join(deck))
```

---

# Solution

```python
# --------------------------------------------------
# File Name : 05_List_31.py
# Problem   : Cut & Shuffle
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input card deck
deck = input().split()
half_idx = len(deck) // 2

# Input commands
commands = input().strip()

# Cut & Shuffle the deck
for cmd in commands:
    # Split the deck into two halves
    first_half = deck[:half_idx]
    second_half = deck[half_idx:]

    # Cut the deck
    if cmd == "C":
        deck = second_half + first_half
    # Shuffle the deck
    elif cmd == "S":
        deck = []
        for i in range(half_idx):
            deck.append(first_half[i])
            deck.append(second_half[i])

# Output the final deck
print(" ".join(deck))
```
