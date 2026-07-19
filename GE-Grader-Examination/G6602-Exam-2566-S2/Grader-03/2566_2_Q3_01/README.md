<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Peak 2D ★☆ (
      <a href="https://drive.google.com/file/d/1LF2pj8dcpoLBjUNJ0WUCw70FL3cgfXMU/view?usp=sharing">
        <code>2566_2_Q3_01</code>
      </a>
    )
  </h1>
</div>

# Contents

- [**แนวคิด**](#แนวคิด)
- [**ขั้นตอนการแก้ปัญหา**](#ขั้นตอนการแก้ปัญหา)
- [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
- [**การรับข้อมูลของ Grader**](#การรับข้อมูลของ-grader)
- [**ข้อควรระวัง**](#ข้อควรระวัง)
- [**Solution**](#solution)

---

# แนวคิด

ข้อมูลสองมิติในข้อนี้เก็บด้วย **ลิสต์ซ้อนลิสต์** โดย `data[r][c]` หมายถึงข้อมูลแถวที่ `r` และคอลัมน์ที่ `c` เช่น

```python
data = [
    [0, 1, 2, 3],
    [1, 9, 2, 3],
    [2, 1, 8, 3],
    [3, 3, 3, 3],
]
```

จุดหนึ่งจะเป็น **จุดสูงสุด** เมื่อมีค่ามากกว่าเพื่อนบ้านทั้ง 4 ทิศ ได้แก่ ด้านบน ด้านล่าง ด้านซ้าย และด้านขวา โดยไม่เปรียบเทียบกับจุดแนวทแยง

ถ้าให้ค่าที่ตำแหน่ง `(r, c)` เป็น $a_{r,c}$ เงื่อนไขคือ

$$
a_{r,c} > a_{r-1,c}
\;\land\;
a_{r,c} > a_{r+1,c}
\;\land\;
a_{r,c} > a_{r,c-1}
\;\land\;
a_{r,c} > a_{r,c+1}
$$

เมื่อนำมาเขียนเป็น Python จะได้

```python
data[r][c] > data[r - 1][c]
and data[r][c] > data[r + 1][c]
and data[r][c] > data[r][c - 1]
and data[r][c] > data[r][c + 1]
```

ต้องใช้ `>` ทุกทิศ ถ้ามีเพื่อนบ้านค่าเท่ากันแม้เพียงด้านเดียว จุดนั้นก็ไม่ใช่จุดสูงสุด

# ขั้นตอนการแก้ปัญหา

1. กำหนด `ans = 0` สำหรับนับจำนวนจุดสูงสุด
2. วนเฉพาะแถวด้านในด้วย `range(1, rows - 1)` จึงไม่เลือกแถวแรกและแถวสุดท้าย
3. ในแต่ละแถว วนเฉพาะคอลัมน์ด้านในด้วย `range(1, cols - 1)`
4. เปรียบเทียบค่าปัจจุบันกับเพื่อนบ้านทั้ง 4 ทิศด้วย `and`
5. ถ้าทุกเงื่อนไขเป็นจริง ให้เพิ่ม `ans` ทีละ `1`
6. เมื่อพิจารณาครบแล้ว คืนค่า `ans`

การไม่วนผ่านขอบมีความสำคัญ เพราะจุดบนขอบไม่มีเพื่อนบ้านครบ 4 ทิศ และโจทย์กำหนดว่าไม่นับจุดเหล่านี้เป็นจุดสูงสุดอยู่แล้ว วิธีนี้จึงไม่ต้องเขียนเงื่อนไขตรวจขอบซ้ำภายในลูป

อัลกอริทึมตรวจแต่ละช่องด้านในหนึ่งครั้ง ใช้เวลา $O(RC)$ และใช้ตัวแปรช่วยเพิ่มเพียงจำนวนคงที่

# ตัวอย่างการทำงาน

จากข้อมูลตัวอย่าง

```text
0 1 2 3
1 9 2 3
2 1 8 3
3 3 3 3
```

- `data[1][1]` มีค่า `9` ซึ่งมากกว่า `1`, `1`, `1` และ `2` จึงเป็นจุดสูงสุด
- `data[2][2]` มีค่า `8` ซึ่งมากกว่า `2`, `3`, `1` และ `3` จึงเป็นจุดสูงสุด
- ค่าอื่นที่อยู่ด้านในไม่ผ่านครบทั้ง 4 เงื่อนไข

ดังนั้น `count_peak(data)` คืนค่า `2`

# การรับข้อมูลของ Grader

ฟังก์ชัน `read_data()` อ่านจำนวนแถว `R` ก่อน แล้วอ่านจำนวนเต็มอีก `R` บรรทัด แต่ละบรรทัดถูกแปลงเป็นลิสต์ด้วย

```python
[int(num) for num in input().strip().split()]
```

โจทย์รับประกันว่าข้อมูลเป็นตารางขนาด $R \times C$ จึงถือว่าทุกแถวมีจำนวนคอลัมน์เท่ากัน โดยไม่มีบรรทัดสำหรับรับค่า `C` แยกต่างหาก

บรรทัดแรกที่ grader ส่งให้โปรแกรมเป็นคำสั่ง Python เช่น

```python
dat=read_data();print(count_peak(dat))
```

คำสั่งนี้ถูกทำงานด้วย `exec(input().strip())` แล้ว `read_data()` จึงอ่าน `R` และข้อมูลอีก `R` แถวตามลำดับ สุดท้ายคำสั่ง `print(...)` เป็นส่วนที่แสดงจำนวนจุดสูงสุด

> [!WARNING]
> `exec()` สามารถทำงานคำสั่ง Python ที่ได้รับมาได้ทั้งหมด ที่ใช้ในข้อนี้เพราะ grader ส่งคำสั่งทดสอบที่เชื่อถือได้เท่านั้น ไม่ควรนำ `exec(input())` ไปใช้กับข้อมูลจากผู้ใช้หรือแหล่งที่ไม่เชื่อถือ

# ข้อควรระวัง

- จุดริมขอบและจุดมุมไม่นับเป็นจุดสูงสุด แม้ค่าจะมากกว่าจุดอื่นทั้งหมด
- ต้องเปรียบเทียบเฉพาะ 4 ทิศ ไม่รวมแนวทแยง
- ใช้ `>` ไม่ใช่ `>=` เพราะค่าที่เท่ากับเพื่อนบ้านไม่ผ่านเงื่อนไข
- จำนวนเต็มติดลบเปรียบเทียบได้ตามปกติ เช่น `-1` มากกว่า `-2`
- ถ้ามีแถวน้อยกว่า `3` แถว หรือมีคอลัมน์น้อยกว่า `3` คอลัมน์ จะไม่มีจุดด้านในและฟังก์ชันคืนค่า `0`

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_2_Q3_01.py
# Problem   : Peak 2D
# Author    : Worralop Srichainont
# Date      : 2025-07-13
# --------------------------------------------------


# Read input data and return a list of lists of integers.
def read_data():
    data = []
    rows = int(input())
    for _ in range(rows):
        data.append([int(num) for num in input().strip().split()])
    return data


# Count the number of peak elements in a 2D grid.
def count_peak(data):
    # Initialize the peak count to zero.
    ans = 0
    # Get the number of rows in the data.
    rows = len(data)
    # Iterate through the data, skipping the first and last rows and columns.
    for r in range(1, rows - 1):
        # Get the number of columns in the current row.
        cols = len(data[r])
        for c in range(1, cols - 1):
            # Check if the current element is greater than its four neighbors.
            if (
                data[r][c] > data[r - 1][c]
                and data[r][c] > data[r + 1][c]
                and data[r][c] > data[r][c - 1]
                and data[r][c] > data[r][c + 1]
            ):
                # If it is, increment the peak count.
                ans += 1
    # Return the total count of peak elements.
    return ans


# Execute the input string as code
exec(input().strip())
```
