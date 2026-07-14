<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Next Card ★★ (
      <a href="https://drive.google.com/file/d/1sBvznMMYRgkH8ogMi8hYEDrj5pDEQcJ9/view?usp=drive_link">
        <code>12_Class_23</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิดของคลาส `Card`**](#แนวคิดของคลาส-card)
-   [**การแปลงไพ่เป็นหมายเลขลำดับ**](#การแปลงไพ่เป็นหมายเลขลำดับ)
-   [**เมท็อด `next1` และ `next2`**](#เมท็อด-next1-และ-next2)
-   [**ลำดับการรับและแสดงผล**](#ลำดับการรับและแสดงผล)
-   [**ตัวอย่างการหาไพ่ใบถัดไป**](#ตัวอย่างการหาไพ่ใบถัดไป)
-   [**Solution**](#solution)

---

## แนวคิดของคลาส `Card`

ไพ่หนึ่งใบมีข้อมูลประจำออบเจ็กต์ 2 ค่า ได้แก่

-   `value` คือค่าของไพ่ เช่น `"3"`, `"10"`, `"J"` หรือ `"A"`
-   `suit` คือดอกของไพ่ ได้แก่ `"club"`, `"diamond"`, `"heart"` และ
    `"spade"`

เมท็อด `__init__` จึงเก็บค่าที่รับมาไว้ใน `self.value` และ `self.suit`
ส่วน `__str__` กำหนดรูปแบบการแสดงไพ่ให้เป็น `(value suit)` เช่น
`(10 heart)` โดยมีช่องว่างหนึ่งตำแหน่งระหว่างค่าและดอก

ลำดับของค่าหน้าไพ่และดอกไพ่ในโจทย์เป็นดังนี้

| ส่วนของไพ่ | ลำดับจากน้อยไปมาก |
|---|---|
| ค่า | `3`, `4`, `5`, ..., `10`, `J`, `Q`, `K`, `A`, `2` |
| ดอก | `club`, `diamond`, `heart`, `spade` |

ดังนั้นไพ่ทุกค่าจะเรียงครบทั้ง 4 ดอกก่อนเปลี่ยนเป็นค่าถัดไป เช่น
`(5 club)`, `(5 diamond)`, `(5 heart)`, `(5 spade)` แล้วจึงเป็น
`(6 club)`

---

## การแปลงไพ่เป็นหมายเลขลำดับ

โปรแกรมกำหนดหมายเลขให้ค่าหน้าไพ่ตั้งแต่ `0` ถึง `12` และกำหนดหมายเลขให้
ดอกไพ่ตั้งแต่ `0` ถึง `3` ผ่าน `VALUE_TO_ORDER` และ `SUIT_TO_ORDER`
จากนั้นรวมสองส่วนให้เป็นหมายเลขของไพ่ตั้งแต่ `0` ถึง `51` ด้วยสูตร

$$
\text{card\_order}
= 4 \times \text{value\_order} + \text{suit\_order}
$$

ซึ่งตรงกับคำสั่ง Python

```python
card_order = (value_order * 4) + suit_order
```

ไพ่ใบถัดไปมีหมายเลข

$$
\text{next\_order} = (\text{card\_order} + 1) \bmod 52
$$

หรือ `card_order = (card_order + 1) % 52` ใน Python การหารเอาเศษด้วย
`52` ทำให้หมายเลขถัดจาก `51` กลับเป็น `0` พอดี จึงได้ว่าไพ่ถัดจาก
`(2 spade)` คือ `(3 club)`

เมื่อได้หมายเลขไพ่แล้ว โปรแกรมแยกกลับเป็นหมายเลขค่าและดอกด้วย

```python
value_order = card_order // 4
suit_order = card_order % 4
```

`// 4` บอกว่าไพ่อยู่ในกลุ่มค่าหน้าใด ส่วน `% 4` บอกดอกภายในกลุ่มนั้น
แล้ว `ORDER_TO_VALUE` และ `ORDER_TO_SUIT` จะแปลงหมายเลขทั้งสองกลับเป็น
ข้อความ

---

## เมท็อด `next1` และ `next2`

เมท็อดทั้งสองหาไพ่ใบถัดไปเหมือนกัน แต่มีผลต่อออบเจ็กต์ต่างกัน

-   `next1()` สร้างและคืน `Card` ใบใหม่ โดยไม่แก้ `value` หรือ `suit`
    ของไพ่เดิม
-   `next2()` แก้ `value` และ `suit` ของออบเจ็กต์เดิม และไม่มีคำสั่ง
    `return` จึงคืนค่า `None` โดยปริยาย

ในเฉลย `next2()` เรียก `self.next1()` เพื่อหาไพ่ใบถัดไป แล้วคัดลอก
`value` และ `suit` จากผลลัพธ์กลับมายัง `self` ดังนั้นตัวแปรที่อ้างถึง
ออบเจ็กต์เดิมจะเห็นค่าที่เปลี่ยนไป

> [!NOTE]
>
> โจทย์อธิบาย `next2()` ว่าแก้ไพ่เดิมโดยไม่สร้างออบเจ็กต์ใหม่
> ส่วนโค้ดเฉลยเรียก `next1()` จึงมี `Card` ชั่วคราวเกิดขึ้นภายในเมท็อด
> อย่างไรก็ตาม พฤติกรรมที่ผู้เรียกได้รับยังตรงตามโจทย์ คือไพ่เดิมถูกแก้ไข
> และไม่มีออบเจ็กต์ไพ่ใบใหม่ถูกคืนออกมาจาก `next2()`

---

## ลำดับการรับและแสดงผล

บรรทัดแรกรับจำนวนไพ่ `n` แล้วอีก `n` บรรทัดรับ `value suit` ของไพ่
แต่ละใบตามลำดับ เพื่อนำไปสร้างลิสต์ `cards`

ผลลัพธ์มีทั้งหมด $3n+2$ บรรทัด แบ่งเป็น 3 ช่วง

1. เรียก `next1()` ของไพ่ทุกใบและพิมพ์ไพ่ใบถัดไป จากนั้นพิมพ์
   `----------`
2. พิมพ์ไพ่เดิมใน `cards` เพื่อแสดงว่า `next1()` ไม่ได้แก้ไขออบเจ็กต์
   จากนั้นพิมพ์ `----------`
3. เรียก `next2()` สองครั้งต่อไพ่หนึ่งใบ แล้วพิมพ์ไพ่เดิมที่ถูกเลื่อนไป
   ข้างหน้า 2 ลำดับ

---

## ตัวอย่างการหาไพ่ใบถัดไป

สำหรับ `(5 diamond)` จะมี `value_order = 2` และ `suit_order = 1`
จึงได้หมายเลข `2 * 4 + 1 = 9` หมายเลขถัดไปคือ `10` เมื่อแยกกลับด้วย
`10 // 4 = 2` และ `10 % 4 = 2` จึงได้ `(5 heart)`

อีกสองกรณีที่ควรสังเกตคือ

-   `(10 spade)` อยู่ท้ายกลุ่มของค่า `10` ไพ่ใบถัดไปจึงเป็น `(J club)`
-   `(2 spade)` มีหมายเลข `51` เมื่อคำนวณ `(51 + 1) % 52` จะได้ `0`
    จึงวนกลับไปเป็น `(3 club)`

---

# Solution

```python
# --------------------------------------------------
# File Name : 12_Class_23.py
# Problem   : Next Card
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# List of orders for each card value and suit
VALUE_TO_ORDER = {
    "3": 0,
    "4": 1,
    "5": 2,
    "6": 3,
    "7": 4,
    "8": 5,
    "9": 6,
    "10": 7,
    "J": 8,
    "Q": 9,
    "K": 10,
    "A": 11,
    "2": 12,
}
SUIT_TO_ORDER = {"club": 0, "diamond": 1, "heart": 2, "spade": 3}
ORDER_TO_VALUE = {
    0: "3",
    1: "4",
    2: "5",
    3: "6",
    4: "7",
    5: "8",
    6: "9",
    7: "10",
    8: "J",
    9: "Q",
    10: "K",
    11: "A",
    12: "2",
}
ORDER_TO_SUIT = {0: "club", 1: "diamond", 2: "heart", 3: "spade"}


class Card:
    # __init__ method
    # Initialize the card object with value and suit
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # __str__ method
    # Convert the card object to a string representation
    def __str__(self):
        return f"({self.value} {self.suit})"

    # next1 method
    # This method will return the next card in order as a new Card object
    def next1(self):
        # Get the current order of the card
        value_order = VALUE_TO_ORDER[self.value]
        suit_order = SUIT_TO_ORDER[self.suit]
        card_order = (value_order * 4) + suit_order
        # Calculate the next card's order
        card_order = (card_order + 1) % 52
        value_order = card_order // 4
        suit_order = card_order % 4
        # Return the next card as a new Card object
        return Card(ORDER_TO_VALUE[value_order], ORDER_TO_SUIT[suit_order])

    # next2 method
    # This method will update the current card to the next card in order
    def next2(self):
        next_card = self.next1()
        self.value = next_card.value
        self.suit = next_card.suit


# Input card number
n = int(input())

# Input cards and store them in a list
cards = []
for _ in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

# Output the next card for each card in the list
for i in range(n):
    print(cards[i].next1())
print("----------")

# Output the current cards
for i in range(n):
    print(cards[i])
print("----------")

# Update each card to the next card in order and print the updated cards
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
```
