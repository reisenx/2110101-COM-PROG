<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

![01-str.png](/Z99-OTHERS/07-str/01-str.png)

# String and File Processing (การประมวลผลสตริงและแฟ้มข้อความ)

# Contents

- [1. String Fundamentals (พื้นฐานของสตริง)](#1-string-fundamentals-พื้นฐานของสตริง)
    - [1.1. String Values and Length (ค่าสตริงและความยาว)](#11-string-values-and-length-ค่าสตริงและความยาว)
    - [1.2. Indexing and Slicing (การเข้าถึงและตัดช่วง)](#12-indexing-and-slicing-การเข้าถึงและตัดช่วง)
    - [1.3. Iteration and Membership (การวนอ่านและตรวจสมาชิก)](#13-iteration-and-membership-การวนอ่านและตรวจสมาชิก)
    - [1.4. Concatenation and Repetition (การเชื่อมและทำซ้ำ)](#14-concatenation-and-repetition-การเชื่อมและทำซ้ำ)
    - [1.5. Escape Characters (อักขระพิเศษ)](#15-escape-characters-อักขระพิเศษ)
- [2. String Methods (เมธอดของสตริง)](#2-string-methods-เมธอดของสตริง)
    - [2.1. Case and Whitespace (ตัวพิมพ์และช่องว่าง)](#21-case-and-whitespace-ตัวพิมพ์และช่องว่าง)
    - [2.2. Searching with `find()` (การค้นหา)](#22-searching-with-find-การค้นหา)
    - [2.3. Splitting and Joining (การแยกและเชื่อม)](#23-splitting-and-joining-การแยกและเชื่อม)
    - [2.4. Method Chaining (การเรียกเมธอดต่อกัน)](#24-method-chaining-การเรียกเมธอดต่อกัน)
    - [2.5. String Immutability (สตริงเปลี่ยนค่าไม่ได้)](#25-string-immutability-สตริงเปลี่ยนค่าไม่ได้)
- [3. Text File Processing (การประมวลผลแฟ้มข้อความ)](#3-text-file-processing-การประมวลผลแฟ้มข้อความ)
    - [3.1. Opening and Closing Files (การเปิดและปิดแฟ้ม)](#31-opening-and-closing-files-การเปิดและปิดแฟ้ม)
    - [3.2. Reading Text Files (การอ่านแฟ้มข้อความ)](#32-reading-text-files-การอ่านแฟ้มข้อความ)
    - [3.3. Processing Records (การประมวลผลระเบียน)](#33-processing-records-การประมวลผลระเบียน)
    - [3.4. Writing Text Files (การเขียนแฟ้มข้อความ)](#34-writing-text-files-การเขียนแฟ้มข้อความ)

---

## 1. String Fundamentals (พื้นฐานของสตริง)

**String (สตริง)** คือข้อมูลประเภท `str` ที่ใช้เก็บข้อความ สตริงหนึ่งประกอบด้วย
อักขระเรียงต่อกัน จึงอ่านอักขระทีละตำแหน่ง ตัดเฉพาะบางช่วง วนอ่านทีละอักขระ
หรือนำสตริงหลายค่าไปประกอบกันได้

```python
message = "Hello"
print(message)
print(type(message))
```

ผลลัพธ์คือ

```
Hello
<class 'str'>
```

## 1.1. String Values and Length (ค่าสตริงและความยาว)

เขียนค่าสตริงโดยครอบข้อความด้วยเครื่องหมายคำพูดคู่ `"` หรือเครื่องหมายคำพูดเดี่ยว
`'` เลือกแบบที่ช่วยให้ข้อความด้านในอ่านง่าย

```python
first = "I'm learning Python."
second = 'She said "Hello".'
empty = ""

print(first)
print(second)
print(len(empty))
```

ผลลัพธ์คือ

```
I'm learning Python.
She said "Hello".
0
```

ฟังก์ชัน `len(s)` คืนจำนวนอักขระในสตริง `s` โดยนับช่องว่างและเครื่องหมายต่าง ๆ
ด้วย ส่วนสตริงว่าง `""` มีความยาว `0`

```python
text = " Hello "
print(len(text))
```

ผลลัพธ์คือ

```
7
```

## 1.2. Indexing and Slicing (การเข้าถึงและตัดช่วง)

อักขระแต่ละตัวมี **index (ดัชนี)** เริ่มจาก `0` ทางซ้าย และใช้ index ติดลบ
เพื่อไล่จากขวาได้ โดย `-1` หมายถึงอักขระตัวสุดท้าย

| String | `P` | `y` | `t` | `h` | `o` | `n` |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: |
| Index | `0` | `1` | `2` | `3` | `4` | `5` |
| Negative index | `-6` | `-5` | `-4` | `-3` | `-2` | `-1` |

```python
word = "Python"
print(word[0])
print(word[3])
print(word[-1])
```

ผลลัพธ์คือ

```
P
h
n
```

**Slicing (การตัดช่วง)** เขียนเป็น `s[start:stop]` โดยรวมตำแหน่ง `start`
แต่ไม่รวมตำแหน่ง `stop` หากเว้นด้านใด Python จะใช้ตั้งแต่ต้นหรือไปจนจบสตริง

```python
word = "Python"
print(word[1:4])
print(word[:2])
print(word[2:])
print(word[::-1])
```

ผลลัพธ์คือ

```
yth
Py
thon
nohtyP
```

> [!WARNING]
>
> การเข้าถึง index ที่อยู่นอกสตริง เช่น `"abc"[3]` ทำให้เกิด `IndexError`
> แต่การ slice เลยขอบเขต เช่น `"abc"[:10]` ทำได้และได้ค่า `"abc"`

## 1.3. Iteration and Membership (การวนอ่านและตรวจสมาชิก)

คำสั่ง `for` ใช้วนอ่านอักขระในสตริงตามลำดับ ส่วนตัวดำเนินการ `in` ใช้ตรวจว่า
อักขระหรือข้อความย่อยปรากฏอยู่ในสตริงหรือไม่

```python
text = "banana"
count = 0

for character in text:
    if character == "a":
        count += 1

print(count)
print("nan" in text)
print("z" in text)
```

ผลลัพธ์คือ

```
3
True
False
```

หากต้องใช้ทั้งตำแหน่งและอักขระ สามารถวน index ด้วย `range(len(s))`

```python
text = "ABC"
for index in range(len(text)):
    print(index, text[index])
```

ผลลัพธ์คือ

```
0 A
1 B
2 C
```

## 1.4. Concatenation and Repetition (การเชื่อมและทำซ้ำ)

ตัวดำเนินการ `+` เชื่อมสตริง และ `*` ทำซ้ำสตริงตามจำนวนเต็มที่กำหนด
การสร้างสตริงใหม่ทีละส่วนจึงทำได้ด้วย augmented assignment `+=`

```python
result = ""
for number in range(2, 7, 2):
    result += str(number)

print(result)
print("-" * 5)
print(2 * result)
```

ผลลัพธ์คือ

```
246
-----
246246
```

> [!WARNING]
>
> ค่าที่นำมาเชื่อมด้วย `+` ต้องเป็น `str` ทั้งคู่ เช่น ให้ใช้
> `"score=" + str(10)` ไม่ใช่ `"score=" + 10` และตัวคูณของสตริงต้องเป็น
> `int`

## 1.5. Escape Characters (อักขระพิเศษ)

เครื่องหมาย backslash `\` ใช้ขึ้นต้น **escape character** เพื่อแทนอักขระที่
เขียนตรง ๆ ใน string literal ได้ยาก

| Escape character | ความหมาย |
| :--: | :-- |
| `\"` | เครื่องหมายคำพูดคู่ `"` |
| `\'` | เครื่องหมายคำพูดเดี่ยว `'` |
| `\\` | backslash `\` |
| `\n` | ขึ้นบรรทัดใหม่ |

```python
quoted = "She said \"Hello\"."
path = "C:\\data\\notes.txt"
two_lines = "first line\nsecond line"

print(quoted)
print(path)
print(two_lines)
```

ผลลัพธ์คือ

```
She said "Hello".
C:\data\notes.txt
first line
second line
```

> [!IMPORTANT]
>
> `\n` ใน string literal เป็นอักขระขึ้นบรรทัดใหม่หนึ่งตัว ไม่ใช่อักขระ `\`
> ตามด้วย `n` ดังนั้น `len("A\nB")` มีค่า `3`

---

## 2. String Methods (เมธอดของสตริง)

**String method** คือคำสั่งที่เรียกผ่านค่าสตริงด้วยรูป `s.method()` เช่น
`s.lower()` และ `s.strip()` เมธอดรับสตริงเดิมมาประมวลผลแล้วคืนผลลัพธ์กลับมา

## 2.1. Case and Whitespace (ตัวพิมพ์และช่องว่าง)

เมธอดพื้นฐานสำหรับปรับตัวพิมพ์และตัด whitespace ที่หัวท้ายมีดังนี้

| Expression | ผลลัพธ์ | ความหมาย |
| :-- | :-- | :-- |
| `" Hello ".lower()` | `" hello "` | เปลี่ยนตัวอักษรเป็นตัวพิมพ์เล็ก |
| `" Hello ".upper()` | `" HELLO "` | เปลี่ยนตัวอักษรเป็นตัวพิมพ์ใหญ่ |
| `" Hello ".strip()` | `"Hello"` | ตัด whitespace ที่หัวและท้าย |

`strip()` ไม่ได้ลบช่องว่างตรงกลางข้อความ จึงเหมาะกับการจัดการข้อมูลที่ผู้ใช้
อาจเผลอเว้นช่องว่างก่อนหรือหลังคำตอบ

```python
answer = "  Yes  "
cleaned = answer.strip()

print(cleaned)
print(cleaned.upper() == "YES")
```

ผลลัพธ์คือ

```
Yes
True
```

## 2.2. Searching with `find()` (การค้นหา)

เมธอด `s.find(target)` คืน index แรกที่พบ `target` ใน `s` และคืน `-1`
เมื่อไม่พบ หากระบุ `start` เป็นอาร์กิวเมนต์ที่สอง การค้นหาจะเริ่มจาก index นั้น

```python
text = "Hello World"
print(text.find("o"))
print(text.find("o", 5))
print(text.find("Python"))
```

ผลลัพธ์คือ

```
4
7
-1
```

ค่าที่คืนจาก `find()` ใช้ร่วมกับ slicing เพื่อดึงข้อความระหว่างเครื่องหมายได้
ตัวอย่างต่อไปนี้ดึงค่าหลัง `name=` จนถึงเครื่องหมาย `;`

```python
text = "id=17;name=Arun;role=student"
pattern = "name="
start = text.find(pattern)

if start >= 0:
    start += len(pattern)
    stop = text.find(";", start)
    if stop >= 0:
        print(text[start:stop])
```

ผลลัพธ์คือ

```
Arun
```

> [!WARNING]
>
> ต้องตรวจว่า index จาก `find()` มีค่าตั้งแต่ `0` ขึ้นไป **ก่อน** บวกความยาว
> ของ pattern มิฉะนั้นค่า `-1` อาจถูกบวกจนดูเหมือนเป็นตำแหน่งที่ค้นพบ

## 2.3. Splitting and Joining (การแยกและเชื่อม)

เมธอด `split()` แบ่งสตริงเป็น `list` ของข้อความย่อย หากไม่ระบุตัวคั่น
จะแบ่งตรง whitespace แต่หากระบุตัวคั่น จะแบ่งตรงข้อความนั้น

```python
line = "red green blue"
colors = line.split()
print(colors)

record = "101,Notebook,45"
fields = record.split(",")
print(fields)
```

ผลลัพธ์คือ

```
['red', 'green', 'blue']
['101', 'Notebook', '45']
```

ในทิศทางกลับกัน `separator.join(parts)` เชื่อมสมาชิกที่เป็นสตริงใน `parts`
โดยวาง `separator` คั่นระหว่างสมาชิก

```python
words = ["String", "File", "Processing"]
title = " - ".join(words)
print(title)
```

ผลลัพธ์คือ

```
String - File - Processing
```

> [!WARNING]
>
> สมาชิกทุกตัวที่ส่งให้ `join()` ต้องเป็น `str` เช่น
> `",".join([1, 2, 3])` ทำให้เกิด `TypeError` ต้องแปลงสมาชิกเป็นสตริงก่อน

## 2.4. Method Chaining (การเรียกเมธอดต่อกัน)

ผลลัพธ์จากเมธอดหนึ่งสามารถเรียกเมธอดถัดไปได้ เรียกว่า **method chaining**
เช่น ขั้นตอนตัดช่องว่าง เปลี่ยนเป็นตัวพิมพ์ใหญ่ แล้วค้นหาข้อความ เขียนแยกได้ดังนี้

```python
line1 = "  ready: OK  "
line2 = line1.strip()
line3 = line2.upper()
index = line3.find("OK")
print(index)
```

ผลลัพธ์คือ

```
7
```

เมื่อเข้าใจลำดับแล้ว สามารถเขียนให้กระชับด้วย method chaining

```python
line = "  ready: OK  "
index = line.strip().upper().find("OK")
print(index)
```

ผลลัพธ์คือ

```
7
```

แต่ละขั้นทำงานจากซ้ายไปขวา โดยผลจาก `strip()` เป็นสตริงที่ใช้เรียก `upper()`
และผลจาก `upper()` ใช้เรียก `find()`

## 2.5. String Immutability (สตริงเปลี่ยนค่าไม่ได้)

สตริงเป็นข้อมูลแบบ **immutable** หมายความว่าไม่สามารถแก้อักขระภายในสตริงเดิม
ด้วยการกำหนดค่าผ่าน index หรือ slice

```python
word = "Hello"
# word[0] = "J"  # TypeError
```

string method ก็ไม่เปลี่ยนค่าเดิม แต่คืนสตริงใหม่ หากต้องการเก็บผลลัพธ์ใหม่
ต้องกำหนดค่ากลับให้ตัวแปร

```python
word = "HellO"
word.lower()
print(word)

word = word.lower()
print(word)
```

ผลลัพธ์คือ

```
HellO
hello
```

> [!IMPORTANT]
>
> แม้แก้สตริงเดิมไม่ได้ แต่เปลี่ยนให้ตัวแปรอ้างถึงสตริงใหม่ได้ เช่น
> `word = word.lower()`

---

## 3. Text File Processing (การประมวลผลแฟ้มข้อความ)

แฟ้มข้อความเก็บข้อมูลเป็นลำดับอักขระเช่นเดียวกับสตริง โปรแกรมจึงอ่านแต่ละบรรทัด
เข้ามาเป็น `str` แล้วใช้ indexing, slicing และ string methods ที่เรียนมาได้

## 3.1. Opening and Closing Files (การเปิดและปิดแฟ้ม)

ฟังก์ชัน `open(filename, mode)` เปิดแฟ้มและคืน **file object** สำหรับติดต่อกับแฟ้ม
เมื่อใช้งานเสร็จต้องเรียก `close()` เพื่อคืนทรัพยากรและทำให้ข้อมูลที่เขียนถูกบันทึก
ครบถ้วน

| Mode | การใช้งาน |
| :--: | :-- |
| `"r"` | เปิดแฟ้มเดิมเพื่ออ่าน หากไม่พบแฟ้มจะเกิด `FileNotFoundError` |
| `"w"` | เปิดแฟ้มเพื่อเขียน โดยลบเนื้อหาเดิม หรือสร้างแฟ้มใหม่หากยังไม่มี |

```python
fin = open("notes.txt", "r", encoding="utf-8")
# อ่านข้อมูลจาก fin
fin.close()
```

การระบุ `encoding="utf-8"` ทำให้การอ่านและเขียนข้อความภาษาไทยมีพฤติกรรมแน่นอน
ไม่ขึ้นกับค่าเริ่มต้นของระบบปฏิบัติการ

> [!WARNING]
>
> การเปิดแฟ้มเดิมด้วย mode `"w"` จะลบเนื้อหาเดิมทันที ควรตรวจชื่อแฟ้มและ mode
> ให้ถูกต้องก่อนเปิด

## 3.2. Reading Text Files (การอ่านแฟ้มข้อความ)

เมธอด `readline()` อ่านบรรทัดถัดไปเป็นสตริง หากบรรทัดในแฟ้มจบด้วย newline
สตริงที่อ่านได้จะมี `\n` ติดมาด้วย และเมื่ออ่านถึงท้ายแฟ้มจะคืนสตริงว่าง `""`

สมมติว่า `notes.txt` มีข้อมูลดังนี้

```
alpha
beta
gamma
```

คำสั่งต่อไปนี้อ่านสองบรรทัดแรก

```python
fin = open("notes.txt", "r", encoding="utf-8")
first = fin.readline().strip()
second = fin.readline().strip()
fin.close()

print(first)
print(second)
```

ผลลัพธ์คือ

```
alpha
beta
```

หากต้องการอ่านทุกบรรทัดจนหมดแฟ้ม ใช้ `for line in fin` ได้โดยตรง

```python
fin = open("notes.txt", "r", encoding="utf-8")
for line in fin:
    print(line.strip().upper())
fin.close()
```

ผลลัพธ์คือ

```
ALPHA
BETA
GAMMA
```

> [!IMPORTANT]
>
> `strip()` ตัด whitespace ทั้งหัวและท้าย หากต้องรักษาช่องว่างของข้อมูลไว้
> ไม่ควรเรียก `strip()` โดยอัตโนมัติ

## 3.3. Processing Records (การประมวลผลระเบียน)

แฟ้มข้อความมักเก็บหนึ่ง **record (ระเบียน)** ต่อหนึ่งบรรทัด โปรแกรมสามารถอ่าน
ทีละบรรทัด แยก fields ด้วย `split()` แปลงประเภทข้อมูล และประมวลผลต่อได้

สมมติว่า `products.txt` เก็บชื่อสินค้าและราคา โดยคั่นด้วย whitespace

```
pencil 12.5
notebook 40
eraser 7.5
```

```python
total = 0.0
products = []

fin = open("products.txt", "r", encoding="utf-8")
for line in fin:
    name, price_text = line.split()
    price = float(price_text)
    products.append([name, price])
    total += price
fin.close()

print(products)
print("Total =", total)
```

ผลลัพธ์คือ

```
[['pencil', 12.5], ['notebook', 40.0], ['eraser', 7.5]]
Total = 60.0
```

ตัวแปรที่ได้จาก `split()` ยังเป็น `str` จึงต้องใช้ `float()` ก่อนคำนวณ ส่วนการ
เก็บ `[name, price]` ลงใน `list` ช่วยให้เรียงลำดับหรือประมวลผลภายหลังได้

## 3.4. Writing Text Files (การเขียนแฟ้มข้อความ)

เมธอด `write(text)` เขียนสตริงต่อจากตำแหน่งปัจจุบันในแฟ้ม และไม่ขึ้นบรรทัดใหม่
ให้อัตโนมัติ หากต้องการแยกบรรทัดต้องใส่ `\n` เอง

```python
fout = open("squares.txt", "w", encoding="utf-8")
for number in range(1, 6):
    square = number ** 2
    fout.write(str(square) + "\n")
fout.close()
```

หลังจากโปรแกรมทำงาน `squares.txt` จะมีข้อมูลดังนี้

```
1
4
9
16
25
```

> [!WARNING]
>
> `write()` รับเฉพาะ `str` จึงต้องแปลงตัวเลขด้วย `str()` ก่อน และควรเรียก
> `close()` หลังเขียนเสร็จเสมอ
