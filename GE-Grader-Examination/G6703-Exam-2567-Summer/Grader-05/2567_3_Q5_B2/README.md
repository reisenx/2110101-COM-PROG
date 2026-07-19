<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Weather Perception ★★☆ (
      <a href="https://drive.google.com/file/d/1TMVjvnJ1ltHH8S8_CrdAnlekX9SKm-QQ/view?usp=sharing">
        <code>2567_3_Q5_B2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แปลงฟาเรนไฮต์เป็นเซลเซียส**](#แปลงฟาเรนไฮต์เป็นเซลเซียส)
-   [**จำแนกความรู้สึกต่ออุณหภูมิ**](#จำแนกความรู้สึกต่ออุณหภูมิ)
-   [**จัดอันดับประเทศ**](#จัดอันดับประเทศ)
-   [**คำสั่งทดสอบจาก Grader**](#คำสั่งทดสอบจาก-grader)
-   [**Solution**](#solution)

---

## แปลงฟาเรนไฮต์เป็นเซลเซียส

ฟังก์ชัน `fahrenheit_to_celsius(fahrenheit)` รับอุณหภูมิหน่วยฟาเรนไฮต์
และคืนอุณหภูมิหน่วยเซลเซียสด้วยสูตร

$$
C = (F - 32) \times \frac{5}{9}
$$

ใน Python เขียนได้ตรงกับสูตรว่า

```python
return (fahrenheit - 32) * 5 / 9
```

เครื่องหมาย `/` ทำให้ผลลัพธ์เป็นจำนวนจริง เช่น `70.7°F` แปลงเป็น `21.5°C`
และ `-4°F` แปลงเป็น `-20.0°C`

---

## จำแนกความรู้สึกต่ออุณหภูมิ

ฟังก์ชัน `get_perception(celsius)` ตรวจเกณฑ์จากอุณหภูมิสูงลงมาต่ำ
เมื่อพบเงื่อนไขแรกที่เป็นจริงจะ `return` ทันที เกณฑ์ที่ **โค้ดชุดนี้ใช้จริง** คือ

| อุณหภูมิเซลเซียส | ค่าที่คืน |
| :--- | :--- |
| `celsius > 35` | `"extreme hot"` |
| `celsius > 25` | `"hot"` |
| `celsius > 15` | `"comfortable"` |
| `celsius > -10` | `"cold"` |
| นอกเหนือจากนี้ | `"extreme cold"` |

เพราะตรวจจากบนลงล่าง เงื่อนไข `celsius > 25` หมายถึงช่วงที่ไม่เกิน `35`
ด้วย ตัวอย่างค่าที่ขอบช่วงคือ `35` ได้ `hot`, `25` ได้ `comfortable`, `15`
ได้ `cold` และ `-10` ได้ `extreme cold`

> [!WARNING]
>
> PDF กำหนดขอบระหว่าง `comfortable` กับ `cold` ที่ `20°C` แต่ค่าคงที่ใน
> Solution ใช้ `15.0` ดังนั้นช่วง `15 < celsius <= 20` จะได้ `comfortable`
> จากโค้ด แม้ตามข้อความโจทย์ควรได้ `cold` README นี้จึงอธิบายพฤติกรรมของ
> โค้ดที่ต้องเก็บไว้ตามต้นฉบับให้ชัดเจน

---

## จัดอันดับประเทศ

`print_countries_ranked_by_perception(countries_info)` รับลิสต์ที่สมาชิกแต่ละตัว
มีรูป `[ชื่อประเทศ, อุณหภูมิฟาเรนไฮต์]` แล้วทำงานสามขั้นตอน

1. แปลงอุณหภูมิด้วย `fahrenheit_to_celsius()`
2. หาความรู้สึกด้วย `get_perception()`
3. เก็บชื่อประเทศลง dictionary โดยใช้ความรู้สึกเป็น key

ลำดับความน่าเที่ยวไม่ได้เรียงตามอุณหภูมิ แต่กำหนดไว้ชัดเจนใน
`PERCEPTION_ORDER`

```python
["comfortable", "cold", "hot", "extreme cold", "extreme hot"]
```

โปรแกรมวนตามลำดับนี้ และใช้ `sorted()` เรียงชื่อประเทศตามพจนานุกรมภายในกลุ่ม
เดียวกัน จากนั้นแสดง `ชื่อประเทศ perception` ทีละบรรทัด ฟังก์ชันนี้แสดงผล
โดยตรงและไม่คืนค่า

---

## คำสั่งทดสอบจาก Grader

โจทย์ประเภทเขียนฟังก์ชันส่งคำสั่ง Python เข้ามาทีละบรรทัด เช่น

```python
print(fahrenheit_to_celsius(70.7));
```

ส่วนท้ายของ Solution อ่านคำสั่งเข้า `cmd` แล้วใช้ `exec(cmd)` เพื่อให้ Grader
เรียกฟังก์ชัน สร้างลิสต์ หรือเพิ่มข้อมูลได้หลายคำสั่ง โปรแกรมหยุดหลังประมวลผล
บรรทัดที่ลงท้ายด้วย `;`

> [!WARNING]
>
> `exec()` สามารถทำงานตามข้อความ Python ได้โดยตรง จึงเหมาะกับข้อมูลทดสอบที่
> เชื่อถือได้จาก Grader เท่านั้น ห้ามใช้รูปแบบนี้กับข้อความจากผู้ใช้หรือแหล่งที่
> ไม่ไว้วางใจ เพราะข้อความนั้นอาจสั่งให้โปรแกรมทำสิ่งที่ไม่ต้องการได้

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_3_Q5_B2.py
# Problem   : Weather Perception
# Author    : Worralop Srichainont
# Date      : 2025-08-01
# --------------------------------------------------

# Constants for temperature perception
PERCEPTION_ORDER = ["comfortable", "cold", "hot", "extreme cold", "extreme hot"]
PERCEPTION_CRITERIA = [
    ["extreme hot", 35.0],
    ["hot", 25.0],
    ["comfortable", 15.0],
    ["cold", -10.0],
]


# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Function to determine the weather perception based on Celsius temperature
def get_perception(celsius):
    for perception, threshold in PERCEPTION_CRITERIA:
        if celsius > threshold:
            return perception
    return "extreme cold"


# Function to print countries ranked by their weather perception
def print_countries_ranked_by_perception(countries_info):
    # Initialize a dictionary to map perceptions to countries
    perception_to_countries = {}

    # Process each country's information
    for country, fahrenheit in countries_info:
        # Determine perception from the Fahrenheit temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        perception = get_perception(celsius)

        # Add the country to the corresponding perception in the dictionary
        if perception not in perception_to_countries:
            perception_to_countries[perception] = []
        perception_to_countries[perception].append(country)

    # Print the countries sorted by perception order
    for perception in PERCEPTION_ORDER:
        # Check if the perception exists in the dictionary
        if perception in perception_to_countries:
            # Sort the countries alphabetically and print them with their perception
            for country in sorted(perception_to_countries[perception]):
                print(country, perception)


# Run the input string as code until it ends with a semicolon
while cmd := input().strip():
    exec(cmd)
    if cmd[-1] == ";":
        break
```
