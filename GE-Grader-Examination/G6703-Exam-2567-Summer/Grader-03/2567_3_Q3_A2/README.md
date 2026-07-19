<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Coveyer Belt ★★ (
      <a href="https://drive.google.com/file/d/1rn2oJeFPBMSNHAICwYwckghCxUb7Coau/view?usp=sharing">
        <code>2567_3_Q3_A2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**มองสายพานเป็นข้อความหนึ่งมิติ**](#มองสายพานเป็นข้อความหนึ่งมิติ)
-   [**การเลื่อนสายพานตามเวลา**](#การเลื่อนสายพานตามเวลา)
-   [**การแปลงกลับเป็นสายพานคดเคี้ยว**](#การแปลงกลับเป็นสายพานคดเคี้ยว)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## มองสายพานเป็นข้อความหนึ่งมิติ

แม้สายพานในภาพจะวกกลับไปมา แต่ผลิตภัณฑ์ยังเคลื่อนที่ตามเส้นทางเดียวต่อเนื่องกัน
เราจึงแทนสายพานทั้งหมดด้วยข้อความหนึ่งมิติก่อนได้

บรรทัดแรกของอินพุตมี `L N T` โดยในโปรแกรมใช้ชื่อตัวแปรดังนี้

-   `cols` คือความยาวแต่ละแถว `L`
-   `rows` คือจำนวนแถว `N`
-   `time` คือเวลาที่ผ่านไป `T` วินาที

จำนวนช่องบนสายพานจึงเท่ากับ

$$
\text{conveyor length} = L \times N
$$

ซึ่งเขียนเป็น Python ได้ว่า

```python
conveyor_length = cols * rows
```

จุด `.` แทนช่องว่างบนสายพาน ส่วนตัวอักษรแต่ละตัวแทนผลิตภัณฑ์หนึ่งชิ้น
ผลิตภัณฑ์ในอินพุตเรียงตามเวลาที่ผลิตออกมา เช่น `ABC` หมายถึง `A` มาก่อน `B`
และ `B` มาก่อน `C`

ฟังก์ชัน `init_conveyor_belt()` กลับข้อความผลิตภัณฑ์ด้วย `items[::-1]`
เพื่อให้ผลิตภัณฑ์ตัวแรกอยู่ติดกับทางเข้าสายพาน แล้วต่อท้ายด้วยช่องว่างเท่ากับ
ความจุของสายพาน

```python
return items[::-1] + (conveyor_length * ".")
```

ถ้า `items` เป็น `ABC` และสายพานมี 6 ช่อง ข้อความเริ่มต้นคือ `CBA......`
โดย `A` อยู่ใกล้ช่องแรกของสายพานที่สุด

---

## การเลื่อนสายพานตามเวลา

สายพานเคลื่อนที่ด้วยความเร็ว 1 ช่องต่อวินาที ดังนั้นเมื่อผ่านไป `T` วินาที
ข้อความต้องเลื่อนไปทางขวา `T` ตำแหน่ง

```python
return ("." * time) + conveyor[:-time]
```

คำสั่งนี้เติม `.` ทางซ้าย `time` ตัว และใช้ slice ตัดข้อมูลด้านท้าย
เมื่อ `time` ไม่เกินความยาวข้อความ จะเป็นการเติมและตัดจำนวนเท่ากัน
จึงทำให้ความยาวข้อความคงเดิม ผลิตภัณฑ์ที่ยังมาไม่ถึงจะแสดงเป็น `.` บนสายพาน
ส่วนผลิตภัณฑ์ที่เคลื่อนเลยปลายข้อความไปแล้วจะหายออกจากระบบ หาก `time`
มากกว่าความยาวข้อความ ส่วน `conveyor[:-time]` จะว่างและช่วงที่นำมาแสดง
ท้ายสุดจะมีแต่ `.` ซึ่งหมายถึงผลิตภัณฑ์ออกจากสายพานหมดแล้ว

หลังเลื่อนเสร็จ โปรแกรมเลือกเฉพาะ `L * N` ตัวท้ายสุด
ซึ่งเป็นส่วนที่อยู่บนสายพานจริง

```python
conveyor_to_display = conveyor[-(rows * cols) :]
```

ถ้าเวลามากจนผลิตภัณฑ์ทุกชิ้นผ่านพ้นสายพานไปแล้ว ส่วนที่นำมาแสดงจะมีแต่ `.`

> [!WARNING]
>
> Solution นี้อาศัยข้อมูลที่ `time > 0` หากกำหนด `time == 0` นิพจน์
> `conveyor[:-0]` จะได้ข้อความว่าง เพราะใน Python ค่า `-0` เท่ากับ `0`
> ทำให้โค้ดแสดงบรรทัดว่างแทนสภาพเริ่มต้นของสายพาน

---

## การแปลงกลับเป็นสายพานคดเคี้ยว

ข้อความที่เลือกมามี `L * N` ตัว โปรแกรมแบ่งข้อความเป็น `N` ช่วง
ช่วงละ `L` ตัวด้วยตำแหน่งเริ่มต้นและตำแหน่งสิ้นสุด

```python
start_index = cols * i
end_index = cols * (i + 1)
```

ทิศทางของสายพานสลับกันในแต่ละแถว จึงแสดงผลดังนี้

-   แถวที่มีดัชนีคู่ `0, 2, 4, ...` แสดงข้อความตามลำดับเดิม
-   แถวที่มีดัชนีคี่ `1, 3, 5, ...` กลับข้อความด้วย `[::-1]`

ดัชนีเริ่มที่ `0` ดังนั้นแถวที่ 1 แสดงตามปกติ แถวที่ 2 กลับด้าน
แล้วสลับเช่นนี้ไปเรื่อย ๆ แต่ละบรรทัดจึงมีความยาว `L` ตัวเสมอ

---

## ตัวอย่างการทำงาน

พิจารณาอินพุต `L = 3`, `N = 2`, `T = 4` และผลิตภัณฑ์ `ABC`

1. สายพานมี `3 * 2 = 6` ช่อง
2. ข้อความเริ่มต้นคือ `CBA......`
3. เลื่อนไปทางขวา 4 ช่อง ได้ `....CBA..`
4. เลือก 6 ตัวท้าย ได้ `.CBA..`
5. แบ่งเป็นช่วง `.CB` และ `A..`
6. แถวที่ 2 ต้องกลับด้านจาก `A..` เป็น `..A`

จึงแสดงผลเป็น

```text
.CB
..A
```

ในทำนองเดียวกัน เมื่อ `T = 7` ผลิตภัณฑ์ `A` ออกจากสายพานแล้ว
แต่ `B` และ `C` ยังอยู่ จึงได้ `...` ในแถวแรกและ `BC.` ในแถวที่สอง

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_3_Q3_A2.py
# Problem   : Conveyor Belt
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------


# Initialize the conveyor belt string with items placed at the front
def init_conveyor_belt(conveyor_length, items):
    return items[::-1] + (conveyor_length * ".")


# Move the conveyor belt by shifting items to the right
def move_conveyor_belt(conveyor, time):
    return ("." * time) + conveyor[:-time]


# Display the conveyor belt in a rows x cols format
def display_conveyor_belt(conveyor, rows, cols):
    # Display only the last rows * cols characters of the conveyor belt
    conveyor_to_display = conveyor[-(rows * cols) :]

    # Output the conveyor belt in each row
    for i in range(rows):
        # Calculate the start and end indices for slicing from the conveyor string
        start_index = cols * i
        end_index = cols * (i + 1)

        # For even indexed rows, display normally
        if i % 2 == 0:
            print(conveyor_to_display[start_index:end_index])
        # For odd indexed rows, display in reverse order
        else:
            print(conveyor_to_display[start_index:end_index][::-1])


# Main function
def main():
    # Read the conveyor belt dimensions and time processed
    cols, rows, time = [int(num) for num in input().split()]
    # Read the items to be placed on the conveyor belt
    items = input().strip()

    # Calculate the total length of the conveyor belt
    conveyor_length = cols * rows

    # Initialize the conveyor belt string
    conveyor = init_conveyor_belt(conveyor_length, items)

    # Move the conveyor belt by the specified time
    conveyor = move_conveyor_belt(conveyor, time)

    # Output
    display_conveyor_belt(conveyor, rows, cols)


# Run the main function
main()
```
