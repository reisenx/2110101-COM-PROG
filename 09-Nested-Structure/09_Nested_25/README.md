<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Tiling Puzzle ★★☆ (
      <a href="https://drive.google.com/file/d/1QgrpIfq7AeOfxVe8VCWx3PAVxvocIl29/view?usp=drive_link">
        <code>09_Nested_25</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การแทนกระดานและหาตำแหน่งช่องว่าง**](#การแทนกระดานและหาตำแหน่งช่องว่าง)
-   [**การแปลงกระดานเป็นลิสต์หนึ่งมิติ**](#การแปลงกระดานเป็นลิสต์หนึ่งมิติ)
-   [**การนับ Inversion**](#การนับ-inversion)
-   [**เงื่อนไขการแก้ปริศนา**](#เงื่อนไขการแก้ปริศนา)
-   [**การรับคำสั่งทดสอบจาก Grader**](#การรับคำสั่งทดสอบจาก-grader)
-   [**Solution**](#solution)

---

## การแทนกระดานและหาตำแหน่งช่องว่าง

โจทย์แทนกระดานขนาด $n \times n$ ด้วยลิสต์ซ้อนลิสต์ของจำนวนเต็ม
โดยใช้ `0` แทนช่องว่าง เช่น

```python
tiles = [
    [1, 2, 0],
    [3, 5, 6],
    [4, 7, 8],
]
```

ฟังก์ชัน `row_number(tiles, target)` เดินดูแถวจากบนลงล่าง
ถ้า `target in tiles[idx]` เป็นจริง จะคืนหมายเลขแถวนั้นทันที

> [!NOTE]
>
> แถวบนสุดมีหมายเลข `0` แถวถัดไปมีหมายเลข `1` ตามลำดับ
> ถ้าไม่พบ `target` ฟังก์ชันจะคืน `-1`

ตามเงื่อนไขของโจทย์ กระดานเป็นสี่เหลี่ยมจัตุรัส มีช่องว่าง `0` เพียงหนึ่งช่อง
และหมายเลขอื่นไม่ซ้ำกัน โค้ดใช้ข้อมูลตามเงื่อนไขนี้โดยไม่ได้ตรวจความถูกต้องของกระดาน

---

## การแปลงกระดานเป็นลิสต์หนึ่งมิติ

ก่อนนับ Inversion เราต้องเรียงสมาชิกทุกแถวต่อกันเป็นลิสต์หนึ่งมิติ
และตัด `0` ซึ่งแทนช่องว่างออก ตัวอย่างเช่น

```text
[[1, 2, 0], [3, 5, 6], [4, 7, 8]]
             ↓ flatten
[1, 2, 3, 5, 6, 4, 7, 8]
```

คำสั่ง `flatten_tiles += row` นำสมาชิกทั้งหมดใน `row` มาต่อท้ายลิสต์ใหม่
เมื่อรวมครบทุกแถวแล้ว `flatten_tiles.remove(0)` จะลบ `0` ตัวแรกออก
จึงไม่แก้ไขลิสต์ `tiles` ต้นฉบับ

โจทย์รับประกันว่ากระดานที่ถูกต้องมี `0` เพียงหนึ่งตัว หากไม่มี `0`
คำสั่ง `remove(0)` จะเกิด error และหากมีหลายตัว โค้ดจะลบเพียงตัวแรกเท่านั้น

---

## การนับ Inversion

**Inversion** คือคู่ของสมาชิกที่ตัวซ้ายอยู่ก่อนตัวขวา แต่มีค่ามากกว่าตัวขวา
ถ้าใช้ดัชนี `i` และ `j` คู่หนึ่งจะเป็น Inversion เมื่อ

$$
i < j \quad \text{และ} \quad x[i] > x[j]
$$

โค้ดใช้ลูปซ้อนกันเพื่อพิจารณาแต่ละคู่เพียงครั้งเดียว

```python
for i in range(len(flat_tiles)):
    for j in range(i + 1, len(flat_tiles)):
        if flat_tiles[i] > flat_tiles[j]:
            inversion_count += 1
```

การเริ่ม `j` ที่ `i + 1` ทำให้ `j` อยู่ทางขวาของ `i` เสมอ
และเครื่องหมาย `>` หมายความว่าค่าที่เท่ากันไม่นับเป็น Inversion

สำหรับลิสต์ `[1, 2, 3, 5, 6, 4, 7, 8]` คู่ที่เป็น Inversion มีเพียง
`(5, 4)` และ `(6, 4)` จึงมีทั้งหมด `2` คู่

ส่วนลิสต์ `[8, 7, 6, 5, 4, 3, 2, 1]` เรียงจากมากไปน้อย
ทุกคู่จึงเป็น Inversion จำนวนทั้งหมดเท่ากับ

$$
\frac{8(8-1)}{2} = 28
$$

ซึ่งตรงกับการที่ลูปพบเงื่อนไข `flat_tiles[i] > flat_tiles[j]`
ครบทั้ง `28` คู่

---

## เงื่อนไขการแก้ปริศนา

ให้ `I` เป็นจำนวน Inversion และ `r` เป็นหมายเลขแถวของ `0`
เมื่อนับแถวจากบนลงล่างโดยเริ่มที่ `0` กระดานจะเลื่อนไปสู่เป้าหมายได้ตามตารางนี้

| จำนวนแถว `n` | เงื่อนไขที่ทำให้แก้ได้ |
|---|---|
| `n` เป็นเลขคี่ | `I` เป็นเลขคู่ โดย `0` อยู่แถวใดก็ได้ |
| `n` เป็นเลขคู่ | `I` และ `r` มีความเป็นคู่คี่ต่างกัน หรือ `I + r` เป็นเลขคี่ |

เงื่อนไขทั้งสองกรณีตรงกับ Python ดังนี้

```python
c1 = rows % 2 == 1 and inversion_count % 2 == 0
c2 = rows % 2 == 0 and (inversion_count + empty_row_idx) % 2 == 1
return c1 or c2
```

-   `x % 2 == 0` ตรวจว่า `x` เป็นเลขคู่
-   `x % 2 == 1` ตรวจว่า `x` เป็นเลขคี่
-   `c1 or c2` ให้ค่า `True` เมื่อเข้าเงื่อนไขอย่างน้อยหนึ่งกรณี

ตัวอย่างกระดานขนาด $3 \times 3$ ในหัวข้อก่อนหน้ามี `I = 2`
จำนวนแถวเป็นเลขคี่และจำนวน Inversion เป็นเลขคู่ จึงได้ `c1 == True`

สำหรับกระดานเป้าหมายขนาด $4 \times 4$ ค่า `I = 0` และช่องว่างอยู่แถว
`r = 3` ดังนั้น `I + r = 3` เป็นเลขคี่ กระดานจึงแก้ได้
แต่ถ้าสลับเพียง `14` กับ `15` จะได้ `I = 1` และ `I + r = 4`
ซึ่งเป็นเลขคู่ จึงแก้ไม่ได้

> [!NOTE]
>
> แม้ comment ในโค้ดจะเขียนว่า `15 puzzle` แต่เงื่อนไขในโจทย์และฟังก์ชัน
> `solvable()` ใช้กับกระดานที่ถูกต้องขนาด $n \times n$ ใด ๆ ได้

---

## การรับคำสั่งทดสอบจาก Grader

บรรทัดสุดท้ายอ่านคำสั่ง Python หนึ่งบรรทัด แล้วใช้ `exec()` สั่งทำงาน
เช่น ข้อมูลนำเข้า

```python
print(solvable([[0, 8, 7], [6, 5, 4], [3, 2, 1]]))
```

คำสั่งนี้เรียก `solvable()` แล้วแสดงผล `True` ออกทางหน้าจอ
ตัวอย่างอื่นอาจเรียก `row_number()`, `flatten()` หรือ `inversions()`
ผลลัพธ์จะแสดงเป็นรูปแบบปกติของ Python เช่น ลิสต์ จำนวนเต็ม หรือ `True`/`False`

> [!WARNING]
>
> `exec()` สามารถสั่งทำงานข้อความที่เป็นโค้ด Python ได้ จึงใช้ในข้อนี้เพื่อรองรับ
> รูปแบบการตรวจของ Grader เท่านั้น ไม่ควรใช้ `exec()` กับข้อความจากแหล่งที่ไม่น่าเชื่อถือ

---

# Solution

```python
# --------------------------------------------------
# File Name : 09_Nested_25.py
# Problem   : Tiling Puzzle
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------


# Get the row number of num in the tiles which is a 2D list.
def row_number(tiles, target):
    for idx in range(len(tiles)):
        if target in tiles[idx]:
            return idx
    return -1


# Flatten the 2D list of tiles into a 1D list, ignoring zeros.
def flatten(tiles):
    flatten_tiles = []
    for row in tiles:
        flatten_tiles += row
    flatten_tiles.remove(0)
    return flatten_tiles


# Count the number of inversions in a list.
# An inversion is a pair of indices (i, j) such that i < j and x[i] > x[j].
def inversions(flat_tiles):
    inversion_count = 0
    for i in range(len(flat_tiles)):
        for j in range(i + 1, len(flat_tiles)):
            if flat_tiles[i] > flat_tiles[j]:
                inversion_count += 1
    return inversion_count


# Check if the 15 puzzle is solvable
def solvable(tiles):
    # Tiles information
    rows = len(tiles)
    inversion_count = inversions(flatten(tiles))
    empty_row_idx = row_number(tiles, 0)

    # Condition for solvability
    c1 = rows % 2 == 1 and inversion_count % 2 == 0
    c2 = rows % 2 == 0 and (inversion_count + empty_row_idx) % 2 == 1
    return c1 or c2


# Execute an input string as code
exec(input().strip())
```
