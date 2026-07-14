<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Complex Number ★★ (
      <a href="https://drive.google.com/file/d/1c-t7FxeJv0xwvdwCdvixSNVJomTEBM_f/view?usp=drive_link">
        <code>12_Class_21</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิดของคลาส Complex**](#แนวคิดของคลาส-complex)
-   [**การแสดงผลจำนวนเชิงซ้อน**](#การแสดงผลจำนวนเชิงซ้อน)
-   [**การบวก คูณ และหาร**](#การบวก-คูณ-และหาร)
-   [**ลำดับการทำงานของโปรแกรม**](#ลำดับการทำงานของโปรแกรม)
-   [**Solution**](#solution)

---

## แนวคิดของคลาส Complex

จำนวนเชิงซ้อนเขียนในรูป $a+bi$ โดย $a$ เป็นส่วนจริง และ $b$
เป็นสัมประสิทธิ์ของส่วนจินตภาพ ในโปรแกรมนี้ จำนวนเชิงซ้อนหนึ่งจำนวนจึงถูกเก็บเป็น
object ของคลาส `Complex` ที่มีข้อมูล 2 ค่า

```python
def __init__(self, a, b):
    self.real = a
    self.imaginary = b
```

ตัวอย่างเช่น `Complex(3, -1)` เก็บ `real` เป็น `3` และเก็บ `imaginary` เป็น
`-1` ซึ่งแทนจำนวน $3-i$

เมท็อดที่มีชื่อขึ้นต้นและลงท้ายด้วย `__` เป็น **special method** ซึ่ง Python
จะเรียกให้เองเมื่อเราใช้คำสั่งหรือตัวดำเนินการที่เกี่ยวข้อง

-   `__str__` ทำงานเมื่อแปลง object เป็นข้อความ เช่น `str(c1)` หรือ `print(c1)`
-   `__add__` ทำงานเมื่อเขียน `c1 + c2`
-   `__mul__` ทำงานเมื่อเขียน `c1 * c2`
-   `__truediv__` ทำงานเมื่อเขียน `c1 / c2`

เมท็อดคำนวณทั้งสามสร้างและคืนค่า `Complex` object ตัวใหม่
จึงไม่แก้ส่วนจริงหรือส่วนจินตภาพของ object เดิม

---

## การแสดงผลจำนวนเชิงซ้อน

การแสดงผลต้องตัดพจน์และสัมประสิทธิ์ที่ไม่จำเป็นออก เช่น $2+0i$ ต้องแสดงเป็น
`2` และ $2-i$ ต้องแสดงเป็น `2-i` ไม่ใช่ `2-1i` เมท็อด `__str__`
จึงพิจารณาส่วนจริง `a` และส่วนจินตภาพ `b` ตามลำดับดังนี้

1. ถ้า `a == 0` และ `b == 0` ให้คืนข้อความ `"0"` ทันที
2. ถ้า `a != 0` ให้เติม `str(a)` ลงในข้อความ
3. ถ้า `b == 0` ไม่ต้องเติมพจน์จินตภาพ
4. ถ้า `b > 0` และมีส่วนจริงอยู่แล้ว ให้เติมเครื่องหมาย `+`
5. ถ้า `abs(b) != 1` ให้เติมค่า `b` แต่ถ้า `b` เป็น `1` หรือ `-1`
   ให้ละเลข `1` เหลือเพียงเครื่องหมายที่จำเป็น
6. เติมตัวอักษร `i` ปิดท้ายพจน์จินตภาพ

ผลลัพธ์สำคัญทุกกรณีมีลักษณะดังนี้

| `a` | `b` | ข้อความที่ได้ | เหตุผล |
|---:|---:|:---:|---|
| `0` | `0` | `0` | ทั้งสองส่วนเป็นศูนย์ |
| `2` | `0` | `2` | ไม่มีพจน์จินตภาพ |
| `0` | `3` | `3i` | ไม่มีส่วนจริง จึงไม่ใส่ `+` ข้างหน้า |
| `0` | `-3` | `-3i` | เครื่องหมายลบติดมากับค่า `b` |
| `0` | `1` | `i` | ละสัมประสิทธิ์ `1` |
| `0` | `-1` | `-i` | ละเลข `1` แต่คงเครื่องหมาย `-` |
| `3` | `1` | `3+i` | มีส่วนจริงและ `b` เป็นบวก |
| `3` | `-1` | `3-i` | มีส่วนจริงและละสัมประสิทธิ์ `1` |

---

## การบวก คูณ และหาร

ให้ `self` แทน $a+bi$ และ `rhs` แทน $c+di$

### การบวก

บวกส่วนจริงเข้าด้วยกัน และบวกสัมประสิทธิ์ของส่วนจินตภาพเข้าด้วยกัน

$$
(a+bi)+(c+di)=(a+c)+(b+d)i
$$

ตรงกับ Python ดังนี้

```python
return Complex(a + c, b + d)
```

### การคูณ

กระจายพจน์แล้วใช้สมบัติ $i^2=-1$ จะได้

$$
(a+bi)(c+di)=(ac-bd)+(ad+bc)i
$$

ส่วนจริงและส่วนจินตภาพใน Python คือ

```python
real = (a * c) - (b * d)
imaginary = (a * d) + (b * c)
```

เช่น $(3+i)(2+i)=5+5i$ เพราะส่วนจริงเป็น `3 * 2 - 1 * 1 = 5`
และส่วนจินตภาพเป็น `3 * 1 + 1 * 2 = 5`

### การหาร

คูณทั้งเศษและส่วนด้วยสังยุค $c-di$ เพื่อทำให้ตัวส่วนไม่มี $i$

$$
\frac{a+bi}{c+di}
=\frac{ac+bd}{c^2+d^2}
+\frac{-ad+bc}{c^2+d^2}i
$$

ตัวส่วนร่วมคือ `c**2 + d**2` และคำนวณสองส่วนด้วย

```python
real = ((a * c) + (b * d)) / (c**2 + d**2)
imaginary = (-(a * d) + (b * c)) / (c**2 + d**2)
```

> [!NOTE]
>
> ตัวดำเนินการ `/` ให้ผลลัพธ์เป็น `float` และ `__str__` ใช้ `str()`
> โดยไม่ได้กำหนดจำนวนตำแหน่งทศนิยมหรือปัดเศษ ดังนั้นโปรแกรมจะแสดงทศนิยมตามรูปแบบ
> ปกติของ Python เช่น `1.4-0.2i`

> [!WARNING]
>
> ตัวหารต้องไม่เป็น `Complex(0, 0)` เพราะจะทำให้ `c**2 + d**2` เป็นศูนย์
> และ Python จะเกิด `ZeroDivisionError`

---

## ลำดับการทำงานของโปรแกรม

ข้อมูลเข้ามีจำนวนเต็ม 5 ค่าในบรรทัดเดียว

```text
t a b c d
```

โปรแกรมสร้าง `c1 = Complex(a, b)` และ `c2 = Complex(c, d)` จากนั้นใช้ `t`
เลือกผลลัพธ์เพียงหนึ่งบรรทัด

| `t` | คำสั่งที่ทำงาน | ผลลัพธ์ |
|:---:|---|---|
| `1` | `print(c1)` | จำนวน $a+bi$ |
| `2` | `print(c2)` | จำนวน $c+di$ |
| `3` | `print(c1 + c2)` | ผลบวก |
| `4` | `print(c1 * c2)` | ผลคูณ |
| ค่าอื่น (`5` ตามตัวอย่างโจทย์) | `print(c1 / c2)` | ผลหาร |

ตัวอย่างข้อมูลเข้า `4 3 1 2 1` สร้างจำนวน $3+i$ และ $2+i$ แล้วเลือกการคูณ
จึงแสดงผล

```text
5+5i
```

---

# Solution

```python
# --------------------------------------------------
# File Name : 12_Class_21.py
# Problem   : Complex Number
# Author    : Worralop Srichainont
# Date      : 2025-06-16
# --------------------------------------------------


class Complex:
    # __init__ method
    # Initialize the complex number object
    # a is real part and b is imaginary part
    def __init__(self, a, b):
        self.real = a
        self.imaginary = b

    # __str__ method
    # Convert the complex object to a string representation
    def __str__(self):
        # Initialize variables
        a, b = self.real, self.imaginary
        complex_str = ""
        # Format the complex number
        if a == 0 and b == 0:
            return "0"

        if a != 0:
            complex_str += str(a)

        if b != 0:
            if b > 0 and a != 0:
                complex_str += "+"
            if abs(b) != 1:
                complex_str += str(b)
            elif b == -1:
                complex_str += "-"
            complex_str += "i"
        return complex_str

    # __add__ method
    # Calculate the sum of 2 complex numbers
    # 'self' is a+bi and 'rhs' is c+di
    def __add__(self, rhs):
        # Initialize variables
        a, b = self.real, self.imaginary
        c, d = rhs.real, rhs.imaginary
        # Return the sum of complex numbers
        return Complex(a + c, b + d)

    # __mul__ method
    # Calculate the product of 2 complex numbers
    # 'self' is a+bi and 'rhs' is c+di
    def __mul__(self, rhs):
        # Initialize variables
        a, b = self.real, self.imaginary
        c, d = rhs.real, rhs.imaginary
        # Return the product of complex numbers
        real = (a * c) - (b * d)
        imaginary = (a * d) + (b * c)
        return Complex(real, imaginary)

    # __truediv__ method
    # Calculate the quotient of 2 complex numbers
    # 'self' is a+bi and 'rhs' is c+di
    def __truediv__(self, rhs):
        # Initialize variables
        a, b = self.real, self.imaginary
        c, d = rhs.real, rhs.imaginary
        # Return the quotient of complex numbers
        real = ((a * c) + (b * d)) / (c**2 + d**2)
        imaginary = (-(a * d) + (b * c)) / (c**2 + d**2)
        return Complex(real, imaginary)


# Input
t, a, b, c, d = [int(x) for x in input().split()]

# Initialize complex numbers
c1 = Complex(a, b)
c2 = Complex(c, d)

# Output
if t == 1:
    print(c1)
elif t == 2:
    print(c2)
elif t == 3:
    print(c1 + c2)
elif t == 4:
    print(c1 * c2)
else:
    print(c1 / c2)
```
