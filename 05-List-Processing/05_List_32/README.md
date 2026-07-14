<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Queue Ticket ★★★ (
      <a href="https://drive.google.com/file/d/1Zr5xve0MFhFOFmckERHE27i3tcze1mQO/view?usp=drive_link">
        <code>05_List_32</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเก็บสถานะของระบบคิว**](#การเก็บสถานะของระบบคิว)
-   [**การทำงานของแต่ละคำสั่ง**](#การทำงานของแต่ละคำสั่ง)
-   [**การคำนวณเวลารอและค่าเฉลี่ย**](#การคำนวณเวลารอและค่าเฉลี่ย)
-   [**ตัวอย่างลูกค้าที่ไม่มาตามการเรียก**](#ตัวอย่างลูกค้าที่ไม่มาตามการเรียก)
-   [**Solution**](#solution)

---

## การเก็บสถานะของระบบคิว

โจทย์ให้รับคำสั่งของระบบบัตรคิวทีละบรรทัด เราจึงต้องเก็บข้อมูลที่จำเป็นไว้
เพื่อให้คำสั่งถัดไปนำไปใช้ต่อได้ ตัวแปรหลักในโปรแกรมมีความหมายดังนี้

| ตัวแปร | ข้อมูลที่เก็บ |
|---|---|
| `queue` | บัตรคิวทั้งหมดในรูป `[หมายเลขบัตร, เวลากดบัตร]` |
| `queue_time` | เวลารอของลูกค้าที่สั่งอาหารสำเร็จแล้ว |
| `ticket` | หมายเลขบัตรที่จะออกให้ลูกค้าคนถัดไป |
| `customer` | ตำแหน่งของลูกค้าคนถัดไปที่จะถูกเรียกใน `queue` |

ตัวอย่างเช่น ถ้ามีคำสั่ง `new 1100` ขณะที่ `ticket` มีค่า `301` โปรแกรมจะเพิ่ม
`[301, 1100]` ลงใน `queue` แล้วเตรียมหมายเลขบัตรใบต่อไปเป็น `302`

เวลาทุกค่าในโจทย์เป็นจำนวนเต็มธรรมดา ไม่ใช่เวลาในรูปชั่วโมงและนาที ดังนั้น
`1120 - 1100` มีค่าเท่ากับ `20` โดยไม่ต้องแปลงหน่วยเวลา

---

## การทำงานของแต่ละคำสั่ง

โปรแกรมแยกคำสั่งและข้อมูลที่ตามมาด้วย `input().strip().split()` แล้วพิจารณา
คำแรกใน `cmd[0]`

| คำสั่ง | การเปลี่ยนแปลงข้อมูล | ผลลัพธ์ |
|---|---|---|
| `reset n` | กำหนด `ticket = n` | ไม่มี |
| `new t` | เพิ่ม `[ticket, t]` ใน `queue` แล้วเพิ่ม `ticket` ขึ้น `1` | `ticket n` |
| `next` | เรียก `queue[customer]` แล้วเพิ่ม `customer` ขึ้น `1` | `call n` |
| `order t` | คำนวณเวลารอของบัตรที่ถูก `next` ล่าสุด | `qtime n dt` |
| `avg_qtime` | หาค่าเฉลี่ยจากเวลารอที่บันทึกไว้ | `avg_qtime x` |

โจทย์รับประกันว่าคำสั่งมาในลำดับที่ถูกต้อง เช่น จะไม่มี `order` ก่อน `next`
และจะไม่มี `next` เมื่อไม่มีลูกค้ารออยู่ จึงเข้าถึงสมาชิกใน `queue` ได้อย่างปลอดภัย

ในโครงโปรแกรมของโจทย์ใช้ `if` ตามด้วย `elif` แต่โค้ดเฉลยใช้ `if` แยกกัน
ผลลัพธ์ยังเหมือนกัน เพราะคำสั่งหนึ่งบรรทัดมีชื่อใน `cmd[0]` เพียงชื่อเดียว
จึงมีเงื่อนไขที่เป็นจริงได้เพียงข้อเดียว

---

## การคำนวณเวลารอและค่าเฉลี่ย

เมื่อได้รับ `order t` ลูกค้าที่กำลังสั่งอาหารคือคนที่ถูกเรียกล่าสุด
หลังคำสั่ง `next` ตัวแปร `customer` ถูกเพิ่มไปแล้ว `1` ตำแหน่ง
จึงต้องอ่านข้อมูลของคนดังกล่าวจาก `queue[customer - 1]`

ถ้าให้ $t_{new}$ เป็นเวลากดบัตร และ $t_{order}$ เป็นเวลาสั่งอาหาร เวลารอคือ

$$
dt = t_{order} - t_{new}
$$

ซึ่งตรงกับคำสั่ง Python

```python
duration = order_time - new_time
```

โปรแกรมเพิ่ม `duration` ลงใน `queue_time` เฉพาะเมื่อมีคำสั่ง `order` ดังนั้น
ลูกค้าที่ถูกเรียกแต่ไม่มาจะไม่ถูกนำมาคิดค่าเฉลี่ย ถ้ามีเวลารอทั้งหมด $m$ ค่า
ค่าเฉลี่ยคือ

$$
\text{avg} = \frac{dt_1 + dt_2 + \cdots + dt_m}{m}
$$

หรือใน Python คือ `sum(queue_time) / len(queue_time)` จากนั้นแสดงผลด้วย
`round(avg, 4)` เพื่อปัดเศษไม่เกิน `4` ตำแหน่งหลังจุดทศนิยม

> [!NOTE]
>
> `round(avg, 4)` ไม่ได้บังคับให้แสดงเลขทศนิยมครบ `4` ตำแหน่งเสมอ เช่น
> ค่าเฉลี่ย `20.0` จะแสดงเป็น `20.0` ไม่ใช่ `20.0000`

แม้โจทย์จะรับประกันว่าจะเรียก `avg_qtime` หลังมีผู้สั่งอาหารแล้ว โค้ดนี้ยัง
กำหนดค่าเฉลี่ยเริ่มต้นเป็น `0.0` ไว้ด้วย ถ้า `queue_time` ยังว่างจะพิมพ์
`avg_qtime 0.0` และไม่เกิดการหารด้วยศูนย์

---

## ตัวอย่างลูกค้าที่ไม่มาตามการเรียก

สมมติว่าในคิวมีบัตร `302` และ `303` ตามลำดับ เมื่อได้รับ `next` สองครั้งติดกัน
โปรแกรมจะแสดง `call 302` แล้ว `call 303` ทำให้ `customer` ชี้ผ่านทั้งสองคน
ถ้าคำสั่งถัดไปคือ `order 1160` โปรแกรมจะใช้ `queue[customer - 1]`
ซึ่งเป็นข้อมูลของบัตร `303`

ดังนั้นบัตร `302` ที่ไม่มาตามการเรียกจะไม่มีเวลาอยู่ใน `queue_time` ส่วนบัตร
`303` ซึ่งกดบัตรเวลา `1130` จะมีเวลารอ `1160 - 1130 = 30` และแสดงผล
`qtime 303 30`

---

# Solution

```python
# --------------------------------------------------
# File Name : 05_List_32.py
# Problem   : Queue Ticket
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Input commands amount
n = int(input())

# Initialize variable
queue = []
queue_time = []
ticket = 0
customer = 0

# Process each command
for _ in range(n):
    # Input command
    cmd = input().strip().split()

    # Command: reset
    # Initialize ticket number
    if cmd[0] == "reset":
        ticket = int(cmd[1])

    # Command: new
    # Add a new customer to the queue
    if cmd[0] == "new":
        new_time = int(cmd[1])
        queue.append([ticket, new_time])

        print("ticket", ticket)
        ticket += 1

    # Command: next
    # Process the next customer in the queue
    if cmd[0] == "next":
        current_ticket = queue[customer][0]
        print("call", current_ticket)
        customer += 1

    # Command: order
    # Update the order time for the current customer
    if cmd[0] == "order":
        current_ticket, new_time = queue[customer - 1]
        order_time = int(cmd[1])

        duration = order_time - new_time
        queue_time.append(duration)
        print("qtime", current_ticket, duration)

    # Command: avg_qtime
    # Calculate the average queue time
    if cmd[0] == "avg_qtime":
        avg = 0.0
        if len(queue_time) > 0:
            avg = sum(queue_time) / len(queue_time)
        print("avg_qtime", round(avg, 4))
```
