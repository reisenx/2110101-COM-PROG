<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Poker Hands ★★ (
      <a href="https://drive.google.com/file/d/1ybCeNooMRTp5wFQULhpAp9nw-TCpEhRa/view?usp=sharing">
        <code>2566_2_Q1_01</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิด**](#แนวคิด)
    -   [รูปแบบข้อมูลของไพ่](#รูปแบบข้อมูลของไพ่)
    -   [แยกค่าไพ่และดอกไพ่](#แยกค่าไพ่และดอกไพ่)
    -   [ตรวจไพ่เรียง](#ตรวจไพ่เรียง)
    -   [ตรวจไพ่ดอกเดียวกัน](#ตรวจไพ่ดอกเดียวกัน)
-   [**ลำดับการตัดสินคำตอบ**](#ลำดับการตัดสินคำตอบ)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

# แนวคิด

โจทย์ให้ไพ่ครั้งละ 5 ใบ แล้วให้จำแนกเป็น `Royal Straight Flush`,
`Straight Flush`, `Straight`, `Flush` หรือ `None` โดยรับจำนวนชุดไพ่ `N`
ก่อน จากนั้นจึงอ่านและแสดงคำตอบทีละชุดตามลำดับข้อมูลนำเข้า

## รูปแบบข้อมูลของไพ่

ไพ่หนึ่งใบแทนด้วยอักขระ 2 ตัว ตัวแรกคือค่าไพ่ และตัวที่สองคือดอกไพ่

-   ค่าไพ่เรียงจากมากไปน้อยเป็น `A`, `K`, `Q`, `J`, `X`, `9`, ...,
    `2` โดยใช้ `X` แทนเลข 10
-   ดอกไพ่ใช้ `C`, `H`, `D` และ `S`
-   ไพ่ทั้ง 5 ใบในข้อมูลนำเข้าเรียงจากค่ามากไปน้อยมาแล้ว

ตัวอย่าง `|5D|4D|3D|2D|AD|` หมายถึง 5, 4, 3, 2 และ A ดอกข้าวหลามตัด
กรณีนี้ A มีค่าน้อยกว่า 2 ได้

> [!WARNING]
> โปรแกรมนี้ไม่ได้เรียงไพ่ให้เอง และคาดว่าเลข 10 จะเขียนเป็น `X` เสมอ
> จึงต้องใช้รูปแบบข้อมูลตามโจทย์

## แยกค่าไพ่และดอกไพ่

เริ่มจากตัดเครื่องหมาย `|` ที่หัวและท้ายสตริงออกด้วย `strip("|")`
หลังจากนั้น ไพ่แต่ละใบยาว 2 ตัวและมี `|` คั่น 1 ตัว ทำให้ค่าไพ่ใบถัดไปอยู่ห่างกันครั้งละ 3 ตำแหน่ง

```python
cards = input().strip("|")
values = cards[::3]
suits = cards[1::3]
```

ถ้า `cards` เป็น `5D|4D|3D|2D|AD` จะได้

| ตัวแปร | ค่า | ความหมาย |
|:--|:--|:--|
| `values` | `5432A` | ค่าไพ่ทั้ง 5 ใบ |
| `suits` | `DDDDD` | ดอกไพ่ทั้ง 5 ใบ |

## ตรวจไพ่เรียง

โปรแกรมเก็บลำดับค่าไพ่ทั้งหมดไว้ในสตริง

```python
STRAIGHT = "AKQJX98765432A"
```

คำสั่ง `values in STRAIGHT` ตรวจว่าสตริงค่าไพ่ทั้ง 5 ตัวปรากฏติดกันใน
`STRAIGHT` หรือไม่ เช่น `QJX98` และ `5432A` ปรากฏติดกัน จึงเป็นไพ่เรียง
การวาง `A` ไว้ทั้งต้นและท้ายทำให้ตรวจได้ทั้ง A ที่สูงกว่า K และ A ที่ต่ำกว่า 2

ส่วน `Royal Straight Flush` ต้องมีค่าไพ่ตรงกับ `AKQJX` เท่านั้น จึงตรวจเพิ่มด้วย

```python
ROYAL_STRAIGHT = "AKQJX"
is_royal_straight = values == ROYAL_STRAIGHT
```

## ตรวจไพ่ดอกเดียวกัน

ไพ่จะเป็น Flush เมื่อดอกทั้ง 5 ใบเหมือนกัน โปรแกรมจึงเตรียมรูปแบบที่เป็นไปได้ไว้ครบทั้ง 4 ดอก

```python
FLUSH = ["CCCCC", "HHHHH", "DDDDD", "SSSSS"]
is_flush = suits in FLUSH
```

# ลำดับการตัดสินคำตอบ

ไพ่หนึ่งชุดอาจเป็นทั้งไพ่เรียงและไพ่ดอกเดียวกัน จึงต้องตรวจประเภทที่มีเงื่อนไขเฉพาะกว่าก่อน

| ลำดับ | เงื่อนไข | คำตอบ |
|:--:|:--|:--|
| 1 | ค่าไพ่เป็น `AKQJX` และดอกเหมือนกันทั้งหมด | `Royal Straight Flush` |
| 2 | ค่าไพ่เรียงและดอกเหมือนกันทั้งหมด | `Straight Flush` |
| 3 | ค่าไพ่เรียง แต่ดอกไม่ได้เหมือนกันทั้งหมด | `Straight` |
| 4 | ดอกเหมือนกันทั้งหมด แต่ค่าไพ่ไม่เรียง | `Flush` |
| 5 | ไม่ตรงกับเงื่อนไขด้านบน | `None` |

โครงสร้าง `if` ตามลำดับนี้ทำให้ `AKQJX` ดอกเดียวกันไม่ถูกตอบเพียง
`Straight Flush` และไพ่เรียงดอกเดียวกันไม่ถูกตอบเพียง `Straight`

# ตัวอย่างการทำงาน

พิจารณาข้อมูล `|5D|4D|3D|2D|AD|`

1.  แยกได้ `values = "5432A"` และ `suits = "DDDDD"`
2.  `"5432A" in STRAIGHT` เป็นจริง จึงเป็นไพ่เรียง
3.  `"DDDDD" in FLUSH` เป็นจริง จึงเป็นไพ่ดอกเดียวกัน
4.  ค่าไพ่ไม่ใช่ `AKQJX` จึงแสดง `Straight Flush`

ในทำนองเดียวกัน `|AC|KC|QC|JC|XC|` ได้ `values = "AKQJX"` และ
`suits = "CCCCC"` จึงแสดง `Royal Straight Flush`

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_2_Q1_01.py
# Problem   : Poker Hands
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------

# Initialize the order of straight and flush
STRAIGHT = "AKQJX98765432A"
ROYAL_STRAIGHT = "AKQJX"
FLUSH = ["CCCCC", "HHHHH", "DDDDD", "SSSSS"]

n = int(input())
for _ in range(n):
    # Extract values and suits from the card set
    cards = input().strip("|")
    values = cards[::3]
    suits = cards[1::3]

    # Check the values and suits for straight and flush
    is_flush = suits in FLUSH
    is_straight = values in STRAIGHT
    is_royal_straight = values == ROYAL_STRAIGHT

    # Output the type of poker hand
    if is_royal_straight and is_flush:
        print("Royal Straight Flush")
    elif is_straight and is_flush:
        print("Straight Flush")
    elif is_straight:
        print("Straight")
    elif is_flush:
        print("Flush")
    else:
        print("None")
```
