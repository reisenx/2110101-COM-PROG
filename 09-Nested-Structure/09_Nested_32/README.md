<p align="left">
  <a href="../README.md">
    <img src="../../Z99-OTHERS/00-common/00-back.png" style="width:10%">
  </a>
</p>

<div align="center">
  <h1>
    First-Fit Best-Fit ★★★ (
      <a href="https://drive.google.com/file/d/1s9ueFIJNywIOl8C9mEoUoqBwR9Ai275I/view?usp=drive_link">
        <code>09_Nested_32</code>
      </a>
    )
  </h1>
</div>

# Contents

-   [**แนวคิดการแบ่งข้อมูลเป็นกลุ่ม**](#แนวคิดการแบ่งข้อมูลเป็นกลุ่ม)
-   [**วิธี First Fit**](#วิธี-first-fit)
-   [**วิธี Best Fit**](#วิธี-best-fit)
-   [**การแบ่งข้อมูลทั้งลิสต์**](#การแบ่งข้อมูลทั้งลิสต์)
-   [**การรับคำสั่งทดสอบจาก Grader**](#การรับคำสั่งทดสอบจาก-grader)
-   [**Solution**](#solution)

---

## แนวคิดการแบ่งข้อมูลเป็นกลุ่ม

ข้อมูลในโจทย์เป็นจำนวนเต็มตั้งแต่ `1` ถึง `100` และแต่ละลิสต์ย่อย
เปรียบเสมือนกล่องที่รับผลรวมได้ไม่เกิน `100` เมื่อพิจารณาจำนวนใหม่ `e`
เราต้องเลือกว่าจะนำไปต่อท้ายลิสต์ย่อยใด หรือสร้างลิสต์ย่อยใหม่

ทั้ง **First Fit** และ **Best Fit** เป็นวิธีแบบ greedy คือเลือกตำแหน่งที่เหมาะสม
จากสถานะปัจจุบันทีละจำนวน วิธีเหล่านี้ใช้งานง่าย แต่ไม่ได้รับประกันว่าจะได้
จำนวนลิสต์ย่อยน้อยที่สุดในทุกกรณี

ข้อมูลจะถูกพิจารณาตามลำดับเดิม ไม่มีการเรียงค่าก่อนแบ่งกลุ่ม
สมาชิกภายในแต่ละกลุ่มจึงปรากฏตามลำดับที่ถูกนำเข้ามา และกลุ่มใหม่จะถูกสร้าง
ต่อท้ายกลุ่มเดิมเสมอ

ฟังก์ชัน `first_fit()` และ `best_fit()` ใช้ `append()` แก้ไขลิสต์ที่รับเข้ามา
โดยตรง และคืนลิสต์ออบเจ็กต์เดิมกลับไป ส่วนฟังก์ชัน `partition_FF()` และ
`partition_BF()` สร้างลิสต์ผลลัพธ์ใหม่ของตนเอง

---

## วิธี First Fit

ฟังก์ชัน `first_fit(numbers, num_to_insert)` ตรวจลิสต์ย่อยจากซ้ายไปขวา
เงื่อนไขที่ใช้ตรวจคือ

$$
\text{ผลรวมเดิม} + \text{จำนวนใหม่} \le 100
$$

ซึ่งตรงกับ Python ดังนี้

```python
sum(numbers[i]) + num_to_insert <= 100
```

เมื่อพบกลุ่มแรกที่ใส่ได้ ฟังก์ชันจะ `append()` จำนวนใหม่แล้ว `return` ทันที
จึงไม่ตรวจกลุ่มทางขวาต่อ หากตรวจครบทุกกลุ่มแล้วยังใส่ไม่ได้
จะสร้างกลุ่มใหม่ `[num_to_insert]`

ตัวอย่าง ต้องการใส่ `20` ลงใน `[[90, 5], [50], [70, 10]]`

-   กลุ่ม `[90, 5]` มีผลรวม `95` เมื่อบวก `20` จะเกิน `100`
-   กลุ่ม `[50]` ใส่ได้ และเป็นกลุ่มแรกที่ผ่านเงื่อนไข

ผลลัพธ์จึงเป็น `[[90, 5], [50, 20], [70, 10]]`

> [!NOTE]
>
> เครื่องหมาย `<=` ทำให้กลุ่มที่มีผลรวมหลังเพิ่มเป็น `100` พอดียังรับข้อมูลได้
> และฟังก์ชันแก้ไขลิสต์ `numbers` เดิมด้วย `append()` พร้อมคืนลิสต์ออบเจ็กต์เดิม

---

## วิธี Best Fit

Best Fit ตรวจทุกกลุ่มที่ใส่จำนวนใหม่ได้ แล้วเลือกกลุ่มที่เหลือพื้นที่น้อยที่สุด
หลังใส่ข้อมูล หรือกล่าวอีกแบบคือเลือกผลรวมที่ใกล้ `100` ที่สุดโดยไม่เกิน `100`

พื้นที่คงเหลือของกลุ่มคำนวณจาก

$$
100 - (\text{ผลรวมเดิม} + \text{จำนวนใหม่})
$$

ซึ่งเขียนในโค้ดเป็น

```python
100 - (sum(numbers[i]) + num_to_insert)
```

โค้ดสร้าง `diffs = [100] * len(numbers)` โดยใช้ `100` เป็นค่าที่หมายถึง
“กลุ่มนี้ใส่ไม่ได้” แล้วแทนค่าเฉพาะตำแหน่งที่ผ่านเงื่อนไข ด้วยข้อกำหนดว่า
จำนวนใหม่อยู่ระหว่าง `1` ถึง `100` กลุ่มที่ใส่ได้จริงจะมีพื้นที่เหลือ `0` ถึง `99`
จึงแยกจากค่าแทน `100` ได้ชัดเจน

จากนั้น `min(diffs)` หาเนื้อที่ที่เหลือน้อยที่สุด และ `diffs.index(min_diff)`
คืนดัชนีแรกที่พบ หากหลายกลุ่มเหลือพื้นที่เท่ากัน Best Fit ของโค้ดนี้จึงเลือก
**กลุ่มซ้ายสุด** ในกลุ่มที่เสมอกัน

ตัวอย่าง ต้องการใส่ `20` ลงใน `[[90, 5], [50], [70, 10]]`

-   กลุ่ม `[90, 5]` ใส่ไม่ได้
-   กลุ่ม `[50]` จะเหลือพื้นที่ `30`
-   กลุ่ม `[70, 10]` จะเหลือพื้นที่ `0`

จึงเลือกกลุ่มสุดท้าย ได้ `[[90, 5], [50], [70, 10, 20]]`
ถ้าไม่มีลิสต์ย่อยตั้งแต่แรก หรือทุกกลุ่มใส่แล้วเกิน `100`
ฟังก์ชันจะสร้างกลุ่มใหม่ต่อท้าย

---

## การแบ่งข้อมูลทั้งลิสต์

ฟังก์ชัน `partition_FF(numbers)` และ `partition_BF(numbers)` เริ่มจากผลลัพธ์ว่าง
แล้วอ่านจำนวนจากลิสต์ต้นฉบับทีละตัว

```python
result = []
for num in numbers:
    result = first_fit(result, num)  # หรือ best_fit(result, num)
```

ความแตกต่างมีเพียงวิธีเลือกกลุ่มในแต่ละรอบ ส่วนลำดับการอ่านข้อมูล
และการสร้างกลุ่มใหม่เหมือนกัน ตัวอย่างข้อมูล `[50, 90, 10, 80, 50, 20]`
ให้ผลดังนี้

```text
First Fit -> [[50, 10, 20], [90], [80], [50]]
Best Fit  -> [[50, 50], [90, 10], [80, 20]]
```

ถ้าลิสต์ต้นฉบับว่าง ลูปจะไม่ทำงานและทั้งสองฟังก์ชันคืนค่า `[]`
การคำนวณทั้งหมดเป็นจำนวนเต็ม จึงไม่มีการปัดเศษหรือจัดรูปแบบตัวเลขเพิ่มเติม

---

## การรับคำสั่งทดสอบจาก Grader

บรรทัด `exec(input().strip())` รับคำสั่ง Python หนึ่งบรรทัดเพื่อให้ Grader
เรียกฟังก์ชัน เช่น `print(partition_FF([50, 90, 10]))`

> [!WARNING]
>
> `exec()` สามารถสั่งทำงานโค้ดใด ๆ ที่อยู่ในข้อความได้ จึงใช้ในข้อนี้เพื่อให้
> Grader ทดสอบฟังก์ชันตามรูปแบบที่กำหนดเท่านั้น ไม่ควรใช้กับข้อมูลจากแหล่ง
> ที่ไม่เชื่อถือ

---

# Solution

```python
# --------------------------------------------------
# File Name : 09_Nested_32.py
# Problem   : First Fit Best Fit
# Author    : Worralop Srichainont
# Date      : 2025-06-12
# --------------------------------------------------


# First Fit: Place the number in the first list that its sum does not exceed 100.
#            Otherwise, create a new list.
def first_fit(numbers, num_to_insert):
    # Check if the number can fit into any existing list
    for i in range(len(numbers)):
        if sum(numbers[i]) + num_to_insert <= 100:
            numbers[i].append(num_to_insert)
            return numbers

    # Otherwise, create a new list for the number
    numbers.append([num_to_insert])
    return numbers


# Best Fit: Place the number in the list that has the least remaining value
#           after adding the number, but still does not exceed 100.
def best_fit(numbers, num_to_insert):
    # If there are no existing lists, create the first one
    if len(numbers) == 0:
        numbers.append([num_to_insert])
        return numbers

    # Calculate the remaining value in each list after adding the number
    diffs = [100] * len(numbers)
    for i in range(len(numbers)):
        if sum(numbers[i]) + num_to_insert <= 100:
            diffs[i] = 100 - (sum(numbers[i]) + num_to_insert)

    # Put the number in the list with the least remaining value
    min_diff = min(diffs)
    if min_diff < 100:
        index = diffs.index(min_diff)
        numbers[index].append(num_to_insert)

    # Otherwise, create a new list for the number
    else:
        numbers.append([num_to_insert])
    return numbers


# Partitioning numbers using First Fit algorithms
def partition_FF(numbers):
    result = []
    for num in numbers:
        result = first_fit(result, num)
    return result


# Partitioning numbers using Best Fit algorithms
def partition_BF(numbers):
    result = []
    for num in numbers:
        result = best_fit(result, num)
    return result


# Execute the input string as code
exec(input().strip())
```
