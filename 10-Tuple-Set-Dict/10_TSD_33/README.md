<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Polynomial ★★★ (
      <a href="https://drive.google.com/file/d/1NzHodyfvlrIU49Ooqf5xPqe2ys6ujKb7/view?usp=drive_link">
        <code>10_TSD_33</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การแทนพหุนามด้วยลิสต์ของทูเพิล**](#การแทนพหุนามด้วยลิสต์ของทูเพิล)
-   [**การบวกพหุนาม**](#การบวกพหุนาม)
-   [**การคูณพหุนาม**](#การคูณพหุนาม)
-   [**การรับคำสั่งทดสอบจาก Grader**](#การรับคำสั่งทดสอบจาก-grader)
-   [**Solution**](#solution)

---

## การแทนพหุนามด้วยลิสต์ของทูเพิล

โจทย์แทนพหุนามตัวแปรเดียวด้วยลิสต์ โดยแต่ละพจน์เป็นทูเพิล
`(coefficient, exponent)` หรือ `(สัมประสิทธิ์, เลขชี้กำลัง)` เช่น

\[
4x^2 + 3x - 1
\]

เขียนใน Python ได้เป็น

```python
[(4, 2), (3, 1), (-1, 0)]
```

ทูเพิล `(4, 2)` หมายถึง \(4x^2\) ส่วน `(-1, 0)` หมายถึง
\(-1x^0=-1\) ลิสต์ผลลัพธ์ต้องเรียงเลขชี้กำลังจากมากไปน้อย
และไม่เก็บพจน์ที่มีสัมประสิทธิ์เป็น `0`

---

## การบวกพหุนาม

พจน์ที่จะบวกกันได้ต้องมีเลขชี้กำลังเท่ากัน เพราะ

\[
ax^k + bx^k = (a+b)x^k
\]

ใน Python จึงใช้ dictionary ชื่อ `result_dict` โดยให้ **เลขชี้กำลังเป็น key**
และ **สัมประสิทธิ์เป็น value** ตัวอย่างเช่น พจน์ `(2, 4)` จะเก็บเป็น
`result_dict[4] = 2`

ฟังก์ชัน `add_poly()` ทำงานตามลำดับดังนี้

1. นำทุกพจน์ของ `polynomial_01` ใส่ใน `result_dict`
2. เดินดูทุกพจน์ของ `polynomial_02` ถ้ายังไม่มีเลขชี้กำลังนั้นให้เริ่มที่ `0`
   แล้วบวกด้วย `result_dict[exponent] += coefficient`
3. ใช้ `sorted(result_dict.items())[::-1]` เรียงเลขชี้กำลังจากมากไปน้อย
4. ใส่ `(coefficient, exponent)` ในผลลัพธ์เฉพาะเมื่อ `coefficient != 0`

เช่น `(2, 4)` กับ `(3, 4)` รวมเป็น `(5, 4)` แต่ `(1, 1)` กับ
`(-1, 1)` รวมกันได้สัมประสิทธิ์ `0` จึงหายไปจากลิสต์ หากทุกพจน์หักล้างกันหมด
พหุนามศูนย์จะแทนด้วยลิสต์ว่าง `[]`

> [!NOTE]
>
> รูปแบบพหุนามของโจทย์เป็นรูปที่รวมพจน์ซึ่งมีเลขชี้กำลังเดียวกันมาแล้ว
> โค้ดจึงกำหนดค่าจาก `polynomial_01` ลง dictionary โดยตรง
> ก่อนนำสัมประสิทธิ์จาก `polynomial_02` มาบวกเพิ่ม

---

## การคูณพหุนาม

การคูณหนึ่งพจน์ใช้กฎ

\[
(ax^m)(bx^n) = (ab)x^{m+n}
\]

ซึ่งตรงกับ Python ดังนี้

```python
new_coefficient = coefficient01 * coefficient02
new_exponent = exponent01 + exponent02
```

ฟังก์ชัน `mult_poly()` ใช้ลูปซ้อนเพื่อคูณทุกพจน์ของพหุนามแรกกับทุกพจน์ของ
พหุนามที่สอง ผลคูณย่อยของพจน์หนึ่งจาก `polynomial_01` จะอยู่ใน `result`
จากนั้นเรียก `add_poly(total_result, result)` เพื่อรวมพจน์เลขชี้กำลังเดียวกัน
และตัดพจน์ที่หักล้างกันเป็นศูนย์ไปพร้อมกัน

ตัวอย่าง

\[
(2x+1)(x-1)=2x^2-x-1
\]

จึงได้ลิสต์ `[(2, 2), (-1, 1), (-1, 0)]` ถ้าพหุนามตัวใดเป็นลิสต์ว่าง
ลูปจะไม่มีพจน์ให้คูณและได้ผลลัพธ์เป็น `[]`

---

## การรับคำสั่งทดสอบจาก Grader

ท้ายโปรแกรมรับคำสั่ง Python จำนวน `3` บรรทัด ตัวอย่างหนึ่งชุดทดสอบอาจเป็น
การกำหนด `p1` การกำหนด `p2` และคำสั่ง `print(add_poly(p1, p2))`

```python
for _ in range(3):
    exec(input().strip())
```

`exec()` ทำให้ Grader ส่งคำสั่งมาสร้างตัวแปรและเรียกฟังก์ชันที่ต้องการตรวจได้
ดังนั้นส่วนนี้ไม่ได้แปลงข้อความเป็นพหุนามด้วยตัวเอง แต่สั่งทำงานข้อความนั้นในฐานะ
โค้ด Python โดยตรง

> [!WARNING]
>
> `exec()` สามารถสั่งทำงานโค้ดใด ๆ ก็ได้ จึงควรใช้เฉพาะกับคำสั่งจาก Grader
> ที่เชื่อถือได้เท่านั้น ห้ามนำรูปแบบนี้ไปรับข้อความจากผู้ใช้ที่ไม่รู้แหล่งที่มา

---

# Solution

```python
# --------------------------------------------------
# File Name : 10_TSD_33.py
# Problem   : Polynomial
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------


def add_poly(polynomial_01, polynomial_02):
    # Initialize variables to hold the result of the addition
    result_dict = {}
    result = []

    # Add terms from the first polynomial
    for coefficient, exponent in polynomial_01:
        result_dict[exponent] = coefficient

    # Add terms from the second polynomial
    for coefficient, exponent in polynomial_02:
        if exponent not in result_dict:
            result_dict[exponent] = 0
        result_dict[exponent] += coefficient

    # Convert the dictionary back to a sorted list of tuples
    # Sort the terms by exponent in descending order
    for exponent, coefficient in sorted(result_dict.items())[::-1]:
        if coefficient != 0:
            result.append((coefficient, exponent))

    # Return the result polynomial
    return result


# Multiplies two polynomials represented as lists of tuples.
def mult_poly(polynomial_01, polynomial_02):
    total_result = []

    # Expand each term in the first polynomial with every term in the second polynomial.
    for coefficient01, exponent01 in polynomial_01:
        result = []
        for coefficient02, exponent02 in polynomial_02:
            # Multiply coefficients and add exponents
            new_coefficient = coefficient01 * coefficient02
            new_exponent = exponent01 + exponent02

            # Append the new term to the result
            result.append((new_coefficient, new_exponent))

        # Add the result of this multiplication to the total result
        total_result = add_poly(total_result, result)

    # Return the final polynomial after all multiplications
    return total_result


for _ in range(3):
    exec(input().strip())
```
