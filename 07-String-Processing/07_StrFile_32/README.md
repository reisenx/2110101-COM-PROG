<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Password Strength ★★★ (
      <a href="https://drive.google.com/file/d/160ndl8Mg6mKUMmBVrq4JHX-GL04ajGuw/view?usp=drive_link">
        <code>07_StrFile_32</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**ภาพรวมการตรวจรหัสผ่าน**](#ภาพรวมการตรวจรหัสผ่าน)
-   [**การตรวจเงื่อนไขพื้นฐาน**](#การตรวจเงื่อนไขพื้นฐาน)
-   [**การตรวจอักขระ 4 ตัวที่ติดกัน**](#การตรวจอักขระ-4-ตัวที่ติดกัน)
-   [**การแสดงผลตามลำดับ**](#การแสดงผลตามลำดับ)
-   [**Solution**](#solution)

---

## ภาพรวมการตรวจรหัสผ่าน

โจทย์นี้รับรหัสผ่านหนึ่งบรรทัด แล้วตรวจว่ารหัสผ่านขาดคุณสมบัติใดบ้าง
การตรวจแต่ละเรื่องถูกแยกเป็นฟังก์ชัน เพื่อให้แต่ละฟังก์ชันมีหน้าที่ชัดเจน
และสามารถตรวจสอบผลได้ทีละเงื่อนไข

ชื่อฟังก์ชันที่ขึ้นต้นด้วย `no_` อาจดูสับสนเล็กน้อย ฟังก์ชันเหล่านี้จะคืนค่า
`True` เมื่อ **พบข้อบกพร่อง** เช่น `no_lowercase(password)` คืนค่า `True`
เมื่อรหัสผ่านไม่มีตัวอักษรพิมพ์เล็ก และคืนค่า `False` เมื่อพบตัวพิมพ์เล็กอย่างน้อยหนึ่งตัว

โปรแกรมตรวจข้อบกพร่องทั้งหมดตามลำดับดังนี้

| ลำดับ | ฟังก์ชันหรือเงื่อนไข | ข้อบกพร่องที่ตรวจพบ | ข้อความที่แสดง |
|---:|---|---|---|
| 1 | `less_than_eight_letter()` | มีอักขระน้อยกว่า 8 ตัว | `Less than 8 characters` |
| 2 | `no_lowercase()` | ไม่มีตัวอักษรพิมพ์เล็ก | `No lowercase letters` |
| 3 | `no_uppercase()` | ไม่มีตัวอักษรพิมพ์ใหญ่ | `No uppercase letters` |
| 4 | `no_number()` | ไม่มีตัวเลข | `No numbers` |
| 5 | `no_symbol()` | ไม่มีสัญลักษณ์ | `No symbols` |
| 6 | `character_repetition()` | มีอักขระเดิมซ้ำกัน 4 ตัว | `Character repetition` |
| 7 | `number_sequence()` | มีตัวเลขเรียงกัน 4 ตัว | `Number sequence` |
| 8 | `letter_sequence()` | มีตัวอักษรเรียงกัน 4 ตัว | `Letter sequence` |
| 9 | `keyboard_pattern()` | มีปุ่มแถวเดียวกันบนแป้นพิมพ์เรียงกัน 4 ตัว | `Keyboard pattern` |

---

## การตรวจเงื่อนไขพื้นฐาน

โปรแกรมรับค่าด้วย `input().strip()` โดย `strip()` จะตัดช่องว่างที่อยู่หน้าสุดและ
ท้ายสุดออกก่อนตรวจสอบ จากนั้น `less_than_eight_letter()` ใช้
`len(password) < 8` เพื่อตรวจจำนวนอักขระทั้งหมด

> [!NOTE]
>
> ความเห็นในโค้ดระบุว่า `less than 8 letters` แต่เงื่อนไขจริงใช้ `len()`
> จึงนับ **อักขระทุกชนิด** ไม่ได้จำกัดเฉพาะตัวอักษรภาษาอังกฤษ

ฟังก์ชัน `no_lowercase()`, `no_uppercase()`, `no_number()` และ `no_symbol()`
จะวนดูอักขระทีละตัว แล้วใช้ `in` ตรวจว่าอักขระนั้นอยู่ในสตริงที่กำหนดหรือไม่
ถ้าพบอักขระประเภทที่ต้องการก็คืนค่า `False` ทันที แต่ถ้าวนจนครบแล้วยังไม่พบ
จึงคืนค่า `True`

ตัวอย่างเช่น `no_number("Python3!")` คืนค่า `False` เพราะพบ `3` อยู่ใน
`NUMBER` ส่วน `no_number("Python!")` คืนค่า `True` เพราะไม่มีตัวเลขเลย

สำหรับสัญลักษณ์ โปรแกรมจะยอมรับเฉพาะอักขระที่อยู่ใน `SYMBOL` เช่น `!`, `@`,
`#`, `_` และ `?` เท่านั้น อักขระอื่นที่ไม่ได้อยู่ในสตริงนี้จะไม่ทำให้
`no_symbol()` คืนค่า `False`

---

## การตรวจอักขระ 4 ตัวที่ติดกัน

ถ้ารหัสผ่านมีความยาว $n$ จะมีช่วงอักขระที่ติดกันช่วงละ 4 ตัวทั้งหมด

$$
n - 4 + 1 = n - 3
$$

ช่วง ดังนั้นโปรแกรมจึงใช้ `range(len(password) - 3)` เพื่อให้ `i` เป็นตำแหน่งเริ่มต้น
ของทุกช่วง และใช้ `password[i : i + 4]` ตัดอักขระออกมาครั้งละ 4 ตัว
ถ้ารหัสผ่านสั้นกว่า 4 ตัว `range()` จะว่างและไม่มีช่วงให้ตรวจ

### อักขระซ้ำกัน

`character_repetition()` เปลี่ยนช่วงที่ตัดได้เป็นตัวพิมพ์เล็กด้วย `lower()`
แล้วเปรียบเทียบกับอักขระตัวแรกซ้ำ 4 ครั้ง

```python
substring = password[i : i + 4].lower()
if substring == substring[0] * 4:
    return True
```

ดังนั้น `aaaa`, `AAAA` และ `aAaA` ล้วนถือว่าเป็นอักขระซ้ำกัน 4 ตัว
เพราะการตรวจนี้ไม่แยกตัวพิมพ์เล็กและตัวพิมพ์ใหญ่

### ลำดับตัวเลขและตัวอักษร

`number_sequence()` ตรวจทั้งลำดับเดินหน้าและย้อนกลับด้วย
`substring in NUMBER` และ `substring[::-1] in NUMBER` ตามลำดับ
โดย `[::-1]` หมายถึงการกลับสตริงจากหลังมาหน้า

ค่าของ `NUMBER` คือ `"01234567890"` ซึ่งมี `0` ทั้งต้นและท้าย ทำให้ตรวจพบ
ลำดับที่วนจาก `9` กลับไป `0` เช่น `7890` ได้ด้วย ส่วนลำดับลด เช่น `0987`
จะตรวจพบเมื่อกลับสตริงแล้วได้ `7890`

`letter_sequence()` ใช้แนวคิดเดียวกัน แต่เปลี่ยนช่วงเป็นตัวพิมพ์เล็กก่อน
แล้วค้นหาใน `LOWERCASE` จึงตรวจพบได้ทั้ง `abcd`, `wXYZ` และ `ZYxW`

### ลำดับปุ่มบนแป้นพิมพ์

`keyboard_pattern()` ตรวจแถวแนวนอน 4 แถวที่กำหนดไว้ใน `PATTERNS` ได้แก่
แถวสัญลักษณ์ แถว `QWERTYUIOP` แถว `ASDFGHJKL` และแถว `ZXCVBNM`
แต่ละช่วงถูกเปลี่ยนเป็นตัวพิมพ์ใหญ่ก่อน แล้วตรวจทั้งทิศทางปกติและทิศทางย้อนกลับ
จึงตรวจพบทั้ง `qwer`, `REWq`, `ASDF` และ `!@#$`

---

## การแสดงผลตามลำดับ

ลิสต์ `OUTPUT` จับคู่ผลการตรวจแต่ละข้อกับข้อความที่ต้องแสดง โปรแกรมวนตามลำดับ
ในลิสต์นี้ หาก `condition` เป็น `True` ก็พิมพ์ข้อความนั้นและเปลี่ยน
`is_password_strong` เป็น `False` จึงสามารถแสดงข้อบกพร่องหลายข้อได้ โดยยังคง
ลำดับตามที่โจทย์กำหนดเสมอ

ตัวอย่างเช่น รหัสผ่าน `abcd9999` ไม่มีตัวพิมพ์ใหญ่ ไม่มีสัญลักษณ์ มี `9999`
ซ้ำกัน และมี `abcd` เป็นลำดับตัวอักษร โปรแกรมจึงแสดงผล

```text
No uppercase letters
No symbols
Character repetition
Letter sequence
```

ถ้าไม่มีเงื่อนไขใดเป็น `True` ค่า `is_password_strong` จะยังคงเป็น `True`
และโปรแกรมจะแสดง `OK` เพียงบรรทัดเดียว

---

# Solution

```python
# --------------------------------------------------
# File Name : 07_StrFile_32.py
# Problem   : Password Strength
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------

# List of characters
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "01234567890"
SYMBOL = "!@#$%^&*()_+-=[]{}\\|;:'\",.<>/?`~"
PATTERNS = ["!@#$%^&*()_+", "QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]


# Check if the password has less than 8 letters
def less_than_eight_letter(password):
    return len(password) < 8


# Check if the password has no lowercase letters
def no_lowercase(password):
    for char in password:
        if char in LOWERCASE:
            return False
    return True


# Check if the password has no uppercase letters
def no_uppercase(password):
    for char in password:
        if char in UPPERCASE:
            return False
    return True


# Check if the password has no numbers
def no_number(password):
    for char in password:
        if char in NUMBER:
            return False
    return True


# Check if the password has no symbols
def no_symbol(password):
    for char in password:
        if char in SYMBOL:
            return False
    return True


# Check if the password has 4 continuous same characters
def character_repetition(password):
    for i in range(len(password) - 3):
        substring = password[i : i + 4].lower()
        if substring == substring[0] * 4:
            return True
    return False


# Check if there are 4 continuous numbers in password that are in order
def number_sequence(password):
    for i in range(len(password) - 3):
        substring = password[i : i + 4]
        if substring in NUMBER or substring[::-1] in NUMBER:
            return True
    return False


# Check if there are 4 continuous characters in password that are in order
def letter_sequence(password):
    for i in range(len(password) - 3):
        substring = password[i : i + 4].lower()
        if substring in LOWERCASE or substring[::-1] in LOWERCASE:
            return True
    return False


# Check if there are 4 continuous characters in password that are in keyboard row order
def keyboard_pattern(password):
    for pattern in PATTERNS:
        for i in range(len(password) - 3):
            substring = password[i : i + 4].upper()
            if substring in pattern or substring[::-1] in pattern:
                return True
    return False


# Input a password
password = input().strip()
is_password_strong = True

# Output
OUTPUT = [
    [less_than_eight_letter(password), "Less than 8 characters"],
    [no_lowercase(password), "No lowercase letters"],
    [no_uppercase(password), "No uppercase letters"],
    [no_number(password), "No numbers"],
    [no_symbol(password), "No symbols"],
    [character_repetition(password), "Character repetition"],
    [number_sequence(password), "Number sequence"],
    [letter_sequence(password), "Letter sequence"],
    [keyboard_pattern(password), "Keyboard pattern"],
]

for condition, message in OUTPUT:
    if condition:
        print(message)
        is_password_strong = False

if is_password_strong:
    print("OK")
```
