<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Body Surface Area (Function) ★ (
      <a href="https://drive.google.com/file/d/1Y5w8Sg8FVCjdQD4DcAN8ckEvMk85V06Y/view?usp=drive_link">
        <code>01_Expr_07</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ส่วนประกอบของฟังก์ชัน**](#ส่วนประกอบของฟังก์ชัน)
-   [**ฟังก์ชันคำนวณทั้งสามสูตร**](#ฟังก์ชันคำนวณทั้งสามสูตร)
-   [**หน้าที่ของ main**](#หน้าที่ของ-main)
-   [**การสั่งทำงานด้วย exec**](#การสั่งทำงานด้วย-exec)
-   [**ความคลาดเคลื่อนของจำนวนจริง**](#ความคลาดเคลื่อนของจำนวนจริง)
-   [**Solution**](#solution)

---

## ส่วนประกอบของฟังก์ชัน

ฟังก์ชันช่วยแยกงานหนึ่งอย่างออกมาเป็นส่วนที่เรียกใช้ซ้ำและทดสอบแยกกันได้
ตัวอย่างโครงสร้างในข้อนี้คือ

```python
def mosteller(w, h):
    return math.sqrt((w * h) / 3600)
```

-   `w` และ `h` คือ **parameters** หรือตัวแปรที่รับค่าจากผู้เรียก
-   `return` ส่งผลการคำนวณกลับไปยังจุดที่เรียกฟังก์ชัน

การเขียน `def` เป็นเพียงการประกาศฟังก์ชัน เนื้อหาจะทำงานเมื่อมีการเรียก เช่น
`mosteller(56, 173)` และค่าที่คืนมาสามารถนำไปเก็บในตัวแปรหรือส่งให้ `print()`
ต่อได้

---

## ฟังก์ชันคำนวณทั้งสามสูตร

ทั้งสามฟังก์ชันรับน้ำหนัก `w` หน่วยกิโลกรัมและส่วนสูง `h` หน่วยเซนติเมตร
เหมือนกัน แต่คืนค่าจากคนละสูตร

**1. Mosteller**

$$
BSA_{Mosteller}
= \frac{\sqrt{w h}}{60}
= \sqrt{\frac{w h}{3600}}
$$

solution เลือกเขียนในรูปหลัง

```python
return math.sqrt((w * h) / 3600)
```

**2. Du Bois**

$$
BSA_{Du\ Bois} = 0.007184 \times w^{0.425} \times h^{0.725}
$$

```python
return 0.007184 * (w**0.425) * (h**0.725)
```

**3. Fujimoto**

$$
BSA_{Fujimoto} = 0.008883 \times w^{0.444} \times h^{0.663}
$$

```python
return 0.008883 * (w**0.444) * (h**0.663)
```

เลขชี้กำลังที่เป็นทศนิยมยังคงใช้ตัวดำเนินการ `**` เช่นเดียวกับเลขชี้กำลัง
จำนวนเต็ม

---

## หน้าที่ของ main

ฟังก์ชัน `main()` ทำหน้าที่ประสานขั้นตอนทั้งหมด โดยอ่าน `w` และ `h`,
เรียกฟังก์ชันคำนวณทั้งสาม แล้วแสดงผลตามลำดับ Mosteller, Du Bois และ
Fujimoto

```python
mosteller_area = mosteller(w, h)
du_bois_area = du_bois(w, h)
fujimoto_area = fujimoto(w, h)
```

ก่อนแสดงผล โปรแกรมใช้ `round(value, 5)` เพื่อปัดเป็น **5 ตำแหน่งทศนิยม**
เช่น เมื่อ `w = 56` และ `h = 173` การเรียก `main()` ให้ผล

```text
Mosteller = 1.64046
Du Bois = 1.66698
Fujimoto = 1.61651
```

> [!NOTE]
>
> comment ใน source code ระบุว่า `formatted to 2 decimal places` แต่คำสั่งจริงคือ
> `round(..., 5)` ดังนั้นพฤติกรรมของโปรแกรมคือปัด 5 ตำแหน่ง นอกจากนี้ `round()`
> ไม่ได้บังคับเติมเลขศูนย์ท้ายให้ครบ 5 หลักเสมอ

---

## การสั่งทำงานด้วย exec

โจทย์ข้อนี้ออกแบบให้บรรทัดแรกของ input เป็นคำสั่ง Python ที่ระบบตรวจจะใช้
เรียกฟังก์ชัน ตัวอย่างเช่น input

```text
print(mosteller(56, 173))
```

ใช้ทดสอบฟังก์ชัน `mosteller()` โดยตรง ส่วน input

```text
main()
56
173
```

ทำให้ `exec(input())` อ่านและรันคำสั่ง `main()` ก่อน จากนั้น `main()` จึงอ่าน
น้ำหนักและส่วนสูงจากสองบรรทัดถัดไป การเขียนบรรทัดนี้ไว้ท้ายไฟล์ทำให้ grader
เลือกทดสอบแต่ละฟังก์ชันหรือทดสอบการทำงานรวมผ่าน `main()` ได้

> [!WARNING]
>
> `exec()` สามารถรันข้อความเป็นคำสั่ง Python ได้ทุกอย่าง จึงไม่ควรใช้กับข้อมูล
> จากผู้ใช้ที่ไม่น่าเชื่อถือ ในข้อนี้ใช้ได้เพราะเป็นรูปแบบ input ที่โจทย์และ grader
> กำหนดไว้โดยเฉพาะ

---

## ความคลาดเคลื่อนของจำนวนจริง

ในคณิตศาสตร์ `sqrt(w * h) / 60` และ `sqrt((w * h) / 3600)` ให้ค่าเท่ากัน
แต่คอมพิวเตอร์เก็บ `float` แบบมีความละเอียดจำกัด และสองนิพจน์มีลำดับการคำนวณ
ต่างกัน จึงอาจต่างกันที่เลขหลักสุดท้าย เช่น

```python
math.sqrt(56 * 173) / 60        # 1.6404606399152375
math.sqrt((56 * 173) / 3600)    # 1.6404606399152377
```

ดังนั้นผลจากการเรียก `mosteller(56, 173)` โดยตรงใน solution อาจต่างจากตัวอย่าง
ที่คำนวณด้วยรูปแรกเพียงหลักสุดท้าย แต่เมื่อ `main()` ปัดด้วย `round(..., 5)`
ทั้งสองแบบได้ `1.64046` เหมือนกัน

---

# Solution

```python
# --------------------------------------------------
# File Name : 01_Expr_07.py
# Problem   : Body Surface Area (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------

import math


# Calculate the body surface area using the Mosteller formula
def mosteller(w, h):
    return math.sqrt((w * h) / 3600)


# Calculate the body surface area using the Du Bois formula
def du_bois(w, h):
    return 0.007184 * (w**0.425) * (h**0.725)


# Calculate the body surface area using the Fujimoto formula
def fujimoto(w, h):
    return 0.008883 * (w**0.444) * (h**0.663)


# Main function to read input and display results
def main():
    # Read weight and height from input
    w = float(input())
    h = float(input())

    # Calculate body surface areas using different formulas
    mosteller_area = mosteller(w, h)
    du_bois_area = du_bois(w, h)
    fujimoto_area = fujimoto(w, h)

    # Print the results formatted to 2 decimal places
    print("Mosteller =", round(mosteller_area, 5))
    print("Du Bois =", round(du_bois_area, 5))
    print("Fujimoto =", round(fujimoto_area, 5))


# Execute the input string as code
exec(input())
```
