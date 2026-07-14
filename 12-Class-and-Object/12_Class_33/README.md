<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Piggy Bank 1 ★★★ (
      <a href="https://drive.google.com/file/d/1rqOJVzUwJG1c7o_rR6NtV8zpFgc-O79q/view?usp=drive_link">
        <code>12_Class_33</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**มองกระปุกออมสินเป็นออบเจ็กต์**](#มองกระปุกออมสินเป็นออบเจ็กต์)
-   [**การเพิ่มเหรียญแต่ละชนิด**](#การเพิ่มเหรียญแต่ละชนิด)
-   [**การหามูลค่ารวมและเปรียบเทียบ**](#การหามูลค่ารวมและเปรียบเทียบ)
-   [**การแปลงกระปุกเป็นข้อความ**](#การแปลงกระปุกเป็นข้อความ)
-   [**การรับคำสั่งจาก grader**](#การรับคำสั่งจาก-grader)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## มองกระปุกออมสินเป็นออบเจ็กต์

โจทย์ข้อนี้ให้เราสร้างคลาส `PiggyBank` เพื่อแทนกระปุกออมสินหนึ่งใบ
ออบเจ็กต์แต่ละตัวต้องจำจำนวนเหรียญของตัวเอง และมีเมธอดสำหรับเพิ่มเหรียญ
หามูลค่ารวม เปรียบเทียบกับกระปุกอีกใบ และแสดงจำนวนเหรียญ

โค้ดเฉลยเก็บสถานะของกระปุกไว้ใน dictionary ชื่อ `self.coins`

```python
self.coins = {1: 0, 2: 0, 5: 0, 10: 0}
```

-   key คือชนิดของเหรียญ ได้แก่ `1`, `2`, `5` และ `10` บาท
-   value คือจำนวนเหรียญชนิดนั้น โดยเริ่มต้นทุกชนิดที่ `0`

เอกสารโจทย์เสนอให้มีตัวแปร 4 ตัวสำหรับเก็บจำนวนเหรียญทั้ง 4 ชนิด
แต่โค้ดเฉลยรวบรวมข้อมูลเดียวกันไว้ใน dictionary หนึ่งตัวแทน
จึงเข้าถึงจำนวนเหรียญชนิดราคา `v` บาทได้ด้วย `self.coins[v]`

## การเพิ่มเหรียญแต่ละชนิด

โจทย์กำหนดเมธอดเพิ่มเหรียญแยกตามชนิด เมธอดทุกตัวรับ `n`
ซึ่งเป็นจำนวนเหรียญที่ต้องการเพิ่ม แล้วบวกเข้าไปในช่องของเหรียญชนิดนั้น

| เมธอด | เหรียญที่เพิ่ม | คำสั่งที่เปลี่ยนสถานะ |
|---|---:|---|
| `add1(n)` | 1 บาท | `self.coins[1] += n` |
| `add2(n)` | 2 บาท | `self.coins[2] += n` |
| `add5(n)` | 5 บาท | `self.coins[5] += n` |
| `add10(n)` | 10 บาท | `self.coins[10] += n` |

ตัวอย่างเช่น ถ้าเดิมมีเหรียญ 5 บาทอยู่ `2` เหรียญ เมื่อเรียก
`p1.add5(3)` ค่า `p1.coins[5]` จะเพิ่มเป็น `5`

## การหามูลค่ารวมและเปรียบเทียบ

หากให้ $n_1$, $n_2$, $n_5$ และ $n_{10}$ เป็นจำนวนเหรียญแต่ละชนิด
มูลค่ารวมของกระปุกคือ

$$
\text{total} = (1 \times n_1) + (2 \times n_2) + (5 \times n_5) + (10 \times n_{10})
$$

สูตรนี้ตรงกับนิพจน์ Python ใน `__int__()` ดังนี้

```python
(
    (10 * self.coins[10])
    + (5 * self.coins[5])
    + (2 * self.coins[2])
    + (1 * self.coins[1])
)
```

เมื่อเขียน `int(p1)` Python จะเรียก `p1.__int__()` ให้อัตโนมัติ
ผลลัพธ์จึงเป็นจำนวนเต็มที่แทนมูลค่าเงินทั้งหมด ไม่ใช่จำนวนเหรียญทั้งหมด

ส่วนการเขียน `p1 < p2` จะเรียก `p1.__lt__(p2)` ซึ่งเปรียบเทียบ
`int(p1) < int(p2)` ดังนั้นผลลัพธ์เป็น `True` ก็ต่อเมื่อมูลค่าเงินใน `p1`
น้อยกว่ามูลค่าเงินใน `p2` อย่างเคร่งครัด หากมูลค่าเท่ากันจะได้ `False`

## การแปลงกระปุกเป็นข้อความ

เมื่อใช้ `str(p1)` หรือ `print(p1)` Python จะเรียก `__str__()`
เพื่อสร้างข้อความรูปแบบต่อไปนี้

```text
{1:จำนวนเหรียญ, 2:จำนวนเหรียญ, 5:จำนวนเหรียญ, 10:จำนวนเหรียญ}
```

dictionary ถูกสร้างโดยใส่ key ตามลำดับ `1`, `2`, `5`, `10`
และ `self.coins.items()` วนตามลำดับนั้น จึงได้ผลลัพธ์ที่แน่นอน เช่น
`{1:1, 2:2, 5:3, 10:4}` แม้เหรียญบางชนิดมีจำนวน `0`
ก็ยังต้องแสดงชนิดนั้นออกมา

## การรับคำสั่งจาก grader

โปรแกรมรับข้อมูลทั้งหมด 2 บรรทัดเป็นชุดคำสั่ง `cmd1` และ `cmd2`
โดยแต่ละบรรทัดอาจมีหลายคำสั่งคั่นด้วยเครื่องหมาย semicolon (`;`)
ทั้งสองบรรทัดสามารถอ้างถึง `p1` หรือ `p2` ได้ และจะทำงานตามลำดับบรรทัด

ตัวอย่างข้อมูลหนึ่งบรรทัด

```text
p1.add1(2);p1.add10(1);print(int(p1), p1)
```

คำสั่ง `input().split(";")` แยกบรรทัดนี้เป็นคำสั่งย่อย จากนั้นลูปเรียก
`eval(c)` ทีละคำสั่ง จึงเพิ่มเหรียญและแสดงผลตามลำดับที่ผู้ตรวจส่งมา
ออบเจ็กต์ `p1` และ `p2` ถูกสร้างก่อนประมวลผลคำสั่งทั้งสองบรรทัด

> [!WARNING]
>
> `eval()` สามารถประมวลผลโค้ด Python ที่อยู่ในข้อความได้
> โจทย์นี้ใช้กับคำสั่งจาก grader ที่เชื่อถือได้เท่านั้น
> ไม่ควรนำรูปแบบนี้ไปใช้กับข้อมูลจากผู้ใช้ที่ไม่ทราบแหล่งที่มา

## ตัวอย่างการทำงาน

สมมติเรียกคำสั่งต่อไปนี้

```python
p1.add1(1)
p1.add2(2)
p1.add5(3)
p1.add10(4)
```

มูลค่ารวมคือ

$$
(1 \times 1) + (2 \times 2) + (5 \times 3) + (10 \times 4) = 60
$$

ดังนั้น `int(p1)` ได้ `60` และ `str(p1)` ได้
`{1:1, 2:2, 5:3, 10:4}` ตามลำดับชนิดเหรียญที่โจทย์กำหนด

---

# Solution

```python
# --------------------------------------------------
# File Name : 12_Class_33.py
# Problem   : Piggy Bank 1
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------


class PiggyBank:
    # __init__ method
    # Initialize the 'PiggyBank' object with a dictionary to store coins
    def __init__(self):
        self.coins = {1: 0, 2: 0, 5: 0, 10: 0}

    # add1 method
    # This method adds 'n' coins of 1 baht to the piggy bank
    def add1(self, n):
        self.coins[1] += n

    # add2 method
    # This method adds 'n' coins of 2 baht to the piggy bank
    def add2(self, n):
        self.coins[2] += n

    # add5 method
    # This method adds 'n' coins of 5 baht to the piggy bank
    def add5(self, n):
        self.coins[5] += n

    # add10 method
    # This method adds 'n' coins of 10 baht to the piggy bank
    def add10(self, n):
        self.coins[10] += n

    # __int__ method
    # This calculates the total amount of money in the piggy bank
    def __int__(self):
        return (
            (10 * self.coins[10])
            + (5 * self.coins[5])
            + (2 * self.coins[2])
            + (1 * self.coins[1])
        )

    # __lt__ method
    # This compares two PiggyBank objects based on their total amount of money
    def __lt__(self, rhs):
        return int(self) < int(rhs)

    # __str__ method
    # This converts the PiggyBank object to a string representation of its coins
    def __str__(self):
        result = []
        for coin_type, coin_count in self.coins.items():
            result.append(f"{coin_type}:{coin_count}")
        return "{" + ", ".join(result) + "}"


# Output
cmd1 = input().split(";")
cmd2 = input().split(";")
p1 = PiggyBank()
p2 = PiggyBank()
for c in cmd1:
    eval(c)
for c in cmd2:
    eval(c)
```
