<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Planting Plan ★★ (
      <a href="https://drive.google.com/file/d/1Luxu2wqzZvYnYrAJkCIlvHvX__ANruyE/view?usp=sharing">
        <code>2567_3_Q2_A2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ความหมายของระยะห่าง**](#ความหมายของระยะห่าง)
-   [**สร้างแผนจากต้นไม้ทีละคู่**](#สร้างแผนจากต้นไม้ทีละคู่)
-   [**ปรับความยาวให้เท่ากับพื้นที่**](#ปรับความยาวให้เท่ากับพื้นที่)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## ความหมายของระยะห่าง

ข้อมูลนำเข้ามีสามบรรทัดตามลำดับ

1.  จำนวนเต็ม `L` หรือ `field_limit` คือความยาวของพื้นที่
2.  ระยะห่างของต้นไม้ชนิด `A`, `B`, `C` ตามลำดับ
3.  ข้อความ `trees_order` บอกลำดับต้นไม้ที่ต้องการปลูก

โจทย์กำหนดว่าถ้าต้นไม้สองต้นต้องอยู่ห่างกัน $k$ ช่อง จะมีจุด `.` คั่นกลาง
$k - 1$ ตัว ตัวอย่างเช่น ระยะห่าง `3` เขียนเป็น `A..A`

ถ้าให้ $k_i$ เป็นระยะห่างของต้นไม้ชนิด $i$ จำนวนจุดที่ต้องเว้นคือ

$$
g_i = k_i - 1
$$

โค้ดจึงลบ 1 จากระยะของต้นไม้ทั้งสามชนิดทันทีที่รับข้อมูล

```python
tree_distance = [int(num) - 1 for num in input().split()]
```

รายการ `TREE_TYPES = ["A", "B", "C"]` ใช้จับคู่ชนิดต้นไม้กับตำแหน่งของ
ระยะห่าง เช่น `TREE_TYPES.index("B")` ได้ตำแหน่ง `1` ซึ่งตรงกับระยะของ `B`

---

## สร้างแผนจากต้นไม้ทีละคู่

โปรแกรมพิจารณาต้นไม้ที่อยู่ติดกันทีละคู่ ตั้งแต่คู่แรกจนถึงคู่รองสุดท้าย
ถ้าต้นไม้สองชนิดมีระยะไม่เท่ากัน โจทย์ให้ใช้ระยะที่มากกว่า จึงคำนวณด้วย

```python
distance = max(tree_distance[idx_01], tree_distance[idx_02])
```

เนื่องจากค่าใน `tree_distance` ถูกแปลงเป็นจำนวนจุดแล้ว `distance` จึงเป็น
จำนวน `.` ที่ต้องใส่ระหว่างต้นไม้คู่นั้นโดยตรง ในแต่ละรอบโปรแกรมต่อ
ต้นไม้ต้นปัจจุบันและจุดเข้ากับ `planting_result`

```python
planting_result += tree_01 + ("." * distance)
```

ลูปหยุดก่อนต้นไม้ต้นสุดท้าย เพราะต้นสุดท้ายไม่มีต้นถัดไปให้คำนวณระยะ
จึงนำต้นสุดท้ายมาต่อเพิ่มหลังจบลูปด้วย `planting_result += trees_order[-1]`
โจทย์รับประกันว่ามีต้นไม้อย่างน้อยหนึ่งต้น ทำให้ `trees_order[-1]` ใช้งานได้

---

## ปรับความยาวให้เท่ากับพื้นที่

แผนที่สร้างจากต้นไม้ทั้งหมดอาจสั้นหรือยาวกว่า `field_limit` โปรแกรมจึงปรับ
ผลลัพธ์ให้มีความยาวเท่ากับ `L` เสมอ

-   ถ้าแผนสั้นกว่า `L` ให้เติม `.` ทางขวาจนครบพื้นที่
-   ถ้าแผนยาวกว่า `L` ให้ตัดเอาเฉพาะ `planting_result[:field_limit]`
-   ถ้ายาวเท่ากับ `L` อยู่แล้ว ไม่ต้องเปลี่ยนแปลง

การตัดข้อความจากซ้ายสอดคล้องกับเงื่อนไขที่ให้ต้นไม้ต้นแรกอยู่ซ้ายสุดเสมอ
ถ้าพื้นที่หมดก่อนปลูกต้นไม้ครบ ต้นไม้และช่องว่างส่วนที่เลยขอบด้านขวาจะไม่ถูก
แสดงผล

---

## ตัวอย่างการทำงาน

**ตัวอย่างที่ 1: ระยะพอดีกับพื้นที่**

กำหนด `L = 9`, ระยะของ `A B C` เป็น `1 2 3` และต้องการปลูก `BBBBB`
ระยะของ `B` เท่ากับ 2 จึงมีจุดคั่นต้นละหนึ่งจุด ได้ผลลัพธ์ยาว 9 ตัวพอดี

```text
B.B.B.B.B
```

**ตัวอย่างที่ 2: เติมพื้นที่ว่างด้านขวา**

กำหนด `L = 5`, ระยะเป็น `1 4 2` และลำดับเป็น `AC` ระยะที่มากกว่าระหว่าง
`A` กับ `C` คือ 2 จึงใช้จุดหนึ่งตัว ได้แผน `A.C` แล้วเติมอีกสองจุด

```text
A.C..
```

**ตัวอย่างที่ 3: พื้นที่หมดก่อนปลูกครบ**

กำหนด `L = 5`, ระยะเป็น `6 4 2` และลำดับเป็น `AA` แผนเต็มก่อนตัดคือ
`A.....A` แต่พื้นที่รับได้เพียง 5 ตัวแรก จึงแสดง

```text
A....
```

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_3_Q2_A2.py
# Problem   : Planting Plan
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------

# Constants for tree types names
TREE_TYPES = ["A", "B", "C"]

# Input length of the field and tree distances
field_limit = int(input())
tree_distance = [int(num) - 1 for num in input().split()]

# Input the order of trees to be planted
trees_order = input().strip()

# Construct a string to show the planting result
planting_result = ""
for i in range(len(trees_order) - 1):
    # Get the current and next tree type
    tree_01 = trees_order[i]
    tree_02 = trees_order[i + 1]

    # Convert tree types to indices
    idx_01 = TREE_TYPES.index(tree_01)
    idx_02 = TREE_TYPES.index(tree_02)

    # Calculate the distance between the current and next tree
    distance = max(tree_distance[idx_01], tree_distance[idx_02])

    # Append the current tree and the distance to the result
    planting_result += tree_01 + ("." * distance)

# Append the last tree to the result
planting_result += trees_order[-1]

# Ensure the planting result does not exceed the field limit
if len(planting_result) < field_limit:
    remaining_space = field_limit - len(planting_result)
    planting_result += "." * remaining_space

elif len(planting_result) > field_limit:
    planting_result = planting_result[:field_limit]

# Output the final planting result
print(planting_result)
```
