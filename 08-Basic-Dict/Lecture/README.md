<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

![Basic Dictionary](/Z99-OTHERS/08-dict/01-dict.png)

# Basic Dictionary (พจนานุกรมพื้นฐาน)

# Contents

- [1. Dictionary Fundamentals (พื้นฐาน Dictionary)](#1-dictionary-fundamentals-พื้นฐาน-dictionary)
    - [1.1. Dictionary and List (Dictionary และ List)](#11-dictionary-and-list-dictionary-และ-list)
    - [1.2. Key-Value Mapping (การจับคู่ Key และ Value)](#12-key-value-mapping-การจับคู่-key-และ-value)
    - [1.3. Creating a Dictionary (การสร้าง Dictionary)](#13-creating-a-dictionary-การสร้าง-dictionary)
- [2. Accessing and Updating Data (การเข้าถึงและแก้ไขข้อมูล)](#2-accessing-and-updating-data-การเข้าถึงและแก้ไขข้อมูล)
    - [2.1. Accessing a Value (การเข้าถึง Value)](#21-accessing-a-value-การเข้าถึง-value)
    - [2.2. Adding and Updating Data (การเพิ่มและเปลี่ยนข้อมูล)](#22-adding-and-updating-data-การเพิ่มและเปลี่ยนข้อมูล)
    - [2.3. Building a Dictionary Step by Step (การสร้าง Dictionary ทีละคู่)](#23-building-a-dictionary-step-by-step-การสร้าง-dictionary-ทีละคู่)
- [3. Membership and Iteration (การตรวจสอบและวนซ้ำ)](#3-membership-and-iteration-การตรวจสอบและวนซ้ำ)
    - [3.1. Membership Testing (การตรวจสอบ Key)](#31-membership-testing-การตรวจสอบ-key)
    - [3.2. Iterating over Keys (การวนซ้ำผ่าน Key)](#32-iterating-over-keys-การวนซ้ำผ่าน-key)
    - [3.3. Length and Aggregation (จำนวนคู่และการรวมค่า)](#33-length-and-aggregation-จำนวนคู่และการรวมค่า)
- [4. Dictionary Patterns (รูปแบบการใช้ Dictionary)](#4-dictionary-patterns-รูปแบบการใช้-dictionary)
    - [4.1. Counting Data (การนับข้อมูล)](#41-counting-data-การนับข้อมูล)
    - [4.2. Dictionary and List Lookup (การค้นหาใน Dictionary และ List)](#42-dictionary-and-list-lookup-การค้นหาใน-dictionary-และ-list)

---

## 1. Dictionary Fundamentals (พื้นฐาน Dictionary)

**Dictionary** หรือข้อมูลประเภท `dict` ใช้เก็บข้อมูลเป็นคู่ ๆ แต่ละคู่ประกอบด้วย
**key** ที่ใช้ระบุข้อมูล และ **value** ซึ่งเป็นค่าที่ต้องการเก็บ

ตัวอย่างเช่น เราอาจเก็บชื่อวันภาษาอังกฤษเป็น key และชื่อย่อภาษาไทยเป็น value

```python
days = {"Mon": "จ", "Tue": "อ", "Wed": "พ"}
print(days)
```

ผลลัพธ์คือ

```
{'Mon': 'จ', 'Tue': 'อ', 'Wed': 'พ'}
```

เครื่องหมาย `:` คั่น key กับ value ของคู่เดียวกัน ส่วนเครื่องหมาย `,` คั่น
แต่ละคู่ใน dictionary

---

## 1.1. Dictionary and List (Dictionary และ List)

ทั้ง `list` และ `dict` เก็บข้อมูลได้หลายค่า แต่ใช้วิธีระบุตำแหน่งต่างกัน

| ประเภทข้อมูล | วิธีเก็บข้อมูล | วิธีเข้าถึงข้อมูล |
| --- | --- | --- |
| `list` | เก็บสมาชิกเรียงตามตำแหน่ง | ใช้ index ซึ่งเป็นจำนวนเต็ม |
| `dict` | เก็บข้อมูลเป็นคู่ key-value | ใช้ key ที่กำหนดไว้ |

สมมติว่าต้องการเก็บชื่อย่อของวัน การใช้ `list` ต้องจำว่าแต่ละวันอยู่ที่ index ใด

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
print(days[2])
```

ผลลัพธ์คือ

```
Wed
```

เมื่อใช้ `dict` เราสามารถเลือก key ที่สื่อความหมายกับข้อมูลได้โดยตรง

```python
days = {"Monday": "Mon", "Tuesday": "Tue", "Wednesday": "Wed"}
print(days["Wednesday"])
```

ผลลัพธ์คือ

```
Wed
```

ดังนั้น `list` เหมาะเมื่อเราสนใจลำดับและตำแหน่งของสมาชิก ส่วน `dict` เหมาะ
เมื่อเราต้องการค้นหา value จาก key ที่มีความหมาย

---

## 1.2. Key-Value Mapping (การจับคู่ Key และ Value)

ให้มอง dictionary เป็น **mapping** ที่เชื่อม key แต่ละตัวไปยัง value หนึ่งค่า

| key | value |
| --- | --- |
| `"A101"` | `"A"` |
| `"A102"` | `"B"` |
| `"A103"` | `"A"` |

จากตารางจะเห็นว่า

- key ใน dictionary เดียวกันต้องไม่ซ้ำกัน
- value ซ้ำกันได้ เช่น `"A101"` และ `"A103"` มี value เป็น `"A"` เหมือนกัน
- การจับคู่มีทิศทางจาก key ไปยัง value จึงใช้ key เพื่อเข้าถึง value
  ไม่ได้ใช้ value เพื่อย้อนกลับไปหา key โดยตรง

ถ้าเขียน key ซ้ำใน dictionary literal คู่หลังสุดจะกำหนด value ของ key นั้น

```python
status = {"A101": "waiting", "A102": "done", "A101": "done"}
print(status)
```

ผลลัพธ์คือ

```
{'A101': 'done', 'A102': 'done'}
```

key ต้องเป็นข้อมูลที่ **hashable** หรือเป็นค่าที่ไม่เปลี่ยนแปลงระหว่างใช้งาน
ตัวอย่าง key ที่ใช้บ่อย ได้แก่ `int`, `float`, `str` และ `tuple` ที่ภายใน
ประกอบด้วยค่าที่ hashable ส่วน value เป็นข้อมูลประเภทใดก็ได้

```python
examples = {
    101: "integer key",
    2.5: "float key",
    "name": "string key",
    (1, 2): "tuple key",
}
print(examples["name"])
```

ผลลัพธ์คือ

```
string key
```

> [!WARNING]
>
> `list`, `dict` และ `set` เปลี่ยนแปลงสมาชิกภายในได้ จึงใช้เป็น key ไม่ได้
> เช่น `{[1, 2]: "point"}` จะเกิด `TypeError`

---

## 1.3. Creating a Dictionary (การสร้าง Dictionary)

สร้าง dictionary โดยเขียนคู่ `key: value` ภายในวงเล็บปีกกา `{}`

```python
profile = {
    "name": "Mali",
    "year": 1,
    "active": True,
}
print(profile)
```

ผลลัพธ์คือ

```
{'name': 'Mali', 'year': 1, 'active': True}
```

dictionary หนึ่งตัวเก็บ value ต่างประเภทกันได้ และสร้าง dictionary ว่างได้ด้วย
`{}`

```python
empty = {}
print(empty)
print(type(empty))
```

ผลลัพธ์คือ

```
{}
<class 'dict'>
```

> [!IMPORTANT]
>
> `{}` คือ dictionary ว่าง ไม่ใช่ set ว่าง

---

## 2. Accessing and Updating Data (การเข้าถึงและแก้ไขข้อมูล)

เมื่อต้องการทำงานกับคู่ข้อมูลหนึ่งคู่ ให้เขียน key ไว้ในวงเล็บเหลี่ยมหลังชื่อ
dictionary รูปแบบนี้ใช้ได้ทั้งการอ่าน การเพิ่ม และการเปลี่ยน value

---

## 2.1. Accessing a Value (การเข้าถึง Value)

การเขียน `dictionary[key]` จะคืน value ที่จับคู่กับ key นั้น

```python
prices = {"pen": 12, "notebook": 35, "eraser": 8}
item_price = prices["notebook"]
print(item_price)
```

ผลลัพธ์คือ

```
35
```

> [!WARNING]
>
> หาก key ไม่มีอยู่ใน dictionary การเข้าถึงด้วยวงเล็บเหลี่ยมจะเกิด
> `KeyError` เช่น `prices["ruler"]` เพื่อหลีกเลี่ยงข้อผิดพลาดนี้ควรตรวจสอบ
> key ก่อนตามหัวข้อ 3.1

dictionary สนับสนุนการเข้าถึงจาก key ไปยัง value เท่านั้น หากต้องการค้นหา key
จาก value อาจต้องตรวจแต่ละคู่ และ value เดียวกันอาจจับคู่กับหลาย key ได้

---

## 2.2. Adding and Updating Data (การเพิ่มและเปลี่ยนข้อมูล)

การกำหนดค่าให้ `dictionary[key]` มีสองกรณี

- ถ้า key ยังไม่มี จะเพิ่มคู่ key-value ใหม่
- ถ้า key มีอยู่แล้ว จะเปลี่ยน value ของ key เดิม

```python
scores = {}
scores["Mali"] = 8
scores["Niran"] = 6
print(scores)

scores["Niran"] = 9
print(scores)
```

ผลลัพธ์คือ

```
{'Mali': 8, 'Niran': 6}
{'Mali': 8, 'Niran': 9}
```

บรรทัด `scores["Niran"] = 9` ไม่ได้สร้าง key ซ้ำ แต่เปลี่ยน value จาก `6`
เป็น `9`

หาก value เป็นตัวเลข เราสามารถอ่านค่าเดิม คำนวณ แล้วกำหนดกลับด้วย augmented
assignment ได้

```python
stock = {"pen": 10, "eraser": 4}
stock["pen"] += 3
print(stock["pen"])
```

ผลลัพธ์คือ

```
13
```

> [!WARNING]
>
> คำสั่ง `stock["ruler"] += 1` จะเกิด `KeyError` ถ้า key `"ruler"`
> ยังไม่มี เพราะ augmented assignment ต้องอ่าน value เดิมก่อนนำมาบวก

---

## 2.3. Building a Dictionary Step by Step (การสร้าง Dictionary ทีละคู่)

เราสามารถเริ่มจาก dictionary ว่าง แล้วใช้ loop เพิ่มข้อมูลทีละคู่ได้

```python
names = ["Mali", "Niran", "Ploy"]
scores = [8, 9, 7]
result = {}

for index in range(len(names)):
    result[names[index]] = scores[index]

print(result)
```

ผลลัพธ์คือ

```
{'Mali': 8, 'Niran': 9, 'Ploy': 7}
```

ในแต่ละรอบ `names[index]` เป็น key และ `scores[index]` เป็น value หากพบ key
เดิมอีกครั้ง value ใหม่จะเขียนทับ value เดิมตามหลักในหัวข้อ 2.2

---

## 3. Membership and Iteration (การตรวจสอบและวนซ้ำ)

dictionary ใช้ร่วมกับ `in`, `not in` และ `for` ได้ โดยเครื่องมือเหล่านี้
ทำงานกับ **key** เป็นหลัก

---

## 3.1. Membership Testing (การตรวจสอบ Key)

นิพจน์ `key in dictionary` ตรวจว่า key อยู่ใน dictionary หรือไม่ ส่วน
`key not in dictionary` ตรวจว่า key ไม่อยู่ใน dictionary

```python
prices = {"pen": 12, "notebook": 35}
print("pen" in prices)
print("ruler" in prices)
print("ruler" not in prices)
print(12 in prices)
```

ผลลัพธ์คือ

```
True
False
True
False
```

บรรทัดสุดท้ายเป็น `False` เพราะ `12` เป็น value ไม่ใช่ key

การตรวจสอบสมาชิกก่อนเข้าถึงช่วยป้องกัน `KeyError`

```python
prices = {"pen": 12, "notebook": 35}
item = "ruler"

if item in prices:
    print(prices[item])
else:
    print("Not found")
```

ผลลัพธ์คือ

```
Not found
```

---

## 3.2. Iterating over Keys (การวนซ้ำผ่าน Key)

คำสั่ง `for key in dictionary` จะหยิบ key ออกมาทีละตัว ภายใน loop จึงใช้
`dictionary[key]` เพื่อเข้าถึง value ที่คู่กันได้

```python
scores = {"Mali": 8, "Niran": 9, "Ploy": 7}

for name in scores:
    print(name, "-->", scores[name])
```

ผลลัพธ์คือ

```
Mali --> 8
Niran --> 9
Ploy --> 7
```

ใน Python 3.11 dictionary **รักษาลำดับการเพิ่ม key** ดังนั้น loop จะได้ key
ตามลำดับที่เพิ่มเข้า dictionary การเปลี่ยน value ของ key เดิมไม่ย้าย key นั้น
ไปท้ายลำดับ

```python
scores = {"Mali": 8, "Niran": 6}
scores["Ploy"] = 7
scores["Niran"] = 9

for name in scores:
    print(name, scores[name])
```

ผลลัพธ์คือ

```
Mali 8
Niran 9
Ploy 7
```

> [!IMPORTANT]
>
> หากรู้ key ที่ต้องการอยู่แล้ว ให้เข้าถึง `dictionary[key]` โดยตรง
> ไม่จำเป็นต้องเขียน loop เพื่อค้นหา key นั้น

---

## 3.3. Length and Aggregation (จำนวนคู่และการรวมค่า)

ฟังก์ชัน `len(dictionary)` คืนจำนวนคู่ key-value ใน dictionary

```python
scores = {"quiz": 8, "midterm": 17, "final": 39}
print(len(scores))
```

ผลลัพธ์คือ

```
3
```

เมื่อต้องการคำนวณจาก value ทุกค่า สามารถวนซ้ำผ่าน key แล้วหยิบ value ของแต่ละ
key มาใช้ ตัวอย่างต่อไปนี้หาค่าเฉลี่ยของ value ที่เป็นตัวเลข

```python
def average(data):
    total = 0
    for key in data:
        total += data[key]
    return total / len(data)


temperatures = {"Mon": 30, "Tue": 32, "Wed": 31}
print(average(temperatures))
```

ผลลัพธ์คือ

```
31.0
```

> [!WARNING]
>
> ฟังก์ชันตัวอย่างต้องได้รับ dictionary ที่ไม่ว่างและมี value เป็นตัวเลข
> หาก dictionary ว่าง การหารด้วย `len(data)` ซึ่งเป็น `0` จะเกิด
> `ZeroDivisionError`

---

## 4. Dictionary Patterns (รูปแบบการใช้ Dictionary)

เมื่อเข้าใจการเพิ่ม การตรวจสอบ และการวนซ้ำแล้ว เราสามารถนำขั้นตอนเหล่านี้
มาประกอบกันเพื่อสรุปข้อมูลได้

---

## 4.1. Counting Data (การนับข้อมูล)

รูปแบบการนับข้อมูลด้วย dictionary คือใช้ข้อมูลที่พบเป็น key และใช้จำนวนครั้ง
ที่พบเป็น value

1. เริ่มจาก dictionary ว่าง
2. อ่านข้อมูลทีละค่า
3. หาก key มีอยู่แล้ว ให้เพิ่ม value ขึ้นหนึ่ง
4. หากยังไม่มี key ให้เพิ่ม key ใหม่โดยเริ่ม value ที่หนึ่ง

```python
colors = ["red", "blue", "red", "green", "blue", "red"]
counts = {}

for color in colors:
    if color in counts:
        counts[color] += 1
    else:
        counts[color] = 1

for color in counts:
    print(color, "-->", counts[color])
```

ผลลัพธ์คือ

```
red --> 3
blue --> 2
green --> 1
```

ตัวอย่างนี้ใช้แนวคิดสามเรื่องร่วมกัน ได้แก่ การตรวจ key ด้วย `in` การเปลี่ยน
value เดิมด้วย `+=` และการเพิ่มคู่ใหม่ด้วย `counts[color] = 1`

---

## 4.2. Dictionary and List Lookup (การค้นหาใน Dictionary และ List)

การตรวจ `key in dictionary` และการเข้าถึง `dictionary[key]` ใช้ key เพื่อค้นหา
ข้อมูลโดยตรง ในกรณีทั่วไปจึงทำงานได้เร็วแม้ dictionary มีข้อมูลจำนวนมาก

ในทางกลับกัน การตรวจ `element in list` อาจต้องเปรียบเทียบสมาชิกทีละตัวตั้งแต่
ต้น list จนกว่าจะพบข้อมูลหรือถึงท้าย list

| งานที่ต้องการ | `list` | `dict` |
| --- | --- | --- |
| เข้าถึงด้วยตำแหน่งจำนวนเต็ม | เหมาะ โดยใช้ `data[index]` | ใช้ได้เมื่อจำนวนเต็มนั้นเป็น key จริง ๆ |
| ตรวจหาข้อมูลทั่วไป | อาจต้องไล่ดูสมาชิกหลายตัว | ตรวจ key ได้รวดเร็วในกรณีทั่วไป |
| เชื่อมตัวระบุกับข้อมูล | ต้องจัดตำแหน่งให้สัมพันธ์กันเอง | เหมาะ เพราะเก็บเป็นคู่ key-value |
| รักษาลำดับการเพิ่มข้อมูล | รักษาลำดับสมาชิก | รักษาลำดับ key ใน Python 3.11 |

> [!IMPORTANT]
>
> การที่ dictionary รักษาลำดับการเพิ่ม key ไม่ได้ทำให้ key กลายเป็น index
> เช่น `data[0]` หมายถึงการขอ value ของ key `0` ไม่ใช่สมาชิกตัวแรก

เลือกใช้ `list` เมื่อโจทย์เน้นลำดับหรือตำแหน่ง และเลือกใช้ `dict` เมื่อมี key
ที่เหมาะสมสำหรับระบุและค้นหา value
