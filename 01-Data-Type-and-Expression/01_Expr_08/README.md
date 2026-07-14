<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Cube Root (Function) ★★ (
      <a href="https://drive.google.com/file/d/1q4SQ2FI5yLt8RGI6L5eDOaKdKPIuf728/view?usp=drive_link">
        <code>01_Expr_08</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**รากที่สองซ้ำ**](#รากที่สองซ้ำ)
-   [**ทำไมจึงประมาณรากที่สามได้**](#ทำไมจึงประมาณรากที่สามได้)
-   [**ไล่ค่าจาก `s1` ถึง `ans`**](#ไล่ค่าจาก-s1-ถึง-ans)
-   [**การรับข้อมูลและการเรียกโปรแกรม**](#การรับข้อมูลและการเรียกโปรแกรม)
-   [**Solution**](#solution)

---

## รากที่สองซ้ำ

การหารากที่สองหนึ่งครั้งเท่ากับการยกกำลัง $1/2$ ถ้าทำซ้ำ $n$ ครั้ง
เลขชี้กำลังจะถูกหารด้วย 2 ทุกครั้ง จึงได้

$$
\underbrace{\sqrt{\sqrt{\cdots\sqrt{x}}}}_{n\text{ ครั้ง}}
=x^{1/2^n}
$$

ใน Python เขียนได้เป็น `x ** (1 / (2**n))` จึงเป็นที่มาของฟังก์ชัน
`sqrt_n_times(x, n)` ตัวอย่างเช่น `sqrt_n_times(10**8, 3)` คำนวณ
$(10^8)^{1/8}=10$

> [!NOTE]
>
> วิธีนี้สร้างรากที่สามจากการหารากที่สองซ้ำ จึงสมมติว่า `x >= 0` และ
> `y >= 0` เพื่อให้ค่าระหว่างทางเป็นจำนวนจริง แม้จำนวนลบจะมีรากที่สามที่เป็น
> จำนวนจริง แต่วิธีนี้ไม่ได้ออกแบบมาสำหรับกรณีนั้น

---

## ทำไมจึงประมาณรากที่สามได้

รากที่สามของ $y$ คือ $y^{1/3}$ ดังนั้นโจทย์สำคัญคือการสร้างเลขชี้กำลัง
$1/3$ จากกำลังที่เกิดด้วยปุ่มรากที่สอง

จากอนุกรมเรขาคณิต

$$
\frac{1}{3}=\frac{1}{4}+\frac{1}{4^2}+\frac{1}{4^3}+\cdots
$$

ผลบวกนี้เขียนเป็นผลคูณได้ว่า

$$
\frac{1}{3}
=\frac{1}{2^2}
\times\left(1+\frac{1}{2^2}\right)
\times\left(1+\frac{1}{2^4}\right)
\times\left(1+\frac{1}{2^8}\right)\cdots
$$

มองง่าย ๆ โดยให้ $r=1/4$ จะเห็นว่า
$r(1+r)=r+r^2$ และ $r(1+r)(1+r^2)=r+r^2+r^3+r^4$
เมื่อคูณวงเล็บถัดไปจะได้พจน์ของอนุกรมเพิ่มขึ้นเรื่อย ๆ จนครบ

ถ้าค่าปัจจุบันคือ $v=y^p$ การคำนวณ
`v * sqrt_n_times(v, n)` จะให้

$$
v\times v^{1/2^n}=y^{p(1+1/2^n)}
$$

แต่ละบรรทัดใน `cube_root` จึงค่อย ๆ เติมวงเล็บหนึ่งตัวในผลคูณของ $1/3$

---

## ไล่ค่าจาก `s1` ถึง `ans`

| ตัวแปร | คำสั่ง Python | เลขชี้กำลังของ $y$ ที่เพิ่มขึ้น |
|---|---|---|
| `s1` | `sqrt_n_times(y, 2)` | เริ่มที่ $1/2^2$ |
| `s2` | `s1 * sqrt_n_times(s1, 2)` | คูณด้วย $(1+1/2^2)$ |
| `s3` | `s2 * sqrt_n_times(s2, 4)` | คูณด้วย $(1+1/2^4)$ |
| `s4` | `s3 * sqrt_n_times(s3, 8)` | คูณด้วย $(1+1/2^8)$ |
| `s5` | `s4 * sqrt_n_times(s4, 16)` | คูณด้วย $(1+1/2^{16})$ |
| `ans` | `s5 * sqrt_n_times(s5, 32)` | คูณด้วย $(1+1/2^{32})$ |

ดังนั้น `ans` มีรูปเป็น $y^p$ เมื่อ

$$
p=\frac{1}{2^2}
\times\left(1+\frac{1}{2^2}\right)
\times\left(1+\frac{1}{2^4}\right)
\times\left(1+\frac{1}{2^8}\right)
\times\left(1+\frac{1}{2^{16}}\right)
\times\left(1+\frac{1}{2^{32}}\right)
\approx\frac{1}{3}
$$

สำหรับวงเล็บห้าตัวที่โค้ดใช้ จะได้
$p=\frac{1}{3}(1-\frac{1}{2^{64}})$ ซึ่งต่างจาก $1/3$ เพียงเล็กน้อยมาก
จึงได้ `ans = y ** p` ซึ่งประมาณ `y ** (1/3)` โดยใช้การหารากที่สองซ้ำ

> [!NOTE]
>
> คำตอบเป็นค่าประมาณ เพราะโปรแกรมหยุดหลังวงเล็บ
> $(1+1/2^{32})$ โดยไม่ได้คูณวงเล็บถัดไป $(1+1/2^{64})$ และชนิด
> `float` เก็บจำนวนจริงได้อย่างจำกัด เช่น `cube_root(27)` อาจได้
> `2.999999999999999` แทน `3.0` ซึ่งเป็นความคลาดเคลื่อนตามปกติของ
> floating point

---

## การรับข้อมูลและการเรียกโปรแกรม

ฟังก์ชัน `main()` อ่านข้อความหนึ่งบรรทัด แปลงเป็น `float` เก็บใน `q`
แล้วแสดง `cube_root(q)`

บรรทัดสุดท้าย `exec(input())` มีไว้สำหรับ grader โดย grader จะส่งคำสั่ง
Python เช่น `main()` หรือ `print(sqrt_n_times(10**8, 3))` เข้ามาให้ทำงาน
ดังนั้นถ้าต้องการเรียก `main()` ข้อมูลอาจมีลักษณะนี้

```text
main()
27
```

บรรทัดแรกถูกอ่านโดย `exec(input())` ส่วนบรรทัด `27` ถูกอ่านภายใน `main()`

> [!WARNING]
>
> `exec()` สามารถรันคำสั่ง Python ใด ๆ ได้ จึงควรใช้บรรทัดนี้เฉพาะกับคำสั่ง
> จาก grader ที่เชื่อถือได้ และไม่ควรใช้รูปแบบ `exec(input())` รับข้อมูลจาก
> ผู้ใช้ทั่วไป

---

# Solution

```python
# --------------------------------------------------
# File Name : 01_Expr_08.py
# Problem   : Cube Root (Function)
# Author    : Worralop Srichainont
# Date      : 2025-06-10
# --------------------------------------------------


# Calculate the square root of a number n times
def sqrt_n_times(x, n):
    return x ** (1 / (2**n))


# Estimate the cube root of a number y using the sqrt_n_times function
def cube_root(y):
    s1 = sqrt_n_times(y, 2)
    s2 = s1 * sqrt_n_times(s1, 2)
    s3 = s2 * sqrt_n_times(s2, 4)
    s4 = s3 * sqrt_n_times(s3, 8)
    s5 = s4 * sqrt_n_times(s4, 16)
    ans = s5 * sqrt_n_times(s5, 32)
    return ans


# Main function to read input and print the cube root
def main():
    q = float(input())
    print(cube_root(q))


# Execute the input string as code
exec(input())
```
