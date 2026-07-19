<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Friends ★★ (
      <a href="https://drive.google.com/file/d/1_I8h_pHSZyKAuHf4Xf_KONQZnPnCFmD_/view?usp=sharing">
        <code>2566_2_Q3_02</code>
      </a>
    )
  </h1>
</div>

# Contents

- [**แนวคิด**](#แนวคิด)
- [**ขั้นตอนการแก้ปัญหา**](#ขั้นตอนการแก้ปัญหา)
- [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
- [**รูปแบบข้อมูลและ Grader**](#รูปแบบข้อมูลและ-grader)
- [**ข้อควรระวัง**](#ข้อควรระวัง)
- [**Solution**](#solution)

---

# แนวคิด

ความสัมพันธ์เพื่อนในข้อนี้เป็นความสัมพันธ์แบบ **สองทิศทาง** ถ้า `A` เป็นเพื่อนกับ `B` แล้ว `B` ก็เป็นเพื่อนกับ `A` ด้วย จึงมองแต่ละชื่อเป็นจุด และทูเปิล `(A, B)` เป็นเส้นเชื่อมระหว่างสองจุดได้

เราต้องรู้ว่าแต่ละคนมีเพื่อนที่ **ไม่ซ้ำกัน** กี่คน โครงสร้างข้อมูลที่เหมาะสมคือ dictionary ที่จับคู่ชื่อกับ `set` ของเพื่อน เช่น

```python
{
    "A": {"B", "C"},
    "B": {"A"},
    "C": {"A"},
}
```

การใช้ `set` ทำให้เพิ่มชื่อเดิมซ้ำแล้วจำนวนสมาชิกไม่เพิ่ม ดังนั้นข้อมูล `(A, B)`, `(A, B)` และ `(B, A)` จะนับเป็นความสัมพันธ์เดียวกัน

ถ้าให้ $F(x)$ เป็นเซตเพื่อนของคนชื่อ $x$ จำนวนเพื่อนคือ

$$
\operatorname{count}(x) = |F(x)|
$$

ซึ่งตรงกับ Python ว่า `len(all_friends[name])`

# ขั้นตอนการแก้ปัญหา

1. สร้าง dictionary ว่างชื่อ `all_friends`
2. สำหรับความสัมพันธ์ `(a, b)` ทุกคู่ สร้างเซตของทั้งสองชื่อหากยังไม่มี
3. เพิ่ม `b` ลงในเซตของ `a` และเพิ่ม `a` ลงในเซตของ `b`

   ```python
   all_friends[a].add(b)
   all_friends[b].add(a)
   ```

4. เรียง `names` ด้วย `sorted(names)` เพื่อให้ผลลัพธ์เรียงตามลำดับพจนานุกรม
5. สำหรับแต่ละชื่อ ถ้าชื่อนั้นไม่มีใน dictionary ให้จำนวนเพื่อนเป็น `0` มิฉะนั้นใช้ขนาดของเซต
6. เพิ่ม `(name, count)` ลงใน `result` แล้วคืนลิสต์เมื่อทำครบทุกชื่อ

การสร้างเซตเพื่อนใช้เวลาโดยเฉลี่ย $O(E)$ เมื่อ $E$ คือจำนวนความสัมพันธ์ และการเรียงชื่อที่สนใจ $N$ ชื่อใช้เวลา $O(N\log N)$

# ตัวอย่างการทำงาน

พิจารณาความสัมพันธ์ต่อไปนี้

```python
[
    ("C", "D"),
    ("C", "D"),
    ("D", "C"),
    ("D", "C"),
    ("C", "d"),
    ("a", "B"),
    ("B", "C"),
]
```

แม้ความสัมพันธ์ระหว่าง `C` กับ `D` ปรากฏหลายครั้ง แต่ `set` ของ `C` คือ `{"D", "d", "B"}` จึงมีเพื่อน `3` คน

เมื่อ `names` เป็น `['C', 'A', 'C', 'd']` จะเรียงได้เป็น `['A', 'C', 'C', 'd']` แล้วคืนค่า

```python
[('A', 0), ('C', 3), ('C', 3), ('d', 1)]
```

สังเกตว่า `C` ปรากฏในคำตอบสองครั้ง เพราะโจทย์ให้ `C` มาใน `names` สองครั้ง และ `A` ต่างจาก `a` เพราะ Python เปรียบเทียบตัวพิมพ์เล็กและตัวพิมพ์ใหญ่แยกกัน

# รูปแบบข้อมูลและ Grader

ฟังก์ชัน `read_friends()` อ่านจำนวนความสัมพันธ์ `N` แล้วอ่านชื่อสองชื่ออีก `N` บรรทัด แต่ละบรรทัดถูกเก็บเป็นทูเปิล

บรรทัดแรกที่ grader ป้อนเป็นคำสั่ง Python เช่น

```python
dat=read_friends();print(count_friends(dat,['A','D','E']))
```

เมื่อ `exec(input().strip())` ทำงานคำสั่งนี้ `read_friends()` จะอ่าน `N` และความสัมพันธ์ จากนั้น `count_friends()` คืนลิสต์ของทูเปิล และ `print(...)` แสดงลิสต์นั้นทางจอภาพ ฟังก์ชัน `count_friends()` เองไม่ได้พิมพ์ผลลัพธ์

> [!WARNING]
> `exec()` สามารถทำงานคำสั่ง Python ที่ได้รับมาได้ทั้งหมด ที่ใช้ในข้อนี้เพราะ grader ส่งคำสั่งทดสอบที่เชื่อถือได้เท่านั้น ไม่ควรนำ `exec(input())` ไปใช้กับข้อมูลจากผู้ใช้หรือแหล่งที่ไม่เชื่อถือ

# ข้อควรระวัง

- ต้องเพิ่มความสัมพันธ์ทั้ง `a → b` และ `b → a`
- ต้องใช้ `set` เพื่อไม่ให้คู่ซ้ำหรือคู่ที่สลับลำดับถูกนับเพิ่ม
- ชื่อที่ไม่ปรากฏในข้อมูลความสัมพันธ์ต้องได้จำนวนเพื่อน `0`
- `sorted(names)` ไม่ลบชื่อซ้ำ ดังนั้นชื่อที่ถูกถามซ้ำต้องปรากฏในผลลัพธ์ซ้ำ
- ชื่อแยกตัวพิมพ์เล็กและตัวพิมพ์ใหญ่ เช่น `A` ไม่ใช่ชื่อเดียวกับ `a`
- ค่าที่คืนเป็นลิสต์ของทูเปิล `(ชื่อ, จำนวนเพื่อน)` ไม่ใช่ dictionary

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_2_Q3_02.py
# Problem   : Friends
# Author    : Worralop Srichainont
# Date      : 2025-07-15
# --------------------------------------------------


# Read relationship data and return a list of tuples.
def read_friends():
    friends = []
    n = int(input())
    for _ in range(n):
        friends.append(tuple(input().strip().split()))
    return friends


# Count the number of friends for each person in the list of names.
def count_friends(friends, names):
    # Create a dictionary to store set of friends of each person.
    all_friends = {}
    for a, b in friends:
        # Initialize the sets for each person if they do not exist.
        if a not in all_friends:
            all_friends[a] = set()
        if b not in all_friends:
            all_friends[b] = set()
        # Add each person to the other's set of friends.
        all_friends[a].add(b)
        all_friends[b].add(a)

    # Sort the names and count the number of friends for each.
    result = []
    for name in sorted(names):
        # If the name is not in the dictionary, they have no friends.
        if name not in all_friends:
            result.append((name, 0))
        # Otherwise, append the name and the count of friends.
        else:
            result.append((name, len(all_friends[name])))
    # Return the sorted list of tuples with names and their friend counts.
    return result


# Execute the input string as code
exec(input().strip())
```
