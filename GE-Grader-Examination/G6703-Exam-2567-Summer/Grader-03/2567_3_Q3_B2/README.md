<p align="left">
  <a href="../../README.md">
    <img src="../../../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    Line Arrangement ★★ (
      <a href="https://drive.google.com/file/d/16O6nEM_cnqoUypfawlbL0e0T6ECHClym/view?usp=sharing">
        <code>2567_3_Q3_B2</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**การแทนข้อมูลเพื่อเรียงลำดับ**](#การแทนข้อมูลเพื่อเรียงลำดับ)
-   [**การแบ่งและเรียงแถวย่อย**](#การแบ่งและเรียงแถวย่อย)
-   [**การเปรียบเทียบกับแถวใหม่**](#การเปรียบเทียบกับแถวใหม่)
-   [**ตัวอย่างการทำงาน**](#ตัวอย่างการทำงาน)
-   [**Solution**](#solution)

---

## การแทนข้อมูลเพื่อเรียงลำดับ

บรรทัดแรกของอินพุตคือจำนวนที่ใช้นับซ้ำ `n` ซึ่งเก็บใน `line_amount`
บรรทัดที่สองเป็นชื่อและความสูงของนักเรียนสลับกัน เช่น `Alice 183 Bob 174`

โจทย์กำหนดให้เรียงคนที่สูงกว่าก่อน และถ้าสูงเท่ากันให้เรียงชื่อตามตัวอักษร
โปรแกรมจึงเก็บนักเรียนแต่ละคนเป็น `[-height, name]`

```python
student_line.append([-height, name])
```

Python เรียง list จากค่าน้อยไปมาก การใช้ความสูงติดลบจึงกลับทิศทางได้
เช่น คนสูง `183` มีค่า `-183` ซึ่งมาก่อน `-174` ของคนสูง `174`
ถ้าความสูงเท่ากัน ช่องแรกจะเท่ากันและ Python จะใช้ชื่อในช่องที่สองตัดสิน

---

## การแบ่งและเรียงแถวย่อย

นักเรียนเริ่มนับ `1` ถึง `n` จากซ้ายไปขวา แล้ววนกลับไปเริ่มที่ `1` ใหม่
คนที่นับได้เลขเดียวกันต้องอยู่ในแถวย่อยเดียวกัน

เมื่อตำแหน่งของ list เริ่มจาก `0` กลุ่มที่นับได้เลข `i + 1`
จึงเลือกได้ด้วยการ slice แบบเว้นช่วง

```python
data[i::sublist_amount]
```

ตัวอย่างเมื่อ `n = 3`

-   `data[0::3]` เลือกตำแหน่ง `0, 3, 6, ...` หรือกลุ่มที่นับได้ `1`
-   `data[1::3]` เลือกตำแหน่ง `1, 4, 7, ...` หรือกลุ่มที่นับได้ `2`
-   `data[2::3]` เลือกตำแหน่ง `2, 5, 8, ...` หรือกลุ่มที่นับได้ `3`

ฟังก์ชัน `sorted_by_sublist()` เรียงนักเรียนภายในแต่ละกลุ่ม
แล้วต่อกลุ่มที่ `1`, `2`, ..., `n` เข้าด้วยกันตามลำดับ

```python
for i in range(sublist_amount):
    result += sorted(data[i::sublist_amount])
```

เพราะแต่ละคนถูกเก็บเป็น `[-height, name]` การเรียงแต่ละกลุ่มจึงได้
ความสูงจากมากไปน้อย และใช้ชื่อ `A` ถึง `Z` เมื่อความสูงเท่ากัน
หากจำนวนนักเรียนหารด้วย `n` ไม่ลงตัว กลุ่มท้าย ๆ เพียงมีสมาชิกน้อยกว่า
และการ slice ยังคงแบ่งกลุ่มได้ถูกต้อง

---

## การเปรียบเทียบกับแถวใหม่

หลังต่อแถวย่อยแล้ว โปรแกรมสร้างแถวอ้างอิงตามขั้นที่ 6 ของโจทย์
โดยเรียงนักเรียนทุกคนพร้อมกัน

```python
student_line.sort()
```

ตอนนี้มี 2 แถวที่ต้องเปรียบเทียบ

-   `student_line` คือแถวที่เรียงนักเรียนทุกคนใหม่ตามความสูง
-   `modified_student_line` คือแถวที่เกิดจากการเรียงภายในแต่ละแถวย่อยแล้วนำมาต่อกัน

ฟังก์ชัน `get_matched_names()` ตรวจทุกดัชนี ถ้านักเรียนในดัชนีเดียวกันของทั้งสองแถว
เป็นคนเดียวกัน แสดงว่านักเรียนคนนั้นยังยืนอยู่ที่เดิมเมื่อเทียบระหว่างขั้นที่ 5 กับขั้นที่ 6

```python
if initial_data[i] == modified_data[i]:
    matched_names.append(name)
```

ชื่อที่พบจะอยู่ตามลำดับของแถวที่เรียงใหม่ คือความสูงจากมากไปน้อย
และเรียงชื่อตามตัวอักษรเมื่อสูงเท่ากัน โปรแกรมเชื่อมชื่อด้วยช่องว่าง
แต่ถ้าไม่มีตำแหน่งใดตรงกันเลยจะแสดงคำว่า `None`

---

## ตัวอย่างการทำงาน

กำหนด `n = 2` และแถวเริ่มต้นเป็น

```text
Alice 183 Bob 174 Adam 170 Dan 175 Alex 165 Bill 178
```

เมื่อนับ `1, 2, 1, 2, ...` จะได้

-   กลุ่ม 1: Alice 183, Adam 170, Alex 165
-   กลุ่ม 2: Bob 174, Dan 175, Bill 178

เรียงภายในแต่ละกลุ่มแล้วนำมาต่อกัน ได้แถวจากขั้นที่ 5 เป็น

```text
Alice Adam Alex Bill Dan Bob
```

เมื่อเรียงนักเรียนทุกคนพร้อมกัน ได้แถวจากขั้นที่ 6 เป็น

```text
Alice Bill Dan Bob Adam Alex
```

มีเพียงตำแหน่งแรกที่เป็น Alice เหมือนกัน จึงแสดงผล

```text
Alice
```

การเปรียบเทียบนี้สนใจทั้งความสูงและชื่อผ่านข้อมูล `[-height, name]`
จึงยังทำงานตามกติกาได้เมื่อนักเรียนหลายคนมีความสูงเท่ากัน

---

# Solution

```python
# --------------------------------------------------
# File Name : 2567_3_Q3_B2.py
# Problem   : Line Arrangement
# Author    : Worralop Srichainont
# Date      : 2025-07-31
# --------------------------------------------------


# Separate the input into sublist by slicing and sort each sublist.
# Then concatenate into a single list.
def sorted_by_sublist(data, sublist_amount):
    result = []
    for i in range(sublist_amount):
        result += sorted(data[i::sublist_amount])
    return result


# Get the names of students whose at the same position in both lists.
def get_matched_names(initial_data, modified_data):
    # Initialize an empty list to store matched names
    matched_names = []

    # Iterate through the initial data and modified data
    for i in range(len(initial_data)):
        # Get the student's name
        name = initial_data[i][1]
        # Check if the name at the same index in both lists matches
        if initial_data[i] == modified_data[i]:
            # If it matches, add the name to the matched names list
            matched_names.append(name)

    # Return the list of matched names
    return matched_names


# Main function
def main():
    # Input the amount of lines that the students will be arranged in
    line_amount = int(input())

    # Input the order of students in their original line
    student_line = []
    data = input().strip().split()
    for i in range(0, len(data), 2):
        # Extract the name and height of each student
        name = data[i]
        height = int(data[i + 1])
        # Append the height and name to a list
        student_line.append([-height, name])

    # Create a modified student line by using the custom sorting function
    modified_student_line = sorted_by_sublist(student_line, line_amount)

    # Sort the student line by height in descending order,
    # then by name in ascending order
    student_line.sort()

    # Get the names of students who are at the same position in both lines
    matched_names = get_matched_names(student_line, modified_student_line)

    # Output the names of students who are at the same position in both lines
    if len(matched_names) > 0:
        print(" ".join(matched_names))
    else:
        print("None")


# Run the main function
main()
```
