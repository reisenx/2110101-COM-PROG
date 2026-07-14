<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Reverse and Keys ★ (
      <a href="https://drive.google.com/file/d/1PLGqq5Xqw2fbWuMnsbC-t3AlIUYLRCoT/view?usp=drive_link">
        <code>08_Dict_11</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การวนดูคีย์และค่าของพจนานุกรม**](#การวนดูคีย์และค่าของพจนานุกรม)
-   [**ฟังก์ชัน `reverse()`**](#ฟังก์ชัน-reverse)
-   [**ฟังก์ชัน `keys()`**](#ฟังก์ชัน-keys)
-   [**การรับคำสั่งจาก Grader**](#การรับคำสั่งจาก-grader)
-   [**Solution**](#solution)

---

## การวนดูคีย์และค่าของพจนานุกรม

ข้อมูลใน `dict` ประกอบด้วยคู่ของ **คีย์** (`key`) และ **ค่า** (`value`)
เช่น `3: "A"` หมายถึงคีย์ `3` เก็บค่า `"A"` ไว้

เมื่อต้องการนำทั้งคีย์และค่ามาใช้งานพร้อมกัน เราสามารถวนลูปผ่าน
`input_dict.items()` ได้ดังนี้

```python
for key, value in input_dict.items():
    ...
```

ตัวอย่างเช่น `input_dict = {3: "A", 2: "B"}` จะทำให้ลูปพบคู่
`(3, "A")` และ `(2, "B")` ตามลำดับที่เพิ่มข้อมูลลงในพจนานุกรม

## ฟังก์ชัน `reverse()`

ฟังก์ชัน `reverse()` ต้องสร้างพจนานุกรม **ชุดใหม่** โดยสลับตำแหน่งของคีย์
และค่าในแต่ละคู่ จาก `(key, value)` ให้กลายเป็น `(value, key)`

| คู่เดิม | คำสั่งที่ใช้เพิ่มคู่ใหม่ | คู่ใหม่ |
| :---: | :--- | :---: |
| `3: "A"` | `new_dict["A"] = 3` | `"A": 3` |
| `2: "B"` | `new_dict["B"] = 2` | `"B": 2` |

เมื่อนำแนวคิดนี้ไปใช้กับทุกคู่ จะได้ขั้นตอนหลักดังนี้

```python
new_dict = {}
for key, value in input_dict.items():
    new_dict[value] = key
return new_dict
```

ดังนั้น `reverse({3: "A", 2: "B"})` จะคืนค่า
`{"A": 3, "B": 2}` โดยไม่ได้แก้ไขพจนานุกรมเดิม

> [!NOTE]
>
> โจทย์กำหนดว่าค่าของพจนานุกรมเดิมไม่ซ้ำกัน เพราะค่าเหล่านี้จะกลายเป็นคีย์
> ของพจนานุกรมใหม่ หากมีค่าซ้ำกัน การกำหนดค่าครั้งหลังจะเขียนทับคีย์เดิม
> นอกจากนี้ ค่าที่นำมาเป็นคีย์ใหม่ต้องเป็นข้อมูลชนิดที่ใช้เป็นคีย์ของ `dict`
> ได้ด้วย

## ฟังก์ชัน `keys()`

ฟังก์ชัน `keys(input_dict, v)` ต้องรวบรวมคีย์ทุกตัวที่มีค่าเท่ากับ `v`
จึงเริ่มจากลิสต์ว่าง แล้วตรวจแต่ละคู่ในพจนานุกรม

```python
keys = []
for key, value in input_dict.items():
    if value == v:
        keys.append(key)
return keys
```

เมื่อเรียก `keys({3: 33, 4: 33, 5: 55, 2: 33}, 33)`
การตรวจข้อมูลจะเป็นดังนี้

| `key` | `value` | `value == 33` | ลิสต์หลังตรวจคู่นี้ |
| :---: | :---: | :---: | :--- |
| `3` | `33` | จริง | `[3]` |
| `4` | `33` | จริง | `[3, 4]` |
| `5` | `55` | เท็จ | `[3, 4]` |
| `2` | `33` | จริง | `[3, 4, 2]` |

โจทย์ยอมให้เรียงคีย์ที่พบแบบใดก็ได้ ส่วนโค้ดนี้จะได้คีย์ตามลำดับที่อยู่ใน
พจนานุกรม หากไม่มีค่าใดเท่ากับ `v` เลย ฟังก์ชันจะคืนลิสต์ว่าง `[]`

## การรับคำสั่งจาก Grader

โจทย์ข้อนี้ไม่ได้กำหนดให้เราเรียกฟังก์ชันหรือแสดงผลเอง แต่ Grader จะส่งคำสั่ง
Python เข้ามา 1 บรรทัด เช่น

```python
print(reverse({3: "A", 2: "B"}) == {"A": 3, "B": 2})
```

คำสั่ง `exec(input().strip())` จะอ่านข้อความ ตัดช่องว่างที่หัวและท้าย
แล้วสั่งให้ Python ทำงานตามข้อความนั้น จึงทำให้ Grader เรียก `reverse()` หรือ
`keys()` และตรวจค่าที่ฟังก์ชันคืนมาได้ ส่วนฟังก์ชันทั้งสองมีหน้าที่ `return`
ผลลัพธ์ ไม่ได้ `print()` ผลลัพธ์ด้วยตนเอง

> [!WARNING]
>
> `exec()` สามารถสั่งให้ Python ทำงานตามข้อความใดก็ได้ จึงใช้ในข้อนี้เพื่อรับ
> คำสั่งจาก Grader ที่เชื่อถือได้เท่านั้น ไม่ควรใช้ `exec()` กับข้อมูลจากผู้ใช้
> หรือแหล่งข้อมูลที่ไม่รู้ที่มา

---

# Solution

```python
# --------------------------------------------------
# File Name : 08_Dict_11.py
# Problem   : Reverse and Keys
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# Reverses the keys and values of a dictionary
def reverse(input_dict):
    new_dict = {}
    for key, value in input_dict.items():
        new_dict[value] = key
    return new_dict


# Returns a list of keys that have the specified value in the dictionary
def keys(input_dict, v):
    keys = []
    for key, value in input_dict.items():
        if value == v:
            keys.append(key)
    return keys


# Execute the input string
exec(input().strip())
```
