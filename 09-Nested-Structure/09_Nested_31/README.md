<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Pythagorean Triple ★★★ (
      <a href="https://drive.google.com/file/d/1SNN6xz6-R4IevIL8uLU9GexVMoLptVhb/view?usp=drive_link">
        <code>09_Nested_31</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การหา GCD และตรวจ Coprime**](#การหา-gcd-และตรวจ-coprime)
-   [**เงื่อนไขของ Primitive Pythagorean Triple**](#เงื่อนไขของ-primitive-pythagorean-triple)
-   [**การสร้างชุดจำนวน**](#การสร้างชุดจำนวน)
-   [**การเรียงลำดับคำตอบ**](#การเรียงลำดับคำตอบ)
-   [**การรับคำสั่งทดสอบจาก Grader**](#การรับคำสั่งทดสอบจาก-grader)
-   [**Solution**](#solution)

---

## การหา GCD และตรวจ Coprime

ฟังก์ชัน `gcd(a, b)` หา **ห.ร.ม.** (Greatest Common Divisor หรือ GCD)
ด้วยขั้นตอนวิธีของยุคลิด โดยแทนค่า `(a, b)` ด้วย `(b, a % b)` ซ้ำไปเรื่อย ๆ
จนกระทั่ง `b` เป็น `0` แล้วคืนค่า `a`

ตัวอย่างเช่น การหา `gcd(48, 18)` มีลำดับค่าดังนี้

```text
(48, 18) -> (18, 12) -> (12, 6) -> (6, 0)
```

ดังนั้น ห.ร.ม. ของ `48` และ `18` คือ `6`

โจทย์นี้ต้องตรวจจำนวนพร้อมกันสามจำนวน จึงหา ห.ร.ม. ของ `a` กับ `b` ก่อน
แล้วนำผลลัพธ์ไปหา ห.ร.ม. ร่วมกับ `c`

```python
gcd(gcd(a, b), c) == 1
```

ถ้าผลลัพธ์เป็น `1` แสดงว่าทั้งสามจำนวนไม่มีตัวหารร่วมที่มากกว่า `1`
ฟังก์ชัน `is_coprime(a, b, c)` จึงคืนค่า `True` มิฉะนั้นจะคืนค่า `False`

> [!NOTE]
>
> คำว่า coprime ในข้อนี้หมายถึง ห.ร.ม. **ร่วมกันทั้งสามจำนวน** เป็น `1`
> ไม่ได้กำหนดว่าทุกคู่ต้องเป็น coprime เช่น `is_coprime(2, 3, 6)` เป็น `True`
> เพราะ ห.ร.ม. ร่วมของ `2`, `3` และ `6` เท่ากับ `1`

---

## เงื่อนไขของ Primitive Pythagorean Triple

ชุดจำนวนพีทาโกรัสประกอบด้วยจำนวนเต็มบวก `a`, `b` และ `c` ที่เป็นไปตามสมการ

$$
a^2 + b^2 = c^2
$$

เมื่อทราบ `a` และ `b` เราจึงคำนวณ `c` ได้จาก

$$
c = \sqrt{a^2 + b^2}
$$

ซึ่งเขียนเป็นภาษา Python ตามโค้ดของข้อนี้ได้ดังนี้

```python
c = (a**2 + b**2) ** (0.5)
```

ส่วนคำว่า **primitive** เพิ่มเงื่อนไขว่า `a`, `b` และ `c` ต้องเป็น coprime
เช่น `[3, 4, 5]` เป็น primitive แต่ `[6, 8, 10]` ไม่เป็น
เพราะทั้งสามจำนวนมีตัวหารร่วมเป็น `2`

นอกจากนี้ คำตอบทุกชุดต้องเป็นไปตามลำดับ `a <= b <= c <= max_len`

---

## การสร้างชุดจำนวน

ฟังก์ชัน `primitive_Pythagorean_triples(max_len)` ใช้ลูปซ้อนกันเลือกค่าที่เป็นไปได้
ของ `a` และ `b`

```python
for a in range(1, max_len + 1):
    for b in range(a + 1, max_len + 1):
```

ค่า `a` เริ่มจาก `1` จึงเป็นจำนวนบวก ส่วน `b` เริ่มจาก `a + 1`
ทำให้ไม่ต้องตรวจทั้ง `(a, b)` และ `(b, a)` ซ้ำกัน
จากนั้นคำนวณ `c` แล้วรับชุดนั้นเมื่อครบทั้งสามเงื่อนไข

1. `c <= max_len` - ด้านที่ยาวที่สุดไม่เกินขอบเขต
2. `c == int(c)` - `c` เป็นจำนวนเต็ม
3. `is_coprime(a, b, c)` - ทั้งสามจำนวนเป็น primitive

ตัวอย่างเมื่อ `a = 3` และ `b = 4` จะได้ `c = 5.0`
จึงผ่านทุกเงื่อนไขและเก็บเป็น `[3, 4, 5]`

> [!NOTE]
>
> นิพจน์ยกกำลัง `0.5` ให้ผลเป็น `float` เช่น `5.0`
> โค้ดนี้ไม่ได้ปัดเศษด้วย `round()` แต่ตรวจว่า `c == int(c)` จริงหรือไม่ก่อน
> แล้วจึงแปลง `c` เป็น `int` ตอนเก็บคำตอบ ผลลัพธ์จึงแสดง `5` ไม่ใช่ `5.0`

---

## การเรียงลำดับคำตอบ

โจทย์กำหนดให้เรียงชุดคำตอบตาม `c` จากน้อยไปมาก และเมื่อ `c` เท่ากัน
ให้เรียงตาม `a` โค้ดจึงเก็บข้อมูลชั่วคราวในลำดับ `[c, a, b]`

```python
triples.append([int(c), a, b])
triples.sort()
```

การเรียงลิสต์ของ Python จะเปรียบเทียบสมาชิกตัวแรกก่อน แล้วจึงเปรียบเทียบ
สมาชิกตัวถัดไปเมื่อค่าแรกเท่ากัน ดังนั้นรูปแบบนี้จึงเรียงตาม `c`, `a` และ `b`
ตามลำดับ ตัวอย่างชุดที่มี `c = 65` จะได้ `[16, 63, 65]`
อยู่ก่อน `[33, 56, 65]`

หลังเรียงเสร็จ ลูปสุดท้ายจะสลับแต่ละชุดกลับเป็น `[a, b, c]`
ก่อนคืนค่า `sorted_triples`

---

## การรับคำสั่งทดสอบจาก Grader

บรรทัดสุดท้ายอ่านคำสั่ง Python หนึ่งบรรทัดจาก Grader แล้วสั่งทำงานด้วย `exec()`
เช่น เมื่อรับ `print(primitive_Pythagorean_triples(10))` โปรแกรมจะแสดง
`[[3, 4, 5]]`

> [!WARNING]
>
> `exec()` สามารถสั่งทำงานโค้ดใด ๆ ที่อยู่ในข้อความได้ จึงใช้ในข้อนี้เพื่อให้
> Grader เรียกฟังก์ชันตามรูปแบบของโจทย์เท่านั้น ไม่ควรใช้ `exec()` กับข้อความ
> จากแหล่งที่ไม่เชื่อถือ

---

# Solution

```python
# --------------------------------------------------
# File Name : 09_Nested_31.py
# Problem   : Pythagorean Triple
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Calculate the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Check if three numbers are coprime (their GCD is 1)
def is_coprime(a, b, c):
    return gcd(gcd(a, b), c) == 1


# Generate all primitive Pythagorean triples with a, b, c <= max_len
# Three numbers a, b, c must satisfy a^2 + b^2 = c^2 and gcd(a, b, c) = 1
def primitive_Pythagorean_triples(max_len):
    triples = []
    for a in range(1, max_len + 1):
        for b in range(a + 1, max_len + 1):
            c = (a**2 + b**2) ** (0.5)
            if c <= max_len and c == int(c) and is_coprime(a, b, c):
                triples.append([int(c), a, b])
    triples.sort()

    sorted_triples = []
    for c, a, b in triples:
        sorted_triples.append([a, b, c])
    return sorted_triples


# Execute an input string
exec(input().strip())
```
