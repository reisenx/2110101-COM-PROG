<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Next Prime ★☆ (
      <a href="https://drive.google.com/file/d/18Vp0BbeYQX3qrRoR6hXtGh6f33BnsPyy/view?usp=drive_link">
        <code>06_Func_12</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การตรวจสอบจำนวนเฉพาะ**](#การตรวจสอบจำนวนเฉพาะ)
-   [**การหาจำนวนเฉพาะตัวถัดไป**](#การหาจำนวนเฉพาะตัวถัดไป)
-   [**การหาคู่จำนวนเฉพาะแฝด**](#การหาคู่จำนวนเฉพาะแฝด)
-   [**การรับคำสั่งทดสอบจาก Grader**](#การรับคำสั่งทดสอบจาก-grader)
-   [**Solution**](#solution)

---

## การตรวจสอบจำนวนเฉพาะ

**จำนวนเฉพาะ** คือจำนวนเต็มที่มากกว่า `1` และมีตัวหารบวกเพียง `1`
กับตัวมันเอง ฟังก์ชัน `is_prime(number)` จึงเริ่มจากแยกกรณีที่ไม่เป็น
จำนวนเฉพาะแน่นอนก่อน

```python
if number <= 1:
    return False
```

สำหรับ `number > 1` ฟังก์ชันจะลองหาตัวหารตั้งแต่ `2` ถึง
$\lfloor\sqrt{\text{number}}\rfloor$ ถ้า `number % k == 0`
แสดงว่า `k` หาร `number` ลงตัว จึงคืนค่า `False`

```python
for k in range(2, int(number**0.5) + 1):
    if number % k == 0:
        return False
```

ในสูตรคณิตศาสตร์ $\sqrt{n}$ ตรงกับ `number**0.5` ใน Python และ
`int(number**0.5) + 1` ทำให้ปลายบนของ `range()` ครอบคลุมจำนวนเต็มที่ไม่เกิน
รากที่สอง เนื่องจากค่าปลายสุดของ `range()` จะไม่ถูกรวมอยู่ด้วย

เหตุผลที่ไม่ต้องลองตัวหารไปจนถึง `number - 1` คือ ถ้า `number` เป็นจำนวนประกอบ
จะเขียนได้เป็น $number = a \times b$ และอย่างน้อยหนึ่งใน `a` หรือ `b`
ต้องมีค่าไม่เกิน $\sqrt{number}$ เสมอ หากวนลูปจนจบแล้วยังไม่พบตัวหาร
ฟังก์ชันจึงคืนค่า `True`

---

## การหาจำนวนเฉพาะตัวถัดไป

`next_prime(number)` ต้องคืนจำนวนเฉพาะที่น้อยที่สุดซึ่ง
**มากกว่า** `number` อย่างเคร่งครัด ฟังก์ชันจึงเพิ่มค่าก่อนตรวจสอบ

```python
number += 1
while not is_prime(number):
    number += 1
```

ถ้าค่าปัจจุบันยังไม่เป็นจำนวนเฉพาะ ลูป `while` จะเพิ่มทีละ `1`
จน `is_prime(number)` ให้ค่า `True` แล้วจึงคืนค่านั้น ตัวอย่างเช่น
`next_prime(20)` เริ่มตรวจจาก `21` และหยุดที่ `23`

แม้ค่าที่รับเข้ามาจะเป็นจำนวนเฉพาะอยู่แล้ว ฟังก์ชันก็จะหาตัวถัดไป เช่น
`next_prime(2)` คืนค่า `3` ไม่ใช่ `2` เพราะคำตอบต้องมากกว่าค่าที่รับมา

---

## การหาคู่จำนวนเฉพาะแฝด

**จำนวนเฉพาะแฝด** (twin primes) คือจำนวนเฉพาะ 2 จำนวนที่ต่างกัน `2`
เช่น `(11, 13)` และ `(41, 43)`

ฟังก์ชัน `next_twin_prime(number)` เริ่มจากหาจำนวนเฉพาะ 2 ตัวที่เรียงติดกัน
หลัง `number`

```python
prime01 = next_prime(number)
prime02 = next_prime(prime01)
```

จากนั้นตรวจผลต่าง `prime02 - prime01` หากยังไม่เท่ากับ `2`
จะเลื่อนหน้าต่างไปข้างหน้า โดยให้จำนวนเฉพาะตัวที่สองกลายเป็นตัวแรก
แล้วหาจำนวนเฉพาะตัวถัดไปมาเป็นตัวที่สอง

```python
while prime02 - prime01 != 2:
    prime01 = prime02
    prime02 = next_prime(prime01)
```

เพราะแต่ละรอบพิจารณาจำนวนเฉพาะที่เรียงติดกันตามลำดับ
คู่แรกที่ทำให้ผลต่างเท่ากับ `2` จึงเป็นคู่จำนวนเฉพาะแฝดที่น้อยที่สุดหลัง
`number` เช่น เมื่อรับ `30` จะตรวจต่อไปจนพบ `41` และ `43`

คำสั่ง `return prime01, prime02` คืนค่าสองค่าพร้อมกันในรูป **tuple**
ดังนั้นเมื่อสั่ง `print(next_twin_prime(30))` จึงแสดง `(41, 43)`

---

## การรับคำสั่งทดสอบจาก Grader

โจทย์ไม่ได้รับตัวเลขโดยตรง แต่รับคำสั่ง Python ที่ Grader ใช้เรียกฟังก์ชัน
เช่น `print(next_prime(20))` บรรทัดสุดท้ายจึงใช้

```python
exec(input().strip())
```

`input()` รับคำสั่งเป็นสตริง, `strip()` ตัดช่องว่างที่หัวและท้ายสตริง และ
`exec()` ประมวลผลสตริงนั้นเป็นคำสั่ง Python ทำให้ Grader เลือกทดสอบ
`is_prime()`, `next_prime()` หรือ `next_twin_prime()` ได้

> [!WARNING]
>
> `exec()` สามารถรันคำสั่ง Python ใด ๆ ที่อยู่ในสตริงได้ จึงควรใช้เฉพาะ
> ข้อมูลทดสอบที่เชื่อถือได้จาก Grader และไม่ควรใช้กับข้อมูลจากผู้ใช้ที่
> ไม่ทราบแหล่งที่มา

---

# Solution

```python
# --------------------------------------------------
# File Name : 06_Func_12.py
# Problem   : Next Prime
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for k in range(2, int(number**0.5) + 1):
        if number % k == 0:
            return False
    return True


# Find the next prime number after N
def next_prime(number):
    number += 1
    while not is_prime(number):
        number += 1
    return number


# Find the next twin prime pair after N
# Twin primes are pairs of prime numbers that differ by 2
def next_twin_prime(number):
    prime01 = next_prime(number)
    prime02 = next_prime(prime01)
    while prime02 - prime01 != 2:
        prime01 = prime02
        prime02 = next_prime(prime01)
    return prime01, prime02


# Execute a input string as code
exec(input().strip())
```
