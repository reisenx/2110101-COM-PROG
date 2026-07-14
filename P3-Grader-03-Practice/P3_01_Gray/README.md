<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Gray Codes ★★★ (
      <a href="https://drive.google.com/file/d/1wtcfvhjixQCCNLIbgYGeM6CuGrg597gz/view?usp=drive_link">
        <code>P3_01_Gray</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**รู้จัก Gray Code**](#รู้จัก-gray-code)
-   [**สร้าง Gray Code ด้วยวิธีสะท้อน**](#สร้าง-gray-code-ด้วยวิธีสะท้อน)
-   [**ตรวจสอบค่า n และ k**](#ตรวจสอบค่า-n-และ-k)
-   [**สร้างบรรทัดบอกตำแหน่ง**](#สร้างบรรทัดบอกตำแหน่ง)
-   [**แบ่ง Gray Codes แสดงผลทีละ k ตัว**](#แบ่ง-gray-codes-แสดงผลทีละ-k-ตัว)
-   [**Solution**](#solution)

---

## รู้จัก Gray Code

Gray Code คือลำดับของเลขฐานสองที่สมาชิกสองตัวซึ่งอยู่ติดกัน
แตกต่างกันเพียง `1` บิต ตัวอย่างเช่น Gray Code ขนาด `2` บิต คือ

```text
00,01,11,10
```

-   `00` กับ `01` ต่างกันที่บิตขวาสุด
-   `01` กับ `11` ต่างกันที่บิตซ้ายสุด
-   `11` กับ `10` ต่างกันที่บิตขวาสุด

Gray Code ขนาด \(n\) บิตมีทั้งหมด

\[
2^n
\]

ตัว ในภาษา Python เขียนจำนวนนี้ได้เป็น `2 ** n`
แต่โปรแกรมข้อนี้ไม่จำเป็นต้องคำนวณค่านี้โดยตรง
เพราะรายการ `codes` จะยาวขึ้นเป็นสองเท่าในแต่ละรอบอยู่แล้ว

ข้อมูลนำเข้ามี `2` บรรทัด บรรทัดแรกคือ `n` ซึ่งกำหนดจำนวนบิต
และบรรทัดที่สองคือ `k` ซึ่งกำหนดจำนวน Gray Codes ที่ต้องการแสดงต่อบรรทัด
เมื่อข้อมูลถูกต้อง โปรแกรมจะแสดงบรรทัดบอกตำแหน่งก่อน
แล้วจึงแสดง Gray Codes ตามลำดับ

---

## สร้าง Gray Code ด้วยวิธีสะท้อน

เริ่มจาก Gray Code ขนาด `1` บิต

```python
codes = ["0", "1"]
```

การเพิ่มขนาดจาก \(b-1\) บิตเป็น \(b\) บิตทำได้ด้วยวิธี **สะท้อน**

1.  นำลำดับเดิมมาต่อกับลำดับเดิมที่กลับด้าน
2.  เติม `"0"` หน้าสมาชิกในครึ่งซ้าย
3.  เติม `"1"` หน้าสมาชิกในครึ่งขวา

เขียนเป็นแนวคิดทางคณิตศาสตร์ได้ว่า

\[
G_b
=
0G_{b-1}
\mathbin{\Vert}
1\operatorname{reverse}(G_{b-1})
\]

โดย \(\mathbin{\Vert}\) หมายถึงการนำสองลำดับมาต่อกัน
ส่วนใน Python การกลับและต่อรายการทำด้วย

```python
codes += codes[::-1]
```

ตัวอย่างการสร้าง Gray Code ขนาด `2` บิต

```text
ลำดับเดิม             0,1
กลับลำดับ             1,0
นำมาต่อกัน            0,1,1,0
เติม 0 และ 1 ข้างหน้า  00,01,11,10
```

ตัวแปร `half` เก็บจำนวนสมาชิกของแต่ละครึ่งหลังจากต่อรายการแล้ว
ดังนั้นคำสั่ง

```python
for i in range(half):
    codes[i] = "0" + codes[i]
    codes[half + i] = "1" + codes[half + i]
```

จะเติมเลขนำหน้าให้ตำแหน่งที่ตรงกันในครึ่งซ้ายและครึ่งขวา
ลูปใหญ่ทำทั้งหมด `bits - 1` รอบ เพราะรายการเริ่มต้นมีขนาด `1` บิตแล้ว

---

## ตรวจสอบค่า n และ k

โจทย์กำหนดให้ `n` และ `k` เป็นจำนวนเต็ม แต่ทั้งคู่ต้องมีค่าอย่างน้อย `1`
ฟังก์ชัน `is_valid()` ตรวจสอบกรณีที่ผิดทั้งคู่ก่อน
เพื่อให้แสดงข้อความเพียงข้อความเดียวตามลำดับนี้

| เงื่อนไข | ข้อความที่แสดง |
| --- | --- |
| `n < 1` และ `k < 1` | `Invalid n and k` |
| `n < 1` | `Invalid n` |
| `k < 1` | `Invalid k` |

หากพบข้อมูลไม่ถูกต้อง ฟังก์ชันคืนค่า `False`
โปรแกรมจึงไม่สร้างบรรทัดบอกตำแหน่งและไม่สร้าง Gray Codes
แต่ถ้าทั้งคู่ถูกต้อง ฟังก์ชันคืนค่า `True` แล้วโปรแกรมจึงทำงานต่อ

> [!NOTE]
>
> คำสั่ง `int(input())` อาศัยข้อกำหนดของโจทย์ว่าข้อมูลนำเข้าเป็นจำนวนเต็ม
> ส่วนฟังก์ชัน `is_valid()` ตรวจเฉพาะว่าค่านั้นเป็นจำนวนเต็มบวกหรือไม่
> และไม่ได้ตรวจขอบเขตบน `n <= 15` กับ `k <= 100`
> เพราะระบบตรวจให้ข้อมูลตามขอบเขตนี้อยู่แล้ว

---

## สร้างบรรทัดบอกตำแหน่ง

Gray Code แต่ละตัวใช้พื้นที่ `n` ตัวอักษร และระหว่าง Gray Codes
มีเครื่องหมายจุลภาคอีก `1` ตัว ดังนั้น `k - 1` ช่วงแรกของบรรทัดบอกตำแหน่ง
ต้องกว้างช่วงละ `n + 1` ตัวอักษร ส่วนช่วงสุดท้ายกว้าง `n` ตัวอักษร
เพราะหลัง Gray Code ตัวสุดท้ายไม่มีเครื่องหมายจุลภาค

ถ้าหมายเลขตำแหน่ง `num` มีจำนวนหลักเท่ากับ
\(\operatorname{digits}(num)\) จำนวนขีดของช่วงทั่วไปคือ

\[
n-\operatorname{digits}(num)+1
\]

ซึ่งตรงกับ

```python
n - len(str(num)) + 1
```

ส่วนช่วงสุดท้ายใช้

\[
n-\operatorname{digits}(k)
\]

ซึ่งตรงกับ `n - len(str(num))` ในกรณีที่ `num == k`
ความยาวรวมของบรรทัดจึงเป็น

\[
kn+(k-1)=k(n+1)-1
\]

ตัวอักษร เท่ากับความกว้างของ Gray Codes `k` ตัวและจุลภาค `k - 1` ตัวพอดี
เช่น `n = 2` และ `k = 8` จะได้

```text
1--2--3--4--5--6--7--8-
```

> [!WARNING]
>
> เมื่อหมายเลขตำแหน่งมีจำนวนหลักเท่ากับหรือมากกว่าความกว้างของช่วง
> ค่าที่นำไปคูณ `"-"` จะเป็นศูนย์หรือติดลบ ซึ่ง Python จะสร้างสตริงว่าง
> เช่น `n = 1` และ `k = 100` ทำให้หมายเลขตั้งแต่ `10` เป็นต้นไปชิดกัน
> เป็น `...9-101112...100` นี่คือพฤติกรรมของโค้ด Solution ตามจริง
> แม้รูปแบบบรรทัดจะไม่รักษาความกว้างคงที่ตามภาพในโจทย์

---

## แบ่ง Gray Codes แสดงผลทีละ k ตัว

หลังสร้าง Gray Codes ครบแล้ว ตัวแปร `idx` ชี้ไปยังสมาชิกตัวแรก
ของกลุ่มที่กำลังจะแสดง คำสั่ง

```python
codes[idx : idx + k]
```

เลือกสมาชิกได้ไม่เกิน `k` ตัว และ

```python
",".join(codes[idx : idx + k])
```

เชื่อมสมาชิกด้วยจุลภาคโดยไม่มีจุลภาคต่อท้าย
จากนั้น `idx += k` เลื่อนไปยังกลุ่มถัดไป

ถ้าจำนวน Gray Codes หารด้วย `k` ไม่ลงตัว
บรรทัดสุดท้ายจะมีสมาชิกน้อยกว่า `k` ตัวตามปกติ
ถ้า `k = 1` โปรแกรมจะแสดง Gray Code บรรทัดละตัว
และถ้า `k` มากกว่า \(2^n\) Gray Codes ทั้งหมดจะอยู่ในบรรทัดเดียว
แม้ว่าบรรทัดบอกตำแหน่งยังคงสร้างครบ `k` ช่วง

การแสดงผลไม่มีการปัดเศษหรือเติมช่องว่าง
Gray Code ทุกตัวมี `n` บิต จุลภาคอยู่ระหว่างตัวเท่านั้น
และลำดับต้องคงตามรายการ `codes` ที่สร้างด้วยวิธีสะท้อน

---

# Solution

```python
# --------------------------------------------------
# File Name : P3_01_Gray.py
# Problem   : Part-III Gray Codes
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------


# Check if n and k are valid integers
def is_valid(n, k):
    if n < 1 and k < 1:
        print("Invalid n and k")
        return False
    elif n < 1:
        print("Invalid n")
        return False
    elif k < 1:
        print("Invalid k")
        return False
    return True


# Print the number pattern based on n and k
def num_pattern(n, k):
    line = ""
    for num in range(1, k + 1):
        if num == k:
            line += f"{num}{(n - len(str(num))) * '-'}"
        else:
            line += f"{num}{(n - len(str(num)) + 1) * '-'}"
    print(line)


# Generate Gray codes for a given number of bits
def gray_codes(bits):
    # Initialize the list with the first two Gray codes
    half = 1
    codes = ["0", "1"]
    # Generate Gray codes
    for _ in range(bits - 1):
        # Append the reverse of the current codes
        codes += codes[::-1]
        half *= 2
        # Prefix '0' to the first half and '1' to the second half
        for i in range(half):
            codes[i] = "0" + codes[i]
            codes[half + i] = "1" + codes[half + i]
    return codes


# Input n and k
n = int(input())
k = int(input())

# Check if n and k are valid
if is_valid(n, k):
    # Print the number pattern
    num_pattern(n, k)
    # Generate and print Gray codes in groups of k
    codes = gray_codes(n)
    idx = 0
    while idx < len(codes):
        print(",".join(codes[idx : idx + k]))
        idx += k
```
