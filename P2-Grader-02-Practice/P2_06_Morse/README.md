<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Morse Code ★★★ (
      <a href="https://drive.google.com/file/d/1GWIgToXTk8FvUjOCKFfwHigVzp-mQqGN/view?usp=drive_link">
        <code>P2_06_Morse</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิดของโจทย์**](#แนวคิดของโจทย์)
-   [**โครงสร้างแฟ้มข้อมูล**](#โครงสร้างแฟ้มข้อมูล)
-   [**อ่านรูปแบบการแปลง**](#อ่านรูปแบบการแปลง)
-   [**แปลงข้อความเป็นรหัสมอร์ส**](#แปลงข้อความเป็นรหัสมอร์ส)
-   [**แปลงรหัสมอร์สเป็นข้อความ**](#แปลงรหัสมอร์สเป็นข้อความ)
-   [**จัดการข้อมูลที่แปลงไม่ได้**](#จัดการข้อมูลที่แปลงไม่ได้)
-   [**ลำดับการทำงานของโปรแกรม**](#ลำดับการทำงานของโปรแกรม)
-   [**ข้อควรระวัง**](#ข้อควรระวัง)
-   [**Solution**](#solution)

---

## แนวคิดของโจทย์

โปรแกรมต้องแปลงข้อมูลได้สองทิศทาง

| คำสั่ง | ทิศทางการแปลง | ตัวอย่าง |
|:---:|---|---|
| `T2M` | ข้อความ (Text) → รหัสมอร์ส (Morse) | `AB` → `.- -...` |
| `M2T` | รหัสมอร์ส (Morse) → ข้อความ (Text) | `.- -...` → `AB` |

สิ่งสำคัญคือข้อมูลจริงไม่ได้ป้อนจากแป้นพิมพ์โดยตรง ผู้ใช้ป้อนเพียง **ชื่อแฟ้ม** แล้วโปรแกรมจึงเปิดแฟ้มนั้นเพื่ออ่านคำสั่ง รูปแบบการแปลง และข้อมูลทุกบรรทัดที่เหลือ

รูปแบบการแปลงไม่ได้กำหนดตายตัวว่า `A` ต้องเป็น `.-` เสมอ โปรแกรมต้องสร้างตารางค้นหาจากบรรทัดที่สองของแฟ้ม จึงใช้ dictionary สองตัวสำหรับค้นหาได้ทั้งสองทิศทาง

## โครงสร้างแฟ้มข้อมูล

ข้อมูลจากแป้นพิมพ์มีหนึ่งบรรทัด

```text
ชื่อแฟ้ม
```

ส่วนแฟ้มที่ระบุมีอย่างน้อยสองบรรทัด และมีโครงสร้างดังนี้

| ตำแหน่งในแฟ้ม | ความหมาย |
|---|---|
| บรรทัดแรก | คำสั่ง `T2M` หรือ `M2T` |
| บรรทัดที่สอง | รูปแบบจับคู่ตัวอักษรกับรหัสมอร์ส |
| บรรทัดที่เหลือ | ข้อมูลที่ต้องแปลง บรรทัดละหนึ่งรายการ |

ตัวอย่างแฟ้มสำหรับแปลงข้อความเป็นรหัสมอร์ส

```text
T2M
[A].-[B]-...[C]-.-.[E].[
A
ABX
BBE
```

โปรแกรมเปิดแฟ้มด้วย `with` ซึ่งช่วยปิดแฟ้มให้อัตโนมัติเมื่อออกจากบล็อก

```python
with open(filename) as file:
    cmd = file.readline().strip()
    line = file.readline().strip()
```

`.readline()` ครั้งแรกอ่านคำสั่ง ครั้งที่สองอ่านรูปแบบการแปลง และ `.strip()` ตัดอักขระขึ้นบรรทัดใหม่ออก หลังจากนั้น `for line in file` จะอ่านเฉพาะบรรทัดข้อมูลที่เหลือ

## อ่านรูปแบบการแปลง

รูปแบบตัวอย่าง

```text
[A].-[B]-...[C]-.-.[E].[
```

หมายถึง

| ตัวอักษร | รหัสมอร์ส |
|:---:|:---:|
| `A` | `.-` |
| `B` | `-...` |
| `C` | `-.-.` |
| `E` | `.` |

ฟังก์ชัน `read_mappings()` เปลี่ยนวงเล็บเหลี่ยมทั้งสองชนิดเป็นช่องว่าง

```python
line = line.replace("[", " ").replace("]", " ")
```

เมื่อเรียก `.split()` จะได้ข้อมูลที่สลับกันระหว่างตัวอักษรกับรหัส

```text
A  .-  B  -...  C  -.-.  E  .
```

โปรแกรมจึงเดินทีละ 2 ตำแหน่ง

```python
for i in range(0, len(mappings), 2):
    char = mappings[i]
    morse_code = mappings[i + 1]
```

แล้วเก็บคู่เดิมและคู่ย้อนกลับพร้อมกัน

```python
CHAR_TO_MORSE[char] = morse_code
MORSE_TO_CHAR[morse_code] = char
```

- `CHAR_TO_MORSE["A"]` ให้ `".-"`
- `MORSE_TO_CHAR[".-"]` ให้ `"A"`

dictionary สองตัวนี้ทำให้แต่ละทิศทางค้นหาคำตอบจาก key ได้โดยตรง

> [!NOTE]
> โปรแกรมตั้งต้นในโจทย์ใช้ `.find()` หาเครื่องหมาย `[` ตัวถัดไป จึงอาศัย `[` ที่ท้ายรูปแบบเป็นจุดสิ้นสุดของรหัสตัวสุดท้าย แต่ Solution นี้เปลี่ยนวงเล็บทั้งหมดเป็นช่องว่างแล้วใช้ `.split()` ดังนั้น `[` ตัวท้ายจึงถูกตัดทิ้งและไม่ใช่ส่วนของรหัสมอร์ส

## แปลงข้อความเป็นรหัสมอร์ส

เมื่อ `cmd == "T2M"` โปรแกรมส่งแต่ละบรรทัดที่เหลือให้ `text_to_morse()`

ฟังก์ชันเริ่มจากลิสต์ว่าง แล้วอ่านตัวอักษรในข้อความทีละตัว

```python
result = []
for char in text:
    if char in CHAR_TO_MORSE:
        result.append(CHAR_TO_MORSE[char])
```

ถ้าตัวอักษรทุกตัวมีในรูปแบบ ลิสต์จะเก็บรหัสมอร์สตามลำดับ เช่น `BBE` กลายเป็น

```python
["-...", "-...", "."]
```

จากนั้น

```python
print(" ".join(result))
```

จะเชื่อมรหัสด้วยช่องว่างหนึ่งช่องและแสดง

```text
-... -... .
```

การใช้ `.join()` ทำให้มีช่องว่างเฉพาะ **ระหว่าง** รหัส ไม่มีช่องว่างเกินที่หัวหรือท้ายบรรทัด

## แปลงรหัสมอร์สเป็นข้อความ

เมื่อ `cmd == "M2T"` โปรแกรมส่งแต่ละบรรทัดให้ `morse_to_text()`

รหัสของตัวอักษรแต่ละตัวคั่นด้วยช่องว่าง จึงแยกด้วย

```python
for code in morse_code.split():
```

`.split()` ที่ไม่ระบุตัวคั่นรองรับช่องว่างติดกันหลายช่องและ tab ได้ จากนั้นนำแต่ละรหัสไปค้นใน `MORSE_TO_CHAR`

```python
result += MORSE_TO_CHAR[code]
```

ตัวอักษรถูกต่อเข้ากับ `result` โดยไม่มีช่องว่าง เช่น

```text
-... -... .
```

จะได้ `BBE`

## จัดการข้อมูลที่แปลงไม่ได้

### ตัวอักษรที่ไม่มีในรูปแบบ

ระหว่าง `T2M` หากพบตัวอักษรที่ไม่เป็น key ของ `CHAR_TO_MORSE` โปรแกรมจะเลิกแปลงบรรทัดนั้น แล้วแทนผลลัพธ์ทั้งหมดด้วยข้อความ

```python
result = [f"Invalid : {text}"]
break
```

เช่น รูปแบบมีเพียง `A`, `B`, `C` และ `E` แต่บรรทัดเป็น `ABX` ผลลัพธ์คือ

```text
Invalid : ABX
```

โปรแกรมไม่แสดงรหัสบางส่วนของ `A` และ `B` เพราะข้อมูลทั้งบรรทัดถือว่าแปลงไม่ได้

### รหัสมอร์สที่ไม่มีในรูปแบบ

ระหว่าง `M2T` หากมีรหัสที่ไม่เป็น key ของ `MORSE_TO_CHAR` โปรแกรมทำแบบเดียวกัน

```python
result = f"Invalid : {morse_code}"
break
```

ข้อความหลัง `Invalid :` คือบรรทัดเดิมที่ผ่าน `.strip()` ไม่ใช่เฉพาะ token ที่ผิด และหลังแสดงข้อผิดพลาด โปรแกรมยังอ่านและประมวลผลบรรทัดถัดไปตามปกติ

### คำสั่งไม่ถูกต้อง

ถ้าบรรทัดแรกไม่ใช่ `T2M` หรือ `M2T` โปรแกรมแสดง

```text
Invalid code
```

และไม่แปลงบรรทัดที่เหลือ อย่างไรก็ตาม โค้ดอ่านและเรียก `read_mappings()` กับบรรทัดที่สองก่อนตรวจค่า `cmd`

## ลำดับการทำงานของโปรแกรม

1. อ่านชื่อแฟ้มจากแป้นพิมพ์ด้วย `input().strip()`
2. เปิดแฟ้มด้วย `with open(filename)`
3. อ่านคำสั่งจากบรรทัดแรก
4. อ่านรูปแบบจากบรรทัดที่สอง และสร้าง dictionary ทั้งสองทิศทาง
5. ตรวจคำสั่ง
   - `M2T` — อ่านทีละบรรทัดแล้วเรียก `morse_to_text()`
   - `T2M` — อ่านทีละบรรทัดแล้วเรียก `text_to_morse()`
   - ค่าอื่น — แสดง `Invalid code`
6. เมื่อออกจากบล็อก `with` แฟ้มจะถูกปิดอัตโนมัติ

สำหรับแต่ละบรรทัด ฟังก์ชันจะแสดงผลทันที จึงรักษาลำดับเดียวกับข้อมูลในแฟ้ม และบรรทัดที่ผิดหนึ่งบรรทัดไม่ทำให้บรรทัดต่อไปถูกข้าม

## ข้อควรระวัง

- การค้นหา key เป็นแบบตรงตัว `A` กับ `a` จึงเป็นคนละตัวกัน หากรูปแบบไม่มีตัวพิมพ์เล็ก ข้อมูลตัวพิมพ์เล็กจะเป็น `Invalid`
- ใน `T2M` โปรแกรมอ่านทุกอักขระ รวมถึงช่องว่างภายในข้อความ แต่รูปแบบที่แยกด้วย `.split()` ไม่สามารถสร้าง key ที่เป็นช่องว่างได้ ข้อความที่มีช่องว่างภายในจึงแปลงไม่ได้ด้วยรูปแบบปกติ
- ใน `M2T` ช่องว่างหลายตัวระหว่างรหัสไม่มีผล เพราะ `.split()` จะแยกเป็น token เดิม
- รูปแบบต้องให้ token เป็นคู่ `ตัวอักษร รหัส` ครบถ้วน หากจำนวน token เป็นเลขคี่ การเข้าถึง `mappings[i + 1]` จะเกิดข้อผิดพลาด
- ถ้าตัวอักษรหรือรหัสซ้ำ assignment ใน dictionary จะเขียนทับค่าก่อนหน้า
- บรรทัดข้อมูลว่างจะทำให้ทั้งสองฟังก์ชันพิมพ์บรรทัดว่างหนึ่งบรรทัด
- รูปแบบผลลัพธ์ต้องรักษาช่องว่างรอบ `:` ใน `Invalid : ...` ส่วน `Invalid code` ไม่มีเครื่องหมาย `:`

---

# Solution

```python
# --------------------------------------------------
# File Name : P2_06_Morse.py
# Problem   : Part-II Morse Code
# Author    : Worralop Srichainont
# Date      : 2025-06-17
# --------------------------------------------------

# Initialize Morse code dictionary
CHAR_TO_MORSE = {}
MORSE_TO_CHAR = {}


# Read Morse code mappings from the input
def read_mappings(line):
    # Replace brackets with whitespace
    line = line.replace("[", " ").replace("]", " ")
    # Split the line into character and Morse code pairs
    mappings = line.split()
    # Store Morse code mappings in dictionaries
    for i in range(0, len(mappings), 2):
        char = mappings[i]
        morse_code = mappings[i + 1]
        CHAR_TO_MORSE[char] = morse_code
        MORSE_TO_CHAR[morse_code] = char


# Convert Morse code to text
def morse_to_text(morse_code):
    result = ""
    for code in morse_code.split():
        if code in MORSE_TO_CHAR:
            result += MORSE_TO_CHAR[code]
        else:
            result = f"Invalid : {morse_code}"
            break
    print(result)


# Convert text to Morse code
def text_to_morse(text):
    result = []
    for char in text:
        if char in CHAR_TO_MORSE:
            result.append(CHAR_TO_MORSE[char])
        else:
            result = [f"Invalid : {text}"]
            break
    print(" ".join(result))


# Input filename
filename = input().strip()

# Read Morse code mappings from the file
with open(filename) as file:
    # Read command from the first line
    cmd = file.readline().strip()

    # Read the second line for Morse code mappings
    line = file.readline().strip()
    read_mappings(line)

    # Process the command for the rest of the file
    if cmd == "M2T":
        for line in file:
            morse_to_text(line.strip())
    elif cmd == "T2M":
        for line in file:
            text_to_morse(line.strip())
    else:
        print("Invalid code")
```
