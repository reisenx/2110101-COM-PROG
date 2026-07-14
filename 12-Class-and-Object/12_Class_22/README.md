<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Card ★★ (
      <a href="https://drive.google.com/file/d/1dNnh5XDHG2dWd4HDvYyNcam2qJ9aHqqf/view?usp=drive_link">
        <code>12_Class_22</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การออกแบบคลาส Card**](#การออกแบบคลาส-card)
-   [**คะแนนไพ่และผลรวม**](#คะแนนไพ่และผลรวม)
-   [**ลำดับของไพ่**](#ลำดับของไพ่)
-   [**ลำดับข้อมูลเข้าและข้อมูลส่งออก**](#ลำดับข้อมูลเข้าและข้อมูลส่งออก)
-   [**Solution**](#solution)

---

## การออกแบบคลาส Card

ไพ่หนึ่งใบมีข้อมูล 2 ส่วน คือค่าของไพ่ `value` เช่น `"A"`, `"10"`, `"K"`
และดอกไพ่ `suit` เช่น `"club"` หรือ `"spade"` เมท็อด `__init__`
เก็บข้อมูลทั้งสองไว้ใน object

```python
def __init__(self, value, suit):
    self.value = value
    self.suit = suit
```

เมื่อ `print()` ไพ่ Python จะเรียก `__str__` ซึ่งใช้ f-string สร้างข้อความรูปแบบ
`(value suit)` โดยมีช่องว่างหนึ่งช่องระหว่างค่าและดอก

```python
def __str__(self):
    return f"({self.value} {self.suit})"
```

ตัวอย่างเช่น `Card("K", "heart")` จะแสดงเป็น `(K heart)` โดยไม่มี comma
หรือเครื่องหมายคำพูด

---

## คะแนนไพ่และผลรวม

คะแนนและลำดับความสูงของไพ่เป็น **คนละกติกา** กัน เมท็อด `getScore`
อ่านคะแนนจาก dictionary `SCORES` ตามตารางนี้

| ค่าของไพ่ | คะแนนจาก `getScore()` |
|---|---:|
| `A` | `1` |
| `2` ถึง `10` | เท่ากับตัวเลขบนไพ่ |
| `J`, `Q`, `K` | `10` |

ดังนั้น `A` มีคะแนนเพียง `1` แม้จะอยู่เกือบสูงสุดในลำดับไพ่ และ `2`
มีคะแนน `2` แม้จะเป็นไพ่สูงสุดตามกติกาการเรียงของโจทย์

เมท็อด `sum` หาผลรวมคะแนนของไพ่สองใบแล้ว mod ด้วย `10`
จึงเก็บไว้เฉพาะหลักหน่วย

$$
\text{ผลรวมไพ่สองใบ}=(\text{score}_1+\text{score}_2)\bmod 10
$$

ตรงกับ Python ดังนี้

```python
return (self.getScore() + other.getScore()) % 10
```

ตัวอย่างเช่น ไพ่ `J spade` มีคะแนน `10` และ `5 diamond` มีคะแนน `5`

```text
(10 + 5) % 10 = 5
```

โปรแกรมหลักเรียก `sum` กับไพ่ที่อยู่ติดกันในลิสต์ ได้แก่คู่ตำแหน่ง `0, 1`,
คู่ตำแหน่ง `1, 2` ไปจนถึงคู่ตำแหน่ง `n - 2, n - 1` จึงมีผลรวมทั้งหมด
`n - 1` ค่า การเขียน `Card.sum(cards[i], cards[i + 1])` ใช้ได้เพราะส่งไพ่ใบแรก
เข้าไปเป็น `self` และไพ่ใบถัดไปเป็น `other`

---

## ลำดับของไพ่

`list.sort()` ต้องทราบว่า object ใดน้อยกว่า object ใด Python จึงเรียกเมท็อด
`__lt__` ของคลาส `Card` ในการเปรียบเทียบ

โจทย์ไม่ได้เรียงตามคะแนนจาก `getScore()` แต่ใช้ลำดับค่าของไพ่ดังนี้

```text
3 < 4 < 5 < 6 < 7 < 8 < 9 < 10 < J < Q < K < A < 2
```

dictionary `VALUE_ORDER` แปลงลำดับนี้เป็นเลข `0` ถึง `12`
ทำให้เปรียบเทียบค่าของไพ่ได้โดยตรง ถ้าค่าของไพ่ไม่เท่ากัน `__lt__`
จะตัดสินจากเลขนี้ทันที

เมื่อไพ่สองใบมีค่าเท่ากัน จึงค่อยเปรียบเทียบดอกตามลำดับ

```text
club < diamond < heart < spade
```

ซึ่ง `SUIT_ORDER` แทนด้วยเลข `0` ถึง `3` เช่นกัน ดังนั้น `K club` น้อยกว่า
`K heart` แต่ `A club` ยังมากกว่า `K spade` เพราะต้องเปรียบเทียบค่าของไพ่ก่อน
ดอกไพ่

หลังจาก `cards.sort()` ลิสต์จะเรียงจากไพ่น้อยไปไพ่มาก และ `print(cards[i])`
จะแสดงไพ่แต่ละใบด้วยรูปแบบจาก `__str__`

---

## ลำดับข้อมูลเข้าและข้อมูลส่งออก

บรรทัดแรกของข้อมูลเข้าเป็นจำนวนไพ่ `n` จากนั้นอีก `n` บรรทัดเป็น `value suit`
ของไพ่ตามลำดับที่รับเข้ามา เช่น

```text
3
A spade
K club
7 diamond
```

โปรแกรมแสดงผลทั้งหมด 3 ส่วน โดยมีบรรทัด `----------` คั่นแต่ละส่วน

1. แสดงคะแนน `getScore()` ของไพ่แต่ละใบตามลำดับข้อมูลเข้า จำนวน `n` บรรทัด
2. แสดง `sum` ของไพ่ทุกคู่ที่ติดกัน จำนวน `n - 1` บรรทัด
3. เรียงไพ่แล้วแสดงจากน้อยไปมาก จำนวน `n` บรรทัด

จึงมีผลลัพธ์รวม `3n + 1` บรรทัด ตัวอย่างจากโจทย์รับ `A spade`, `K heart`,
`K club`, `7 diamond`, `2 spade` ส่วนแรกจะแสดงคะแนน `1, 10, 10, 7, 2`
ส่วนผลรวมไพ่ติดกันเป็น `1, 0, 7, 9` และส่วนสุดท้ายเรียงเป็น
`7 diamond`, `K club`, `K heart`, `A spade`, `2 spade`

> [!NOTE]
>
> ถ้ามีไพ่เพียงใบเดียว ลูป `range(n - 1)` จะไม่แสดงผลรวมของคู่ไพ่
> แต่โปรแกรมยังแสดงเส้นคั่นทั้งสองบรรทัดและแสดงไพ่ใบนั้นในส่วนสุดท้าย

---

# Solution

```python
# --------------------------------------------------
# File Name : 12_Class_22.py
# Problem   : Card
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------

# List of scores for each card value and their order
SCORES = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}
VALUE_ORDER = {
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
SUIT_ORDER = {"club": 0, "diamond": 1, "heart": 2, "spade": 3}


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

    # getScore method
    # Get the score of the card based on its value
    def getScore(self):
        return SCORES[self.value]

    # sum method
    # Calculate the sum of scores of two cards and return the last digit
    def sum(self, other):
        return (self.getScore() + other.getScore()) % 10

    # __lt__ method
    # Compare two card objects based on their value and suit
    # Return True if self is less than rhs, otherwise return False
    def __lt__(self, rhs):
        # Compare by value first
        if VALUE_ORDER[self.value] < VALUE_ORDER[rhs.value]:
            return True
        elif VALUE_ORDER[self.value] > VALUE_ORDER[rhs.value]:
            return False
        # If values are equal, compare by suit
        return SUIT_ORDER[self.suit] < SUIT_ORDER[rhs.suit]


# Input card number
n = int(input())

# Input cards and store them in a list
cards = []
for _ in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

# Output the scores of each card
for i in range(n):
    print(cards[i].getScore())
print("----------")

# Output the sum of scores of adjacent cards
for i in range(n - 1):
    print(Card.sum(cards[i], cards[i + 1]))
print("----------")

# Output the cards sorted by value and suit
cards.sort()
for i in range(n):
    print(cards[i])
```
