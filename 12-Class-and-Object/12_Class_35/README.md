<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Roman Numberal ★★★ (
      <a href="https://drive.google.com/file/d/11l2prjZRO4y18gnNhQcr6QshCzTOvojf/view?usp=drive_link">
        <code>12_Class_35</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**เลขโรมันและคลาส `Roman`**](#เลขโรมันและคลาส-roman)
-   [**การแปลงเลขโรมันเป็นจำนวนเต็ม**](#การแปลงเลขโรมันเป็นจำนวนเต็ม)
-   [**การเปรียบเทียบและการแสดงผล**](#การเปรียบเทียบและการแสดงผล)
-   [**การบวกและแปลงกลับเป็นเลขโรมัน**](#การบวกและแปลงกลับเป็นเลขโรมัน)
-   [**รูปแบบข้อมูลเข้าและผลลัพธ์**](#รูปแบบข้อมูลเข้าและผลลัพธ์)
-   [**Solution**](#solution)

---

## เลขโรมันและคลาส `Roman`

เลขโรมันในโจทย์นี้ประกอบด้วยสัญลักษณ์พื้นฐาน 7 ตัว

| สัญลักษณ์ | `I` | `V` | `X` | `L` | `C` | `D` | `M` |
| :--------: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|     ค่า     |  1  |  5  | 10  | 50  | 100 | 500 | 1000 |

บางค่าจะเขียนด้วยการวางสัญลักษณ์ค่าน้อยไว้หน้าสัญลักษณ์ค่ามาก เช่น `IV` คือ
`4`, `IX` คือ `9`, `XL` คือ `40`, `XC` คือ `90`, `CD` คือ `400` และ
`CM` คือ `900`

คลาส `Roman` เก็บข้อความเลขโรมันไว้ใน `self.roman` โดยตรง เมท็อดพิเศษแต่ละตัว
ทำให้เราสามารถใช้วัตถุได้เหมือนข้อมูลพื้นฐานของ Python

-   `str(a)` เรียก `a.__str__()` เพื่อขอข้อความเลขโรมัน
-   `int(a)` เรียก `a.__int__()` เพื่อแปลงเป็นจำนวนเต็ม
-   `a < b` เรียก `a.__lt__(b)` เพื่อเปรียบเทียบค่า
-   `a + b` เรียก `a.__add__(b)` และคืนวัตถุ `Roman` ตัวใหม่

โจทย์กำหนดให้เลขโรมันที่ใช้อยู่ในช่วง `1` ถึง `4999`

---

## การแปลงเลขโรมันเป็นจำนวนเต็ม

พจนานุกรม `ROMAN_TO_NUMBER` แบ่งรูปแบบเลขโรมันเป็นกลุ่มตามอักขระตัวแรก
เช่น กลุ่มที่ขึ้นต้นด้วย `C` มี `CCC`, `CM`, `CD`, `CC` และ `C`
พร้อมค่าจำนวนเต็มของแต่ละรูปแบบ

เมท็อด `__int__` ใช้ตัวแปร `string` เป็นสำเนาของเลขโรมัน และทำซ้ำตามขั้นตอนนี้

1. ดูอักขระตัวแรกด้วย `string[0]` เพื่อเลือกกลุ่มที่ต้องตรวจ
2. หารูปแบบที่ตรงกับด้านหน้าของ `string` ด้วย
   `string.find(substring) == 0`
3. บวก `value` ของรูปแบบนั้นเข้า `number`
4. ตัดส่วนที่อ่านแล้วออกด้วย `string = string[len(substring):]`
5. ทำต่อจนกระทั่ง `string` ว่าง

ตัวอย่าง `MCMLXXXVII` ถูกแบ่งเป็น `M + CM + LXXX + VII` จึงมีค่า

$$
1000 + 900 + 80 + 7 = 1987
$$

ใน Python ค่าของแต่ละส่วนจะถูกสะสมด้วย `number += value`

> [!NOTE]
>
> โค้ดนี้ทำงานภายใต้เงื่อนไขของโจทย์ว่าอินพุตเป็นเลขโรมันมาตรฐานที่ถูกต้อง
> และไม่ได้มีขั้นตอนตรวจหรือแก้ข้อความเลขโรมันที่ไม่ถูกต้อง

---

## การเปรียบเทียบและการแสดงผล

`__str__` คืน `self.roman` จึงแสดงข้อความเดิมที่เก็บไว้โดยไม่แปลงรูป เช่น
`str(Roman("IV"))` ได้ `"IV"`

ส่วน `__lt__` แปลงวัตถุทั้งสองเป็นจำนวนเต็มก่อนเปรียบเทียบ

```python
return int(self) < int(rhs)
```

ดังนั้น `Roman("III") < Roman("IV")` ให้ผลเป็น `True` เพราะ Python
เปรียบเทียบ `3 < 4` หากค่าทั้งสองเท่ากัน เครื่องหมาย `<` จะให้ `False`

---

## การบวกและแปลงกลับเป็นเลขโรมัน

เมท็อด `__add__` เริ่มจากแปลงตัวตั้งและตัวบวกเป็นจำนวนเต็ม

```python
total = int(self) + int(rhs)
```

จากนั้น `NUMBER_TO_ROMAN` จะพิจารณาหลัก `1000`, `100`, `10` และ `1`
ตามลำดับ ในแต่ละหลักคำนวณเลขประจำหลักและเศษที่เหลือด้วย

$$
\text{idx} = \text{total} \mathbin{//} \text{value}
$$

```python
idx = total // value
result += roman_numerals[idx]
total %= value
```

ตัวอย่าง `MCCXXXIV + LXVI` คือ `1234 + 66 = 1300` ตารางจึงเลือก `M`
ในหลักพันและ `CCC` ในหลักร้อย ได้วัตถุใหม่ `Roman("MCCC")`

ตารางหลักพันมีดัชนีตั้งแต่ `0` ถึง `4` จึงรองรับผลลัพธ์สูงสุด `4999`
ตามขอบเขตโจทย์ หากผลบวกเกินช่วงนี้ โค้ดที่ให้มาจะไม่สามารถเลือกข้อความจากตารางได้

---

## รูปแบบข้อมูลเข้าและผลลัพธ์

อินพุตมีข้อความ 3 ตัวคั่นด้วยช่องว่าง คือ `t`, `r1` และ `r2` แล้วสร้าง
`a = Roman(r1)` กับ `b = Roman(r2)` ค่า `t` เลือกสิ่งที่จะแสดงดังนี้

| `t` | คำสั่งที่ทำงาน | ผลลัพธ์ |
| :-: | :------------- | :------ |
| `1` | `print(a < b)` | `True` หรือ `False` จากการเปรียบเทียบ |
| `2` | `print(int(a), int(b))` | จำนวนเต็มของทั้งสองค่า |
| `3` | `print(str(a), str(b))` | ข้อความเลขโรมันเดิมของทั้งสองค่า |
| `4` | `print(int(a + b))` | ผลบวกในรูปจำนวนเต็ม |
| ค่าอื่น | `print(str(a + b))` | ผลบวกในรูปเลขโรมัน |

`print()` ใส่ช่องว่างระหว่างผลลัพธ์สองค่าในกรณี `t` เป็น `2` หรือ `3`
โดยอัตโนมัติ

---

# Solution

```python
# --------------------------------------------------
# File Name : 12_Class_35.py
# Problem   : Roman Numeral
# Author    : Worralop Srichainont
# Date      : 2025-08-09
# --------------------------------------------------

# Dictionary to convert between numbers and Roman numerals
NUMBER_TO_ROMAN = {
    1000: ("", "M", "MM", "MMM", "MMMM"),
    100: ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
    10: ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
    1: ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
}

ROMAN_TO_NUMBER = {
    "I": (("III", 3), ("IX", 9), ("IV", 4), ("II", 2), ("I", 1)),
    "V": (("VIII", 8), ("VII", 7), ("VI", 6), ("V", 5)),
    "X": (("XXX", 30), ("XC", 90), ("XL", 40), ("XX", 20), ("X", 10)),
    "L": (("LXXX", 80), ("LXX", 70), ("LX", 60), ("L", 50)),
    "C": (("CCC", 300), ("CM", 900), ("CD", 400), ("CC", 200), ("C", 100)),
    "D": (("DCCC", 800), ("DCC", 700), ("DC", 600), ("D", 500)),
    "M": (("MMMM", 4000), ("MMM", 3000), ("MM", 2000), ("M", 1000)),
}


class Roman:
    # __init__ method
    # Initializes the Roman numeral with a string representation.
    def __init__(self, roman):
        self.roman = roman

    # __lt__ method
    # Compares two Roman numeral objects based on their integer values.
    def __lt__(self, rhs):
        return int(self) < int(rhs)

    # __str__ method
    # Returns the string representation of the Roman numeral.
    def __str__(self):
        return self.roman

    # __int__ method
    # Converts the Roman numeral to its integer value.
    def __int__(self):
        # Initialize the number to 0
        number = 0
        string = self.roman
        # Loop through the string until it is empty
        while string != "":
            # Check for the longest matching Roman numeral substring
            for substring, value in ROMAN_TO_NUMBER[string[0]]:
                # Found a match substring at the start of the string
                if string.find(substring) == 0:
                    # Add the value to the number
                    number += value
                    # Remove the matched substring from the string
                    string = string[len(substring) :]
                    break
        return number

    # __add__ method
    # Calculates the sum of two Roman numeral objects and returns a new Roman object.
    def __add__(self, rhs):
        # Initialize the sum of the two Roman numerals, and string result
        total = int(self) + int(rhs)

        # Convert the total back to Roman numeral format
        result = ""
        for value, roman_numerals in NUMBER_TO_ROMAN.items():
            idx = total // value
            result += roman_numerals[idx]
            total %= value

        # Return a new Roman object with the resulting Roman numeral
        return Roman(result)


# Output
t, r1, r2 = input().split()
a = Roman(r1)
b = Roman(r2)
if t == "1":
    print(a < b)
elif t == "2":
    print(int(a), int(b))
elif t == "3":
    print(str(a), str(b))
elif t == "4":
    print(int(a + b))
else:
    print(str(a + b))
```
