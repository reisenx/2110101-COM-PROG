<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Change of Major (Function) ★★ (
      <a href="https://drive.google.com/file/d/1nQPh-_8_xB0CoRFRaLPMdGSMfGRpBB1v/view?usp=drive_link">
        <code>03_If_F02</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**สัญญาของฟังก์ชัน**](#สัญญาของฟังก์ชัน)
-   [**การตรวจสอบคุณสมบัติ**](#การตรวจสอบคุณสมบัติ)
-   [**การเปรียบเทียบผู้สมัคร**](#การเปรียบเทียบผู้สมัคร)
-   [**การทำงานของตัวตรวจ**](#การทำงานของตัวตรวจ)
-   [**Solution**](#solution)

---

## สัญญาของฟังก์ชัน

โจทย์ต้องการฟังก์ชันที่มีแนวคิดของสัญญาดังนี้

```python
choose(student_01, student_02) -> list[str]
```

พารามิเตอร์แต่ละตัวเป็นลิสต์ข้อมูลนิสิต 5 ค่าในลำดับ
`[ID, GPAX, comprog, cal1, cal2]`

| ข้อมูล | ชนิดข้อมูล | ความหมาย |
|---|---|---|
| `ID` | `str` | เลขประจำตัวนิสิต |
| `GPAX` | `float` | เกรดเฉลี่ยสะสม |
| `comprog`, `cal1`, `cal2` | `str` | เกรดรายวิชา ซึ่งเป็น `A`, `B`, `C`, `D` หรือ `F` |

คำสั่งกำหนดค่าหลายตัวพร้อมกัน เช่น

```python
id_01, gpax_01, com_01, calculus1_01, calculus2_01 = student_01
```

เรียกว่า **การ unpack ลิสต์** ทำให้แต่ละช่องมีชื่อตามความหมายและนำไปใช้ใน
เงื่อนไขได้อ่านง่ายขึ้น

ฟังก์ชันส่งกลับลิสต์ของเลขประจำตัวที่ได้รับเลือก อาจเป็นลิสต์ว่าง
ลิสต์ที่มีหนึ่งค่า หรือลิสต์ที่มีสองค่า ฟังก์ชันใช้ `return` ส่งคำตอบกลับไปยัง
ผู้เรียกและไม่ได้ `print()` คำตอบเอง

## การตรวจสอบคุณสมบัติ

นิสิตผ่านเกณฑ์เบื้องต้นเมื่อได้เกรด `A` ในวิชา Computer Programming
และได้เกรดไม่ต่ำกว่า `C` ใน Calculus I และ Calculus II

```python
com_01 == "A" and calculus1_01 <= "C" and calculus2_01 <= "C"
```

Python เปรียบเทียบข้อความตามลำดับตัวอักษร สำหรับชุดเกรดที่โจทย์รับประกัน
ลำดับ `A < B < C < D < F` ตรงกับลำดับจากเกรดดีกว่าไปเกรดต่ำกว่า
ดังนั้น `grade <= "C"` จึงหมายถึงเกรด `A`, `B` หรือ `C`

> [!NOTE]
>
> วิธีเปรียบเทียบเกรดด้วยข้อความใช้ได้เพราะโจทย์จำกัดค่าไว้เป็น
> `A`, `B`, `C`, `D`, `F` เท่านั้น ไม่ควรสรุปว่าข้อความแทนเกรดทุกรูปแบบ
> จะเรียงตามคุณภาพได้โดยอัตโนมัติ

## การเปรียบเทียบผู้สมัคร

ถ้ามีนิสิตผ่านเกณฑ์เพียงคนเดียว ฟังก์ชันส่งกลับเลขประจำตัวของคนนั้นทันที
แต่ถ้าผ่านทั้งสองคน ต้องเปรียบเทียบตามลำดับ GPAX, เกรด Calculus I
และเกรด Calculus II

โค้ดสร้างกุญแจเปรียบเทียบดังนี้

```python
grades_01 = [-gpax_01, calculus1_01, calculus2_01]
grades_02 = [-gpax_02, calculus1_02, calculus2_02]
```

Python เปรียบเทียบลิสต์แบบ **lexicographic** คือเริ่มจากสมาชิกตัวแรก
และพิจารณาสมาชิกถัดไปเมื่อค่าก่อนหน้าเท่ากัน กุญแจที่มีค่าน้อยกว่าเป็นผู้ชนะ

1. ใช้ `-gpax` เพื่อให้ผู้ที่มี GPAX มากกว่ากลายเป็นค่าติดลบที่น้อยกว่า
2. ถ้า GPAX เท่ากัน เกรด Calculus I ที่ดีกว่าจะเป็นตัวอักษรที่น้อยกว่า
3. ถ้ายังเท่ากัน จึงเปรียบเทียบเกรด Calculus II

ผลลัพธ์ทั้งหมดจึงเป็นดังนี้

| สถานการณ์ | ค่าที่ `return` |
|---|---|
| ไม่มีผู้ผ่านเกณฑ์ | `[]` |
| ผ่านเพียงคนเดียว | `[id_01]` หรือ `[id_02]` |
| ผ่านทั้งคู่และคนหนึ่งมีกุญแจดีกว่า | ลิสต์ที่มี ID ของคนนั้น |
| ผ่านทั้งคู่และกุญแจเท่ากันทุกค่า | `[id_01, id_02]` |

กรณีเสมอ ฟังก์ชันรักษาลำดับพารามิเตอร์ คือ ID ของ `student_01`
อยู่ก่อน ID ของ `student_02` โดยไม่ได้นำเลขประจำตัวมาเรียงใหม่

## การทำงานของตัวตรวจ

ข้อมูลนำเข้าของโปรแกรมนี้เป็นคำสั่ง Python หนึ่งบรรทัดที่ grader ควบคุม เช่น

```python
print(choose(["7039999921", 3.5, "A", "B", "A"], ["7030000021", 3.5, "A", "B", "A"]))
```

`exec(input())` อ่านคำสั่งนั้นแล้วสั่งให้ Python ทำงาน จึงสามารถเรียก
`choose()` และใช้ `print()` แสดงลิสต์ที่ฟังก์ชันส่งกลับได้

> [!WARNING]
>
> `exec()` สามารถรันคำสั่ง Python ใด ๆ ที่ได้รับมา จึงใช้ได้ในข้อนี้เพราะ
> ข้อมูลมาจาก grader ที่เชื่อถือได้เท่านั้น ห้ามใช้ `exec()` กับข้อมูลจาก
> ผู้ใช้หรือแหล่งที่ไม่เชื่อถือ

---

# Solution

```python
# --------------------------------------------------
# File Name : 03_If_F02.py
# Problem   : Change of Major (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------


def choose(student_01, student_02):
    # Assign variables
    id_01, gpax_01, com_01, calculus1_01, calculus2_01 = student_01
    id_02, gpax_02, com_02, calculus1_02, calculus2_02 = student_02

    # Set initial values for success of change of major
    # A student must have COM equal to A and CAL at least C
    is_qualified_01 = com_01 == "A" and calculus1_01 <= "C" and calculus2_01 <= "C"
    is_qualified_02 = com_02 == "A" and calculus1_02 <= "C" and calculus2_02 <= "C"

    # Find the result of change of major
    if is_qualified_01 and is_qualified_02:
        # Compare GPAX then CAL1 and CAL2
        grades_01 = [-gpax_01, calculus1_01, calculus2_01]
        grades_02 = [-gpax_02, calculus1_02, calculus2_02]

        if grades_01 < grades_02:
            return [id_01]
        if grades_01 > grades_02:
            return [id_02]
        return [id_01, id_02]

    if is_qualified_01:
        return [id_01]

    if is_qualified_02:
        return [id_02]

    return []


# Execute the input string as code
exec(input())
```
