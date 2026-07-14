<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Change of Major ★★ (
      <a href="https://drive.google.com/file/d/1yA8yH-Dgw-BvW8xSvtdKQ4XUjsrqT13-/view?usp=drive_link">
        <code>03_If_02</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**เกณฑ์การผ่านคุณสมบัติ**](#เกณฑ์การผ่านคุณสมบัติ)
-   [**การเปรียบเทียบลำดับความสำคัญ**](#การเปรียบเทียบลำดับความสำคัญ)
-   [**ผลลัพธ์ทุกกรณี**](#ผลลัพธ์ทุกกรณี)
-   [**Solution**](#solution)

---

## เกณฑ์การผ่านคุณสมบัติ

โปรแกรมรับข้อมูลนิสิต 2 คน คนละหนึ่งบรรทัด แต่ละบรรทัดเรียงข้อมูลดังนี้

1. เลขประจำตัวนิสิต เก็บเป็น `str`
2. GPAX แปลงเป็น `float`
3. เกรดวิชา Computer Programming เก็บเป็น `str`
4. เกรด Calculus 1 เก็บเป็น `str`
5. เกรด Calculus 2 เก็บเป็น `str`

การเก็บเลขประจำตัวเป็นข้อความช่วยรักษาตัวเลขทุกหลักไว้ ส่วน GPAX
ต้องเป็นจำนวนจริงเพื่อใช้เปรียบเทียบเชิงตัวเลข โค้ดใช้ `split()` แยกทั้ง 5 ค่า
แล้วกำหนดให้ตัวแปรของคนที่ 1 และคนที่ 2 แยกจากกัน

นิสิตจะผ่านคุณสมบัติเมื่อเกรด Computer Programming เป็น `A`
และ Calculus ทั้งสองวิชาได้อย่างน้อย `C`

```python
is_qualified_01 = (com_01 == "A") and (calculus1_01 <= "C") and (calculus2_01 <= "C")
```

โจทย์รับประกันว่าเกรดเป็นเพียง `A`, `B`, `C`, `D` หรือ `F`
ซึ่งเรียงตามตัวอักษรเป็น `"A" < "B" < "C" < "D" < "F"`
ดังนั้น `grade <= "C"` จึงยอมรับ `A`, `B` และ `C` ได้พอดี

> [!NOTE]
>
> การเปรียบเทียบข้อความแบบนี้อาศัยชุดเกรดที่โจทย์รับประกัน
> ไม่ใช่วิธีแปลงข้อความใด ๆ ให้เป็นคะแนนทั่วไป

## การเปรียบเทียบลำดับความสำคัญ

ถ้าผ่านคุณสมบัติทั้งสองคน โปรแกรมสร้างลิสต์สำหรับเปรียบเทียบดังนี้

```python
student_01 = [-gpax_01, calculus1_01, calculus2_01]
student_02 = [-gpax_02, calculus1_02, calculus2_02]
```

Python เปรียบเทียบลิสต์จากสมาชิกซ้ายไปขวา และหยุดที่คู่แรกที่ต่างกัน
จึงตรงกับลำดับความสำคัญของโจทย์

1. เปรียบเทียบ `-gpax` ก่อน การใส่เครื่องหมายลบทำให้ GPAX ที่มากกว่า
   กลายเป็นค่าที่น้อยกว่า เช่น `-3.5 < -3.1`
2. ถ้า GPAX เท่ากัน จึงเปรียบเทียบเกรด Calculus 1
   ตัวอักษรที่น้อยกว่าเป็นเกรดที่สูงกว่า
3. ถ้ายังเท่ากัน จึงเปรียบเทียบเกรด Calculus 2 ด้วยหลักเดียวกัน

ดังนั้น `student_01 < student_02` หมายถึงคนที่ 1 มีลำดับดีกว่า
ส่วน `student_01 > student_02` หมายถึงคนที่ 2 ดีกว่า
ถ้าลิสต์เท่ากันทั้งหมด โปรแกรมต้องเลือกทั้งคู่และแสดง `Both`

## ผลลัพธ์ทุกกรณี

| คุณสมบัติและผลเปรียบเทียบ | สิ่งที่แสดง |
|---|---|
| ไม่ผ่านทั้งสองคน | `None` |
| ผ่านเฉพาะคนที่ 1 | เลขประจำตัวคนที่ 1 |
| ผ่านเฉพาะคนที่ 2 | เลขประจำตัวคนที่ 2 |
| ผ่านทั้งคู่ และคนที่ 1 มีลำดับดีกว่า | เลขประจำตัวคนที่ 1 |
| ผ่านทั้งคู่ และคนที่ 2 มีลำดับดีกว่า | เลขประจำตัวคนที่ 2 |
| ผ่านทั้งคู่ และเกณฑ์ทั้งสามเท่ากัน | `Both` |

ตัวอย่างเช่น ถ้าทั้งคู่ผ่านเกณฑ์ คนที่ 1 มีข้อมูล GPAX/Calculus เป็น
`3.1, B, B` และคนที่ 2 เป็น `3.0, A, A` โปรแกรมเลือกคนที่ 1
ทันทีจาก GPAX โดยยังไม่ใช้เกรด Calculus

คอมเมนต์ในโค้ดเขียนว่า `Output the result for each student`
แต่พฤติกรรมจริงตามโจทย์คือแสดงผลการเลือกเพียงหนึ่งบรรทัด
ได้แก่เลขประจำตัวหนึ่งคน, `Both` หรือ `None` ไม่ได้แสดงสถานะของนิสิต
แต่ละคนแยกกัน คอมเมนต์เดิมยังคงอยู่ใน Solution เพื่อให้ตรงกับไฟล์ต้นฉบับ

---

# Solution

```python
# --------------------------------------------------
# File Name : 03_If_02.py
# Problem   : Change of Major
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------

# Input two students' information
data = input().strip().split()
id_01, com_01, calculus1_01, calculus2_01 = data[0], data[2], data[3], data[4]
gpax_01 = float(data[1])

data = input().strip().split()
id_02, com_02, calculus1_02, calculus2_02 = data[0], data[2], data[3], data[4]
gpax_02 = float(data[1])

# Set initial values for success of change of major
# A student must have COM equal to A and CALCULUS at least C
is_qualified_01 = (com_01 == "A") and (calculus1_01 <= "C") and (calculus2_01 <= "C")
is_qualified_02 = (com_02 == "A") and (calculus1_02 <= "C") and (calculus2_02 <= "C")

# Output the result for each student
if is_qualified_01 and is_qualified_02:
    # Compare GPAX then CALCULUS 1 and CALCULUS 2
    student_01 = [-gpax_01, calculus1_01, calculus2_01]
    student_02 = [-gpax_02, calculus1_02, calculus2_02]
    if student_01 < student_02:
        print(id_01)
    elif student_01 > student_02:
        print(id_02)
    else:
        print("Both")

elif is_qualified_01:
    print(id_01)

elif is_qualified_02:
    print(id_02)

else:
    print("None")
```
