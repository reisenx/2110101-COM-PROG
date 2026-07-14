<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Cash ★★★ (
      <a href="https://drive.google.com/file/d/1pfFCHg9Yo25WSBDuLaZHa2IGHpXGuupL/view?usp=drive_link">
        <code>08_Dict_31</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การแทนเงินด้วย Dictionary**](#การแทนเงินด้วย-dictionary)
-   [**การหาจำนวนเงินรวม**](#การหาจำนวนเงินรวม)
-   [**การเติมเงินเข้ากระเป๋า**](#การเติมเงินเข้ากระเป๋า)
-   [**การจ่ายเงินออกจากกระเป๋า**](#การจ่ายเงินออกจากกระเป๋า)
-   [**ข้อควรระวังเรื่องลำดับของ Dictionary**](#ข้อควรระวังเรื่องลำดับของ-dictionary)
-   [**การรับคำสั่งจาก Grader**](#การรับคำสั่งจาก-grader)
-   [**Solution**](#solution)

---

## การแทนเงินด้วย Dictionary

โจทย์ใช้ `dict` แทนเงินในกระเป๋า โดย key คือมูลค่าของเหรียญหรือธนบัตร
และ value คือจำนวนที่มี เช่น

```python
pocket = {100: 5, 50: 2, 10: 5, 1: 15}
```

หมายถึงมีธนบัตร 100 บาท 5 ใบ, ธนบัตร 50 บาท 2 ใบ,
เหรียญ 10 บาท 5 เหรียญ และเหรียญ 1 บาท 15 เหรียญ
เมื่อวนด้วย `pocket.items()` ตัวแปร `money` จะเก็บมูลค่า
ส่วน `quantity` จะเก็บจำนวนของเงินมูลค่านั้น

ฟังก์ชัน `take()` แก้ไข `pocket` ตัวเดิมและคืนกระเป๋าใบนั้นกลับมา
ส่วน `pay()` จะแก้ไข `pocket` ตัวเดิมเมื่อจ่ายสำเร็จ
แต่ค่าที่คืนจาก `pay()` คือ `dict` ของเงินที่จ่ายออกไป ไม่ใช่กระเป๋า
จึงควรเก็บผลของ `pay()` แยกจากตัวแปร `pocket`

---

## การหาจำนวนเงินรวม

ฟังก์ชัน `total(pocket)` นำมูลค่าของเงินแต่ละชนิดคูณกับจำนวนที่มี
แล้วบวกผลทั้งหมดเข้าด้วยกัน

$$
\text{total} = \sum (\text{money} \times \text{quantity})
$$

สูตรนี้ตรงกับคำสั่ง Python
`total_money += money * quantity` ภายในลูป

ตัวอย่าง `{100: 2, 50: 2, 5: 2, 1: 2}` มีเงินรวม

$$
(100 \times 2) + (50 \times 2) + (5 \times 2) + (1 \times 2) = 312
$$

ฟังก์ชันจึงคืนจำนวนเต็ม `312` และลำดับของ key ใน `dict`
ไม่มีผลกับการหาผลรวม

---

## การเติมเงินเข้ากระเป๋า

ฟังก์ชัน `take(pocket, money_in)` วนดูเงินแต่ละชนิดใน `money_in`
ถ้ามูลค่านั้นยังไม่มีใน `pocket` จะสร้าง key ใหม่โดยกำหนดจำนวนเริ่มต้นเป็น
`0` ก่อน แล้วจึงบวกจำนวนที่รับเข้ามา

```python
if money not in pocket:
    pocket[money] = 0
pocket[money] += quantity
```

เช่น เริ่มจาก `pocket = {100: 5}` แล้วรับ
`money_in = {100: 2, 1: 3}`

| มูลค่า | จำนวนเดิม | จำนวนที่รับเพิ่ม | จำนวนใหม่ |
|:---:|---:|---:|---:|
| `100` | 5 | 2 | 7 |
| `1` | 0 | 3 | 3 |

หลังเรียกฟังก์ชัน `pocket` จึงเป็น `{100: 7, 1: 3}`
และฟังก์ชันคืน `pocket` ตัวเดียวกันกลับมาด้วย

ถ้ารับเงินจำนวน `0` ของมูลค่าที่ยังไม่มี key นั้นก็ยังถูกสร้างไว้
ตัวอย่างในโจทย์จึงได้ `{100: 5, 1: 0}`
นอกจากนี้ key ใหม่จะถูกเพิ่มไว้ท้าย `dict`
ซึ่งมีผลต่อการทำงานของ `pay()` ที่อธิบายในหัวข้อถัดไป

---

## การจ่ายเงินออกจากกระเป๋า

ฟังก์ชัน `pay(pocket, money_out)` ใช้วิธี greedy
คือพยายามหยิบเงินตามลำดับที่วนพบ โดยหยิบแต่ละมูลค่าให้มากที่สุด
เท่าที่จำนวนเงินคงเหลือและจำนวนที่มีอนุญาต

ก่อนเริ่มเลือกเงิน โค้ดตรวจ `total(pocket) >= money_out`
ถ้าเงินรวมยังน้อยกว่าที่ต้องการ จะคืน `{}` ทันทีโดยไม่แก้ไข `pocket`

สำหรับเงินมูลค่า `d` ที่มีอยู่ `q` ชิ้น และยอดที่ยังต้องจ่ายเท่ากับ `r`
จำนวนชิ้นที่จะหยิบคำนวณจาก

$$
q_{\text{used}}
=
\min\left(\left\lfloor\frac{r}{d}\right\rfloor, q\right)
$$

ใน Python เขียนเป็น
`quantity_used = min(money_out // money, quantity)`
โดย `money_out // money` บอกจำนวนชิ้นสูงสุดที่ยอดคงเหลือจ่ายได้
และ `min()` ป้องกันไม่ให้หยิบเกินจำนวนที่มีในกระเป๋า
จากนั้นลดเงินที่ยังต้องจ่ายด้วย
`money_out -= money * quantity_used`

ตัวอย่าง จ่าย 12 บาทจาก `{10: 5, 1: 7}`

| มูลค่า | จำนวนที่มี | ยอดก่อนหยิบ | จำนวนที่หยิบ | ยอดหลังหยิบ |
|---:|---:|---:|---:|---:|
| 10 | 5 | 12 | `min(12 // 10, 5) = 1` | 2 |
| 1 | 7 | 2 | `min(2 // 1, 7) = 2` | 0 |

ยอดคงเหลือเป็น `0` จึงคืนเงินที่จ่ายเป็น `{10: 1, 1: 2}`
แล้วหักออกจากกระเป๋า ทำให้เหลือ `{10: 4, 1: 5}`
key ใน `pocket_pay` ถูกเพิ่มตามลำดับที่วน `pocket`
ดังนั้นลำดับที่เห็นเมื่อแสดงผล `dict` ที่คืนมาก็เป็นลำดับเดียวกัน

โค้ดยังไม่หักเงินออกจาก `pocket` ระหว่างที่กำลังทดลองเลือก
แต่เก็บสิ่งที่เลือกไว้ใน `pocket_pay` ก่อน
เมื่อยอดคงเหลือเป็น `0` จึงค่อยหักเงินจริงทั้งหมด
ลักษณะนี้ทำให้การจ่ายที่ล้มเหลวสามารถยกเลิกได้โดยไม่ต้องคืนเงินทีละรายการ

ตัวอย่าง ถ้าจ่าย 18 บาทจาก `{10: 5, 1: 7}`
วิธี greedy จะเลือก 10 บาท 1 ชิ้นและ 1 บาท 7 ชิ้น
แต่ยังขาดอีก 1 บาท จึงคืน `{}` และเก็บ `pocket` เดิมไว้ครบ
ในทางกลับกัน การจ่าย 57 บาทจะใช้เงินทั้งหมดและคืน
`{10: 5, 1: 7}` ส่วน `pocket` จะเหลือ `{10: 0, 1: 0}`
เพราะโค้ดไม่ลบ key ที่มีจำนวนเหลือศูนย์

ถ้าขอจ่าย `0` บาท โค้ดจะคืน `{}` และไม่เปลี่ยนกระเป๋า
ซึ่งมีรูปแบบผลลัพธ์เหมือนกรณีจ่ายไม่สำเร็จ

---

## ข้อควรระวังเรื่องลำดับของ Dictionary

> [!WARNING]
>
> PDF กำหนดให้เลือกเงินมูลค่าสูงสุดก่อน แต่โค้ด Solution ไม่ได้เรียง key
> และวนด้วย `pocket.items()` ตามลำดับที่ key ถูกเพิ่มเข้า `dict`
> เพื่อให้พฤติกรรมตรงกับโจทย์ จึงต้องเตรียม key ใน `pocket`
> จากมูลค่าสูงไปต่ำตั้งแต่ต้น

ตัวอย่าง `pocket = {1: 7, 10: 5}` มีเงินพอจ่าย 12 บาท
แต่โค้ดจะพิจารณาเหรียญ 1 บาทก่อน ใช้ไป 7 เหรียญ แล้วเหลือยอด 5 บาท
ซึ่งธนบัตร 10 บาทจ่ายไม่ได้ จึงคืน `{}`
แม้คำตอบ `{10: 1, 1: 2}` จะมีอยู่ก็ตาม

`take()` จะเพิ่มมูลค่าใหม่ไว้ท้าย `dict` ด้วย
ดังนั้นการเติมเงินมูลค่าสูงเข้าไปภายหลังอาจทำให้ลำดับไม่ใช่จากสูงไปต่ำ

นอกจากนี้วิธี greedy ไม่มีการย้อนกลับไปลองชุดเงินแบบอื่น
เช่น `{4: 1, 3: 2}` เมื่อต้องจ่าย 6 จะเลือก 4 ก่อนแล้วจ่ายต่อไม่ได้
จึงคืน `{}` ทั้งที่การใช้ 3 จำนวนสองชิ้นรวมกันได้ 6
ดังนั้น comment ที่เรียกผลลัพธ์นี้ว่า “จ่ายไม่ได้”
หมายถึงจ่ายไม่ได้ตามลำดับ greedy ของโค้ด ไม่ได้หมายความว่าไม่มีชุดเงินอื่นเสมอไป

ใน PDF ใช้ชื่อพารามิเตอร์ `amt` ใน `pay(pocket, amt)`
แต่ Solution นิยามเป็น `pay(pocket, money_out)`
ตัวอย่างที่ส่งค่าแบบตำแหน่ง เช่น `pay(pocket, 12)` จึงทำงานเหมือนเดิม
แต่การเรียกด้วยชื่อ `pay(pocket, amt=12)` จะเกิด `TypeError`
เพราะชื่อจริงในโค้ดคือ `money_out`

---

## การรับคำสั่งจาก Grader

บรรทัด `exec(input().strip())` รับคำสั่ง Python หนึ่งบรรทัด
เช่น `p={10: 5, 1: 7}; print(pay(p, 12)); print(p)`
แล้วรันคำสั่งนั้น เพื่อให้ Grader เรียกหลายฟังก์ชันและตรวจการเปลี่ยนแปลงของ
`pocket` ได้

> [!WARNING]
>
> `exec()` สามารถรันคำสั่ง Python ใด ๆ ที่ได้รับมาได้
> จึงควรใช้เฉพาะกับคำสั่งทดสอบที่เชื่อถือได้จาก Grader
> และไม่ควรใช้กับข้อมูลจากผู้ใช้หรือแหล่งที่ไม่น่าเชื่อถือ

---

# Solution

```python
# --------------------------------------------------
# File Name : 08_Dict_31.py
# Problem   : Cash
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Calculate the total money in the pocket
def total(pocket):
    total_money = 0
    for money, quantity in pocket.items():
        total_money += money * quantity
    return total_money


# This function takes money and adds it to the pocket
def take(pocket, money_in):
    for money, quantity in money_in.items():
        if money not in pocket:
            pocket[money] = 0
        pocket[money] += quantity
    return pocket


# This function pays the money from the pocket
# The pocket must be able to pay the exact amount of money_out
# Return a dictionary of money and quantity used to pay
# If it is impossible to pay, return an empty dictionary
def pay(pocket, money_out):
    if total(pocket) >= money_out:
        # Find the money and quantity to pay
        pocket_pay = {}
        for money, quantity in pocket.items():
            quantity_used = min(money_out // money, quantity)
            money_out -= money * quantity_used
            if quantity_used > 0:
                pocket_pay[money] = quantity_used

        # If it is possible to pay, money_out will be 0
        # Subtract "pocket" with "pocket_pay"
        if money_out == 0:
            for money, quantity_used in pocket_pay.items():
                pocket[money] -= quantity_used
            return pocket_pay

    # If it is impossible to pay, return empty dictionary
    return {}


# Execute an input string as code
exec(input().strip())
```
