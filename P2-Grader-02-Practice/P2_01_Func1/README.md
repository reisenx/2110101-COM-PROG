<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Odd Odd Functions ★★ (
      <a href="https://drive.google.com/file/d/1fysZG6sj3HcgmMIxE94B25Qk0fBw_b2x/view?usp=drive_link">
        <code>P2_01_Func1</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิดสำคัญ**](#แนวคิดสำคัญ)
-   [**อธิบายการทำงาน**](#อธิบายการทำงาน)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**การทำงานร่วมกับ Grader**](#การทำงานร่วมกับ-grader)
-   [**Solution**](#solution)

---

## แนวคิดสำคัญ

โจทย์นี้ให้เราเขียนฟังก์ชันสำหรับตรวจสอบและรวบรวม **จำนวนคี่** จากลิสต์ โดย Grader จะส่งคำสั่งภาษา Python เข้ามาเรียกใช้ฟังก์ชันเหล่านี้อีกที โปรแกรมจึงต้องประกาศฟังก์ชันให้ครบก่อน แล้วค่อยรับคำสั่งทดสอบในบรรทัดสุดท้าย

### ตรวจจำนวนคี่ด้วยเศษจากการหาร

จำนวนเต็มเป็นจำนวนคี่เมื่อหารด้วย `2` แล้วเหลือเศษ `1`

$$
n \bmod 2 = 1
$$

เขียนเป็น Python ได้ว่า

```python
number % 2 == 1
```

นิพจน์เปรียบเทียบนี้ให้ค่า `True` หรือ `False` โดยตรง จึงนำไป `return` ได้เลย วิธีนี้ใช้กับจำนวนคี่ลบใน Python ได้เช่นกัน เช่น `-3 % 2` มีค่าเป็น `1`

### ออกจากฟังก์ชันทันทีเมื่อรู้คำตอบ

ฟังก์ชันที่ตรวจสมาชิกหลายตัวไม่จำเป็นต้องวนลูปจนจบเสมอไป

-   ถ้าต้องการรู้ว่า “มีจำนวนคี่อย่างน้อยหนึ่งตัวหรือไม่” เมื่อพบตัวแรกก็ `return True` ได้ทันที
-   ถ้าต้องการรู้ว่า “ทุกตัวเป็นจำนวนคี่หรือไม่” เมื่อพบตัวที่ไม่คี่ก็ `return False` ได้ทันที

การหยุดทันทีเช่นนี้เรียกว่า **short-circuit** และช่วยให้ไม่ต้องตรวจข้อมูลส่วนที่เหลือโดยไม่จำเป็น

---

## อธิบายการทำงาน

### `is_odd(number)`

ฟังก์ชันนี้เป็นพื้นฐานของฟังก์ชันอื่น โดยคืนผลของ `number % 2 == 1` จึงได้ Boolean ตามที่โจทย์ต้องการ

### `has_odds(numbers)`

วนดูสมาชิกตามลำดับและเรียก `is_odd(number)` ถ้าพบจำนวนคี่ให้คืน `True` ทันที แต่ถ้าวนจนครบโดยไม่พบเลยจึงคืน `False`

### `all_odds(numbers)`

แนวคิดกลับด้านกับ `has_odds` กล่าวคือ ถ้าพบสมาชิกที่ **ไม่ใช่** จำนวนคี่ ให้คืน `False` ทันที หากตรวจครบทุกตัวแล้วยังไม่พบตัวที่ผิดเงื่อนไขจึงคืน `True`

### `no_odds(numbers)`

“ไม่มีจำนวนคี่เลย” เป็นนิเสธของ “มีจำนวนคี่อย่างน้อยหนึ่งตัว” จึงนำผลของ `has_odds(numbers)` มากลับค่าด้วย `not`

> [!NOTE]
> สำหรับลิสต์ว่าง `has_odds([])` เป็น `False` เพราะไม่มีจำนวนคี่ให้พบ ส่วน `all_odds([])` และ `no_odds([])` เป็น `True` เพราะไม่มีสมาชิกใดขัดกับเงื่อนไขของทั้งสองฟังก์ชัน

### `get_odds(numbers)`

สร้างลิสต์ `result` ขึ้นมาใหม่ แล้ววนอ่าน `numbers` จากซ้ายไปขวา ถ้าสมาชิกเป็นจำนวนคี่จึงใช้ `append` เพิ่มลงในผลลัพธ์ วิธีนี้รักษาลำดับเดิมและไม่แก้ไขลิสต์ที่รับเข้ามา

ตัวอย่างเช่น

```text
numbers = [1, 3, 11, 2, 17]
result  = [1, 3, 11, 17]
```

### `zip_odds(a, b)`

ฟังก์ชันนี้ทำงานเป็นสองช่วง

1.  เรียก `get_odds` เพื่อสร้าง `odds_a` และ `odds_b` ซึ่งมีเฉพาะจำนวนคี่
2.  ที่ตำแหน่ง `idx` เดียวกัน ให้เพิ่มค่าจาก `odds_a` ก่อน แล้วจึงเพิ่มค่าจาก `odds_b` ถ้าลิสต์นั้นยังมีสมาชิกอยู่

ลูปใช้ความยาวที่มากกว่าของสองลิสต์ จึงเก็บสมาชิกที่เหลือจากลิสต์ที่ยาวกว่าได้ครบ โดยยังคงเริ่มสลับจากฝั่ง `a` เสมอ

---

## ตัวอย่างการทำงาน

พิจารณาคำสั่ง

```python
zip_odds([2, 4, 97, 99], [1, 3, 11, 2, 17])
```

หลังกรองจำนวนคู่ทิ้ง จะได้

```text
odds_a = [97, 99]
odds_b = [1, 3, 11, 17]
```

จากนั้นสลับสมาชิกตามลำดับดังนี้

| `idx` | ค่าจาก `odds_a` | ค่าจาก `odds_b` | ผลลัพธ์สะสม |
|---:|:---:|:---:|:---|
| `0` | `97` | `1` | `[97, 1]` |
| `1` | `99` | `3` | `[97, 1, 99, 3]` |
| `2` | ไม่มี | `11` | `[97, 1, 99, 3, 11]` |
| `3` | ไม่มี | `17` | `[97, 1, 99, 3, 11, 17]` |

ผลสุดท้ายจึงเป็น `[97, 1, 99, 3, 11, 17]` ตรงกับลำดับที่โจทย์กำหนด

---

## การทำงานร่วมกับ Grader

โจทย์ไม่ได้รับลิสต์โดยตรง แต่รับ **คำสั่ง Python หนึ่งบรรทัด** เช่น

```python
print(get_odds([1, 3, 11, 2, 17]))
```

คำสั่ง `input().strip()` อ่านและตัดช่องว่างที่หัวท้าย จากนั้น `exec(...)` จึงประมวลผลข้อความนั้นเป็นคำสั่ง Python ทำให้ Grader เรียกฟังก์ชันใดก็ได้ที่ประกาศไว้ด้านบน และถ้าคำสั่งมี `print` ผลลัพธ์จึงแสดงออกทางจอภาพ

> [!WARNING]
> `exec` สามารถรันคำสั่ง Python ใด ๆ ได้ จึงควรใช้เฉพาะกับข้อมูลจาก Grader ที่เชื่อถือได้เท่านั้น ห้ามนำรูปแบบนี้ไปรันข้อความจากผู้ใช้ที่ไม่รู้แหล่งที่มา

---

# Solution

```python
# --------------------------------------------------
# File Name : P2_01_Func1.py
# Problem   : Part-II Odd Odd Functions
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------


# Check if a number is odd
def is_odd(number):
    return number % 2 == 1


# Check if there are any odd numbers in the data
def has_odds(numbers):
    for number in numbers:
        if is_odd(number):
            return True
    return False


# Check if all numbers in the data are odd
def all_odds(numbers):
    for number in numbers:
        if not is_odd(number):
            return False
    return True


# Check if there are no odd numbers in the data
def no_odds(numbers):
    return not has_odds(numbers)


# Get a list of all odd numbers from the data
def get_odds(numbers):
    result = []
    for number in numbers:
        if is_odd(number):
            result.append(number)
    return result


# Zip two lists of odd numbers together, alternating between the two lists
def zip_odds(a, b):
    # Get the odd numbers from both lists
    odds_a = get_odds(a)
    odds_b = get_odds(b)
    # Create a new list to hold the zipped result
    result = []
    # Zip the two lists of odd numbers together
    for idx in range(max(len(odds_a), len(odds_b))):
        if idx < len(odds_a):
            result.append(odds_a[idx])

        if idx < len(odds_b):
            result.append(odds_b[idx])
    # Return the zipped list of odd numbers
    return result


# Execute the input string as code
exec(input().strip())
```
