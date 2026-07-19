<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Seating Map ★☆ (
      <a href="https://drive.google.com/file/d/18G-CQOFTieLXVpGkQaB3E-3rvsJKQNLY/view?usp=sharing">
        <code>2565_2_Q3_02</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การแปลงหมายเลขที่นั่งเป็นแถวและคอลัมน์**](#การแปลงหมายเลขที่นั่งเป็นแถวและคอลัมน์)
-   [**การสร้างและแสดงผังที่นั่ง**](#การสร้างและแสดงผังที่นั่ง)
-   [**Solution**](#solution)

---

## การแปลงหมายเลขที่นั่งเป็นแถวและคอลัมน์

ฟังก์ชัน `print_seats(assignments, n_rows, n_cols)` รับข้อมูล 3 ส่วน

-   `assignments` เป็นรายการ `[name, pos]` โดย `name` เป็นชื่อย่อ 2 ตัวอักษร
    และ `pos` เป็นหมายเลขที่นั่ง
-   `n_rows` คือจำนวนแถว
-   `n_cols` คือจำนวนที่นั่งในแต่ละแถว

หมายเลขที่นั่งในโจทย์เริ่มจาก `1` แต่ index ของ list ใน Python เริ่มจาก `0`
จึงต้องใช้ `pos - 1` ก่อนหาแถวและคอลัมน์

$$
\text{row} = \left\lfloor \frac{\text{pos} - 1}{\text{n\_cols}} \right\rfloor,
\qquad
\text{column} = (\text{pos} - 1) \bmod \text{n\_cols}
$$

สูตรทั้งสองเขียนเป็น Python ได้ดังนี้

```python
r = (pos - 1) // n_cols
c = (pos - 1) % n_cols
```

`//` หาว่าเลื่อนผ่านแถวที่เต็มมาแล้วกี่แถว ส่วน `%` หาตำแหน่งที่เหลืออยู่
ภายในแถวนั้น ตัวอย่างเช่น `pos = 6` และ `n_cols = 3` จะได้ `r = 1`
และ `c = 2` ซึ่งหมายถึงแถวที่ 2 คอลัมน์ที่ 3 เมื่อมองแบบหมายเลขที่นั่งทั่วไป

---

## การสร้างและแสดงผังที่นั่ง

โปรแกรมเริ่มจากสร้าง list สองมิติขนาด `n_rows` แถว แถวละ `n_cols` ช่อง
โดยกำหนดให้ทุกช่องเป็นที่นั่งว่าง `"| -- "`

```python
seats = [["| -- "] * n_cols for _ in range(n_rows)]
```

จากนั้นวนอ่าน `name` และ `pos` ใน `assignments` คำนวณ `(r, c)`
แล้วแทนช่องนั้นด้วย `f"| {name} "` เมื่อข้อมูลครบจึงเชื่อมทุกช่องในแต่ละแถว
ด้วย `"".join(row)` และเติมขีดตั้ง `|` ปิดท้าย

สตริงของแต่ละช่องมีช่องว่าง 1 ตัวหลังขีดตั้ง และอีก 1 ตัวหลังชื่อหรือ `--`
จึงได้รูปแบบ เช่น `| SS | -- | CP |` โปรแกรมแสดงแถวจากบนลงล่าง
และแสดงที่นั่งในแต่ละแถวจากซ้ายไปขวา

หาก `assignments` เป็น list ว่าง ทุกตำแหน่งจะแสดงเป็น `--`
และหากตำแหน่งเดิมปรากฏมากกว่าหนึ่งครั้ง ชื่อจากรายการที่มาทีหลัง
จะเขียนทับชื่อเดิมตามลำดับการวนของโค้ด

บรรทัดสุดท้าย `exec(input().strip())` มีไว้ให้ grader ส่งคำสั่งเรียกฟังก์ชัน
เช่น `print_seats([...], 2, 3)` เข้ามาเป็น input แล้วให้โปรแกรมเรียกใช้งานทันที

> [!WARNING]
>
> `exec()` สามารถรันข้อความที่เป็นคำสั่ง Python ใด ๆ ได้ จึงเหมาะเฉพาะกับ input
> ที่เชื่อถือได้จาก grader ของโจทย์นี้ ไม่ควรใช้กับข้อความจากผู้ใช้หรือแหล่งที่ไม่น่าเชื่อถือ

---

# Solution

```python
# --------------------------------------------------
# File Name : 2565_2_Q3_02.py
# Problem   : Seating Map
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------


# Print the seating assignments in a formatted way
def print_seats(assignments, n_rows, n_cols):
    # Create a 2D list to represent the seating map
    seats = [["| -- "] * n_cols for _ in range(n_rows)]
    # Fill the seating map with the names from the assignments
    for name, pos in assignments:
        # Calculate the row and column based on the position
        r = (pos - 1) // n_cols
        c = (pos - 1) % n_cols
        # Place the name in the correct position in the seating map
        seats[r][c] = f"| {name} "

    # Print the seating map
    for row in seats:
        print("".join(row) + "|")


# Execute a input string as code
exec(input().strip())
```
