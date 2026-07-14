<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    DNA ★★ (
      <a href="https://drive.google.com/file/d/1Wf86Zr6UPfiMRRsVYhBadj8Yu2H5rkZ8/view?usp=drive_link">
        <code>07_StrFile_31</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การเตรียมและตรวจสอบสาย DNA**](#การเตรียมและตรวจสอบสาย-dna)
-   [**การหาคู่สมของนิวคลีโอไทด์**](#การหาคู่สมของนิวคลีโอไทด์)
-   [**การทำงานของโอเปอร์เรเตอร์ R**](#การทำงานของโอเปอร์เรเตอร์-r)
-   [**การทำงานของโอเปอร์เรเตอร์ F**](#การทำงานของโอเปอร์เรเตอร์-f)
-   [**การทำงานของโอเปอร์เรเตอร์ D**](#การทำงานของโอเปอร์เรเตอร์-d)
-   [**Solution**](#solution)

---

## การเตรียมและตรวจสอบสาย DNA

สาย DNA ที่ถูกต้องประกอบด้วยนิวคลีโอไทด์เพียง 4 ชนิด คือ `A`, `T`, `G`
และ `C` โดยโจทย์ถือว่าตัวพิมพ์เล็กและตัวพิมพ์ใหญ่ไม่ต่างกัน โปรแกรมจึงใช้
`strip()` ตัดช่องว่างที่หัวและท้าย แล้วใช้ `upper()` เปลี่ยนข้อมูลเป็นตัวพิมพ์ใหญ่

```python
dna = input().strip().upper()
```

ค่าคงที่ `NUCLEOTIDE = "AGTC"` รวมอักขระที่ยอมรับไว้ โปรแกรมเริ่มต้นด้วย
`is_dna = True` แล้วตรวจอักขระทีละตัว หากพบอักขระที่ไม่อยู่ใน
`NUCLEOTIDE` จะเปลี่ยนค่าเป็น `False` และใช้ `break` หยุดตรวจทันที

```python
for char in dna:
    if char not in NUCLEOTIDE:
        is_dna = False
        break
```

โปรแกรมรับชื่อโอเปอร์เรเตอร์ในบรรทัดถัดไปและเปลี่ยนเป็นตัวพิมพ์ใหญ่เช่นกัน
ถ้า DNA ไม่ถูกต้อง โปรแกรมจะไม่ทำโอเปอร์เรเตอร์ แต่แสดงข้อความ
`Invalid DNA` เพียงบรรทัดเดียว

## การหาคู่สมของนิวคลีโอไทด์

นิวคลีโอไทด์แต่ละชนิดมีคู่สมดังนี้

| นิวคลีโอไทด์ | คู่สม |
|---|---|
| `A` | `T` |
| `T` | `A` |
| `G` | `C` |
| `C` | `G` |

ลำดับอักขระใน `NUCLEOTIDE` คือ `A`, `G`, `T`, `C` ทำให้คู่สมของแต่ละตัว
อยู่ห่างออกไป 2 ตำแหน่งแบบวนรอบ โปรแกรมจึงหา index ใหม่ด้วยสูตร

$$
\text{complement index} = (\text{index} + 2) \bmod 4
$$

ซึ่งเขียนในภาษา Python ได้เป็น

```python
NUCLEOTIDE[(idx + 2) % 4]
```

ตัวอย่างเช่น `A` อยู่ตำแหน่ง `0` จึงได้ตำแหน่ง `(0 + 2) % 4 = 2`
ซึ่งเป็น `T` ส่วน `C` อยู่ตำแหน่ง `3` จึงวนกลับไปตำแหน่ง
`(3 + 2) % 4 = 1` ซึ่งเป็น `G`

## การทำงานของโอเปอร์เรเตอร์ R

โอเปอร์เรเตอร์ `R` ใช้หา **reverse complement** โดยทำสองขั้นตอนตามลำดับ

1. เปลี่ยนนิวคลีโอไทด์ทุกตัวให้เป็นคู่สม แล้วต่อผลไว้ใน `modified_dna`
2. กลับลำดับข้อความด้วย slice `[::-1]` ก่อนแสดงผล

ตัวอย่าง `AGTC` จะถูกเปลี่ยนเป็นคู่สม `TCAG` ก่อน แล้วจึงกลับลำดับเป็น
`GACT` การเปลี่ยนเป็นคู่สมก่อนกลับลำดับทำให้เห็นกระบวนการตรงกับนิยามของโจทย์

```python
print(modified_dna[::-1])
```

## การทำงานของโอเปอร์เรเตอร์ F

โอเปอร์เรเตอร์ `F` นับความถี่ของนิวคลีโอไทด์แต่ละชนิด โปรแกรมสร้าง
`counts = [0] * 4` แล้วเพิ่มช่องที่ตรงกับตำแหน่งของอักขระใน
`NUCLEOTIDE`

เนื่องจาก `NUCLEOTIDE` เรียงเป็น `A`, `G`, `T`, `C` ค่าภายในลิสต์จึงอยู่
ในลำดับนี้ โปรแกรมแยกค่าออกมาเป็น `A, G, T, C` ก่อนจัดลำดับการแสดงผลใหม่
ให้ตรงตามโจทย์ คือ `A`, `T`, `G`, `C`

```python
A, G, T, C = counts
print(f"A={A}, T={T}, G={G}, C={C}")
```

รูปแบบผลลัพธ์มีช่องว่างหนึ่งช่องหลังเครื่องหมายจุลภาคทุกตัว เช่น
`A=3, T=5, G=3, C=4`

## การทำงานของโอเปอร์เรเตอร์ D

โอเปอร์เรเตอร์ `D` ใช้นับจำนวนครั้งที่คู่นิวคลีโอไทด์ที่กำหนดปรากฏติดกัน
โปรแกรมจะรับข้อมูลคู่เพิ่มอีกหนึ่งบรรทัด **เฉพาะเมื่อ DNA ถูกต้องและ
โอเปอร์เรเตอร์เป็น `D`** แล้วเปลี่ยนคู่ดังกล่าวเป็นตัวพิมพ์ใหญ่

การหาคู่ทำด้วยหน้าต่างยาว 2 ตัวอักษร โดยเริ่มที่ตำแหน่ง `i` ตั้งแต่ `0` ถึง
`len(dna) - 2`

```python
for i in range(len(dna) - 1):
    if dna[i : i + 2] == pair:
        pair_count += 1
```

คู่มีลำดับ ดังนั้น `GC` ไม่เท่ากับ `CG` และโปรแกรมเลื่อนหน้าต่างครั้งละหนึ่ง
ตำแหน่งจึงนับคู่ที่ซ้อนกันได้ ตัวอย่าง DNA `AAAA` มีหน้าต่าง `AA` ที่เริ่ม ณ
ตำแหน่ง `0`, `1` และ `2` รวมทั้งหมด `3` คู่

> [!NOTE]
>
> หากสาย DNA มีอักขระที่ไม่ถูกต้อง โปรแกรมจะแสดง `Invalid DNA` โดยไม่รับ
> บรรทัดข้อมูลคู่เพิ่ม แม้ชื่อโอเปอร์เรเตอร์ที่รับไว้จะเป็น `D`

---

# Solution

```python
# --------------------------------------------------
# File Name : 07_StrFile_31.py
# Problem   : DNA
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# Initialize the nucleotide characters
NUCLEOTIDE = "AGTC"

# Input DNA sequence
dna = input().strip().upper()

# Validate the DNA sequence
is_dna = True
for char in dna:
    if char not in NUCLEOTIDE:
        is_dna = False
        break

# Input command
cmd = input().strip().upper()

# Process commands if the sequence is valid
if is_dna:
    # Reverse the DNA sequence
    # Change A to T, T to A, C to G, and G to C
    # Then reverse the string
    if cmd == "R":
        modified_dna = ""
        for char in dna:
            idx = NUCLEOTIDE.index(char)
            modified_dna += NUCLEOTIDE[(idx + 2) % 4]
        print(modified_dna[::-1])

    # Count the occurrences of each nucleotide
    elif cmd == "F":
        counts = [0] * 4
        for char in dna:
            idx = NUCLEOTIDE.index(char)
            counts[idx] += 1
        # Output
        A, G, T, C = counts
        print(f"A={A}, T={T}, G={G}, C={C}")

    # Count the occurrences of a specific nucleotide pair
    elif cmd == "D":
        pair = input().strip().upper()
        pair_count = 0
        for i in range(len(dna) - 1):
            if dna[i : i + 2] == pair:
                pair_count += 1
        print(pair_count)

# Invalid DNA sequence
else:
    print("Invalid DNA")
```
