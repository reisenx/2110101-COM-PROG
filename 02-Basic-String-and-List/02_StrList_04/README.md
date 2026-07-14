<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    N Digits ★ (
      <a href="https://drive.google.com/file/d/1x9TSTjfAS4zqxaoHenatkl9PoeYzBxYE/view?usp=drive_link">
        <code>02_StrList_04</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การนับจำนวนหลัก**](#การนับจำนวนหลัก)
-   [**การคำนวณจำนวนเลขศูนย์**](#การคำนวณจำนวนเลขศูนย์)
-   [**การสร้างผลลัพธ์**](#การสร้างผลลัพธ์)
-   [**Solution**](#solution)

---

## การนับจำนวนหลัก

โจทย์รับจำนวนเต็มบวก $M$ และจำนวนหลักอย่างน้อยที่ต้องการ $N$
โปรแกรมเก็บ $M$ ไว้ในตัวแปร `number` ชนิด `str`
เพื่อให้นับจำนวนหลักด้วย `len()` และนำเลข `0` ไปต่อด้านหน้าได้สะดวก

```python
number = input().strip()
```

ตัวอย่างเช่น ถ้า `number` เป็น `"123"` ค่า `len(number)` จะเท่ากับ `3`
ส่วน $N$ ต้องใช้ในการลบ จึงแปลงข้อมูลบรรทัดที่สองเป็น `int`
และเก็บไว้ใน `display_digits`

---

## การคำนวณจำนวนเลขศูนย์

ให้ $z$ เป็นจำนวนเลขศูนย์ที่ต้องเติมด้านซ้าย จำนวนที่ต้องการคือ
$N - \operatorname{len}(M)$ แต่ถ้า $M$ มีจำนวนหลักครบหรือเกิน $N$ อยู่แล้ว
เราต้องเติมศูนย์ `0` ตัว ไม่ใช่จำนวนติดลบ ดังนั้น

$$
z = \max\bigl(0, N - \operatorname{len}(M)\bigr)
$$

สูตรนี้ตรงกับโค้ด

```python
leading_zeros = max(0, display_digits - len(number))
```

`max()` เลือกค่าที่มากที่สุดจากสองค่า จึงทำให้ `leading_zeros`
ไม่ต่ำกว่า `0`

| $M$ | $N$ | `len(number)` | `leading_zeros` | ผลลัพธ์ |
| :---: | :---: | :-----------: | :-------------: | :------: |
| `123` | `5` | `3` | `2` | `00123` |
| `123` | `3` | `3` | `0` | `123` |
| `123` | `2` | `3` | `0` | `123` |

กรณีสุดท้ายแสดงให้เห็นว่า ถ้า $M$ มีหลักมากกว่า $N$
โปรแกรมจะคง $M$ ทั้งหมดไว้และไม่ตัดตัวเลขออก

---

## การสร้างผลลัพธ์

สำหรับข้อความ ตัวดำเนินการ `*` ใช้ทำซ้ำได้ นิพจน์
`'0' * leading_zeros` จึงสร้างข้อความเลขศูนย์ตามจำนวนที่คำนวณไว้

```python
'0' * 2  # ได้ "00"
```

f-string นำข้อความเลขศูนย์นี้ไปวางหน้า `number`

```python
f"{'0' * leading_zeros}{number}"
```

ผลลัพธ์เป็นข้อความหนึ่งบรรทัดโดยไม่มีช่องว่างเพิ่มเติม
และไม่มีการปัดเศษหรือเปลี่ยนค่าของเลขเดิม

---

# Solution

```python
# --------------------------------------------------
# File Name : 02_StrList_04.py
# Problem   : N Digits
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------

# Input a number
number = input().strip()

# Input number of digits to display
display_digits = int(input())

# Calculate leading zeros if the number of digits to display is greater
leading_zeros = max(0, display_digits - len(number))

# Output the number with leading zeros
print(f"{'0' * leading_zeros}{number}")
```
