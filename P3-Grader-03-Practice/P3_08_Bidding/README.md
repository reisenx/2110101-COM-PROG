<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Bidding ★★★☆ (
      <a href="https://drive.google.com/file/d/1ERinoNzOYUVL2pBiceM8YmRaSHNoq4iW/view?usp=drive_link">
        <code>P3_08_Bidding</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**กติกาของการประมูล**](#กติกาของการประมูล)
-   [**การออกแบบโครงสร้างข้อมูล**](#การออกแบบโครงสร้างข้อมูล)
-   [**การเสนอราคาและถอนราคา**](#การเสนอราคาและถอนราคา)
-   [**การหาผู้ชนะ**](#การหาผู้ชนะ)
-   [**การรวมยอดของผู้ประมูล**](#การรวมยอดของผู้ประมูล)
-   [**การจัดรูปแบบผลลัพธ์**](#การจัดรูปแบบผลลัพธ์)
-   [**ลำดับการทำงาน**](#ลำดับการทำงาน)
-   [**Solution**](#solution)

---

## กติกาของการประมูล

บรรทัดแรกระบุจำนวนรายการ `n` จากนั้นแต่ละบรรทัดเป็นคำสั่งเกี่ยวกับการประมูล

| คำสั่ง | รูปแบบ | ความหมาย |
|---|---|---|
| `B` | `B user product price` | ผู้ประมูล `user` เสนอราคา `price` สำหรับสินค้า `product` |
| `W` | `W user product` | ถอนราคาของ `user` สำหรับ `product` |

การเสนอราคาครั้งใหม่ของผู้ประมูลคนเดิมสำหรับสินค้าเดิม
จะ **แทนที่** ราคาครั้งก่อน ไม่ได้นำราคามาบวกกัน
จึงสามารถใช้ได้ทั้งการเพิ่มและลดราคา

การถอนราคาที่ไม่มีอยู่จะถูกข้ามไป
หลังประมวลผลครบทุกคำสั่ง ผู้ชนะของสินค้าแต่ละชิ้นคือผู้ที่มีราคาปัจจุบันสูงสุด
ถ้าราคาเท่ากัน ผู้ที่เสนอราคาปัจจุบันก่อนเป็นผู้ชนะ

> [!NOTE]
>
> เมื่อผู้ประมูลเสนอราคาสินค้าเดิมอีกครั้ง
> ทั้งราคาและเวลาของราคาเดิมจะถูกแทนที่
> ดังนั้นการเสนอใหม่ถือว่าเกิดในเวลาของคำสั่งล่าสุด

---

## การออกแบบโครงสร้างข้อมูล

โจทย์ต้องตอบคำถามสองด้าน คือ

1. สินค้าแต่ละชิ้นมีราคาใดที่ยังใช้งานอยู่บ้าง
2. ผู้ประมูลแต่ละคนชนะสินค้าอะไรและต้องจ่ายรวมเท่าไร

โค้ดจึงใช้ dictionary สองชุด

```python
products = {}
users = {}
```

`products` มีรูปแบบ

```text
รหัสสินค้า -> {รหัสผู้ประมูล -> [ราคา, เวลา]}
```

ตัวอย่างสถานะของสินค้า `p1` หลังมีผู้เสนอราคาเท่ากันสองคนอาจเป็น

```python
products["p1"] = {
    "b3": [11, 0],
    "b1": [11, 6],
}
```

ค่าเวลาไม่ใช่เวลาจากนาฬิกา แต่เป็นลำดับคำสั่งจาก `range(n)`
จึงใช้เปรียบเทียบได้ว่าใครเสนอราคาก่อน

ส่วน `users` มีรูปแบบ

```text
รหัสผู้ประมูล -> {"money": ยอดรวม, "products": [สินค้าที่ชนะ]}
```

ข้อมูลส่วนนี้เริ่มด้วยยอด `0` และรายการว่าง
แล้วจึงเติมผลการประมูลหลังอ่านคำสั่งทั้งหมดครบแล้ว

---

## การเสนอราคาและถอนราคา

ฟังก์ชัน `bid_product()` สร้างช่องข้อมูลของสินค้าและผู้ประมูลเมื่อพบครั้งแรก
จากนั้นบันทึกราคาปัจจุบันด้วยคำสั่ง

```python
products[product][user] = [price, time]
```

การกำหนดค่าลง key เดิมทำให้ราคาครั้งใหม่แทนที่ราคาครั้งก่อนโดยอัตโนมัติ

ฟังก์ชัน `withdraw_product()` ตรวจสอบก่อนว่ามีทั้งสินค้าและราคาของผู้ประมูลคนนั้น
ถ้าไม่พบจะ `return` โดยไม่เปลี่ยนข้อมูล แต่ถ้าพบจะลบด้วย

```python
del products[product][user]
```

แม้ผู้ประมูลจะถอนราคาทั้งหมด ผู้ประมูลคนนั้นยังอยู่ใน `users`
จึงยังต้องปรากฏในผลลัพธ์ด้วยยอด `$0`
ในทางกลับกัน รหัสที่ปรากฏเฉพาะในคำสั่งถอนและไม่เคยเสนอราคา
จะไม่ถูกสร้างใน `users` และไม่ถูกแสดง

---

## การหาผู้ชนะ

สำหรับสินค้าแต่ละชิ้น ฟังก์ชัน `get_winner()`
เปลี่ยนราคาของผู้ประมูลแต่ละคนเป็นรายการจัดอันดับ

```python
[-price, time, user]
```

เมื่อ Python เรียง list หลายค่า จะเปรียบเทียบค่าจากซ้ายไปขวา

1. `-price` ทำให้ราคาสูงกลายเป็นค่าที่เล็กกว่า จึงมาก่อนเมื่อเรียงจากน้อยไปมาก
2. `time` ทำให้คำสั่งที่เกิดก่อนมาก่อนเมื่อราคาเท่ากัน
3. `user` เป็นเกณฑ์สุดท้ายหากสองค่าแรกเท่ากัน

จากตัวอย่างสถานะของ `p1`

```text
b3 -> [-11, 0, "b3"]
b1 -> [-11, 6, "b1"]
```

ราคาทั้งคู่เป็น `11` แต่เวลา `0` มาก่อนเวลา `6` ดังนั้น `b3` เป็นผู้ชนะ

ถ้าสินค้าไม่มีราคาที่ยังใช้งานอยู่ ฟังก์ชันจะคืน `("", -1)`
เพื่อบอกว่าไม่มีผู้ชนะ

---

## การรวมยอดของผู้ประมูล

ฟังก์ชัน `update_all_users()` พิจารณาสินค้าทีละชิ้น
เรียก `get_winner()` แล้วอัปเดตข้อมูลผู้ชนะดังนี้

```python
users[user]["money"] += price
users[user]["products"].append(product)
```

สินค้าแต่ละชิ้นจึงถูกคิดเงินให้ผู้ชนะเพียงคนเดียว
ส่วนผู้ที่ไม่ชนะสินค้าใดยังคงมียอด `0` และรายการสินค้าว่าง

โค้ดเพิ่มสินค้าให้ผู้ชนะเฉพาะเมื่อ `price > 0`
ขณะที่ PDF ไม่ได้ระบุขอบเขตของราคาอย่างชัดเจน
ดังนั้น canonical solution นี้ตั้งอยู่บนสมมติฐานว่าราคาประมูลที่ถูกต้องเป็นจำนวนเต็มบวก
ถ้าราคาสูงสุดเป็น `0` หรือติดลบ โค้ดจะไม่มอบสินค้านั้นให้ใคร

---

## การจัดรูปแบบผลลัพธ์

ผลลัพธ์หนึ่งบรรทัดเริ่มจากรูปแบบ

```text
รหัสผู้ประมูล: $ยอดรวม
```

ถ้าผู้ประมูลชนะสินค้าอย่างน้อยหนึ่งชิ้น จึงต่อท้ายด้วย

```text
 -> รหัสสินค้า1 รหัสสินค้า2
```

`sorted(details["products"])` เรียงรหัสสินค้าจากน้อยไปมาก
และ `results.sort()` เรียงทั้งบรรทัดตามรหัสผู้ประมูล
จำนวนเงินเป็นจำนวนเต็ม จึงไม่มีการปัดเศษ

ตัวอย่างจากโจทย์แสดงผลดังนี้

```text
b1: $0
b2: $9 -> p2
b3: $16 -> p1 p4
```

สังเกตว่า `b1` ไม่มีสินค้า จึงไม่มีเครื่องหมาย `->`

---

## ลำดับการทำงาน

1. รับจำนวนคำสั่ง
2. ใช้ลำดับรอบเป็น `time` แล้วประมวลผล `B` หรือ `W`
3. เมื่อครบทุกคำสั่ง หาผู้ชนะของสินค้าแต่ละชิ้น
4. รวมราคาและรายการสินค้าไว้ที่ผู้ชนะ
5. เรียงรหัสสินค้าและรหัสผู้ประมูล แล้วแสดงผลทีละบรรทัด

PDF ระบุว่าคำสั่งที่ไม่ใช่ `B` หรือ `W` ควรถูกข้าม
โค้ดนี้ทำเช่นนั้นได้เมื่อบรรทัดมีอย่างน้อยสามส่วน
เพราะใน `main()` มีการอ่าน `line[0]`, `line[1]` และ `line[2]`
ก่อนตรวจชนิดคำสั่ง หากบรรทัดคำสั่งอื่นสั้นกว่าสามส่วนจะเกิด `IndexError`
แทนที่จะข้ามบรรทัด ดังนั้นโค้ดจึงอาศัยรูปแบบข้อมูลจาก Grader ที่มีจำนวนส่วนเพียงพอ

---

# Solution

```python
# --------------------------------------------------
# File Name : P3_08_Bidding.py
# Problem   : Part-III Bidding
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# Initialize dictionaries to store products and users
products = {}
users = {}


# Bid on a product by a user with a specified price and time
def bid_product(user, product, price, time):
    # If the product or user does not exist, initialize them
    if product not in products:
        products[product] = {}
    if user not in users:
        users[user] = {"money": 0, "products": []}
    # Add or update the user's bid for the product
    products[product][user] = [price, time]


# Withdraw a user's bid for a product
def withdraw_product(user, product):
    # Ignore if the product or user does not exist
    if product not in products or user not in products[product]:
        return
    # Remove the user's bid for the product
    del products[product][user]


# Get the winner of a product based on the highest bid
def get_winner(product):
    # If the product does not exist or has no bids
    if product not in products or len(products[product]) == 0:
        return "", -1
    # Sort the bids for the product by price (descending) and time (ascending)
    product_ranks = []
    for user, [price, time] in products[product].items():
        product_ranks.append([-price, time, user])
    product_ranks.sort()
    # The winner is the user with the highest bid
    price, user = -product_ranks[0][0], product_ranks[0][2]
    return user, price


# Update all users with the winning bids for each product
def update_all_users():
    # Iterate through each product to determine the winner
    for product, _ in products.items():
        user, price = get_winner(product)
        # Update the user's money and products if they won
        if price > 0:
            users[user]["money"] += price
            users[user]["products"].append(product)


# Report the final results of all users
def report():
    # Initialize a list to store the result of each user
    results = []
    # Iterate through each user and format their results
    for user, details in users.items():
        result = f"{user}: ${details['money']}"
        # If the user has won products
        if len(details["products"]) > 0:
            result += f" -> {' '.join(sorted(details['products']))}"
        results.append(result)
    # Sort the results alphabetically by user name
    results.sort()
    # Print the final results
    print("\n".join(results))


# Main function to read commands and process bids
def main():
    # Read the number of commands
    n = int(input())
    for time in range(n):
        line = input().strip().split()
        command, user, product = line[0], line[1], line[2]
        # Bid (B) command
        if command == "B":
            price = int(line[3])
            bid_product(user, product, price, time)
        # Withdraw (W) command
        elif command == "W":
            withdraw_product(user, product)
    # After processing all commands, update user data and report results
    update_all_users()
    report()


# Run the main function to start the bidding process
main()
```
