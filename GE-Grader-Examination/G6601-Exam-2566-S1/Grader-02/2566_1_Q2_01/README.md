<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Outlier ★☆ (
      <a href="https://drive.google.com/file/d/1uZYl_y7cE_lXltvPjL7cJdszyvffykMn/view?usp=sharing">
        <code>2566_1_Q2_01</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**โจทย์ต้องการอะไร**](#โจทย์ต้องการอะไร)
-   [**การหามัธยฐานและควอร์ไทล์**](#การหามัธยฐานและควอร์ไทล์)
-   [**การหา Outlier ด้วย IQR**](#การหา-outlier-ด้วย-iqr)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**ข้อควรระวัง**](#ข้อควรระวัง)
-   [**Solution**](#solution)

---

## โจทย์ต้องการอะไร

โจทย์ให้ข้อมูลจำนวนเต็มบวกอย่างน้อย 4 จำนวนมาในบรรทัดเดียว
โดยแต่ละจำนวนคั่นด้วยช่องว่าง เราต้องหาว่าข้อมูลตัวใดเป็น **Outlier**
หรือข้อมูลที่แตกต่างจากข้อมูลส่วนใหญ่มากเกินไปด้วยวิธี Interquartile Range (IQR)

ผลลัพธ์มี 2 บรรทัดตามลำดับดังนี้

1. แสดงขอบเขตล่าง `L` และขอบเขตบน `U` ในรูปแบบ `L = ... U = ...`
2. แสดง Outlier เรียงจากน้อยไปมากและคั่นด้วยช่องว่าง ถ้าไม่มี Outlier ให้แสดง `Not found`

ก่อนจะคำนวณ IQR เราต้องเรียงข้อมูลจากน้อยไปมากก่อน

```python
numbers = [int(num) for num in input().split()]
numbers.sort()
```

---

## การหามัธยฐานและควอร์ไทล์

**มัธยฐาน (Median)** คือค่าที่อยู่ตรงกลางของข้อมูลที่เรียงลำดับแล้ว
วิธีหาขึ้นอยู่กับจำนวนข้อมูล

-   ถ้ามีข้อมูลเป็นจำนวนคี่ มัธยฐานคือค่าตรงกลางที่ตำแหน่ง `n // 2`
-   ถ้ามีข้อมูลเป็นจำนวนคู่ มัธยฐานคือค่าเฉลี่ยของข้อมูลตรงกลาง 2 ค่า
    ที่ตำแหน่ง `(n // 2) - 1` และ `n // 2`

ฟังก์ชัน `get_median()` จึงเขียนได้ดังนี้

```python
if n % 2 == 1:
    return float(numbers[n // 2])
return (numbers[(n // 2) - 1] + numbers[n // 2]) / 2.0
```

สำหรับการหาควอร์ไทล์ ให้แบ่งข้อมูลที่เรียงแล้วออกเป็นครึ่งซ้ายและครึ่งขวา

```python
first_half = numbers[: n // 2]
second_half = numbers[-(n // 2) :]
```

-   `Q1` คือมัธยฐานของ `first_half`
-   `Q3` คือมัธยฐานของ `second_half`

> [!NOTE]
>
> ถ้าข้อมูลทั้งหมดมีจำนวนเป็นเลขคี่ ค่าตรงกลางของข้อมูลทั้งหมดจะไม่อยู่ในครึ่งใดเลย
> เช่น ข้อมูล 13 จำนวนจะถูกแบ่งเป็นครึ่งละ 6 จำนวน และเว้นข้อมูลลำดับที่ 7 ไว้
> การเขียน `numbers[-(n // 2) :]` ทำให้ครึ่งขวามีจำนวนสมาชิกเท่ากับ
> ครึ่งซ้ายพอดี

---

## การหา Outlier ด้วย IQR

เมื่อได้ `Q1` และ `Q3` แล้ว ให้คำนวณ IQR ด้วยสูตร

$$
IQR = Q_3 - Q_1
$$

ซึ่งตรงกับ Python ว่า

```python
iqr = q3 - q1
```

จากนั้นคำนวณขอบเขตล่าง `L` และขอบเขตบน `U`

$$
L = Q_1 - 1.5 \times IQR
$$

```python
lower_bound = q1 - (1.5 * iqr)
```

$$
U = Q_3 + 1.5 \times IQR
$$

```python
upper_bound = q3 + (1.5 * iqr)
```

จำนวน `num` เป็น Outlier เมื่อเป็นจริงอย่างน้อยหนึ่งเงื่อนไขต่อไปนี้

$$
num < L \quad \text{หรือ} \quad num > U
$$

```python
if num < lower_bound or num > upper_bound:
    outliers.append(num)
```

โปรแกรมวนตรวจข้อมูลที่เรียงแล้ว จึงได้ Outlier เรียงจากน้อยไปมาก
โดยไม่ต้องเรียงซ้ำ จากนั้นแปลงแต่ละจำนวนเป็นข้อความ
และเชื่อมด้วยช่องว่างผ่าน `" ".join(...)`

ค่า `L` และ `U` ถูกพิมพ์ด้วย `f`-string โดยตรง
โปรแกรมไม่ได้กำหนดจำนวนตำแหน่งทศนิยมหรือปัดเศษ
จึงควรใช้ค่าที่ Python แสดงตามปกติ เช่น `17.0`, `3.5` หรือ `2.25`

---

## ตัวอย่างการทำงาน

พิจารณาข้อมูล

```text
5 6 7 1 3 5 6 5 6 20 5 18 5 6
```

เมื่อเรียงจากน้อยไปมาก จะได้

```text
1 3 5 5 5 5 5 6 6 6 6 7 18 20
```

ข้อมูลมีทั้งหมด 14 จำนวน จึงแบ่งได้ครึ่งละ 7 จำนวน

```text
ครึ่งซ้าย: 1 3 5 5 5 5 5
ครึ่งขวา: 6 6 6 6 7 18 20
```

ดังนั้น `Q1 = 5.0`, `Q3 = 6.0` และ

$$
IQR = 6.0 - 5.0 = 1.0
$$

คำนวณขอบเขตได้ดังนี้

$$
L = 5.0 - 1.5(1.0) = 3.5
$$

$$
U = 6.0 + 1.5(1.0) = 7.5
$$

ค่าที่น้อยกว่า `3.5` คือ `1`, `3` และค่าที่มากกว่า `7.5` คือ `18`, `20`
ผลลัพธ์จึงเป็น

```text
L = 3.5 U = 7.5
1 3 18 20
```

สำหรับข้อมูลจำนวนคี่ เช่นข้อมูลที่เรียงแล้วเป็น

```text
1 3 4 5 5 5 | 5 | 6 6 6 7 18 20
```

ค่า `5` ตรงกลางจะไม่ถูกนำไปหาควอร์ไทล์
ครึ่งซ้ายจึงให้ `Q1 = (4 + 5) / 2 = 4.5`
และครึ่งขวาให้ `Q3 = (6 + 7) / 2 = 6.5`

ถ้าข้อมูลทุกจำนวนอยู่ระหว่าง `L` และ `U` เช่น `20 22 20 20 22 22 23`
ซึ่งได้ `L = 17.0` และ `U = 25.0` บรรทัดที่สองจะแสดง `Not found`

---

## ข้อควรระวัง

-   เงื่อนไขใช้ `<` และ `>` ไม่ใช่ `<=` และ `>=` ดังนั้นค่าที่เท่ากับ `L`
    หรือ `U` พอดี **ไม่เป็น** Outlier
-   เมื่อข้อมูลทั้งหมดมีจำนวนเป็นเลขคี่ ต้องตัดค่าตรงกลางออกก่อนหามัธยฐาน
    ของแต่ละครึ่ง
-   โปรแกรมไม่ปัดเศษและไม่บังคับจำนวนตำแหน่งทศนิยม ให้พิมพ์ค่า `float`
    ตามที่ Python คำนวณได้
-   ถ้า Outlier ค่าเดียวกันปรากฏหลายครั้ง ต้องแสดงทุกครั้ง
    เพราะแต่ละตำแหน่งถือเป็นข้อมูลคนละตัว
-   โจทย์รับประกันว่ามีจำนวนเต็มบวกอย่างน้อย 4 จำนวน
    โปรแกรมจึงไม่ต้องตรวจสอบข้อมูลที่อยู่นอกเงื่อนไขนี้
-   วิธีแก้นี้ไม่ต้องใช้ `import` ใด ๆ

---

# Solution

```python
# --------------------------------------------------
# File Name : 2566_1_Q2_01.py
# Problem   : Outlier
# Author    : Worralop Srichainont
# Date      : 2025-07-12
# --------------------------------------------------


# Calculate the median of a list of sorted numbers
def get_median(numbers):
    n = len(numbers)
    if n % 2 == 1:
        return float(numbers[n // 2])
    return (numbers[(n // 2) - 1] + numbers[n // 2]) / 2.0


# Input the list of numbers and sort them in ascending order
numbers = [int(num) for num in input().split()]
numbers.sort()

# Split the list into two halves
n = len(numbers)
first_half = numbers[: n // 2]
second_half = numbers[-(n // 2) :]

# Calculate the IQR
q1 = get_median(first_half)
q3 = get_median(second_half)
iqr = q3 - q1

# Calculate the lower and upper bounds for outliers
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

# Find outliers in the list of numbers
outliers = []
for num in numbers:
    if num < lower_bound or num > upper_bound:
        outliers.append(num)

# Output
print(f"L = {lower_bound} U = {upper_bound}")
# Output the outliers if any, otherwise print "Not found"
if len(outliers) > 0:
    print(" ".join([str(num) for num in outliers]))
else:
    print("Not found")
```
